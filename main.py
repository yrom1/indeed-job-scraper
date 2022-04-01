#!/usr/bin/env python
# coding: utf-8
"""Indeed job posting scraper."""

import random
import re
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import quote

import bs4
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup, NavigableString


def htmlify(input: str) -> str:
    """
    in: `Benefits Analyst (Junior)`
    out: `Benefits%20Analyst%20%28Junior%29`
    """
    output = quote(input)
    return output


def clean_HTML(input: str) -> str:
    """I can't display HTML inside a cell in a DataFrame (it seems)"""
    # remove tags <somethign> and leave contents between tags
    out = re.sub("<.*?>", "", input)
    out = re.sub("\n", " ", out)
    return out


def clean_date_Series(input: str) -> int:
    """Remove the characters from the days ago posting col
    So I can sort postings by that number.

    Sometimes the input can be: 'Just posted'
    So I'm going to return '0' in that case.
    """
    output = re.sub("\D", "", input)
    output = re.sub("\s*", "", output)
    if output == "":
        int_output = 0  # 'Just posted.' -> '' -> '0'
    else:
        int_output = int(output)
    return int_output


def make_link(title: str, company: str) -> str:
    # https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20Flighthub
    return f"https://ca.indeed.com/jobs?q={htmlify(title)}%20{htmlify(company)}"


def main(
    input="data junior",
    output_path=str(Path.home() / "pickleFrame"),
    pages_per_search=1,
) -> None:
    """Scrape indeed for job postings based on input.
    Args:
        input: String to search on indeed.
        output_path: Place to store DateFrame pickle.
        pages_per_search: Max number of indeed pages to scrape based on search.
    """
    Path(output_path).mkdir(parents=True, exist_ok=True)

    pages = []
    for start in range(0, pages_per_search * 10, 10):
        page = requests.get(
            f"https://ca.indeed.com/jobs?q={htmlify(input)}&l=Canada&start="
            + str(start)
        )
        soup = BeautifulSoup(page.text, "html.parser")
        pages.append(soup)
        time.sleep(random.randrange(3, 6) + random.random())

    titles = pd.Series([], dtype="string")
    companyNames = pd.Series([], dtype="string")
    jobSnippets = pd.Series([], dtype="string")
    locations = pd.Series([], dtype="string")
    dates = pd.Series([], dtype="string")
    for page in pages:
        # print('find_all in dir(page)', 'find_all' in dir(page)) # >>> find_all in dir(page) True
        jobs = page.find_all("div", attrs={"class": "job_seen_beacon"})  # type: ignore
        for job in jobs:

            # Job Title
            title = (
                job.find("h2", attrs={"class": "jobTitle"})
                .find("span", attrs={"title": True})
                .next
            )
            titles = titles.append(pd.Series([str(title)]))

            # Company Name
            companyName = job.find("span", attrs={"class": "companyName"})
            tempCompanyName = companyName
            companyName = companyName.find(
                "a", attrs={"class": "turnstileLink companyOverviewLink"}
            )
            if companyName is None:
                companyName = tempCompanyName
            companyName = companyName.next
            companyNames = companyNames.append(pd.Series([str(companyName)]))

            # Job snip
            jobSnippet = job.find("div", attrs={"class": "job-snippet"}).next
            jobSnippets = jobSnippets.append(
                pd.Series([str(clean_HTML(str(jobSnippet)))])
            )

            # Location
            location = job.find("div", attrs={"class": "companyLocation"}).next
            locations = locations.append(pd.Series([str(location)]))

            # Posting Date
            date = job.find("span", attrs={"class": "date"})
            date = "".join(
                [element for element in date if isinstance(element, NavigableString)]
            )
            dates = dates.append(pd.Series([str(date)]))

    clean_dates = dates.apply(clean_date_Series)

    links = pd.Series([], dtype="string")
    for (company, title) in zip(titles, companyNames):
        links = links.append(pd.Series([str(make_link(company, title))]))

    df_links = pd.DataFrame(
        {
            f"{titles=}".split("=")[0]: titles,
            f"{companyNames=}".split("=")[0]: companyNames,
            f"{links=}".split("=")[0]: links,
        }
    )
    df_links.head()

    assert (
        len(titles)
        == len(companyNames)
        == len(jobSnippets)
        == len(locations)
        == len(dates)
        == len(clean_dates)
    )
    df = pd.DataFrame(
        {
            f"{titles=}".split("=")[0]: titles,
            f"{companyNames=}".split("=")[0]: companyNames,
            f"{jobSnippets=}".split("=")[0]: jobSnippets,
            f"{locations=}".split("=")[0]: locations,
            f"{dates=}".split("=")[0]: dates,
            f"{clean_dates=}".split("=")[0]: clean_dates,
        }
    )

    final_df = pd.merge(
        df,
        df_links,
        how="inner",
        left_on=[f"{titles=}".split("=")[0], f"{companyNames=}".split("=")[0]],
        right_on=[f"{titles=}".split("=")[0], f"{companyNames=}".split("=")[0]],
    )

    sorted_df = final_df.sort_values(f"{clean_dates=}".split("=")[0])

    pd.set_option("display.max_rows", len(sorted_df))
    sorted_no_duplicates_df = sorted_df.drop_duplicates()

    sorted_no_duplicates_df.to_pickle(
        str(
            Path(output_path)
            / f"{'_'.join(str(datetime.today()).split())}_{'_'.join(input.split())}.p"
        )
    )


if __name__ == "__main__":
    TEST_INPUT = """<ul style="list-style-type:circle;margin-top: 0px;margin-bottom: 0px;padding-left:20px;">\n<li style="margin-bottom:0px;">Interpret <b>data</b>, formulate reports, and make recommendations to the team.</li>\n<li>Remain fully informed on latest <b>data</b> trends, practice, and process.</li>\n</ul><ul style="list-style-type:circle;margin-top: 0px;margin-bottom: 0px;padding-left:20px;">\n<li style="margin-bottom:0px;">Interpret <b>data</b>, formulate reports, and make recommendations to the team.</li>\n<li>Remain fully informed on latest <b>data</b> trends, practice, and process.</li>\n</ul>"""
    TEST_DATE = """23 days ago"""
    assert htmlify("Benefits Analyst (Junior)") == "Benefits%20Analyst%20%28Junior%29"
    assert (
        make_link("Junior Data Analyst", "FlightHub")
        == "https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20FlightHub"
    )
    assert clean_date_Series(TEST_DATE) == 23
    import sys

    main(sys.argv[1], sys.argv[2], int(sys.argv[3]))

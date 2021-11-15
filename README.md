```python
from bs4 import BeautifulSoup
import bs4
import requests
import time
import pandas as pd
import random
import numpy as np
```


```python
# A "data junior" search seems to give me jobs that I think are interesting:
# https://ca.indeed.com/jobs?q=data%20junior&l=Canada
# When you go on the next page it:s
# https://ca.indeed.com/jobs?q=data+junior&l=Canada&start=10
# Then next page:
# https://ca.indeed.com/jobs?q=data+junior&l=Canada&start=20

# There only seems to be about 10 pages of results.
# If you try something like:
# https://ca.indeed.com/jobs?q=data+junior&l=Canada&start=1000
# It just give you the last page, so just check until the response stops changing?

# Also, you can use start=0 for the first page:
# https://ca.indeed.com/jobs?q=data+junior&l=Canada&start=0
# Is the same as
# https://ca.indeed.com/jobs?q=data%20junior&l=Canada

MAX_NUMBER_OF_PAGES_PER_SEARCH = 1  # testing

pages = []
for start in range(0, MAX_NUMBER_OF_PAGES_PER_SEARCH * 10, 10):
    page = requests.get(
        "https://ca.indeed.com/jobs?q=data%20junior&l=Canada&start=" + str(start)
    )
    soup = BeautifulSoup(page.text, "html.parser")
    pages.append(soup)
    time.sleep(random.randrange(3, 6) + random.random())
```


```python
ids = []
TEST_PAGE = pages[0]
a_tags = TEST_PAGE.find_all('a', attrs={'href':True})
for a_tag in a_tags:
    a_tag_return = a_tag.find('table', attrs={'class':'jobCard_mainContent'})
    if a_tag_return is not None:
        ids.append(a_tag_return)

# Okay, this is a link that redirects to a job posting
# https://ca.indeed.com/jobs?q=Benefits%20Analyst%20(Junior)&l=Canada&vjk=e1d5a71499ccf4ea
# in particular there's this e1d5a71499ccf4ea value, we can get a jk=e1d5a71499ccf4ea
# https://ca.indeed.com/jobs?q=Benefits%20Analyst%20%28Junior%29&l=Canada&vjk=e1d5a71499ccf4ea

len(ids), ids[3]

```




    (15,
     <table cellpadding="0" cellspacing="0" class="jobCard_mainContent" role="presentation"><tbody><tr><td class="resultContent"><div class="heading4 color-text-primary singleLineTitle tapItem-gutter"><h2 class="jobTitle jobTitle-color-purple"><span title="Junior Data Analyst">Junior Data Analyst</span></h2></div><div class="heading6 company_location tapItem-gutter"><pre><span class="companyName"><a class="turnstileLink companyOverviewLink" data-tn-element="companyName" href="/cmp/Scandinavian-Building-Services" rel="noopener" target="_blank">Scandinavian Building Services</a></span><span class="ratingsDisplay withRatingLink"><a class="ratingLink" data-tn-variant="cmplinktst2" href="/cmp/Scandinavian-Building-Services/reviews" rel="noopener" target="_blank" title="Scandinavian Building Services reviews"><span aria-label="3.0 of stars rating" class="ratingNumber" role="img"><span aria-hidden="true">3.0</span><svg aria-hidden="true" class="starIcon" fill="none" height="12" role="presentation" viewbox="0 0 16 16" width="12" xmlns="http://www.w3.org/2000/svg"><path d="M8 12.8709L12.4542 15.5593C12.7807 15.7563 13.1835 15.4636 13.0968 15.0922L11.9148 10.0254L15.8505 6.61581C16.1388 6.36608 15.9847 5.89257 15.6047 5.86033L10.423 5.42072L8.39696 0.640342C8.24839 0.289808 7.7516 0.289808 7.60303 0.640341L5.57696 5.42072L0.395297 5.86033C0.015274 5.89257 -0.13882 6.36608 0.149443 6.61581L4.0852 10.0254L2.90318 15.0922C2.81653 15.4636 3.21932 15.7563 3.54584 15.5593L8 12.8709Z" fill="#767676"></path></svg></span></a></span><div class="companyLocation">Edmonton, AB<span class="remote-bullet">•</span><span>Remote</span></div></pre></div><div class="heading6 error-text tapItem-gutter"></div></td></tr></tbody></table>)




```python
import urllib.request

def htmlify(input: str) -> str:
    """
    in: `Benefits Analyst (Junior)`
    out: `Benefits%20Analyst%20%28Junior%29`
    """
    output = urllib.request.quote(input)
    return output

assert htmlify('Benefits Analyst (Junior)') == 'Benefits%20Analyst%20%28Junior%29'
```


```python
import re

TEST_INPUT = """<ul style="list-style-type:circle;margin-top: 0px;margin-bottom: 0px;padding-left:20px;">\n<li style="margin-bottom:0px;">Interpret <b>data</b>, formulate reports, and make recommendations to the team.</li>\n<li>Remain fully informed on latest <b>data</b> trends, practice, and process.</li>\n</ul><ul style="list-style-type:circle;margin-top: 0px;margin-bottom: 0px;padding-left:20px;">\n<li style="margin-bottom:0px;">Interpret <b>data</b>, formulate reports, and make recommendations to the team.</li>\n<li>Remain fully informed on latest <b>data</b> trends, practice, and process.</li>\n</ul>"""


def clean_HTML(input: str) -> str:
    """I can't display HTML inside a cell in a DataFrame (it seems)"""
    # remove tags <somethign> and leave contents between tags
    out = re.sub("<.*?>", "", input)
    out = re.sub("\n", " ", out)
    return out


print(clean_HTML(TEST_INPUT))
```

     Interpret data, formulate reports, and make recommendations to the team. Remain fully informed on latest data trends, practice, and process.  Interpret data, formulate reports, and make recommendations to the team. Remain fully informed on latest data trends, practice, and process. 



```python
# When you search there's box cards for each posting, the class for the box is:
# class="jobsearch-SerpJobCard unifiedRow row result clickcard"
# that wasn't working for me though, so I changed it to 'class':"job_seen_beacon"

titles = pd.Series([], dtype="string")
companyNames = pd.Series([], dtype="string")
jobSnippets = pd.Series([], dtype="string")
locations = pd.Series([], dtype="string")
dates = pd.Series([], dtype="string")
for page in pages:
    jobs = page.find_all("div", attrs={"class": "job_seen_beacon"})
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
        jobSnippets = jobSnippets.append(pd.Series([str(clean_HTML(str(jobSnippet)))]))

        # Location
        location = job.find("div", attrs={"class": "companyLocation"}).next
        locations = locations.append(pd.Series([str(location)]))

        # Posting Date
        date = job.find("span", attrs={"class": "date"}).next
        dates = dates.append(pd.Series([str(date)]))
```


```python
def clean_date_Series(input: str) -> str:
    """Remove the characters from the days ago posting col
    so I can sort postings by that number."""
    output = re.sub("\D", "", input)
    output = re.sub("\s*", "", output)
    output = int(output)
    return output


TEST_DATE = """23 days ago"""
assert clean_date_Series(TEST_DATE) == 23
clean_dates = dates.apply(clean_date_Series)
```


```python
def make_link(title: str, company: str) -> str:
    # https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20Flighthub
    return f'https://ca.indeed.com/jobs?q={htmlify(title)}%20{htmlify(company)}'

assert make_link('Junior Data Analyst', 'FlightHub') == "https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20FlightHub"
```


```python
links = pd.Series([], dtype='string')
for (company, title) in zip(titles, companyNames):
    links = links.append(pd.Series([str(make_link(company, title))]))
len(links)
```




    15




```python
df_links = pd.DataFrame({f'{titles=}'.split('=')[0]:titles, f'{companyNames=}'.split('=')[0]: companyNames, f'{links=}'.split('=')[0]: links})
df_links.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>titles</th>
      <th>companyNames</th>
      <th>links</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Junior Machine Learning Engineer / Data Scientist</td>
      <td>Virtus Groups</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Machine%20Learning%20Engineer%20/%20Data%20Scientist%20Virtus%20Groups</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Junior Data Analyst</td>
      <td>O2E Brands</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20O2E%20Brands</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Junior Data Analyst</td>
      <td>OSL Retail Services Inc</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20OSL%20Retail%20Services%20Inc</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Junior Data Analyst</td>
      <td>Scandinavian Building Services</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20Scandinavian%20Building%20Services</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Jr. Data Analyst</td>
      <td>Ratehub</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data%20Analyst%20Ratehub</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
df.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>titles</th>
      <th>companyNames</th>
      <th>jobSnippets</th>
      <th>locations</th>
      <th>dates</th>
      <th>clean_dates</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Junior Machine Learning Engineer / Data Scientist</td>
      <td>Virtus Groups</td>
      <td>Candidates must be a Canadian Citizen or Permanent Resident having resided in Canada for at least 10 years. You will be given the chance to work with state-of…</td>
      <td>Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Junior Data Analyst</td>
      <td>O2E Brands</td>
      <td>Passion for data visualization with Tableau. Experience blending data from disparate sources. Ensure consistent application of data governance initiatives.</td>
      <td>Vancouver, BC</td>
      <td>24 days ago</td>
      <td>24</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Junior Data Analyst</td>
      <td>OSL Retail Services Inc</td>
      <td>Acquire data from primary or secondary data sources and maintain databases/data systems. Proven working experience as a data analyst or business data analyst.</td>
      <td>Mississauga, ON</td>
      <td>3 days ago</td>
      <td>3</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Junior Data Analyst</td>
      <td>Scandinavian Building Services</td>
      <td>Previous experience with large scale data analysis or data reconciliations. Advanced level Microsoft Excel and data analytics skills.</td>
      <td>Edmonton, AB</td>
      <td>10 days ago</td>
      <td>10</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Jr. Data Analyst</td>
      <td>Ratehub</td>
      <td>Support in developing and maintaining our data model by understanding key data sources and relationships between them.</td>
      <td>Toronto, ON</td>
      <td>3 days ago</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
final_df = pd.merge(df, df_links, how='inner', left_on=['titles', 'companyNames'], right_on=['titles', 'companyNames'])
final_df.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>titles</th>
      <th>companyNames</th>
      <th>jobSnippets</th>
      <th>locations</th>
      <th>dates</th>
      <th>clean_dates</th>
      <th>links</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Junior Machine Learning Engineer / Data Scientist</td>
      <td>Virtus Groups</td>
      <td>Candidates must be a Canadian Citizen or Permanent Resident having resided in Canada for at least 10 years. You will be given the chance to work with state-of…</td>
      <td>Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Machine%20Learning%20Engineer%20/%20Data%20Scientist%20Virtus%20Groups</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Junior Data Analyst</td>
      <td>O2E Brands</td>
      <td>Passion for data visualization with Tableau. Experience blending data from disparate sources. Ensure consistent application of data governance initiatives.</td>
      <td>Vancouver, BC</td>
      <td>24 days ago</td>
      <td>24</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20O2E%20Brands</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Junior Data Analyst</td>
      <td>OSL Retail Services Inc</td>
      <td>Acquire data from primary or secondary data sources and maintain databases/data systems. Proven working experience as a data analyst or business data analyst.</td>
      <td>Mississauga, ON</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20OSL%20Retail%20Services%20Inc</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Junior Data Analyst</td>
      <td>Scandinavian Building Services</td>
      <td>Previous experience with large scale data analysis or data reconciliations. Advanced level Microsoft Excel and data analytics skills.</td>
      <td>Edmonton, AB</td>
      <td>10 days ago</td>
      <td>10</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20Scandinavian%20Building%20Services</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Jr. Data Analyst</td>
      <td>Ratehub</td>
      <td>Support in developing and maintaining our data model by understanding key data sources and relationships between them.</td>
      <td>Toronto, ON</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data%20Analyst%20Ratehub</td>
    </tr>
  </tbody>
</table>
</div>




```python
sorted_df = final_df.sort_values(f"{clean_dates=}".split("=")[0])
sorted_df.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>titles</th>
      <th>companyNames</th>
      <th>jobSnippets</th>
      <th>locations</th>
      <th>dates</th>
      <th>clean_dates</th>
      <th>links</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>14</th>
      <td>Analyste PMO junior - Junior PMO Analyst</td>
      <td>Gameloft</td>
      <td>Being responsible for the regular data analytics, report generation and key performance indicators. 1 year of experience in project management or PMO-related…</td>
      <td>Montréal, QC</td>
      <td>2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Analyste%20PMO%20junior%20-%20Junior%20PMO%20Analyst%20Gameloft</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Junior Data Analyst</td>
      <td>OSL Retail Services Inc</td>
      <td>Acquire data from primary or secondary data sources and maintain databases/data systems. Proven working experience as a data analyst or business data analyst.</td>
      <td>Mississauga, ON</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20OSL%20Retail%20Services%20Inc</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Jr. Data Analyst</td>
      <td>Ratehub</td>
      <td>Support in developing and maintaining our data model by understanding key data sources and relationships between them.</td>
      <td>Toronto, ON</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data%20Analyst%20Ratehub</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Junior Data Analyst</td>
      <td>FlightHub</td>
      <td>Analyzing data sets and identifying trends and patterns; Our team will count on you to use data from various sources to identify issues as they happen and to…</td>
      <td>Montréal, QC</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20FlightHub</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Junior Data Engineer</td>
      <td>Kora</td>
      <td>Help maintain and update the company-level data warehouse to ensure data accuracy. The Data Engineer will support our financial department and data scientists…</td>
      <td>Toronto, ON</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Engineer%20Kora</td>
    </tr>
  </tbody>
</table>
</div>




```python
sorted_df.to_csv('jobs.csv')
```


```python

```

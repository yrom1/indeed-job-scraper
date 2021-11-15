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

MAX_NUMBER_OF_PAGES_PER_SEARCH = 10  # testing

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




    144




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
      <td>Junior Data Analyst</td>
      <td>O2E Brands</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20A...</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Junior Data Analyst</td>
      <td>OSL Retail Services Inc</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20A...</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Junior Machine Learning Engineer / Data Scientist</td>
      <td>Virtus Groups</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Machine%...</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Junior Data Analyst</td>
      <td>Scandinavian Building Services</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20A...</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Junior Research Analyst</td>
      <td>Carleton University</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Research...</td>
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
      <td>Junior Data Analyst</td>
      <td>O2E Brands</td>
      <td>Passion for data visualization with Tableau. ...</td>
      <td>Vancouver, BC</td>
      <td>24 days ago</td>
      <td>24</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Junior Data Analyst</td>
      <td>OSL Retail Services Inc</td>
      <td>Acquire data from primary or secondary data s...</td>
      <td>Mississauga, ON</td>
      <td>3 days ago</td>
      <td>3</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Junior Machine Learning Engineer / Data Scientist</td>
      <td>Virtus Groups</td>
      <td>Candidates must be a Canadian Citizen or Perm...</td>
      <td>Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Junior Data Analyst</td>
      <td>Scandinavian Building Services</td>
      <td>Previous experience with large scale data ana...</td>
      <td>Edmonton, AB</td>
      <td>10 days ago</td>
      <td>10</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Junior Research Analyst</td>
      <td>Carleton University</td>
      <td>?experience organizing and validating data. ?...</td>
      <td>Ottawa, ON</td>
      <td>19 days ago</td>
      <td>19</td>
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
      <td>Junior Data Analyst</td>
      <td>O2E Brands</td>
      <td>Passion for data visualization with Tableau. ...</td>
      <td>Vancouver, BC</td>
      <td>24 days ago</td>
      <td>24</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20A...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Junior Data Analyst</td>
      <td>OSL Retail Services Inc</td>
      <td>Acquire data from primary or secondary data s...</td>
      <td>Mississauga, ON</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20A...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Junior Machine Learning Engineer / Data Scientist</td>
      <td>Virtus Groups</td>
      <td>Candidates must be a Canadian Citizen or Perm...</td>
      <td>Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Machine%...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Junior Machine Learning Engineer / Data Scientist</td>
      <td>Virtus Groups</td>
      <td>Candidates must be a Canadian Citizen or Perm...</td>
      <td>Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Machine%...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Junior Machine Learning Engineer / Data Scientist</td>
      <td>Virtus Groups</td>
      <td>Candidates must be a Canadian Citizen or Perm...</td>
      <td>Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Machine%...</td>
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
      <th>33</th>
      <td>Analyste PMO junior - Junior PMO Analyst</td>
      <td>Gameloft</td>
      <td>Being responsible for the regular data analyt...</td>
      <td>Montréal, QC</td>
      <td>2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Analyste%20PMO%20...</td>
    </tr>
    <tr>
      <th>69</th>
      <td>Data Engineer - Level I</td>
      <td>Swift Medical</td>
      <td>As the world leader in digital wound care man...</td>
      <td>Toronto, ON</td>
      <td>2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Engineer%2...</td>
    </tr>
    <tr>
      <th>101</th>
      <td>Analyst, Client Data I</td>
      <td>Mosaic North America</td>
      <td>Intermediate knowledge of data cleansing and ...</td>
      <td>Toronto, ON</td>
      <td>2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Analyst%2C%20Clie...</td>
    </tr>
    <tr>
      <th>123</th>
      <td>Junior Agile Developer- SAP Analytics Cloud</td>
      <td>SAP</td>
      <td>We’re looking for a junior developer who is e...</td>
      <td>Vancouver, BC</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Agile%20...</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Junior Data Analyst</td>
      <td>FlightHub</td>
      <td>Analyzing data sets and identifying trends an...</td>
      <td>Montréal, QC</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20A...</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.set_option('display.max_rows', len(sorted_df))
sorted_no_duplicates_df = sorted_df.drop_duplicates()
sorted_no_duplicates_df 
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
      <th>33</th>
      <td>Analyste PMO junior - Junior PMO Analyst</td>
      <td>Gameloft</td>
      <td>Being responsible for the regular data analyt...</td>
      <td>Montréal, QC</td>
      <td>2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Analyste%20PMO%20...</td>
    </tr>
    <tr>
      <th>69</th>
      <td>Data Engineer - Level I</td>
      <td>Swift Medical</td>
      <td>As the world leader in digital wound care man...</td>
      <td>Toronto, ON</td>
      <td>2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Engineer%2...</td>
    </tr>
    <tr>
      <th>101</th>
      <td>Analyst, Client Data I</td>
      <td>Mosaic North America</td>
      <td>Intermediate knowledge of data cleansing and ...</td>
      <td>Toronto, ON</td>
      <td>2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Analyst%2C%20Clie...</td>
    </tr>
    <tr>
      <th>123</th>
      <td>Junior Agile Developer- SAP Analytics Cloud</td>
      <td>SAP</td>
      <td>We’re looking for a junior developer who is e...</td>
      <td>Vancouver, BC</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Agile%20...</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Junior Data Analyst</td>
      <td>FlightHub</td>
      <td>Analyzing data sets and identifying trends an...</td>
      <td>Montréal, QC</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20A...</td>
    </tr>
    <tr>
      <th>92</th>
      <td>I/O R.O. Enrolment Data Quality Assurance Officer</td>
      <td>George Brown College</td>
      <td>Experience with data mining and reporting uti...</td>
      <td>Toronto, ON</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=I/O%20R.O.%20Enro...</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Jr. Data Analyst</td>
      <td>Ratehub</td>
      <td>Support in developing and maintaining our dat...</td>
      <td>Toronto, ON</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data%20Anal...</td>
    </tr>
    <tr>
      <th>59</th>
      <td>SAS Developer</td>
      <td>MSi Corp (Bell Canada)</td>
      <td>Document data mapping diagrams and data dicti...</td>
      <td>Ottawa, ON</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=SAS%20Developer%2...</td>
    </tr>
    <tr>
      <th>72</th>
      <td>Jr. Data Analyst</td>
      <td>Flex Surveys</td>
      <td>Translating complex data and research outcome...</td>
      <td>Greater Toronto Area, ON</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data%20Anal...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Junior Data Analyst</td>
      <td>OSL Retail Services Inc</td>
      <td>Acquire data from primary or secondary data s...</td>
      <td>Mississauga, ON</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20A...</td>
    </tr>
    <tr>
      <th>54</th>
      <td>Junior Asset Management Consultant and Data An...</td>
      <td>GM BluePlan Engineering</td>
      <td>Develop and analyze asset data to support ass...</td>
      <td>Vaughan, ON</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Asset%20...</td>
    </tr>
    <tr>
      <th>169</th>
      <td>Business Intelligence Specialist - Junior</td>
      <td>Bevertec CST Inc</td>
      <td>Report development and data management. O Pre...</td>
      <td>Toronto, ON</td>
      <td>4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Business%20Intell...</td>
    </tr>
    <tr>
      <th>117</th>
      <td>Research Analyst I, Commercialization</td>
      <td>University Health Network</td>
      <td>Advanced skills in statistical analysis and d...</td>
      <td>Toronto, ON</td>
      <td>4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Research%20Analys...</td>
    </tr>
    <tr>
      <th>119</th>
      <td>OPÉRATRICE OU OPÉRATEUR EN INFORMATIQUE CLASSE...</td>
      <td>Riverside School Board</td>
      <td>They make backup copies, copy compressor dest...</td>
      <td>Saint-Hubert, QC</td>
      <td>4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=OP%C3%89RATRICE%2...</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Junior Data Engineer</td>
      <td>Kora</td>
      <td>Help maintain and update the company-level da...</td>
      <td>Toronto, ON</td>
      <td>4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20E...</td>
    </tr>
    <tr>
      <th>100</th>
      <td>Junior Financial Analyst (FT)</td>
      <td>Part Time CFO Services Inc.</td>
      <td>The Junior Financial Analyst position will be...</td>
      <td>Peterborough, ON</td>
      <td>4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financia...</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Junior Business Intelligence Specialist (RQ02143)</td>
      <td>Amanst Inc</td>
      <td>Report development and data management. Prepa...</td>
      <td>Greater Toronto Area, ON</td>
      <td>5 days ago</td>
      <td>5</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business...</td>
    </tr>
    <tr>
      <th>64</th>
      <td>Data Analyst- Central Production</td>
      <td>Monsters Aliens Robots Zombies</td>
      <td>Creating data modeling techniques to calculat...</td>
      <td>Toronto, ON</td>
      <td>5 days ago</td>
      <td>5</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Analyst-%2...</td>
    </tr>
    <tr>
      <th>28</th>
      <td>IT Support – Junior Data Coordinator</td>
      <td>Wellsite Masters</td>
      <td>Coordinate and manipulate all data that is de...</td>
      <td>Calgary, AB</td>
      <td>5 days ago</td>
      <td>5</td>
      <td>https://ca.indeed.com/jobs?q=IT%20Support%20%E...</td>
    </tr>
    <tr>
      <th>68</th>
      <td>Jr. Business Analyst</td>
      <td>The Portage Mutual Insurance Company</td>
      <td>Someone who enjoys working with data and solv...</td>
      <td>Winnipeg, MB</td>
      <td>5 days ago</td>
      <td>5</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Business%20...</td>
    </tr>
    <tr>
      <th>178</th>
      <td>Laboratory Assistant I - Virology Pre-analytics</td>
      <td>Alberta Precision Laboratories</td>
      <td>You may be required to perform data entry and...</td>
      <td>Edmonton, AB</td>
      <td>5 days ago</td>
      <td>5</td>
      <td>https://ca.indeed.com/jobs?q=Laboratory%20Assi...</td>
    </tr>
    <tr>
      <th>150</th>
      <td>Laboratory Assistant I - Virology Pre-analytics</td>
      <td>Alberta Precision Labs</td>
      <td>You may be required to perform data entry and...</td>
      <td>Edmonton, AB</td>
      <td>5 days ago</td>
      <td>5</td>
      <td>https://ca.indeed.com/jobs?q=Laboratory%20Assi...</td>
    </tr>
    <tr>
      <th>81</th>
      <td>Jr. Business Intelligence Developer, Enterpris...</td>
      <td>Southlake Regional Health Centre</td>
      <td>Develop ETL procedures, SSIS packages and mai...</td>
      <td>Newmarket, ON</td>
      <td>6 days ago</td>
      <td>6</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Business%20...</td>
    </tr>
    <tr>
      <th>94</th>
      <td>Junior Graphic Marketing Specialist</td>
      <td>Excel Management Limited Partnership</td>
      <td>Through surveys, focus groups, sales and onli...</td>
      <td>Calgary, AB</td>
      <td>6 days ago</td>
      <td>6</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Graphic%...</td>
    </tr>
    <tr>
      <th>57</th>
      <td>IT Analyst I - IT Data Protection Admin</td>
      <td>Alberta Health Services</td>
      <td>Experience with reporting, monitoring, alerti...</td>
      <td>Calgary, AB</td>
      <td>6 days ago</td>
      <td>6</td>
      <td>https://ca.indeed.com/jobs?q=IT%20Analyst%20I%...</td>
    </tr>
    <tr>
      <th>58</th>
      <td>Junior MS Database Developer</td>
      <td>Blue North Strategies</td>
      <td>Data management: 3 years (preferred). &amp;gt; Co...</td>
      <td>Guelph, ON</td>
      <td>6 days ago</td>
      <td>6</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20MS%20Dat...</td>
    </tr>
    <tr>
      <th>88</th>
      <td>STATISTICAL ANALYST (I)</td>
      <td>McMaster University</td>
      <td>Recommend modifications to processes related ...</td>
      <td>Hamilton, ON</td>
      <td>6 days ago</td>
      <td>6</td>
      <td>https://ca.indeed.com/jobs?q=STATISTICAL%20ANA...</td>
    </tr>
    <tr>
      <th>70</th>
      <td>Junior Marketing Specialist</td>
      <td>RV SnapPad</td>
      <td>Using formulas to parse data and create visua...</td>
      <td>Calgary, AB</td>
      <td>6 days ago</td>
      <td>6</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Marketin...</td>
    </tr>
    <tr>
      <th>138</th>
      <td>Analyste fonctionnel I (Applicatif - atout BI)</td>
      <td>Hydro Québec</td>
      <td>Analyser les besoins informatiques et techniq...</td>
      <td>Chicoutimi, QC</td>
      <td>7 days ago</td>
      <td>7</td>
      <td>https://ca.indeed.com/jobs?q=Analyste%20foncti...</td>
    </tr>
    <tr>
      <th>142</th>
      <td>Analyste fonctionnel I (BI/Analytique)</td>
      <td>Hydro Québec</td>
      <td>Analyser les besoins informatiques et techniq...</td>
      <td>Chicoutimi, QC</td>
      <td>7 days ago</td>
      <td>7</td>
      <td>https://ca.indeed.com/jobs?q=Analyste%20foncti...</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Analyste de l’exploitation des données – Nivea...</td>
      <td>Equifax</td>
      <td>Ensure receipt of data and performs data qual...</td>
      <td>Montréal, QC</td>
      <td>7 days ago</td>
      <td>7</td>
      <td>https://ca.indeed.com/jobs?q=Analyste%20de%20l...</td>
    </tr>
    <tr>
      <th>144</th>
      <td>Analytics Product Owner I</td>
      <td>TD Bank</td>
      <td>Manage workload of analytics team; assigning ...</td>
      <td>Toronto, ON</td>
      <td>9 days ago</td>
      <td>9</td>
      <td>https://ca.indeed.com/jobs?q=Analytics%20Produ...</td>
    </tr>
    <tr>
      <th>121</th>
      <td>Business Analyst I</td>
      <td>Global Excel Management</td>
      <td>Knowledge of process and data modeling; Are y...</td>
      <td>Sherbrooke, QC</td>
      <td>9 days ago</td>
      <td>9</td>
      <td>https://ca.indeed.com/jobs?q=Business%20Analys...</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Junior Data Analyst</td>
      <td>Scandinavian Building Services</td>
      <td>Previous experience with large scale data ana...</td>
      <td>Edmonton, AB</td>
      <td>10 days ago</td>
      <td>10</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20A...</td>
    </tr>
    <tr>
      <th>45</th>
      <td>Junior Customer Service and Data Entry</td>
      <td>Pinnacle Fibres Inc.</td>
      <td>Handles quality documentation entry and onlin...</td>
      <td>Saint-Lambert, QC</td>
      <td>10 days ago</td>
      <td>10</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Customer...</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Junior Business Intelligence Analyst</td>
      <td>Great Canadian Casinos</td>
      <td>Ensures compliance with all data management p...</td>
      <td>Richmond, BC</td>
      <td>10 days ago</td>
      <td>10</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business...</td>
    </tr>
    <tr>
      <th>126</th>
      <td>Financial Analyst I</td>
      <td>Vancouver Drydock</td>
      <td>Perform reconciliations and resolve data disc...</td>
      <td>North Vancouver, BC</td>
      <td>10 days ago</td>
      <td>10</td>
      <td>https://ca.indeed.com/jobs?q=Financial%20Analy...</td>
    </tr>
    <tr>
      <th>129</th>
      <td>Analyste tarifaire junior (support administrat...</td>
      <td>GLS Canada</td>
      <td>Relevant experience in data manipulation. Nou...</td>
      <td>Dorval, QC</td>
      <td>10 days ago</td>
      <td>10</td>
      <td>https://ca.indeed.com/jobs?q=Analyste%20tarifa...</td>
    </tr>
    <tr>
      <th>98</th>
      <td>Data Steward I</td>
      <td>TD Bank</td>
      <td>Explain trends and gaps between different dat...</td>
      <td>Montréal, QC</td>
      <td>10 days ago</td>
      <td>10</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Steward%20...</td>
    </tr>
    <tr>
      <th>84</th>
      <td>Jr Business Data Analyst</td>
      <td>Youth Services Bureau of Ottawa</td>
      <td>Analyze, review, extract and summarize pertin...</td>
      <td>Ottawa, ON</td>
      <td>11 days ago</td>
      <td>11</td>
      <td>https://ca.indeed.com/jobs?q=Jr%20Business%20D...</td>
    </tr>
    <tr>
      <th>25</th>
      <td>JUNIOR FINANCIAL ANALYST</td>
      <td>Ministry of Colleges and Universities</td>
      <td>Research and analyze statistical data from a ...</td>
      <td>Toronto, ON</td>
      <td>11 days ago</td>
      <td>11</td>
      <td>https://ca.indeed.com/jobs?q=JUNIOR%20FINANCIA...</td>
    </tr>
    <tr>
      <th>87</th>
      <td>Junior Database Administrator</td>
      <td>Dawn InfoTek Inc.</td>
      <td>Provide all the Database Administrative servi...</td>
      <td>Toronto, ON</td>
      <td>11 days ago</td>
      <td>11</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Database...</td>
    </tr>
    <tr>
      <th>86</th>
      <td>Business Intelligence Reports Developer I</td>
      <td>Global Excel Management</td>
      <td>Work with all areas to resolve data issues an...</td>
      <td>Sherbrooke, QC</td>
      <td>12 days ago</td>
      <td>12</td>
      <td>https://ca.indeed.com/jobs?q=Business%20Intell...</td>
    </tr>
    <tr>
      <th>89</th>
      <td>Analyst I, Security Advisory and Data Security</td>
      <td>Moneris Solutions Corporation</td>
      <td>Knowledge of data classification and data los...</td>
      <td>Etobicoke, ON</td>
      <td>12 days ago</td>
      <td>12</td>
      <td>https://ca.indeed.com/jobs?q=Analyst%20I%2C%20...</td>
    </tr>
    <tr>
      <th>90</th>
      <td>The Bay | Jr. Data Scientist</td>
      <td>Hudson's Bay</td>
      <td>Work with various data owners to discover and...</td>
      <td>Toronto, ON</td>
      <td>12 days ago</td>
      <td>12</td>
      <td>https://ca.indeed.com/jobs?q=The%20Bay%20%7C%2...</td>
    </tr>
    <tr>
      <th>196</th>
      <td>Data Steward I, ITSS Data Governance</td>
      <td>TD Bank</td>
      <td>Complete metadata and data quality tasks. Ide...</td>
      <td>Toronto, ON</td>
      <td>12 days ago</td>
      <td>12</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Steward%20...</td>
    </tr>
    <tr>
      <th>105</th>
      <td>Junior Financial Analyst</td>
      <td>HUB International</td>
      <td>Assist in organizing building lease data and ...</td>
      <td>Chilliwack, BC</td>
      <td>12 days ago</td>
      <td>12</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financia...</td>
    </tr>
    <tr>
      <th>51</th>
      <td>Junior Research Analyst</td>
      <td>Simcoe County District School Board</td>
      <td>Research and/or data analysis; In building da...</td>
      <td>Midhurst, ON</td>
      <td>12 days ago</td>
      <td>12</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Research...</td>
    </tr>
    <tr>
      <th>46</th>
      <td>Junior Business Analyst - OpenRoad Head Office</td>
      <td>OpenRoad Auto Group</td>
      <td>Identifying opportunities that improve data a...</td>
      <td>Richmond, BC</td>
      <td>12 days ago</td>
      <td>12</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business...</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Junior Machine Learning Scientist</td>
      <td>Ecoation</td>
      <td>Analyzing customer horticultural data to prov...</td>
      <td>North Vancouver, BC</td>
      <td>12 days ago</td>
      <td>12</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Machine%...</td>
    </tr>
    <tr>
      <th>38</th>
      <td>Junior Financial Analyst</td>
      <td>Sault Area Hospital Foundation</td>
      <td>Create and design reports and spreadsheets to...</td>
      <td>Sault Ste. Marie, ON</td>
      <td>12 days ago</td>
      <td>12</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financia...</td>
    </tr>
    <tr>
      <th>49</th>
      <td>Jr Data Analyst</td>
      <td>JELD-WEN, inc</td>
      <td>Strong knowledge of using multiple query tool...</td>
      <td>Woodbridge, ON</td>
      <td>12 days ago</td>
      <td>12</td>
      <td>https://ca.indeed.com/jobs?q=Jr%20Data%20Analy...</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Junior EA &amp; Data Entry Associate</td>
      <td>Redwood Classics Apparel</td>
      <td>Facilitates/attends special working group mee...</td>
      <td>Toronto, ON</td>
      <td>13 days ago</td>
      <td>13</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20EA%20%26...</td>
    </tr>
    <tr>
      <th>186</th>
      <td>Analyst, Client Business I</td>
      <td>Mosaic North America</td>
      <td>Interpret data, formulate reports, and make r...</td>
      <td>Toronto, ON</td>
      <td>13 days ago</td>
      <td>13</td>
      <td>https://ca.indeed.com/jobs?q=Analyst%2C%20Clie...</td>
    </tr>
    <tr>
      <th>190</th>
      <td>Junior Financial Analyst</td>
      <td>The Group Master</td>
      <td>Reporting to the assistant controller, the ju...</td>
      <td>Boucherville, QC</td>
      <td>13 days ago</td>
      <td>13</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financia...</td>
    </tr>
    <tr>
      <th>118</th>
      <td>RESEARCH/DATABASE COORDINATOR I (Data Custodian)</td>
      <td>Centre for Global Health Research</td>
      <td>Experience working with GIS/spatial data, hea...</td>
      <td>Toronto, ON</td>
      <td>14 days ago</td>
      <td>14</td>
      <td>https://ca.indeed.com/jobs?q=RESEARCH/DATABASE...</td>
    </tr>
    <tr>
      <th>50</th>
      <td>Junior Business Analyst</td>
      <td>Pivotree</td>
      <td>Prototyping - Create wireframes of potential ...</td>
      <td>Toronto, ON</td>
      <td>14 days ago</td>
      <td>14</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business...</td>
    </tr>
    <tr>
      <th>53</th>
      <td>Financial Analyst (Program), Junior</td>
      <td>General Dynamics Missions Systems-Canada</td>
      <td>Support program audit requirements and reques...</td>
      <td>Ottawa, ON</td>
      <td>14 days ago</td>
      <td>14</td>
      <td>https://ca.indeed.com/jobs?q=Financial%20Analy...</td>
    </tr>
    <tr>
      <th>158</th>
      <td>Financial Analyst I (Contract)</td>
      <td>Duca</td>
      <td>As part of the Financial Planning &amp;amp; Analy...</td>
      <td>Toronto, ON</td>
      <td>16 days ago</td>
      <td>16</td>
      <td>https://ca.indeed.com/jobs?q=Financial%20Analy...</td>
    </tr>
    <tr>
      <th>173</th>
      <td>Financial Analyst I (Contract)</td>
      <td>DUCA Financial Services Credit Union Ltd.</td>
      <td>As part of the Financial Planning &amp;amp; Analy...</td>
      <td>Toronto, ON</td>
      <td>16 days ago</td>
      <td>16</td>
      <td>https://ca.indeed.com/jobs?q=Financial%20Analy...</td>
    </tr>
    <tr>
      <th>128</th>
      <td>Jr. Murex Business Analyst</td>
      <td>CPQi</td>
      <td>Knowledge and understanding of Murex features...</td>
      <td>Halifax, NS</td>
      <td>17 days ago</td>
      <td>17</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Murex%20Bus...</td>
    </tr>
    <tr>
      <th>44</th>
      <td>Jr. Data Engineer - Vancouver</td>
      <td>Randstad</td>
      <td>Proactively monitor data flow across systems ...</td>
      <td>Vancouver, BC</td>
      <td>17 days ago</td>
      <td>17</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data%20Engi...</td>
    </tr>
    <tr>
      <th>36</th>
      <td>Junior Data Analyst</td>
      <td>The Mustard Seed</td>
      <td>Analyze donor and volunteer data to ensure th...</td>
      <td>Calgary, AB</td>
      <td>18 days ago</td>
      <td>18</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20A...</td>
    </tr>
    <tr>
      <th>107</th>
      <td>Marketing &amp; Content Jr. Analyst</td>
      <td>Stingray</td>
      <td>Identify and extract relevant performance ana...</td>
      <td>Montréal, QC</td>
      <td>18 days ago</td>
      <td>18</td>
      <td>https://ca.indeed.com/jobs?q=Marketing%20%26%2...</td>
    </tr>
    <tr>
      <th>103</th>
      <td>Business Analyst I, Wireless Fulfillment (Logi...</td>
      <td>TELUS</td>
      <td>Manage and monitor data and inputs required f...</td>
      <td>Scarborough, ON</td>
      <td>19 days ago</td>
      <td>19</td>
      <td>https://ca.indeed.com/jobs?q=Business%20Analys...</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Junior Research Analyst</td>
      <td>Carleton University</td>
      <td>?experience organizing and validating data. ?...</td>
      <td>Ottawa, ON</td>
      <td>19 days ago</td>
      <td>19</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Research...</td>
    </tr>
    <tr>
      <th>65</th>
      <td>Trading Desk Analyst</td>
      <td>Aquanow</td>
      <td>Daily processing of transactions and key cont...</td>
      <td>Vancouver, BC</td>
      <td>19 days ago</td>
      <td>19</td>
      <td>https://ca.indeed.com/jobs?q=Trading%20Desk%20...</td>
    </tr>
    <tr>
      <th>91</th>
      <td>Junior BI Analytics Developer - Bilingual</td>
      <td>AstraNorth</td>
      <td>Primary Skills*: BI Tools - tableau, . NET , ...</td>
      <td>Montréal, QC</td>
      <td>19 days ago</td>
      <td>19</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20BI%20Ana...</td>
    </tr>
    <tr>
      <th>52</th>
      <td>Jr. Quality Assurance Analyst (Manufacturing)</td>
      <td>MDA</td>
      <td>Implementing approved sampling, reporting and...</td>
      <td>Kanata, ON</td>
      <td>20 days ago</td>
      <td>20</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Quality%20A...</td>
    </tr>
    <tr>
      <th>114</th>
      <td>Finance Ops Analyst I</td>
      <td>TD Bank</td>
      <td>Support the collection of meaningful data and...</td>
      <td>Dieppe, NB</td>
      <td>24 days ago</td>
      <td>24</td>
      <td>https://ca.indeed.com/jobs?q=Finance%20Ops%20A...</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Junior Data Analyst</td>
      <td>O2E Brands</td>
      <td>Passion for data visualization with Tableau. ...</td>
      <td>Vancouver, BC</td>
      <td>24 days ago</td>
      <td>24</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20A...</td>
    </tr>
    <tr>
      <th>182</th>
      <td>Analyst, Business I</td>
      <td>Mosaic North America</td>
      <td>Interpret data, formulate reports, and make r...</td>
      <td>Toronto, ON</td>
      <td>24 days ago</td>
      <td>24</td>
      <td>https://ca.indeed.com/jobs?q=Analyst%2C%20Busi...</td>
    </tr>
    <tr>
      <th>113</th>
      <td>Junior Financial Analyst /Bookkeeper</td>
      <td>Process Fusion Inc.</td>
      <td>Collect, interpret, and report on financial d...</td>
      <td>Toronto, ON</td>
      <td>25 days ago</td>
      <td>25</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financia...</td>
    </tr>
    <tr>
      <th>109</th>
      <td>Business Analytics Specialist I</td>
      <td>InComm Payments</td>
      <td>This is a career building opportunity for rec...</td>
      <td>Mississauga, ON</td>
      <td>26 days ago</td>
      <td>26</td>
      <td>https://ca.indeed.com/jobs?q=Business%20Analyt...</td>
    </tr>
    <tr>
      <th>60</th>
      <td>CT Data Engineer I - Power BI</td>
      <td>EY</td>
      <td>Reviewing and understanding complex data sets...</td>
      <td>Toronto, ON</td>
      <td>26 days ago</td>
      <td>26</td>
      <td>https://ca.indeed.com/jobs?q=CT%20Data%20Engin...</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Junior Business Analyst</td>
      <td>Eastwood and Cleef</td>
      <td>\*Tasks include, but are not limited to: clie...</td>
      <td>Toronto, ON</td>
      <td>26 days ago</td>
      <td>26</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business...</td>
    </tr>
    <tr>
      <th>99</th>
      <td>Junior Data Scientist</td>
      <td>Providence Health Care</td>
      <td>Reviews clinical data at aggregate levels on ...</td>
      <td>Vancouver, BC</td>
      <td>27 days ago</td>
      <td>27</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20S...</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Junior Data Analysis Assistant</td>
      <td>Universal Rehabilitation Service Agency</td>
      <td>Support the Program Director to create proces...</td>
      <td>Calgary, AB</td>
      <td>28 days ago</td>
      <td>28</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20A...</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Junior Machine Learning Engineer / Data Scientist</td>
      <td>Virtus Groups</td>
      <td>Our client is seeking a Junior Machine Learni...</td>
      <td>Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Machine%...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Junior Machine Learning Engineer / Data Scientist</td>
      <td>Virtus Groups</td>
      <td>Candidates must be a Canadian Citizen or Perm...</td>
      <td>Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Machine%...</td>
    </tr>
    <tr>
      <th>177</th>
      <td>Junior Quantitative Analyst</td>
      <td>Société Générale</td>
      <td>Assessing data quality and consistency betwee...</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Quantita...</td>
    </tr>
    <tr>
      <th>160</th>
      <td>MARKETING SPECIALIST</td>
      <td>ABI - Allstream Business Inc</td>
      <td>This is a junior marketing role with experien...</td>
      <td>Mississauga, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=MARKETING%20SPECI...</td>
    </tr>
    <tr>
      <th>66</th>
      <td>Junior Business Intelligence Analyst</td>
      <td>Secure Energy</td>
      <td>Inform data integrity and tool availability. ...</td>
      <td>Calgary, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business...</td>
    </tr>
    <tr>
      <th>41</th>
      <td>Junior Database Administrator</td>
      <td>OkRx</td>
      <td>Perform complex data migration procedures. Se...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Database...</td>
    </tr>
    <tr>
      <th>42</th>
      <td>Junior Business Analyst</td>
      <td>RPM TECHNOLOGIES CORP</td>
      <td>Documenting and analyzing the required inform...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business...</td>
    </tr>
    <tr>
      <th>97</th>
      <td>Toronto - Junior Technical Business Analyst/ J...</td>
      <td>FDM Group</td>
      <td>These roles are crucial in helping organizati...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Toronto%20-%20Jun...</td>
    </tr>
    <tr>
      <th>96</th>
      <td>Junior Engineer - Logistics Simulation &amp; Busin...</td>
      <td>Ausenco</td>
      <td>Many of the projects will employ logistics si...</td>
      <td>Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Engineer...</td>
    </tr>
    <tr>
      <th>95</th>
      <td>Junior Pricing Analyst</td>
      <td>Bélanger UPT</td>
      <td>Collects data and maintains the database. Pre...</td>
      <td>Mississauga, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Pricing%...</td>
    </tr>
    <tr>
      <th>93</th>
      <td>Junior Pricing/ Program Analyst</td>
      <td>Brandt</td>
      <td>Extract and manipulate large data sets to reg...</td>
      <td>Regina, SK</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Pricing/...</td>
    </tr>
    <tr>
      <th>47</th>
      <td>Field Data Scientist I / Junior Field Data Sci...</td>
      <td>ThinkData Works</td>
      <td>Conducting research to identify data sources ...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Field%20Data%20Sc...</td>
    </tr>
    <tr>
      <th>48</th>
      <td>Junior Data Analyst / IT Support Technician</td>
      <td>The Stevens Company Limited</td>
      <td>In-depth knowledge of applicable data privacy...</td>
      <td>Brampton, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20A...</td>
    </tr>
    <tr>
      <th>85</th>
      <td>Junior Sales Data Coordinator</td>
      <td>Bélanger UPT</td>
      <td>Reporting to the National Sales &amp;amp; Marketi...</td>
      <td>Mississauga, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Sales%20...</td>
    </tr>
    <tr>
      <th>83</th>
      <td>Junior Marketing Associate - Internship</td>
      <td>AltaML</td>
      <td>As the Junior Marketing Associate, you will l...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Marketin...</td>
    </tr>
    <tr>
      <th>102</th>
      <td>Junior Financial Analyst</td>
      <td>Community Natural Foods</td>
      <td>Distribute incoming mail (inter office &amp;amp; ...</td>
      <td>Calgary, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financia...</td>
    </tr>
    <tr>
      <th>82</th>
      <td>Junior Online Marketing Analyst</td>
      <td>Core Online Marketing</td>
      <td>Analytical Skills to interpret data and prese...</td>
      <td>Oakville, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Online%2...</td>
    </tr>
    <tr>
      <th>56</th>
      <td>Data Analyst</td>
      <td>WorkTango</td>
      <td>Manage our ETL process for client data transf...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Analyst%20...</td>
    </tr>
    <tr>
      <th>61</th>
      <td>Jr. Data Scientist</td>
      <td>SimpTek Technologies</td>
      <td>Integration with 3rd party API’s for data col...</td>
      <td>Fredericton, NB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data%20Scie...</td>
    </tr>
    <tr>
      <th>77</th>
      <td>Junior Database Analyst</td>
      <td>HealthHub Solutions</td>
      <td>Maintain reliability, stability and data inte...</td>
      <td>Mississauga, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Database...</td>
    </tr>
    <tr>
      <th>73</th>
      <td>Junior Financial Analyst, Consulting</td>
      <td>BDO</td>
      <td>Strong data collection and analytical skills ...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financia...</td>
    </tr>
    <tr>
      <th>62</th>
      <td>Junior Business Analyst</td>
      <td>Miller Paving Limited</td>
      <td>Analyzing and summarizing various sales and o...</td>
      <td>Whitby, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business...</td>
    </tr>
    <tr>
      <th>71</th>
      <td>Benefits Analyst (Junior)</td>
      <td>JRP Employee Benefit Solutions</td>
      <td>Request or run reports to gather data from in...</td>
      <td>Winnipeg, MB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Benefits%20Analys...</td>
    </tr>
    <tr>
      <th>63</th>
      <td>Junior/Senior Data Scientist</td>
      <td>TELUS</td>
      <td>You’ll collaborate with teams across the comp...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior/Senior%20D...</td>
    </tr>
    <tr>
      <th>55</th>
      <td>Junior Big Data Engineer, Business Intelligenc...</td>
      <td>CBC/Radio-Canada</td>
      <td>Batch-processed data as well as streaming dat...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Big%20Da...</td>
    </tr>
    <tr>
      <th>104</th>
      <td>Data I/O Coordinator</td>
      <td>FuseFX</td>
      <td>Identifying discrepancies, and errors in data...</td>
      <td>Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Data%20I/O%20Coor...</td>
    </tr>
    <tr>
      <th>39</th>
      <td>Junior Analyst Intern, Data &amp; Technology (4-mo...</td>
      <td>University Pension Plan</td>
      <td>Experience with basic data querying (SQL Serv...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Analyst%...</td>
    </tr>
    <tr>
      <th>106</th>
      <td>Jr. Business Analyst</td>
      <td>Intimate Interactive Advertising</td>
      <td>Monitor reports and analyze data to identify ...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Business%20...</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Data Analytics Junior Technologist B</td>
      <td>St. Clair College</td>
      <td>Previous experience working with large data s...</td>
      <td>Windsor, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Analytics%...</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Junior Business Analyst – CPM/BI</td>
      <td>Corporate Renaissance Group</td>
      <td>Assist in data transformation and validation....</td>
      <td>Ottawa, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business...</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Jr. Data/Reporting Analyst</td>
      <td>Scarsin</td>
      <td>Data management, data analysis and ETL proces...</td>
      <td>Markham, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data/Report...</td>
    </tr>
    <tr>
      <th>134</th>
      <td>Jr Financial Analyst - Rogers Insurance</td>
      <td>Sharp Insurance</td>
      <td>Strong attention to detail while maintaining ...</td>
      <td>Calgary, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr%20Financial%20...</td>
    </tr>
    <tr>
      <th>67</th>
      <td>Junior Data Engineer – Client Innovation Cente...</td>
      <td>Groom &amp; Associes</td>
      <td>Knowledge of tools to perform data quality, d...</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20E...</td>
    </tr>
    <tr>
      <th>130</th>
      <td>Financial Business Analyst / Junior Accountant</td>
      <td>Cam Clark Auto Group</td>
      <td>Experience with interactive data visualizatio...</td>
      <td>Airdrie, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Financial%20Busin...</td>
    </tr>
    <tr>
      <th>127</th>
      <td>Inventory Coordinator I</td>
      <td>Groupe Robert</td>
      <td>Maintain inventory data integrity and tracks ...</td>
      <td>Mississauga, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Inventory%20Coord...</td>
    </tr>
    <tr>
      <th>125</th>
      <td>Montreal - Analyste Technique Junior ou chef d...</td>
      <td>FDM Group</td>
      <td>Certains postes courants dans lesquels vous p...</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Montreal%20-%20An...</td>
    </tr>
    <tr>
      <th>124</th>
      <td>Jr Financial Analyst</td>
      <td>Rogers Insurance Ltd</td>
      <td>Strong attention to detail while maintaining ...</td>
      <td>Calgary, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr%20Financial%20...</td>
    </tr>
    <tr>
      <th>122</th>
      <td>Ingénieur de données I / Data Engineer I</td>
      <td>CAE Inc.</td>
      <td>Keep data separated and secure across nationa...</td>
      <td>Saint-Laurent, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Ing%C3%A9nieur%20...</td>
    </tr>
    <tr>
      <th>120</th>
      <td>MES Business Analyst</td>
      <td>SyLogix Consulting Inc.</td>
      <td>Prior experience with OSIsoft PI or another d...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=MES%20Business%20...</td>
    </tr>
    <tr>
      <th>116</th>
      <td>Financial Analyst I, CCRU</td>
      <td>University Health Network</td>
      <td>Experience with financial and cost accounting...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Financial%20Analy...</td>
    </tr>
    <tr>
      <th>115</th>
      <td>Junior Business Analyst</td>
      <td>Genpact</td>
      <td>Expertise in Excel and PowerPoint including P...</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business...</td>
    </tr>
    <tr>
      <th>112</th>
      <td>I.T Business Analyst (Contract)</td>
      <td>Alberta Motor Association</td>
      <td>You have a knack for data and details, withou...</td>
      <td>Edmonton, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=I.T%20Business%20...</td>
    </tr>
    <tr>
      <th>111</th>
      <td>Clinical Data Manager I</td>
      <td>Labcorp</td>
      <td>Perform reconciliation of the clinical databa...</td>
      <td>Canada</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Clinical%20Data%2...</td>
    </tr>
    <tr>
      <th>110</th>
      <td>Junior Research Analyst (Fluency in Chinese/Fr...</td>
      <td>BLUE UMBRELLA LIMITED</td>
      <td>Accurately summarize the collected data and p...</td>
      <td>Mississauga, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Research...</td>
    </tr>
    <tr>
      <th>108</th>
      <td>Business Analyst I</td>
      <td>TES - The Employment Solution</td>
      <td>Errors are generally related to user data/pro...</td>
      <td>Edmonton, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Business%20Analys...</td>
    </tr>
  </tbody>
</table>
</div>




```python

```

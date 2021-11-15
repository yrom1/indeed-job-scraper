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

MAX_NUMBER_OF_PAGES_PER_SEARCH = 10 # testing

pages = []
for start in range(0, MAX_NUMBER_OF_PAGES_PER_SEARCH*10, 10):
    page = requests.get('https://ca.indeed.com/jobs?q=data%20junior&l=Canada&start=' + str(start))
    soup = BeautifulSoup(page.text, 'html.parser')
    pages.append(soup)
    time.sleep(random.randrange(3, 6) + random.random())
```


```python
# from bs4 import BeautifulSoup
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.set_page_load_timeout(5)
# driver.get('https://ca.indeed.com/jobs?q=data%20junior&l=Canada&start=0')
# html = driver.page_source
# soup = BeautifulSoup(html)

# # check out the docs for the kinds of things you can do with 'find_all'
# # this (untested) snippet should find tags with a specific class ID
# # see: http://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-by-css-class
# for tag in soup.find_all("div", class_="jobsearch-SerpJobCard unifiedRow row result"):
#     print(tag.text)
```


```python
import re

TEST_INPUT = """<ul style="list-style-type:circle;margin-top: 0px;margin-bottom: 0px;padding-left:20px;">\n<li style="margin-bottom:0px;">Interpret <b>data</b>, formulate reports, and make recommendations to the team.</li>\n<li>Remain fully informed on latest <b>data</b> trends, practice, and process.</li>\n</ul><ul style="list-style-type:circle;margin-top: 0px;margin-bottom: 0px;padding-left:20px;">\n<li style="margin-bottom:0px;">Interpret <b>data</b>, formulate reports, and make recommendations to the team.</li>\n<li>Remain fully informed on latest <b>data</b> trends, practice, and process.</li>\n</ul>"""

def clean_HTML(input: str) -> str:
    """I can't display HTML inside a cell in a DataFrame (it seems)"""
    # remove tags <somethign> and leave contents between tags
    out = re.sub("<.*?>", '', input)
    out = re.sub('\n', ' ', out)
    return out

print(clean_HTML(TEST_INPUT))
```

     Interpret data, formulate reports, and make recommendations to the team. Remain fully informed on latest data trends, practice, and process.  Interpret data, formulate reports, and make recommendations to the team. Remain fully informed on latest data trends, practice, and process. 



```python
# When you search there's box cards for each posting, the class for the box is:
# class="jobsearch-SerpJobCard unifiedRow row result clickcard"
# that wasn't working for me though, so I changed it to 'class':"job_seen_beacon"

titles = pd.Series([], dtype='string')
companyNames = pd.Series([], dtype='string')
jobSnippets = pd.Series([], dtype='string')
locations = pd.Series([], dtype='string')
dates = pd.Series([], dtype='string')
for page in pages:
    jobs = page.find_all('div', attrs={'class':"job_seen_beacon"})
    for job in jobs:
        
        # Job Title
        title = job.find('h2', attrs={'class':'jobTitle'}).find('span', attrs={'title':True}).next 
        titles = titles.append(pd.Series([str(title)]))

        # Company Name
        companyName = job.find('span', attrs={'class':'companyName'})
        tempCompanyName = companyName
        companyName = companyName.find('a', attrs={'class':'turnstileLink companyOverviewLink'})
        if companyName is None: companyName = tempCompanyName
        companyName = companyName.next       
        companyNames = companyNames.append(pd.Series([str(companyName)]))
        
        # Job snip
        jobSnippet = job.find('div', attrs={'class':'job-snippet'}).next
        jobSnippets = jobSnippets.append(pd.Series([str(clean_HTML(str(jobSnippet)))]))

        # Location
        location = job.find('div', attrs={'class':'companyLocation'}).next
        locations = locations.append(pd.Series([str(location)]))

        # Posting Date
        date = job.find('span', attrs={'class':'date'}).next
        dates = dates.append(pd.Series([str(date)]))
        
pd.set_option('display.max_colwidth', None)
#titles, companyNames, jobSnippets
job

```




    <div class="job_seen_beacon"><table cellpadding="0" cellspacing="0" class="jobCard_mainContent" role="presentation"><tbody><tr><td class="resultContent"><div class="heading4 color-text-primary singleLineTitle tapItem-gutter"><h2 class="jobTitle jobTitle-color-purple"><span title="Data Steward I, ITSS Data Governance">Data Steward I, ITSS Data Governance</span></h2></div><div class="heading6 company_location tapItem-gutter"><pre><span class="companyName"><a class="turnstileLink companyOverviewLink" data-tn-element="companyName" href="/cmp/Td-Bank" rel="noopener" target="_blank">TD Bank</a></span><span class="ratingsDisplay withRatingLink"><a class="ratingLink" data-tn-variant="cmplinktst2" href="/cmp/Td-Bank/reviews" rel="noopener" target="_blank" title="TD Bank reviews"><span aria-label="3.8 of stars rating" class="ratingNumber" role="img"><span aria-hidden="true">3.8</span><svg aria-hidden="true" class="starIcon" fill="none" height="12" role="presentation" viewbox="0 0 16 16" width="12" xmlns="http://www.w3.org/2000/svg"><path d="M8 12.8709L12.4542 15.5593C12.7807 15.7563 13.1835 15.4636 13.0968 15.0922L11.9148 10.0254L15.8505 6.61581C16.1388 6.36608 15.9847 5.89257 15.6047 5.86033L10.423 5.42072L8.39696 0.640342C8.24839 0.289808 7.7516 0.289808 7.60303 0.640341L5.57696 5.42072L0.395297 5.86033C0.015274 5.89257 -0.13882 6.36608 0.149443 6.61581L4.0852 10.0254L2.90318 15.0922C2.81653 15.4636 3.21932 15.7563 3.54584 15.5593L8 12.8709Z" fill="#767676"></path></svg></span></a></span><div class="companyLocation">Toronto, ON</div></pre></div><div class="heading6 error-text tapItem-gutter"></div></td></tr></tbody></table><table class="jobCardShelfContainer" role="presentation"><tbody><tr class="jobCardShelf"></tr><tr class="underShelfFooter"><td><div class="heading6 tapItem-gutter result-footer"><div class="job-snippet"><ul style="list-style-type:circle;margin-top: 0px;margin-bottom: 0px;padding-left:20px;">
    <li style="margin-bottom:0px;">Complete metadata and <b>data</b> quality tasks.</li>
    <li style="margin-bottom:0px;">Identify and monitor the quality of critical <b>data</b> elements.</li>
    <li>Manage <b>data</b> work activities requiring coordination across…</li>
    </ul></div><span class="date">11 days ago</span><span class="result-link-bar-separator">·</span><button aria-expanded="false" class="sl resultLink more_links_button" type="button">More...</button></div><div class="tab-container"><div class="more-links-container result-tab" role="presentation"><div class="more_links"><button aria-label="Close" class="close-button" title="Close" type="button"></button><ul><li><span class="mat">View all <a href="/Td-Bank-jobs">TD Bank jobs</a> - <a href="/jobs-in-Toronto,-ON">Toronto jobs</a></span></li><li><span class="mat">Salary Search: <a href="/career/steward/salaries/Toronto--ON?campaignid=serp-more&amp;fromjk=a389fb7810071a50&amp;from=serp-more">Data Steward I, ITSS Data Governance salaries in Toronto, ON</a></span></li><li><span class="mat">See popular <a href="/cmp/Td-Bank/faq">questions &amp; answers about TD Bank</a></span></li></ul></div></div></div></td></tr></tbody></table><div aria-live="polite"></div></div>




```python
def clean_date_Series(input: str) -> str:
    """Remove the characters from the days ago posting col
    so I can sort postings by that number."""
    output = re.sub('\D', '', input)
    output = re.sub('\s*', '', output)
    output = int(output)
    return output

TEST_DATE = """23 days ago"""
assert clean_date_Series(TEST_DATE) == 23
clean_dates = dates.apply(clean_date_Series)
```


```python
assert len(titles) == len(companyNames) == len(jobSnippets) == len(locations) == len(dates) == len(clean_dates)
df = pd.DataFrame({f'{titles=}'.split('=')[0]: titles, f'{companyNames=}'.split('=')[0]: companyNames, f'{jobSnippets=}'.split('=')[0]: jobSnippets, f'{locations=}'.split('=')[0]: locations, f'{dates=}'.split('=')[0]: dates, f'{clean_dates=}'.split('=')[0]: clean_dates})
df = df.reset_index()
df.tail()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
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
      <th>136</th>
      <td>0</td>
      <td>Analyst, Business I</td>
      <td>Mosaic North America</td>
      <td>Interpret data, formulate reports, and make recommendations to the team. Remain fully informed on latest data trends, practice, and process.</td>
      <td>Toronto, ON</td>
      <td>24 days ago</td>
      <td>24</td>
    </tr>
    <tr>
      <th>137</th>
      <td>0</td>
      <td>Laboratory Assistant I - Virology Pre-analytics</td>
      <td>Alberta Precision Laboratories</td>
      <td>You may be required to perform data entry and specimen processing functions in other areas of the lab. As a Laboratory Assistant I, Clinical Microbiology …</td>
      <td>Edmonton, AB</td>
      <td>4 days ago</td>
      <td>4</td>
    </tr>
    <tr>
      <th>138</th>
      <td>0</td>
      <td>Business Development Analyst I</td>
      <td>Best Buy Canada</td>
      <td>Provides insights to team on key opportunities areas of growth with existing and new categories, through analysis of key market data.</td>
      <td>Burnaby, BC</td>
      <td>10 days ago</td>
      <td>10</td>
    </tr>
    <tr>
      <th>139</th>
      <td>0</td>
      <td>Junior Financial Analyst</td>
      <td>The Group Master</td>
      <td>Reporting to the assistant controller, the junior financial analyst is a key player in producing information that helps decision-making.</td>
      <td>Boucherville, QC</td>
      <td>12 days ago</td>
      <td>12</td>
    </tr>
    <tr>
      <th>140</th>
      <td>0</td>
      <td>Data Steward I, ITSS Data Governance</td>
      <td>TD Bank</td>
      <td>Complete metadata and data quality tasks. Identify and monitor the quality of critical data elements. Manage data work activities requiring coordination across…</td>
      <td>Toronto, ON</td>
      <td>11 days ago</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
sorted_df = df.sort_values(f'{clean_dates=}'.split('=')[0])
sorted_df.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
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
      <th>27</th>
      <td>0</td>
      <td>Analyste PMO junior - Junior PMO Analyst</td>
      <td>Gameloft</td>
      <td>Being responsible for the regular data analytics, report generation and key performance indicators. 1 year of experience in project management or PMO-related…</td>
      <td>Montréal, QC</td>
      <td>1 day ago</td>
      <td>1</td>
    </tr>
    <tr>
      <th>45</th>
      <td>0</td>
      <td>SAS Developer</td>
      <td>MSi Corp (Bell Canada)</td>
      <td>Document data mapping diagrams and data dictionaries. Work with business analysts to understand the business requirements for data modelling and data context.</td>
      <td>Ottawa, ON</td>
      <td>2 days ago</td>
      <td>2</td>
    </tr>
    <tr>
      <th>60</th>
      <td>0</td>
      <td>I/O R.O. Enrolment Data Quality Assurance Officer</td>
      <td>George Brown College</td>
      <td>Experience with data mining and reporting utilizing current software applications such as Microsoft Access, SQL data mining and reporting is required.</td>
      <td>Toronto, ON</td>
      <td>2 days ago</td>
      <td>2</td>
    </tr>
    <tr>
      <th>59</th>
      <td>0</td>
      <td>Jr. Data Analyst</td>
      <td>Flex Surveys</td>
      <td>Translating complex data and research outcomes into engaging and actionable formats for clients. We offer an array of survey consulting services and develop…</td>
      <td>Greater Toronto Area, ON</td>
      <td>2 days ago</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>Junior Data Analyst</td>
      <td>FlightHub</td>
      <td>Analyzing data sets and identifying trends and patterns; Our team will count on you to use data from various sources to identify issues as they happen and to…</td>
      <td>Montréal, QC</td>
      <td>2 days ago</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



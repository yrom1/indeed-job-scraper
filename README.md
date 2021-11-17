```python
import pandas as pd
```


```python
import src.main
src.main.__doc__
```




    'Indeed job posting scraper.'




```python
from src.main import main
main.__doc__
```




    'Scrape indeed for job postings based on input.\n    Args:\n        input: String to search on indeed.\n    '




```python
df = main("data junior")
```


```python
# number of jobs postings scraped
len(df)
```




    127




```python
# some basic data is scraped, enough to see if clicking the link is interesting
pd.set_option('display.max_colwidth', None)
df[['titles', 'companyNames', 'jobSnippets', 'locations', 'dates']].head()
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>73</th>
      <td>Data Scientist I</td>
      <td>TD Bank</td>
      <td>Capture and analyze information or data on current and future trends. You will employ these disciplines to help create data related solutions to drive business…</td>
      <td>Toronto, ON</td>
      <td>Today</td>
    </tr>
    <tr>
      <th>88</th>
      <td>Research Analyst I</td>
      <td>SickKids</td>
      <td>The Bassani lab has a number of new projects focused at improving the data collection procedures through reducing the dimensionality of data collection tools,…</td>
      <td>Toronto, ON</td>
      <td>Just posted</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Junior Machine Learning Scientist</td>
      <td>Ecoation</td>
      <td>Analyzing customer horticultural data to provide meaningful insights. Occasional field visits to greenhouses to collect data, develop or test approaches.</td>
      <td>North Vancouver, BC</td>
      <td>Today</td>
    </tr>
    <tr>
      <th>120</th>
      <td>BI Developer - I</td>
      <td>Best Buy Canada</td>
      <td>Some experience manipulating data with Python. Guarantee the accuracy of your products by proactively and regularly validating against raw data using SQL.</td>
      <td>Burnaby, BC</td>
      <td>Today</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Junior Business Analyst intern</td>
      <td>Jonar</td>
      <td>As a Junior Business Analyst, you’ll learn how to analyze and work with complex data, design workflows and use cases, and provide suggestions on how to improve…</td>
      <td>Montréal, QC</td>
      <td>Today</td>
    </tr>
  </tbody>
</table>
</div>




```python
# this output is best viewed in VSCode
df
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
      <th>73</th>
      <td>Data Scientist I</td>
      <td>TD Bank</td>
      <td>Capture and analyze information or data on current and future trends. You will employ these disciplines to help create data related solutions to drive business…</td>
      <td>Toronto, ON</td>
      <td>Today</td>
      <td>0</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Scientist%20I%20TD%20Bank</td>
    </tr>
    <tr>
      <th>88</th>
      <td>Research Analyst I</td>
      <td>SickKids</td>
      <td>The Bassani lab has a number of new projects focused at improving the data collection procedures through reducing the dimensionality of data collection tools,…</td>
      <td>Toronto, ON</td>
      <td>Just posted</td>
      <td>0</td>
      <td>https://ca.indeed.com/jobs?q=Research%20Analyst%20I%20SickKids</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Junior Machine Learning Scientist</td>
      <td>Ecoation</td>
      <td>Analyzing customer horticultural data to provide meaningful insights. Occasional field visits to greenhouses to collect data, develop or test approaches.</td>
      <td>North Vancouver, BC</td>
      <td>Today</td>
      <td>0</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Machine%20Learning%20Scientist%20Ecoation</td>
    </tr>
    <tr>
      <th>120</th>
      <td>BI Developer - I</td>
      <td>Best Buy Canada</td>
      <td>Some experience manipulating data with Python. Guarantee the accuracy of your products by proactively and regularly validating against raw data using SQL.</td>
      <td>Burnaby, BC</td>
      <td>Today</td>
      <td>0</td>
      <td>https://ca.indeed.com/jobs?q=BI%20Developer%20-%20I%20Best%20Buy%20Canada</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Junior Business Analyst intern</td>
      <td>Jonar</td>
      <td>As a Junior Business Analyst, you’ll learn how to analyze and work with complex data, design workflows and use cases, and provide suggestions on how to improve…</td>
      <td>Montréal, QC</td>
      <td>Today</td>
      <td>0</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20intern%20Jonar</td>
    </tr>
    <tr>
      <th>98</th>
      <td>Analyst, Client Data I</td>
      <td>Mosaic North America</td>
      <td>Intermediate knowledge of data cleansing and data transformation using systems such as Azure Databricks, Alteryx, SQL, and R/Python.</td>
      <td>Toronto, ON</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Analyst%2C%20Client%20Data%20I%20Mosaic%20North%20America</td>
    </tr>
    <tr>
      <th>36</th>
      <td>Analyste PMO junior - Junior PMO Analyst</td>
      <td>Gameloft</td>
      <td>Being responsible for the regular data analytics, report generation and key performance indicators. 1 year of experience in project management or PMO-related…</td>
      <td>Montréal, QC</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Analyste%20PMO%20junior%20-%20Junior%20PMO%20Analyst%20Gameloft</td>
    </tr>
    <tr>
      <th>64</th>
      <td>Data Engineer - Level I</td>
      <td>Swift Medical</td>
      <td>As the world leader in digital wound care management, we deliver advanced wound care visualization and touchless 3D measurement through our smartphone-ready…</td>
      <td>Toronto, ON</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Engineer%20-%20Level%20I%20Swift%20Medical</td>
    </tr>
    <tr>
      <th>52</th>
      <td>SAS Developer</td>
      <td>MSi Corp (Bell Canada)</td>
      <td>Document data mapping diagrams and data dictionaries. Work with business analysts to understand the business requirements for data modelling and data context.</td>
      <td>Ottawa, ON</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=SAS%20Developer%20MSi%20Corp%20%28Bell%20Canada%29</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Junior Data Analyst</td>
      <td>FlightHub</td>
      <td>Analyzing data sets and identifying trends and patterns; Our team will count on you to use data from various sources to identify issues as they happen and to…</td>
      <td>Montréal, QC</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20FlightHub</td>
    </tr>
    <tr>
      <th>70</th>
      <td>I/O R.O. Enrolment Data Quality Assurance Officer</td>
      <td>George Brown College</td>
      <td>Experience with data mining and reporting utilizing current software applications such as Microsoft Access, SQL data mining and reporting is required.</td>
      <td>Toronto, ON</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=I/O%20R.O.%20Enrolment%20Data%20Quality%20Assurance%20Officer%20George%20Brown%20College</td>
    </tr>
    <tr>
      <th>62</th>
      <td>Jr. Data Analyst</td>
      <td>Flex Surveys</td>
      <td>Translating complex data and research outcomes into engaging and actionable formats for clients. We offer an array of survey consulting services and develop…</td>
      <td>Greater Toronto Area, ON</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data%20Analyst%20Flex%20Surveys</td>
    </tr>
    <tr>
      <th>136</th>
      <td>Junior Agile Developer- SAP Analytics Cloud</td>
      <td>SAP</td>
      <td>Contribute to hands-on coding, design and testing to deliver best solutions to our customers. Collaborate in a team environment that extends to colleagues in…</td>
      <td>Vancouver, BC</td>
      <td>4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Agile%20Developer-%20SAP%20Analytics%20Cloud%20SAP</td>
    </tr>
    <tr>
      <th>139</th>
      <td>Junior Agile Developer- SAP Analytics Cloud</td>
      <td>SAP</td>
      <td>We’re looking for a junior developer who is eager to learn, a creative problem solver, resourceful in getting things to work and productive working…</td>
      <td>Vancouver, BC</td>
      <td>4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Agile%20Developer-%20SAP%20Analytics%20Cloud%20SAP</td>
    </tr>
    <tr>
      <th>90</th>
      <td>Junior Financial Analyst (FT)</td>
      <td>Part Time CFO Services Inc.</td>
      <td>The Junior Financial Analyst position will be responsible for performing day to day processing of various accounting transactions as well as providing support…</td>
      <td>Peterborough, ON</td>
      <td>4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financial%20Analyst%20%28FT%29%20Part%20Time%20CFO%20Services%20Inc.</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Junior Asset Management Consultant and Data Analyst</td>
      <td>GM BluePlan Engineering</td>
      <td>Develop and analyze asset data to support asset management planning. Create and manage asset inventories and data structures, including the development of…</td>
      <td>Vaughan, ON</td>
      <td>4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Asset%20Management%20Consultant%20and%20Data%20Analyst%20GM%20BluePlan%20Engineering</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Junior Data Analyst</td>
      <td>OSL Retail Services Inc</td>
      <td>Acquire data from primary or secondary data sources and maintain databases/data systems. Proven working experience as a data analyst or business data analyst.</td>
      <td>Mississauga, ON</td>
      <td>4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20OSL%20Retail%20Services%20Inc</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Junior Data Engineer</td>
      <td>Kora</td>
      <td>Help maintain and update the company-level data warehouse to ensure data accuracy. The Data Engineer will support our financial department and data scientists…</td>
      <td>Toronto, ON</td>
      <td>4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Engineer%20Kora</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Jr. Data Analyst</td>
      <td>Ratehub</td>
      <td>Support in developing and maintaining our data model by understanding key data sources and relationships between them.</td>
      <td>Toronto, ON</td>
      <td>4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data%20Analyst%20Ratehub</td>
    </tr>
    <tr>
      <th>104</th>
      <td>Research Analyst I, Commercialization</td>
      <td>University Health Network</td>
      <td>Advanced skills in statistical analysis and data management software applications. To complete various data-related tasks/projects assigned, including but not…</td>
      <td>Toronto, ON</td>
      <td>4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Research%20Analyst%20I%2C%20Commercialization%20University%20Health%20Network</td>
    </tr>
    <tr>
      <th>119</th>
      <td>OPÉRATRICE OU OPÉRATEUR EN INFORMATIQUE CLASSE I / DATA PROC...</td>
      <td>Riverside School Board</td>
      <td>They make backup copies, copy compressor destroy files on various media and transfer data from one workstation or organization to another.</td>
      <td>Saint-Hubert, QC</td>
      <td>5 days ago</td>
      <td>5</td>
      <td>https://ca.indeed.com/jobs?q=OP%C3%89RATRICE%20OU%20OP%C3%89RATEUR%20EN%20INFORMATIQUE%20CLASSE%20I%20/%20DATA%20PROC...%20Riverside%20School%20Board</td>
    </tr>
    <tr>
      <th>61</th>
      <td>Jr. Business Analyst</td>
      <td>The Portage Mutual Insurance Company</td>
      <td>Someone who enjoys working with data and solving problems. The candidate must have the ability to effectively work both independently as well as a member of a…</td>
      <td>Winnipeg, MB</td>
      <td>5 days ago</td>
      <td>5</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Business%20Analyst%20The%20Portage%20Mutual%20Insurance%20Company</td>
    </tr>
    <tr>
      <th>45</th>
      <td>Data Analyst- Central Production</td>
      <td>Monsters Aliens Robots Zombies</td>
      <td>Creating data modeling techniques to calculate the ROI of R&amp;amp;D investments. Working with the Central Production Manager on resourcing, scheduling, and other data…</td>
      <td>Toronto, ON</td>
      <td>5 days ago</td>
      <td>5</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Analyst-%20Central%20Production%20Monsters%20Aliens%20Robots%20Zombies</td>
    </tr>
    <tr>
      <th>44</th>
      <td>Junior Business Intelligence Specialist (RQ02143)</td>
      <td>Amanst Inc</td>
      <td>Report development and data management. Prepare ad-hoc data extracts (via SQL or Excel) for data analysis into detailed, summary or aggregated formats.</td>
      <td>Greater Toronto Area, ON</td>
      <td>6 days ago</td>
      <td>6</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Intelligence%20Specialist%20%28RQ02143%29%20Amanst%20Inc</td>
    </tr>
    <tr>
      <th>68</th>
      <td>Junior Marketing Specialist</td>
      <td>RV SnapPad</td>
      <td>Using formulas to parse data and create visualizations. The Junior Marketing Specialist will assist in all aspects of the marketing, graphics, web development…</td>
      <td>Calgary, AB</td>
      <td>6 days ago</td>
      <td>6</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Marketing%20Specialist%20RV%20SnapPad</td>
    </tr>
    <tr>
      <th>149</th>
      <td>Laboratory Assistant I - Virology Pre-analytics</td>
      <td>Alberta Precision Labs</td>
      <td>You may be required to perform data entry and specimen processing functions in other areas of the lab. As a Laboratory Assistant I, Clinical Microbiology …</td>
      <td>Edmonton, AB</td>
      <td>6 days ago</td>
      <td>6</td>
      <td>https://ca.indeed.com/jobs?q=Laboratory%20Assistant%20I%20-%20Virology%20Pre-analytics%20Alberta%20Precision%20Labs</td>
    </tr>
    <tr>
      <th>127</th>
      <td>Junior Financial Analyst, Billing /Analyste financier junior...</td>
      <td>Estruxture Data Centers</td>
      <td>Solid computer skills: good knowledge of Excel functionalities (pivot tables, vlookups, sumif/sumifs, data sorting and filtering), Google and/or Microsoft Suite…</td>
      <td>Montréal, QC</td>
      <td>6 days ago</td>
      <td>6</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financial%20Analyst%2C%20Billing%20/Analyste%20financier%20junior...%20Estruxture%20Data%20Centers</td>
    </tr>
    <tr>
      <th>23</th>
      <td>IT Support – Junior Data Coordinator</td>
      <td>Wellsite Masters</td>
      <td>Coordinate and manipulate all data that is derived from WM Systems. Create reports in Microsoft Excel, Word and PowerPoint as required.</td>
      <td>Calgary, AB</td>
      <td>6 days ago</td>
      <td>6</td>
      <td>https://ca.indeed.com/jobs?q=IT%20Support%20%E2%80%93%20Junior%20Data%20Coordinator%20Wellsite%20Masters</td>
    </tr>
    <tr>
      <th>173</th>
      <td>Laboratory Assistant I - Virology Pre-analytics</td>
      <td>Alberta Precision Laboratories</td>
      <td>You may be required to perform data entry and specimen processing functions in other areas of the lab. As a Laboratory Assistant I, Clinical Microbiology …</td>
      <td>Edmonton, AB</td>
      <td>6 days ago</td>
      <td>6</td>
      <td>https://ca.indeed.com/jobs?q=Laboratory%20Assistant%20I%20-%20Virology%20Pre-analytics%20Alberta%20Precision%20Laboratories</td>
    </tr>
    <tr>
      <th>83</th>
      <td>Junior Graphic Marketing Specialist</td>
      <td>Excel Management Limited Partnership</td>
      <td>Through surveys, focus groups, sales and online data, gain insights into the buyer’s journey. The *Junior Graphic Marketing Specialist* is responsible for…</td>
      <td>Calgary, AB</td>
      <td>7 days ago</td>
      <td>7</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Graphic%20Marketing%20Specialist%20Excel%20Management%20Limited%20Partnership</td>
    </tr>
    <tr>
      <th>67</th>
      <td>IT Analyst I - IT Data Protection Admin</td>
      <td>Alberta Health Services</td>
      <td>Experience with reporting, monitoring, alerting and management tools for enterprise data protection systems. The data protection environment consists primarily…</td>
      <td>Calgary, AB</td>
      <td>7 days ago</td>
      <td>7</td>
      <td>https://ca.indeed.com/jobs?q=IT%20Analyst%20I%20-%20IT%20Data%20Protection%20Admin%20Alberta%20Health%20Services</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Analyste de l’exploitation des données – Niveau débutant / D...</td>
      <td>Equifax</td>
      <td>Ensure receipt of data and performs data quality review and prepares data for loading or appending to appropriate databases.</td>
      <td>Montréal, QC</td>
      <td>7 days ago</td>
      <td>7</td>
      <td>https://ca.indeed.com/jobs?q=Analyste%20de%20l%E2%80%99exploitation%20des%20donn%C3%A9es%20%E2%80%93%20Niveau%20d%C3%A9butant%20/%20D...%20Equifax</td>
    </tr>
    <tr>
      <th>46</th>
      <td>Junior MS Database Developer</td>
      <td>Blue North Strategies</td>
      <td>Data management: 3 years (preferred). &amp;gt; Complete documentation, transmission and validation of client data. &amp;gt; Provide support and programming to all aspects of…</td>
      <td>Guelph, ON</td>
      <td>7 days ago</td>
      <td>7</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20MS%20Database%20Developer%20Blue%20North%20Strategies</td>
    </tr>
    <tr>
      <th>135</th>
      <td>Analyste fonctionnel I (Applicatif - atout BI)</td>
      <td>Hydro Québec</td>
      <td>Analyser les besoins informatiques et techniques des utilisatèurs et participer à la recommandation d'une solution fonctionnelle adaptée.</td>
      <td>Chicoutimi, QC</td>
      <td>8 days ago</td>
      <td>8</td>
      <td>https://ca.indeed.com/jobs?q=Analyste%20fonctionnel%20I%20%28Applicatif%20-%20atout%20BI%29%20Hydro%20Qu%C3%A9bec</td>
    </tr>
    <tr>
      <th>131</th>
      <td>Analyste fonctionnel I (BI/Analytique)</td>
      <td>Hydro Québec</td>
      <td>Analyser les besoins informatiques et techniques des utilisatèurs et participer à la recommandation d'une solution fonctionnelle adaptée.</td>
      <td>Chicoutimi, QC</td>
      <td>8 days ago</td>
      <td>8</td>
      <td>https://ca.indeed.com/jobs?q=Analyste%20fonctionnel%20I%20%28BI/Analytique%29%20Hydro%20Qu%C3%A9bec</td>
    </tr>
    <tr>
      <th>141</th>
      <td>Analytics Product Owner I</td>
      <td>TD Bank</td>
      <td>Manage workload of analytics team; assigning data request to staff based on skills and development needs. Ensure team uses knowledge of data capabilities across…</td>
      <td>Toronto, ON</td>
      <td>10 days ago</td>
      <td>10</td>
      <td>https://ca.indeed.com/jobs?q=Analytics%20Product%20Owner%20I%20TD%20Bank</td>
    </tr>
    <tr>
      <th>114</th>
      <td>Business Analyst I</td>
      <td>Global Excel Management</td>
      <td>Knowledge of process and data modeling; Are you a detail-oriented person? Are you interested in working in a multilingual, dynamic and friendly environment that…</td>
      <td>Sherbrooke, QC</td>
      <td>10 days ago</td>
      <td>10</td>
      <td>https://ca.indeed.com/jobs?q=Business%20Analyst%20I%20Global%20Excel%20Management</td>
    </tr>
    <tr>
      <th>121</th>
      <td>Financial Analyst I</td>
      <td>Vancouver Drydock</td>
      <td>Perform reconciliations and resolve data discrepancies to ensure accuracy of customer invoices. Assemble cost database files and supporting documentation by…</td>
      <td>North Vancouver, BC</td>
      <td>11 days ago</td>
      <td>11</td>
      <td>https://ca.indeed.com/jobs?q=Financial%20Analyst%20I%20Vancouver%20Drydock</td>
    </tr>
    <tr>
      <th>123</th>
      <td>Analyste tarifaire junior (support administratif) - Junior P...</td>
      <td>GLS Canada</td>
      <td>Relevant experience in data manipulation. Nous sommes présentement à la recherche d’un(e) Analyste tarifaire junior – support administratif pour notre siège…</td>
      <td>Dorval, QC</td>
      <td>11 days ago</td>
      <td>11</td>
      <td>https://ca.indeed.com/jobs?q=Analyste%20tarifaire%20junior%20%28support%20administratif%29%20-%20Junior%20P...%20GLS%20Canada</td>
    </tr>
    <tr>
      <th>116</th>
      <td>Data Steward I</td>
      <td>TD Bank</td>
      <td>Are you an experienced data steward and data analysis expert? Complete metadata and data quality tasks. Manage data work activities requiring coordination…</td>
      <td>Toronto, ON</td>
      <td>11 days ago</td>
      <td>11</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Steward%20I%20TD%20Bank</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Junior Business Intelligence Analyst</td>
      <td>Great Canadian Casinos</td>
      <td>Ensures compliance with all data management policies and procedures including Crown Corporation partners. The incumbent will ensure adherence to all policies…</td>
      <td>Richmond, BC</td>
      <td>11 days ago</td>
      <td>11</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Intelligence%20Analyst%20Great%20Canadian%20Casinos</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Junior Data Analyst</td>
      <td>Scandinavian Building Services</td>
      <td>Previous experience with large scale data analysis or data reconciliations. Advanced level Microsoft Excel and data analytics skills.</td>
      <td>Edmonton, AB</td>
      <td>11 days ago</td>
      <td>11</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20Scandinavian%20Building%20Services</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Junior Customer Service and Data Entry</td>
      <td>Pinnacle Fibres Inc.</td>
      <td>Handles quality documentation entry and online data submission for export. We are currently searching for an independent, self-starter with minimum 1-3 years of…</td>
      <td>Saint-Lambert, QC</td>
      <td>11 days ago</td>
      <td>11</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Customer%20Service%20and%20Data%20Entry%20Pinnacle%20Fibres%20Inc.</td>
    </tr>
    <tr>
      <th>187</th>
      <td>Data Steward I, ITSS Data Governance</td>
      <td>TD Bank</td>
      <td>Are you an experienced data steward and data analysis expert? Complete metadata and data quality tasks. Manage data work activities requiring coordination…</td>
      <td>Toronto, ON</td>
      <td>12 days ago</td>
      <td>12</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Steward%20I%2C%20ITSS%20Data%20Governance%20TD%20Bank</td>
    </tr>
    <tr>
      <th>79</th>
      <td>Jr Business Data Analyst</td>
      <td>Youth Services Bureau of Ottawa</td>
      <td>Analyze, review, extract and summarize pertinent data from client records to meet data collection standards. Direct knowledge of database management and various…</td>
      <td>Ottawa, ON</td>
      <td>12 days ago</td>
      <td>12</td>
      <td>https://ca.indeed.com/jobs?q=Jr%20Business%20Data%20Analyst%20Youth%20Services%20Bureau%20of%20Ottawa</td>
    </tr>
    <tr>
      <th>76</th>
      <td>Junior Database Administrator</td>
      <td>Dawn InfoTek Inc.</td>
      <td>Provide all the Database Administrative services to application development team. Develop Db2 DDL/DML scripts and enhance DB performance.</td>
      <td>Toronto, ON</td>
      <td>12 days ago</td>
      <td>12</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Database%20Administrator%20Dawn%20InfoTek%20Inc.</td>
    </tr>
    <tr>
      <th>75</th>
      <td>The Bay | Jr. Data Scientist</td>
      <td>Hudson's Bay</td>
      <td>Work with various data owners to discover and select available data from internal sources and external vendors. Assists in the development of strategic plans.</td>
      <td>Toronto, ON</td>
      <td>12 days ago</td>
      <td>12</td>
      <td>https://ca.indeed.com/jobs?q=The%20Bay%20%7C%20Jr.%20Data%20Scientist%20Hudson%27s%20Bay</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Junior Financial Analyst</td>
      <td>Sault Area Hospital Foundation</td>
      <td>Create and design reports and spreadsheets to provide value added data and analysis to Executive Director and Foundation team. Electronic and cash deposits.</td>
      <td>Sault Ste. Marie, ON</td>
      <td>12 days ago</td>
      <td>12</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financial%20Analyst%20Sault%20Area%20Hospital%20Foundation</td>
    </tr>
    <tr>
      <th>184</th>
      <td>Data Steward I, ITSS Data Governance</td>
      <td>TD Bank</td>
      <td>Complete metadata and data quality tasks. Identify and monitor the quality of critical data elements. Manage data work activities requiring coordination across…</td>
      <td>Toronto, ON</td>
      <td>12 days ago</td>
      <td>12</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Steward%20I%2C%20ITSS%20Data%20Governance%20TD%20Bank</td>
    </tr>
    <tr>
      <th>56</th>
      <td>Junior Business Analyst</td>
      <td>FYidoctors</td>
      <td>Provide data administration and pipeline tracking to our business development team. Diligently follow-up with vendors and other parties to ensure data integrity…</td>
      <td>Calgary, AB</td>
      <td>12 days ago</td>
      <td>12</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20FYidoctors</td>
    </tr>
    <tr>
      <th>10</th>
      <td>JUNIOR FINANCIAL ANALYST</td>
      <td>Ministry of Colleges and Universities</td>
      <td>Research and analyze statistical data from a variety of sources. You have well developed knowledge of financial information systems in order to obtain and…</td>
      <td>Toronto, ON</td>
      <td>12 days ago</td>
      <td>12</td>
      <td>https://ca.indeed.com/jobs?q=JUNIOR%20FINANCIAL%20ANALYST%20Ministry%20of%20Colleges%20and%20Universities</td>
    </tr>
    <tr>
      <th>182</th>
      <td>Junior Financial Analyst</td>
      <td>The Group Master</td>
      <td>Reporting to the assistant controller, the junior financial analyst is a key player in producing information that helps decision-making.</td>
      <td>Boucherville, QC</td>
      <td>13 days ago</td>
      <td>13</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financial%20Analyst%20The%20Group%20Master</td>
    </tr>
    <tr>
      <th>179</th>
      <td>Analyst, Client Business I</td>
      <td>Mosaic North America</td>
      <td>Interpret data, formulate reports, and make recommendations to the team. Remain fully informed on latest data trends, practice, and process.</td>
      <td>Toronto, ON</td>
      <td>13 days ago</td>
      <td>13</td>
      <td>https://ca.indeed.com/jobs?q=Analyst%2C%20Client%20Business%20I%20Mosaic%20North%20America</td>
    </tr>
    <tr>
      <th>100</th>
      <td>Business Analyst I</td>
      <td>TD Bank</td>
      <td>Knowledge of system analysis process and techniques, as well as system components, functionality, interfaces, data flows and business rules.</td>
      <td>Toronto, ON</td>
      <td>13 days ago</td>
      <td>13</td>
      <td>https://ca.indeed.com/jobs?q=Business%20Analyst%20I%20TD%20Bank</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Junior EA &amp; Data Entry Associate</td>
      <td>Redwood Classics Apparel</td>
      <td>Facilitates/attends special working group meetings, senior management team meetings and expedites a range of time sensitive tasks.</td>
      <td>Toronto, ON</td>
      <td>13 days ago</td>
      <td>13</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20EA%20%26%20Data%20Entry%20Associate%20Redwood%20Classics%20Apparel</td>
    </tr>
    <tr>
      <th>95</th>
      <td>Junior Financial Analyst</td>
      <td>HUB International</td>
      <td>Assist in organizing building lease data and payments. Based in Chilliwack BC, and reporting to the Finance Manager, the Junior Financial Analyst will be part…</td>
      <td>Chilliwack, BC</td>
      <td>13 days ago</td>
      <td>13</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financial%20Analyst%20HUB%20International</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Junior Research Analyst</td>
      <td>Simcoe County District School Board</td>
      <td>Research and/or data analysis; In building data collection tools with survey software, e.g. Survey Monkey; And other board staff for impact analysis and data…</td>
      <td>Midhurst, ON</td>
      <td>13 days ago</td>
      <td>13</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Research%20Analyst%20Simcoe%20County%20District%20School%20Board</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Jr Data Analyst</td>
      <td>JELD-WEN, inc</td>
      <td>Strong knowledge of using multiple query tools to extract relevant customizable data. Candidate must be well-versed in analyzing pricing across the enterprise…</td>
      <td>Woodbridge, ON</td>
      <td>13 days ago</td>
      <td>13</td>
      <td>https://ca.indeed.com/jobs?q=Jr%20Data%20Analyst%20JELD-WEN%2C%20inc</td>
    </tr>
    <tr>
      <th>33</th>
      <td>Junior Business Analyst - OpenRoad Head Office</td>
      <td>OpenRoad Auto Group</td>
      <td>Identifying opportunities that improve data accuracy and efficiency of our processes. While this is a junior position, some experience is preferred.</td>
      <td>Richmond, BC</td>
      <td>13 days ago</td>
      <td>13</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20-%20OpenRoad%20Head%20Office%20OpenRoad%20Auto%20Group</td>
    </tr>
    <tr>
      <th>71</th>
      <td>Analyst I, Security Advisory and Data Security</td>
      <td>Moneris Solutions Corporation</td>
      <td>Knowledge of data classification and data loss prevention principles. Support the provision of data protection subject matter advice related to Moneris' data…</td>
      <td>Etobicoke, ON</td>
      <td>13 days ago</td>
      <td>13</td>
      <td>https://ca.indeed.com/jobs?q=Analyst%20I%2C%20Security%20Advisory%20and%20Data%20Security%20Moneris%20Solutions%20Corporation</td>
    </tr>
    <tr>
      <th>77</th>
      <td>Business Intelligence Reports Developer I</td>
      <td>Global Excel Management</td>
      <td>Work with all areas to resolve data issues and identifying root causes; Understand the business processes and business rules to assist with data extraction and…</td>
      <td>Sherbrooke, QC</td>
      <td>13 days ago</td>
      <td>13</td>
      <td>https://ca.indeed.com/jobs?q=Business%20Intelligence%20Reports%20Developer%20I%20Global%20Excel%20Management</td>
    </tr>
    <tr>
      <th>110</th>
      <td>RESEARCH/DATABASE COORDINATOR I (Data Custodian)</td>
      <td>Centre for Global Health Research</td>
      <td>Experience working with GIS/spatial data, health survey data, and vital statistics. Familiarity with health information regulations, data governance, and data…</td>
      <td>Toronto, ON</td>
      <td>14 days ago</td>
      <td>14</td>
      <td>https://ca.indeed.com/jobs?q=RESEARCH/DATABASE%20COORDINATOR%20I%20%28Data%20Custodian%29%20Centre%20for%20Global%20Health%20Research</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Financial Analyst (Program), Junior</td>
      <td>General Dynamics Missions Systems-Canada</td>
      <td>Support program audit requirements and requests for financial data. General Dynamics Mission Systems–Canada is seeking a Program Financial Analyst for the…</td>
      <td>Ottawa, ON</td>
      <td>14 days ago</td>
      <td>14</td>
      <td>https://ca.indeed.com/jobs?q=Financial%20Analyst%20%28Program%29%2C%20Junior%20General%20Dynamics%20Missions%20Systems-Canada</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Junior Business Analyst</td>
      <td>Pivotree</td>
      <td>Prototyping - Create wireframes of potential page designs to facilitate the design discussions and explore requirements, data and process needs.</td>
      <td>Toronto, ON</td>
      <td>14 days ago</td>
      <td>14</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20Pivotree</td>
    </tr>
    <tr>
      <th>156</th>
      <td>Jr. Data Engineer - Vancouver</td>
      <td>Randstad</td>
      <td>Proactively monitor data flow across systems for data accuracy and consistency. Work with stakeholders to assist with data-related technical issues and support…</td>
      <td>Vancouver, BC</td>
      <td>17 days ago</td>
      <td>17</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data%20Engineer%20-%20Vancouver%20Randstad</td>
    </tr>
    <tr>
      <th>144</th>
      <td>Financial Analyst I (Contract)</td>
      <td>Duca</td>
      <td>As part of the Financial Planning &amp;amp; Analysis team the Financial Analyst is responsible for conducting high-level analysis and reporting of financial data to…</td>
      <td>Toronto, ON</td>
      <td>17 days ago</td>
      <td>17</td>
      <td>https://ca.indeed.com/jobs?q=Financial%20Analyst%20I%20%28Contract%29%20Duca</td>
    </tr>
    <tr>
      <th>160</th>
      <td>Financial Analyst I (Contract)</td>
      <td>DUCA Financial Services Credit Union Ltd.</td>
      <td>As part of the Financial Planning &amp;amp; Analysis team the Financial Analyst is responsible for conducting high-level analysis and reporting of financial data to…</td>
      <td>Toronto, ON</td>
      <td>17 days ago</td>
      <td>17</td>
      <td>https://ca.indeed.com/jobs?q=Financial%20Analyst%20I%20%28Contract%29%20DUCA%20Financial%20Services%20Credit%20Union%20Ltd.</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Junior Data Analyst</td>
      <td>The Mustard Seed</td>
      <td>Analyze donor and volunteer data to ensure that data is input into the database based on business rules. This is a junior level position responsible for the…</td>
      <td>Calgary, AB</td>
      <td>18 days ago</td>
      <td>18</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20The%20Mustard%20Seed</td>
    </tr>
    <tr>
      <th>122</th>
      <td>Jr. Murex Business Analyst</td>
      <td>CPQi</td>
      <td>Knowledge and understanding of Murex features such as Fixings, Simulations, MxML, Market data integration/setup for pricing feeds, pre/post trade workflow,…</td>
      <td>Halifax, NS</td>
      <td>18 days ago</td>
      <td>18</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Murex%20Business%20Analyst%20CPQi</td>
    </tr>
    <tr>
      <th>103</th>
      <td>Marketing &amp; Content Jr. Analyst</td>
      <td>Stingray</td>
      <td>Identify and extract relevant performance analysis data. The ideal candidate is a smart data-driven individual passionate about tracking and analyzing data to…</td>
      <td>Montréal, QC</td>
      <td>18 days ago</td>
      <td>18</td>
      <td>https://ca.indeed.com/jobs?q=Marketing%20%26%20Content%20Jr.%20Analyst%20Stingray</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Junior Research Analyst</td>
      <td>Carleton University</td>
      <td>?experience organizing and validating data. ?experience with data visualization and reporting. The ability to organize data accurately and prepare for reporting…</td>
      <td>Ottawa, ON</td>
      <td>19 days ago</td>
      <td>19</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Research%20Analyst%20Carleton%20University</td>
    </tr>
    <tr>
      <th>78</th>
      <td>Junior BI Analytics Developer - Bilingual</td>
      <td>AstraNorth</td>
      <td>Primary Skills*: BI Tools - tableau, . NET , SQL, SSIS, SSAS, Power BI,. Python, Spark, DataBricks, ADF, French speaking. Temporarily due to COVID-19.</td>
      <td>Montréal, QC</td>
      <td>19 days ago</td>
      <td>19</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20BI%20Analytics%20Developer%20-%20Bilingual%20AstraNorth</td>
    </tr>
    <tr>
      <th>60</th>
      <td>Trading Desk Analyst</td>
      <td>Aquanow</td>
      <td>Daily processing of transactions and key controls. Account and asset reconciliation and recordkeeping. Develop and implement effective internal controls.</td>
      <td>Vancouver, BC</td>
      <td>19 days ago</td>
      <td>19</td>
      <td>https://ca.indeed.com/jobs?q=Trading%20Desk%20Analyst%20Aquanow</td>
    </tr>
    <tr>
      <th>93</th>
      <td>Business Analyst I, Wireless Fulfillment (Logistics)</td>
      <td>TELUS</td>
      <td>Manage and monitor data and inputs required for testing and analysis (sales order management, returns, etc.). Here’s the impact you’ll have:</td>
      <td>Scarborough, ON</td>
      <td>20 days ago</td>
      <td>20</td>
      <td>https://ca.indeed.com/jobs?q=Business%20Analyst%20I%2C%20Wireless%20Fulfillment%20%28Logistics%29%20TELUS</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Jr. Quality Assurance Analyst (Manufacturing)</td>
      <td>MDA</td>
      <td>Implementing approved sampling, reporting and data analysis as required. Assist in developing, maintaining, and evaluating the company Quality system meeting…</td>
      <td>Kanata, ON</td>
      <td>20 days ago</td>
      <td>20</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Quality%20Assurance%20Analyst%20%28Manufacturing%29%20MDA</td>
    </tr>
    <tr>
      <th>106</th>
      <td>Finance Ops Analyst I</td>
      <td>TD Bank</td>
      <td>Support the collection of meaningful data and/or research, coordinating efforts with various finance areas. Provide accurate and thorough data analysis for own…</td>
      <td>Dieppe, NB</td>
      <td>24 days ago</td>
      <td>24</td>
      <td>https://ca.indeed.com/jobs?q=Finance%20Ops%20Analyst%20I%20TD%20Bank</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Junior Data Analyst</td>
      <td>O2E Brands</td>
      <td>Passion for data visualization with Tableau. Experience blending data from disparate sources. Ensure consistent application of data governance initiatives.</td>
      <td>Vancouver, BC</td>
      <td>25 days ago</td>
      <td>25</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20O2E%20Brands</td>
    </tr>
    <tr>
      <th>168</th>
      <td>Analyst, Business I</td>
      <td>Mosaic North America</td>
      <td>Interpret data, formulate reports, and make recommendations to the team. Remain fully informed on latest data trends, practice, and process.</td>
      <td>Toronto, ON</td>
      <td>25 days ago</td>
      <td>25</td>
      <td>https://ca.indeed.com/jobs?q=Analyst%2C%20Business%20I%20Mosaic%20North%20America</td>
    </tr>
    <tr>
      <th>105</th>
      <td>Junior Financial Analyst /Bookkeeper</td>
      <td>Process Fusion Inc.</td>
      <td>Collect, interpret, and report on financial data. Ability to analyze and present numerical data in tables, spreadsheets, and forms. Temporarily due to COVID-19.</td>
      <td>Toronto, ON</td>
      <td>25 days ago</td>
      <td>25</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financial%20Analyst%20/Bookkeeper%20Process%20Fusion%20Inc.</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Junior Business Analyst</td>
      <td>Eastwood and Cleef</td>
      <td>\*Tasks include, but are not limited to: client interviews, analytical work with detailed operations and/or financial data, support of client presentations,…</td>
      <td>Toronto, ON</td>
      <td>26 days ago</td>
      <td>26</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20Eastwood%20and%20Cleef</td>
    </tr>
    <tr>
      <th>108</th>
      <td>Business Analytics Specialist I</td>
      <td>InComm Payments</td>
      <td>This is a career building opportunity for recent graduates with skills related to financial analytics, data analytics, and data reporting.</td>
      <td>Mississauga, ON</td>
      <td>27 days ago</td>
      <td>27</td>
      <td>https://ca.indeed.com/jobs?q=Business%20Analytics%20Specialist%20I%20InComm%20Payments</td>
    </tr>
    <tr>
      <th>39</th>
      <td>CT Data Engineer I - Power BI</td>
      <td>EY</td>
      <td>Reviewing and understanding complex data sets to establish data quality and highlighting where data cleansing is required to remediate the data.</td>
      <td>Toronto, ON</td>
      <td>27 days ago</td>
      <td>27</td>
      <td>https://ca.indeed.com/jobs?q=CT%20Data%20Engineer%20I%20-%20Power%20BI%20EY</td>
    </tr>
    <tr>
      <th>69</th>
      <td>Jr. Data Analyst (supply chain and demand planning)</td>
      <td>Noya Cannabis Inc.</td>
      <td>Perform data analysis to identify data integrity issues/trends. Own data accuracy/data clean up issues for assigned product portfolio.</td>
      <td>Hamilton, ON</td>
      <td>28 days ago</td>
      <td>28</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data%20Analyst%20%28supply%20chain%20and%20demand%20planning%29%20Noya%20Cannabis%20Inc.</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Junior Data Analysis Assistant</td>
      <td>Universal Rehabilitation Service Agency</td>
      <td>Support the Program Director to create process manuals for Program Coordinators related to data collection and reporting. High level of attention to detail.</td>
      <td>Calgary, AB</td>
      <td>28 days ago</td>
      <td>28</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Analysis%20Assistant%20Universal%20Rehabilitation%20Service%20Agency</td>
    </tr>
    <tr>
      <th>91</th>
      <td>Junior Data Scientist</td>
      <td>Providence Health Care</td>
      <td>Reviews clinical data at aggregate levels on a regular basis using analytical reporting tools to support the identification of risks and data patterns or trends…</td>
      <td>Vancouver, BC</td>
      <td>28 days ago</td>
      <td>28</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Scientist%20Providence%20Health%20Care</td>
    </tr>
    <tr>
      <th>164</th>
      <td>Junior Quantitative Analyst</td>
      <td>Société Générale</td>
      <td>Assessing data quality and consistency between data characteristics and modeling assumptions; Experience in large data management and quantitative analysis is a…</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Quantitative%20Analyst%20Soci%C3%A9t%C3%A9%20G%C3%A9n%C3%A9rale</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Benefits Analyst (Junior)</td>
      <td>JRP Employee Benefit Solutions</td>
      <td>Request or run reports to gather data from insurers; review to ensure it is complete and accurate; provide analysis and/or prepare the data for advanced…</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Benefits%20Analyst%20%28Junior%29%20JRP%20Employee%20Benefit%20Solutions</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Jr. Data/Reporting Analyst</td>
      <td>Scarsin</td>
      <td>Data management, data analysis and ETL process skills and concepts including data modeling and transformations. Required Knowledge, Skills and Experience.</td>
      <td>Markham, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data/Reporting%20Analyst%20Scarsin</td>
    </tr>
    <tr>
      <th>41</th>
      <td>Junior Data Analyst / IT Support Technician</td>
      <td>The Stevens Company Limited</td>
      <td>In-depth knowledge of applicable data privacy practices and laws; Build reports, dashboards, and data visualizations used by business stakeholders including the…</td>
      <td>Brampton, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20/%20IT%20Support%20Technician%20The%20Stevens%20Company%20Limited</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Jr. Data Scientist</td>
      <td>SimpTek Technologies</td>
      <td>Integration with 3rd party API’s for data collection and analysis, including weather data, time-series data, and event-based data sets.</td>
      <td>Fredericton, NB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data%20Scientist%20SimpTek%20Technologies</td>
    </tr>
    <tr>
      <th>47</th>
      <td>Junior Power Analyst</td>
      <td>Dynasty Power Inc.</td>
      <td>Analyze data to look for profitable trading strategies. Passion for trading, financial derivatives and financial data analysis considered an asset.</td>
      <td>Calgary, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Power%20Analyst%20Dynasty%20Power%20Inc.</td>
    </tr>
    <tr>
      <th>38</th>
      <td>Junior Big Data Engineer, Business Intelligence (6 Month Con...</td>
      <td>CBC/Radio-Canada</td>
      <td>Batch-processed data as well as streaming data. You may have experience with data architecture, building robust and clean data models, and working with…</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Big%20Data%20Engineer%2C%20Business%20Intelligence%20%286%20Month%20Con...%20CBC/Radio-Canada</td>
    </tr>
    <tr>
      <th>42</th>
      <td>Data Analyst</td>
      <td>WorkTango</td>
      <td>Manage our ETL process for client data transfers to enrich our proprietary data set. 1+ years experience working with advanced Excel and data analysis,…</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Analyst%20WorkTango</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Data Analytics Junior Technologist B</td>
      <td>St. Clair College</td>
      <td>Previous experience working with large data sets. Previous experience working with large data sets. Status: *Regular Part Time (2 Positions).</td>
      <td>Windsor, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Analytics%20Junior%20Technologist%20B%20St.%20Clair%20College</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Junior Analyst Intern, Data &amp; Technology (4-month Term)</td>
      <td>University Pension Plan</td>
      <td>Experience with basic data querying (SQL Server, MySQL, MongoDB). The UPP is a new, jointly sponsored pension plan that serves all active, retired, and deferred…</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Analyst%20Intern%2C%20Data%20%26%20Technology%20%284-month%20Term%29%20University%20Pension%20Plan</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Junior Business Analyst</td>
      <td>RPM TECHNOLOGIES CORP</td>
      <td>Documenting and analyzing the required information and data to determine potential solutions from a technical and business perspective.</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20RPM%20TECHNOLOGIES%20CORP</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Junior Business Analyst – CPM/BI</td>
      <td>Corporate Renaissance Group</td>
      <td>Assist in data transformation and validation. B.Comm with accounting/finance background and exposure to data analytics. Medical &amp;amp; dental groups benefits plan.</td>
      <td>Ottawa, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20%E2%80%93%20CPM/BI%20Corporate%20Renaissance%20Group</td>
    </tr>
    <tr>
      <th>155</th>
      <td>MARKETING SPECIALIST</td>
      <td>ABI - Allstream Business Inc</td>
      <td>This is a junior marketing role with experience in event management and demand generation. Continuously assess and report on the results of lead gen initiatives…</td>
      <td>Mississauga, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=MARKETING%20SPECIALIST%20ABI%20-%20Allstream%20Business%20Inc</td>
    </tr>
    <tr>
      <th>117</th>
      <td>MES Business Analyst</td>
      <td>SyLogix Consulting Inc.</td>
      <td>Prior experience with OSIsoft PI or another data historian. The project includes the implementation and validation of Manufacturing Execution System (MES) and…</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=MES%20Business%20Analyst%20SyLogix%20Consulting%20Inc.</td>
    </tr>
    <tr>
      <th>118</th>
      <td>Jr Financial Analyst</td>
      <td>Rogers Insurance Ltd</td>
      <td>Strong attention to detail while maintaining accuracy in work, with a high level of competence in analyzing data. Ad hoc reporting and projects, as required.</td>
      <td>Calgary, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr%20Financial%20Analyst%20Rogers%20Insurance%20Ltd</td>
    </tr>
    <tr>
      <th>113</th>
      <td>Ingénieur de données I / Data Engineer I</td>
      <td>CAE Inc.</td>
      <td>Keep data separated and secure across national boundaries through multiple data centers. Build the infrastructure required for optimal extraction,…</td>
      <td>Saint-Laurent, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Ing%C3%A9nieur%20de%20donn%C3%A9es%20I%20/%20Data%20Engineer%20I%20CAE%20Inc.</td>
    </tr>
    <tr>
      <th>112</th>
      <td>Montreal - Analyste Technique Junior ou chef de Projet Techn...</td>
      <td>FDM Group</td>
      <td>En tant qu'analyste technique junior ou chef de projet technique junior chez FDM, vous suivrez une formation spécifique à l'industrie et poursuivrez votre…</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Montreal%20-%20Analyste%20Technique%20Junior%20ou%20chef%20de%20Projet%20Techn...%20FDM%20Group</td>
    </tr>
    <tr>
      <th>111</th>
      <td>Financial Analyst I, CCRU</td>
      <td>University Health Network</td>
      <td>Experience with financial and cost accounting and with analyzing and interpreting large quantities of financial and statistical data; systems thinker.</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Financial%20Analyst%20I%2C%20CCRU%20University%20Health%20Network</td>
    </tr>
    <tr>
      <th>109</th>
      <td>Junior Business Analyst</td>
      <td>Genpact</td>
      <td>Expertise in Excel and PowerPoint including Pivot Tables, vlookups, embedded formulas, and data manipulation. Experience with financial management and budgeting…</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20Genpact</td>
    </tr>
    <tr>
      <th>124</th>
      <td>Financial Business Analyst / Junior Accountant</td>
      <td>Cam Clark Auto Group</td>
      <td>Experience with interactive data visualization software. Satisfy data sampling, project analysis, testing verification, and other user requests from existing…</td>
      <td>Airdrie, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Financial%20Business%20Analyst%20/%20Junior%20Accountant%20Cam%20Clark%20Auto%20Group</td>
    </tr>
    <tr>
      <th>125</th>
      <td>Inventory Coordinator I</td>
      <td>Groupe Robert</td>
      <td>Maintain inventory data integrity and tracks accuracy of inventory. Proceed to the various data entries in the system and concerning new products or new…</td>
      <td>Mississauga, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Inventory%20Coordinator%20I%20Groupe%20Robert</td>
    </tr>
    <tr>
      <th>126</th>
      <td>Jr Financial Analyst - Rogers Insurance</td>
      <td>Sharp Insurance</td>
      <td>Strong attention to detail while maintaining accuracy in work, with a high level of competence in analyzing data. Jr Financial Analyst - Rogers Insurance.</td>
      <td>Calgary, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr%20Financial%20Analyst%20-%20Rogers%20Insurance%20Sharp%20Insurance</td>
    </tr>
    <tr>
      <th>107</th>
      <td>Business Analyst I #Remote</td>
      <td>PointClickCare</td>
      <td>Experience with modeling tools relating to process, data, and workflow at the conceptual level. Elicit from and collaborate with the BSM on the applicable…</td>
      <td>Mississauga, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Business%20Analyst%20I%20%23Remote%20PointClickCare</td>
    </tr>
    <tr>
      <th>102</th>
      <td>Biostatistician I</td>
      <td>University Health Network</td>
      <td>Familiarity in the methods of missing data is an asset. Demonstrated competency in managing and analyzing real-world clinical data. Hours: 37.5 hours per week.</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Biostatistician%20I%20University%20Health%20Network</td>
    </tr>
    <tr>
      <th>101</th>
      <td>Jr. Business Analyst</td>
      <td>Intimate Interactive Advertising</td>
      <td>Monitor reports and analyze data to identify areas of improvement. Ability to display data in an easy to read way and draw conclusions from it.</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Business%20Analyst%20Intimate%20Interactive%20Advertising</td>
    </tr>
    <tr>
      <th>99</th>
      <td>Data Scientist I (Quants)</td>
      <td>TD Bank</td>
      <td>Provide technical expertise across a broad range of data analysis functions including data modeling, visualization, data profiling, data origin and lineage,…</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Scientist%20I%20%28Quants%29%20TD%20Bank</td>
    </tr>
    <tr>
      <th>97</th>
      <td>Data I/O Coordinator</td>
      <td>FuseFX</td>
      <td>Identifying discrepancies, and errors in data, then forwarding to Producers and Supervisors. Strategize and update shows ready for Archive and De-archive of…</td>
      <td>Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Data%20I/O%20Coordinator%20FuseFX</td>
    </tr>
    <tr>
      <th>96</th>
      <td>Junior Financial Analyst</td>
      <td>Community Natural Foods</td>
      <td>Distribute incoming mail (inter office &amp;amp; Post office). Open AP mail and sort. Review invoices in CRS and approve. Check manual splits and correct if needed.</td>
      <td>Calgary, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financial%20Analyst%20Community%20Natural%20Foods</td>
    </tr>
    <tr>
      <th>94</th>
      <td>Junior Engineer - Logistics Simulation &amp; Business Intelligen...</td>
      <td>Ausenco</td>
      <td>Many of the projects will employ logistics simulation modelling and data analytics techniques. Have some experience with business intelligence and data…</td>
      <td>Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Engineer%20-%20Logistics%20Simulation%20%26%20Business%20Intelligen...%20Ausenco</td>
    </tr>
    <tr>
      <th>89</th>
      <td>Toronto - Junior Technical Business Analyst/ Junior Technica...</td>
      <td>FDM Group</td>
      <td>These roles are crucial in helping organizations with the accuracy and timely presentation of data, in line with internal process, governance, and regulatory…</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Toronto%20-%20Junior%20Technical%20Business%20Analyst/%20Junior%20Technica...%20FDM%20Group</td>
    </tr>
    <tr>
      <th>80</th>
      <td>Junior Financial Analyst, Consulting</td>
      <td>BDO</td>
      <td>Strong data collection and analytical skills including the ability to manage, manipulate and streamline large volumes of data.</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financial%20Analyst%2C%20Consulting%20BDO</td>
    </tr>
    <tr>
      <th>74</th>
      <td>Junior Marketing Associate - Internship</td>
      <td>AltaML</td>
      <td>As the Junior Marketing Associate, you will learn and work alongside high-performing and creative professionals and play a crucial role on AlphaLayer’s Product…</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Marketing%20Associate%20-%20Internship%20AltaML</td>
    </tr>
    <tr>
      <th>72</th>
      <td>Junior Pricing Analyst</td>
      <td>Bélanger UPT</td>
      <td>Collects data and maintains the database. Prepares financial and sku analysis reports, analyses margins and competitive market data.</td>
      <td>Mississauga, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Pricing%20Analyst%20B%C3%A9langer%20UPT</td>
    </tr>
    <tr>
      <th>66</th>
      <td>Junior Sales Data Coordinator</td>
      <td>Bélanger UPT</td>
      <td>Reporting to the National Sales &amp;amp; Marketing Director, the Junior Sales Data Coordinator will be internal link between the pricing analyst and inside sales.</td>
      <td>Mississauga, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Sales%20Data%20Coordinator%20B%C3%A9langer%20UPT</td>
    </tr>
    <tr>
      <th>65</th>
      <td>Junior Financial Analyst</td>
      <td>Park Lawn Corporation</td>
      <td>Perform year-end and quarter-end analysis, forecasts, and data visualization. Compile monthly corporate reports for management while collaborating with the rest…</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financial%20Analyst%20Park%20Lawn%20Corporation</td>
    </tr>
    <tr>
      <th>63</th>
      <td>Junior Business Intelligence Analyst</td>
      <td>Secure Energy</td>
      <td>Inform data integrity and tool availability. Identifying and integrating data sources into the analytics environment. Training and ad-hoc support.</td>
      <td>Calgary, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Intelligence%20Analyst%20Secure%20Energy</td>
    </tr>
    <tr>
      <th>59</th>
      <td>Junior Data Engineer – Client Innovation Center (CIC) – Part...</td>
      <td>Groom &amp; Associes</td>
      <td>Knowledge of tools to perform data quality, data cleansing, data wrangling and data standards; Data processing, data design and modeling, deploying the model.</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Engineer%20%E2%80%93%20Client%20Innovation%20Center%20%28CIC%29%20%E2%80%93%20Part...%20Groom%20%26%20Associes</td>
    </tr>
    <tr>
      <th>58</th>
      <td>Junior Business Analyst</td>
      <td>Miller Paving Limited</td>
      <td>Analyzing and summarizing various sales and operational data. Assist the Manager, Material Marketing and Business Development in the key functions of business…</td>
      <td>Whitby, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20Miller%20Paving%20Limited</td>
    </tr>
    <tr>
      <th>57</th>
      <td>Junior Technical Business Analyst</td>
      <td>GoMaterials</td>
      <td>Experience with project management and data visualization tools (JIRA, Confluence, Lucidchart). The Junior Technical Business Analyst will work closely with our…</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Technical%20Business%20Analyst%20GoMaterials</td>
    </tr>
    <tr>
      <th>55</th>
      <td>Junior/Senior Data Scientist</td>
      <td>TELUS</td>
      <td>You’ll collaborate with teams across the company, seeking out various data sources to help identify new business opportunities while championing data driven…</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior/Senior%20Data%20Scientist%20TELUS</td>
    </tr>
    <tr>
      <th>115</th>
      <td>Client Financial Reporting Analyst - Junior - Waterloo</td>
      <td>Randstad</td>
      <td>Gathering applicable data for financial statement, (premium, claims and reserves) calculate, prepare, complete accounting and update applicable systems.</td>
      <td>Waterloo, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Client%20Financial%20Reporting%20Analyst%20-%20Junior%20-%20Waterloo%20Randstad</td>
    </tr>
    <tr>
      <th>92</th>
      <td>Junior Pricing/ Program Analyst</td>
      <td>Brandt</td>
      <td>Extract and manipulate large data sets to regularly analyze competitive landscape, devise strategies and evaluate results.</td>
      <td>Regina, SK</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Pricing/%20Program%20Analyst%20Brandt</td>
    </tr>
  </tbody>
</table>
</div>




```python

```

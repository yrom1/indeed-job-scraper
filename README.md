```python
import pandas as pd

from src.main import main
```


```python
main("data junior")
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
      <th>34</th>
      <td>Junior Business Analyst intern</td>
      <td>Jonar</td>
      <td>As a Junior Business Analyst, you’ll learn ho...</td>
      <td>Montréal, QC</td>
      <td>Just posted</td>
      <td>0</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business...</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Junior Machine Learning Scientist</td>
      <td>Ecoation</td>
      <td>Analyzing customer horticultural data to prov...</td>
      <td>North Vancouver, BC</td>
      <td>Today</td>
      <td>0</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Machine%...</td>
    </tr>
    <tr>
      <th>94</th>
      <td>Data Scientist I</td>
      <td>TD Bank</td>
      <td>Capture and analyze information or data on cu...</td>
      <td>Toronto, ON</td>
      <td>Today</td>
      <td>0</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Scientist%...</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Junior Data Analyst</td>
      <td>FlightHub</td>
      <td>Analyzing data sets and identifying trends an...</td>
      <td>Montréal, QC</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20A...</td>
    </tr>
    <tr>
      <th>80</th>
      <td>Jr. Data Analyst</td>
      <td>Flex Surveys</td>
      <td>Translating complex data and research outcome...</td>
      <td>Greater Toronto Area, ON</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data%20Anal...</td>
    </tr>
    <tr>
      <th>78</th>
      <td>Data Engineer - Level I</td>
      <td>Swift Medical</td>
      <td>As the world leader in digital wound care man...</td>
      <td>Toronto, ON</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Engineer%2...</td>
    </tr>
    <tr>
      <th>98</th>
      <td>I/O R.O. Enrolment Data Quality Assurance Officer</td>
      <td>George Brown College</td>
      <td>Experience with data mining and reporting uti...</td>
      <td>Toronto, ON</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=I/O%20R.O.%20Enro...</td>
    </tr>
    <tr>
      <th>72</th>
      <td>SAS Developer</td>
      <td>MSi Corp (Bell Canada)</td>
      <td>Document data mapping diagrams and data dicti...</td>
      <td>Ottawa, ON</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=SAS%20Developer%2...</td>
    </tr>
    <tr>
      <th>61</th>
      <td>Analyste PMO junior - Junior PMO Analyst</td>
      <td>Gameloft</td>
      <td>Being responsible for the regular data analyt...</td>
      <td>Montréal, QC</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Analyste%20PMO%20...</td>
    </tr>
    <tr>
      <th>116</th>
      <td>Analyst, Client Data I</td>
      <td>Mosaic North America</td>
      <td>Intermediate knowledge of data cleansing and ...</td>
      <td>Toronto, ON</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Analyst%2C%20Clie...</td>
    </tr>
    <tr>
      <th>105</th>
      <td>Engineering Analyst I</td>
      <td>TES - The Employment Solution</td>
      <td>Knowledge of statistical, mathematical and da...</td>
      <td>Markham, ON</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Engineering%20Ana...</td>
    </tr>
    <tr>
      <th>121</th>
      <td>Research Analyst I, Commercialization</td>
      <td>University Health Network</td>
      <td>Advanced skills in statistical analysis and d...</td>
      <td>Toronto, ON</td>
      <td>4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Research%20Analys...</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Junior Data Analyst</td>
      <td>OSL Retail Services Inc</td>
      <td>Acquire data from primary or secondary data s...</td>
      <td>Mississauga, ON</td>
      <td>4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20A...</td>
    </tr>
    <tr>
      <th>109</th>
      <td>Junior Financial Analyst (FT)</td>
      <td>Part Time CFO Services Inc.</td>
      <td>The Junior Financial Analyst position will be...</td>
      <td>Peterborough, ON</td>
      <td>4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financia...</td>
    </tr>
    <tr>
      <th>148</th>
      <td>Junior Agile Developer- SAP Analytics Cloud</td>
      <td>SAP</td>
      <td>Contribute to hands-on coding, design and tes...</td>
      <td>Vancouver, BC</td>
      <td>4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Agile%20...</td>
    </tr>
    <tr>
      <th>33</th>
      <td>Junior Data Engineer</td>
      <td>Kora</td>
      <td>Help maintain and update the company-level da...</td>
      <td>Toronto, ON</td>
      <td>4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20E...</td>
    </tr>
    <tr>
      <th>48</th>
      <td>Junior Asset Management Consultant and Data An...</td>
      <td>GM BluePlan Engineering</td>
      <td>Develop and analyze asset data to support ass...</td>
      <td>Vaughan, ON</td>
      <td>4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Asset%20...</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Jr. Data Analyst</td>
      <td>Ratehub</td>
      <td>Support in developing and maintaining our dat...</td>
      <td>Toronto, ON</td>
      <td>4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data%20Anal...</td>
    </tr>
    <tr>
      <th>39</th>
      <td>IT Support – Junior Data Coordinator</td>
      <td>Wellsite Masters</td>
      <td>Coordinate and manipulate all data that is de...</td>
      <td>Calgary, AB</td>
      <td>5 days ago</td>
      <td>5</td>
      <td>https://ca.indeed.com/jobs?q=IT%20Support%20%E...</td>
    </tr>
    <tr>
      <th>81</th>
      <td>Jr. Business Analyst</td>
      <td>The Portage Mutual Insurance Company</td>
      <td>Someone who enjoys working with data and solv...</td>
      <td>Winnipeg, MB</td>
      <td>5 days ago</td>
      <td>5</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Business%20...</td>
    </tr>
    <tr>
      <th>139</th>
      <td>OPÉRATRICE OU OPÉRATEUR EN INFORMATIQUE CLASSE...</td>
      <td>Riverside School Board</td>
      <td>They make backup copies, copy compressor dest...</td>
      <td>Saint-Hubert, QC</td>
      <td>5 days ago</td>
      <td>5</td>
      <td>https://ca.indeed.com/jobs?q=OP%C3%89RATRICE%2...</td>
    </tr>
    <tr>
      <th>177</th>
      <td>Laboratory Assistant I - Virology Pre-analytics</td>
      <td>Alberta Precision Laboratories</td>
      <td>You may be required to perform data entry and...</td>
      <td>Edmonton, AB</td>
      <td>5 days ago</td>
      <td>5</td>
      <td>https://ca.indeed.com/jobs?q=Laboratory%20Assi...</td>
    </tr>
    <tr>
      <th>191</th>
      <td>Laboratory Assistant I - Virology Pre-analytics</td>
      <td>Alberta Precision Labs</td>
      <td>You may be required to perform data entry and...</td>
      <td>Edmonton, AB</td>
      <td>5 days ago</td>
      <td>5</td>
      <td>https://ca.indeed.com/jobs?q=Laboratory%20Assi...</td>
    </tr>
    <tr>
      <th>83</th>
      <td>Jr. Business Intelligence Developer, Enterpris...</td>
      <td>Southlake Regional Health Centre</td>
      <td>Develop ETL procedures, SSIS packages and mai...</td>
      <td>Newmarket, ON</td>
      <td>6 days ago</td>
      <td>6</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Business%20...</td>
    </tr>
    <tr>
      <th>68</th>
      <td>IT Analyst I - IT Data Protection Admin</td>
      <td>Alberta Health Services</td>
      <td>Experience with reporting, monitoring, alerti...</td>
      <td>Calgary, AB</td>
      <td>6 days ago</td>
      <td>6</td>
      <td>https://ca.indeed.com/jobs?q=IT%20Analyst%20I%...</td>
    </tr>
    <tr>
      <th>154</th>
      <td>Junior Financial Analyst, Billing /Analyste fi...</td>
      <td>Estruxture Data Centers</td>
      <td>Solid computer skills: good knowledge of Exce...</td>
      <td>Montréal, QC</td>
      <td>6 days ago</td>
      <td>6</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financia...</td>
    </tr>
    <tr>
      <th>95</th>
      <td>Junior Marketing Specialist</td>
      <td>RV SnapPad</td>
      <td>Using formulas to parse data and create visua...</td>
      <td>Calgary, AB</td>
      <td>6 days ago</td>
      <td>6</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Marketin...</td>
    </tr>
    <tr>
      <th>65</th>
      <td>Junior Business Intelligence Specialist (RQ02143)</td>
      <td>Amanst Inc</td>
      <td>Report development and data management. Prepa...</td>
      <td>Greater Toronto Area, ON</td>
      <td>6 days ago</td>
      <td>6</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business...</td>
    </tr>
    <tr>
      <th>67</th>
      <td>Junior MS Database Developer</td>
      <td>Blue North Strategies</td>
      <td>Data management: 3 years (preferred). &amp;gt; Co...</td>
      <td>Guelph, ON</td>
      <td>7 days ago</td>
      <td>7</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20MS%20Dat...</td>
    </tr>
    <tr>
      <th>162</th>
      <td>Analyste fonctionnel I (BI/Analytique)</td>
      <td>Hydro Québec</td>
      <td>Analyser les besoins informatiques et techniq...</td>
      <td>Chicoutimi, QC</td>
      <td>7 days ago</td>
      <td>7</td>
      <td>https://ca.indeed.com/jobs?q=Analyste%20foncti...</td>
    </tr>
    <tr>
      <th>46</th>
      <td>Analyste de l’exploitation des données – Nivea...</td>
      <td>Equifax</td>
      <td>Ensure receipt of data and performs data qual...</td>
      <td>Montréal, QC</td>
      <td>7 days ago</td>
      <td>7</td>
      <td>https://ca.indeed.com/jobs?q=Analyste%20de%20l...</td>
    </tr>
    <tr>
      <th>168</th>
      <td>Analyste fonctionnel I (Applicatif - atout BI)</td>
      <td>Hydro Québec</td>
      <td>Analyser les besoins informatiques et techniq...</td>
      <td>Chicoutimi, QC</td>
      <td>7 days ago</td>
      <td>7</td>
      <td>https://ca.indeed.com/jobs?q=Analyste%20foncti...</td>
    </tr>
    <tr>
      <th>44</th>
      <td>Junior Customer Service and Data Entry</td>
      <td>Pinnacle Fibres Inc.</td>
      <td>Handles quality documentation entry and onlin...</td>
      <td>Saint-Lambert, QC</td>
      <td>10 days ago</td>
      <td>10</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Customer...</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Junior Data Analyst</td>
      <td>Scandinavian Building Services</td>
      <td>Previous experience with large scale data ana...</td>
      <td>Edmonton, AB</td>
      <td>10 days ago</td>
      <td>10</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20A...</td>
    </tr>
    <tr>
      <th>145</th>
      <td>Business Analyst I</td>
      <td>Global Excel Management</td>
      <td>Knowledge of process and data modeling; As a ...</td>
      <td>Sherbrooke, QC</td>
      <td>10 days ago</td>
      <td>10</td>
      <td>https://ca.indeed.com/jobs?q=Business%20Analys...</td>
    </tr>
    <tr>
      <th>189</th>
      <td>Analytics Product Owner I</td>
      <td>TD Bank</td>
      <td>Manage workload of analytics team; assigning ...</td>
      <td>Toronto, ON</td>
      <td>10 days ago</td>
      <td>10</td>
      <td>https://ca.indeed.com/jobs?q=Analytics%20Produ...</td>
    </tr>
    <tr>
      <th>150</th>
      <td>Analyste tarifaire junior (support administrat...</td>
      <td>GLS Canada</td>
      <td>Relevant experience in data manipulation. Nou...</td>
      <td>Dorval, QC</td>
      <td>10 days ago</td>
      <td>10</td>
      <td>https://ca.indeed.com/jobs?q=Analyste%20tarifa...</td>
    </tr>
    <tr>
      <th>146</th>
      <td>Data Steward I</td>
      <td>TD Bank</td>
      <td>Complete metadata and data quality tasks. Ide...</td>
      <td>Toronto, ON</td>
      <td>11 days ago</td>
      <td>11</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Steward%20...</td>
    </tr>
    <tr>
      <th>132</th>
      <td>Financial Analyst I</td>
      <td>Vancouver Drydock</td>
      <td>Perform reconciliations and resolve data disc...</td>
      <td>North Vancouver, BC</td>
      <td>11 days ago</td>
      <td>11</td>
      <td>https://ca.indeed.com/jobs?q=Financial%20Analy...</td>
    </tr>
    <tr>
      <th>47</th>
      <td>Junior Business Intelligence Analyst</td>
      <td>Great Canadian Casinos</td>
      <td>Ensures compliance with all data management p...</td>
      <td>Richmond, BC</td>
      <td>11 days ago</td>
      <td>11</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business...</td>
    </tr>
    <tr>
      <th>32</th>
      <td>JUNIOR FINANCIAL ANALYST</td>
      <td>Ministry of Colleges and Universities</td>
      <td>Research and analyze statistical data from a ...</td>
      <td>Toronto, ON</td>
      <td>12 days ago</td>
      <td>12</td>
      <td>https://ca.indeed.com/jobs?q=JUNIOR%20FINANCIA...</td>
    </tr>
    <tr>
      <th>102</th>
      <td>Jr Business Data Analyst</td>
      <td>Youth Services Bureau of Ottawa</td>
      <td>Analyze, review, extract and summarize pertin...</td>
      <td>Ottawa, ON</td>
      <td>12 days ago</td>
      <td>12</td>
      <td>https://ca.indeed.com/jobs?q=Jr%20Business%20D...</td>
    </tr>
    <tr>
      <th>187</th>
      <td>Data Steward I, ITSS Data Governance</td>
      <td>TD Bank</td>
      <td>Complete metadata and data quality tasks. Ide...</td>
      <td>Toronto, ON</td>
      <td>12 days ago</td>
      <td>12</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Steward%20...</td>
    </tr>
    <tr>
      <th>41</th>
      <td>Junior Financial Analyst</td>
      <td>Sault Area Hospital Foundation</td>
      <td>Create and design reports and spreadsheets to...</td>
      <td>Sault Ste. Marie, ON</td>
      <td>12 days ago</td>
      <td>12</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financia...</td>
    </tr>
    <tr>
      <th>71</th>
      <td>Junior Business Analyst</td>
      <td>FYidoctors</td>
      <td>Provide data administration and pipeline trac...</td>
      <td>Calgary, AB</td>
      <td>12 days ago</td>
      <td>12</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business...</td>
    </tr>
    <tr>
      <th>54</th>
      <td>Junior Business Analyst - OpenRoad Head Office</td>
      <td>OpenRoad Auto Group</td>
      <td>Identifying opportunities that improve data a...</td>
      <td>Richmond, BC</td>
      <td>13 days ago</td>
      <td>13</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business...</td>
    </tr>
    <tr>
      <th>184</th>
      <td>Junior Financial Analyst</td>
      <td>The Group Master</td>
      <td>Reporting to the assistant controller, the ju...</td>
      <td>Boucherville, QC</td>
      <td>13 days ago</td>
      <td>13</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financia...</td>
    </tr>
    <tr>
      <th>101</th>
      <td>Business Intelligence Reports Developer I</td>
      <td>Global Excel Management</td>
      <td>Work with all areas to resolve data issues an...</td>
      <td>Sherbrooke, QC</td>
      <td>13 days ago</td>
      <td>13</td>
      <td>https://ca.indeed.com/jobs?q=Business%20Intell...</td>
    </tr>
    <tr>
      <th>99</th>
      <td>Analyst I, Security Advisory and Data Security</td>
      <td>Moneris Solutions Corporation</td>
      <td>Knowledge of data classification and data los...</td>
      <td>Etobicoke, ON</td>
      <td>13 days ago</td>
      <td>13</td>
      <td>https://ca.indeed.com/jobs?q=Analyst%20I%2C%20...</td>
    </tr>
    <tr>
      <th>176</th>
      <td>Analyst, Client Business I</td>
      <td>Mosaic North America</td>
      <td>Interpret data, formulate reports, and make r...</td>
      <td>Toronto, ON</td>
      <td>13 days ago</td>
      <td>13</td>
      <td>https://ca.indeed.com/jobs?q=Analyst%2C%20Clie...</td>
    </tr>
    <tr>
      <th>114</th>
      <td>Junior Financial Analyst</td>
      <td>HUB International</td>
      <td>Assist in organizing building lease data and ...</td>
      <td>Chilliwack, BC</td>
      <td>13 days ago</td>
      <td>13</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financia...</td>
    </tr>
    <tr>
      <th>57</th>
      <td>Jr Data Analyst</td>
      <td>JELD-WEN, inc</td>
      <td>Strong knowledge of using multiple query tool...</td>
      <td>Woodbridge, ON</td>
      <td>13 days ago</td>
      <td>13</td>
      <td>https://ca.indeed.com/jobs?q=Jr%20Data%20Analy...</td>
    </tr>
    <tr>
      <th>124</th>
      <td>Business Analyst I</td>
      <td>TD Bank</td>
      <td>Knowledge of system analysis process and tech...</td>
      <td>Toronto, ON</td>
      <td>13 days ago</td>
      <td>13</td>
      <td>https://ca.indeed.com/jobs?q=Business%20Analys...</td>
    </tr>
    <tr>
      <th>52</th>
      <td>Junior Research Analyst</td>
      <td>Simcoe County District School Board</td>
      <td>Research and/or data analysis; In building da...</td>
      <td>Midhurst, ON</td>
      <td>13 days ago</td>
      <td>13</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Research...</td>
    </tr>
    <tr>
      <th>45</th>
      <td>Junior EA &amp; Data Entry Associate</td>
      <td>Redwood Classics Apparel</td>
      <td>Facilitates/attends special working group mee...</td>
      <td>Toronto, ON</td>
      <td>13 days ago</td>
      <td>13</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20EA%20%26...</td>
    </tr>
    <tr>
      <th>62</th>
      <td>Junior Business Analyst</td>
      <td>Pivotree</td>
      <td>Prototyping - Create wireframes of potential ...</td>
      <td>Toronto, ON</td>
      <td>14 days ago</td>
      <td>14</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business...</td>
    </tr>
    <tr>
      <th>122</th>
      <td>RESEARCH/DATABASE COORDINATOR I (Data Custodian)</td>
      <td>Centre for Global Health Research</td>
      <td>Experience working with GIS/spatial data, hea...</td>
      <td>Toronto, ON</td>
      <td>14 days ago</td>
      <td>14</td>
      <td>https://ca.indeed.com/jobs?q=RESEARCH/DATABASE...</td>
    </tr>
    <tr>
      <th>60</th>
      <td>Financial Analyst (Program), Junior</td>
      <td>General Dynamics Missions Systems-Canada</td>
      <td>Support program audit requirements and reques...</td>
      <td>Ottawa, ON</td>
      <td>14 days ago</td>
      <td>14</td>
      <td>https://ca.indeed.com/jobs?q=Financial%20Analy...</td>
    </tr>
    <tr>
      <th>70</th>
      <td>Jr. Data Engineer - Vancouver</td>
      <td>Randstad</td>
      <td>Proactively monitor data flow across systems ...</td>
      <td>Vancouver, BC</td>
      <td>17 days ago</td>
      <td>17</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data%20Engi...</td>
    </tr>
    <tr>
      <th>190</th>
      <td>Financial Analyst I (Contract)</td>
      <td>Duca</td>
      <td>As part of the Financial Planning &amp;amp; Analy...</td>
      <td>Toronto, ON</td>
      <td>17 days ago</td>
      <td>17</td>
      <td>https://ca.indeed.com/jobs?q=Financial%20Analy...</td>
    </tr>
    <tr>
      <th>192</th>
      <td>Financial Analyst I (Contract)</td>
      <td>DUCA Financial Services Credit Union Ltd.</td>
      <td>As part of the Financial Planning &amp;amp; Analy...</td>
      <td>Toronto, ON</td>
      <td>17 days ago</td>
      <td>17</td>
      <td>https://ca.indeed.com/jobs?q=Financial%20Analy...</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Junior Data Analyst</td>
      <td>The Mustard Seed</td>
      <td>Analyze donor and volunteer data to ensure th...</td>
      <td>Calgary, AB</td>
      <td>18 days ago</td>
      <td>18</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20A...</td>
    </tr>
    <tr>
      <th>149</th>
      <td>Jr. Murex Business Analyst</td>
      <td>CPQi</td>
      <td>Knowledge and understanding of Murex features...</td>
      <td>Halifax, NS</td>
      <td>18 days ago</td>
      <td>18</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Murex%20Bus...</td>
    </tr>
    <tr>
      <th>75</th>
      <td>Trading Desk Analyst</td>
      <td>Aquanow</td>
      <td>Daily processing of transactions and key cont...</td>
      <td>Vancouver, BC</td>
      <td>19 days ago</td>
      <td>19</td>
      <td>https://ca.indeed.com/jobs?q=Trading%20Desk%20...</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Junior Research Analyst</td>
      <td>Carleton University</td>
      <td>?experience organizing and validating data. ?...</td>
      <td>Ottawa, ON</td>
      <td>19 days ago</td>
      <td>19</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Research...</td>
    </tr>
    <tr>
      <th>59</th>
      <td>Jr. Quality Assurance Analyst (Manufacturing)</td>
      <td>MDA</td>
      <td>Implementing approved sampling, reporting and...</td>
      <td>Kanata, ON</td>
      <td>20 days ago</td>
      <td>20</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Quality%20A...</td>
    </tr>
    <tr>
      <th>110</th>
      <td>Business Analyst I, Wireless Fulfillment (Logi...</td>
      <td>TELUS</td>
      <td>Manage and monitor data and inputs required f...</td>
      <td>Scarborough, ON</td>
      <td>20 days ago</td>
      <td>20</td>
      <td>https://ca.indeed.com/jobs?q=Business%20Analys...</td>
    </tr>
    <tr>
      <th>79</th>
      <td>Junior Financial Analyst</td>
      <td>Axis Auto Finance</td>
      <td>Advanced Excel and data mining skills. Assist...</td>
      <td>Mississauga, ON</td>
      <td>20 days ago</td>
      <td>20</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financia...</td>
    </tr>
    <tr>
      <th>127</th>
      <td>Finance Ops Analyst I</td>
      <td>TD Bank</td>
      <td>Support the collection of meaningful data and...</td>
      <td>Dieppe, NB</td>
      <td>24 days ago</td>
      <td>24</td>
      <td>https://ca.indeed.com/jobs?q=Finance%20Ops%20A...</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Junior Data Analyst</td>
      <td>O2E Brands</td>
      <td>Passion for data visualization with Tableau. ...</td>
      <td>Vancouver, BC</td>
      <td>24 days ago</td>
      <td>24</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20A...</td>
    </tr>
    <tr>
      <th>120</th>
      <td>Junior Financial Analyst /Bookkeeper</td>
      <td>Process Fusion Inc.</td>
      <td>Collect, interpret, and report on financial d...</td>
      <td>Toronto, ON</td>
      <td>25 days ago</td>
      <td>25</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financia...</td>
    </tr>
    <tr>
      <th>170</th>
      <td>Analyst, Business I</td>
      <td>Mosaic North America</td>
      <td>Interpret data, formulate reports, and make r...</td>
      <td>Toronto, ON</td>
      <td>25 days ago</td>
      <td>25</td>
      <td>https://ca.indeed.com/jobs?q=Analyst%2C%20Busi...</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Junior Business Analyst</td>
      <td>Eastwood and Cleef</td>
      <td>\*Tasks include, but are not limited to: clie...</td>
      <td>Toronto, ON</td>
      <td>26 days ago</td>
      <td>26</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business...</td>
    </tr>
    <tr>
      <th>63</th>
      <td>CT Data Engineer I - Power BI</td>
      <td>EY</td>
      <td>Reviewing and understanding complex data sets...</td>
      <td>Toronto, ON</td>
      <td>27 days ago</td>
      <td>27</td>
      <td>https://ca.indeed.com/jobs?q=CT%20Data%20Engin...</td>
    </tr>
    <tr>
      <th>111</th>
      <td>Junior Data Scientist</td>
      <td>Providence Health Care</td>
      <td>Reviews clinical data at aggregate levels on ...</td>
      <td>Vancouver, BC</td>
      <td>28 days ago</td>
      <td>28</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20S...</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Junior Data Analysis Assistant</td>
      <td>Universal Rehabilitation Service Agency</td>
      <td>Support the Program Director to create proces...</td>
      <td>Calgary, AB</td>
      <td>28 days ago</td>
      <td>28</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20A...</td>
    </tr>
    <tr>
      <th>96</th>
      <td>Jr. Data Analyst (supply chain and demand plan...</td>
      <td>Noya Cannabis Inc.</td>
      <td>Perform data analysis to identify data integr...</td>
      <td>Hamilton, ON</td>
      <td>28 days ago</td>
      <td>28</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data%20Anal...</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Junior Machine Learning Engineer / Data Scientist</td>
      <td>Virtus Groups</td>
      <td>Candidates must be a Canadian Citizen or Perm...</td>
      <td>Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Machine%...</td>
    </tr>
    <tr>
      <th>134</th>
      <td>Jr Financial Analyst</td>
      <td>Rogers Insurance Ltd</td>
      <td>Strong attention to detail while maintaining ...</td>
      <td>Calgary, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr%20Financial%20...</td>
    </tr>
    <tr>
      <th>160</th>
      <td>Business Analyst I</td>
      <td>TES - The Employment Solution</td>
      <td>Errors are generally related to user data/pro...</td>
      <td>Edmonton, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Business%20Analys...</td>
    </tr>
    <tr>
      <th>147</th>
      <td>MES Business Analyst</td>
      <td>SyLogix Consulting Inc.</td>
      <td>Prior experience with OSIsoft PI or another d...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=MES%20Business%20...</td>
    </tr>
    <tr>
      <th>151</th>
      <td>Financial Business Analyst / Junior Accountant</td>
      <td>Cam Clark Auto Group</td>
      <td>Experience with interactive data visualizatio...</td>
      <td>Airdrie, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Financial%20Busin...</td>
    </tr>
    <tr>
      <th>152</th>
      <td>Jr Financial Analyst - Rogers Insurance</td>
      <td>Sharp Insurance</td>
      <td>Strong attention to detail while maintaining ...</td>
      <td>Calgary, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr%20Financial%20...</td>
    </tr>
    <tr>
      <th>129</th>
      <td>Montreal - Analyste Technique Junior ou chef d...</td>
      <td>FDM Group</td>
      <td>Certains postes courants dans lesquels vous p...</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Montreal%20-%20An...</td>
    </tr>
    <tr>
      <th>97</th>
      <td>Junior Online Marketing Analyst</td>
      <td>Core Online Marketing</td>
      <td>Analytical Skills to interpret data and prese...</td>
      <td>Oakville, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Online%2...</td>
    </tr>
    <tr>
      <th>126</th>
      <td>Clinical Data Manager I</td>
      <td>Labcorp</td>
      <td>Perform reconciliation of the clinical databa...</td>
      <td>Canada</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Clinical%20Data%2...</td>
    </tr>
    <tr>
      <th>49</th>
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
      <td>Junior Business Analyst – CPM/BI</td>
      <td>Corporate Renaissance Group</td>
      <td>Assist in data transformation and validation....</td>
      <td>Ottawa, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business...</td>
    </tr>
    <tr>
      <th>38</th>
      <td>Junior Business Analyst</td>
      <td>RPM TECHNOLOGIES CORP</td>
      <td>Documenting and analyzing the required inform...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business...</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Jr. Data/Reporting Analyst</td>
      <td>Scarsin</td>
      <td>Data management, data analysis and ETL proces...</td>
      <td>Markham, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data/Report...</td>
    </tr>
    <tr>
      <th>36</th>
      <td>Data Analytics Junior Technologist B</td>
      <td>St. Clair College</td>
      <td>Previous experience working with large data s...</td>
      <td>Windsor, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Analytics%...</td>
    </tr>
    <tr>
      <th>50</th>
      <td>Field Data Scientist I / Junior Field Data Sci...</td>
      <td>ThinkData Works</td>
      <td>Conducting research to identify data sources ...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Field%20Data%20Sc...</td>
    </tr>
    <tr>
      <th>128</th>
      <td>Ingénieur de données I / Data Engineer I</td>
      <td>CAE Inc.</td>
      <td>Build the infrastructure required for optimal...</td>
      <td>Saint-Laurent, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Ing%C3%A9nieur%20...</td>
    </tr>
    <tr>
      <th>51</th>
      <td>Junior Analyst Intern, Data &amp; Technology (4-mo...</td>
      <td>University Pension Plan</td>
      <td>Experience with basic data querying (SQL Serv...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Analyst%...</td>
    </tr>
    <tr>
      <th>64</th>
      <td>Junior Big Data Engineer, Business Intelligenc...</td>
      <td>CBC/Radio-Canada</td>
      <td>Batch-processed data as well as streaming dat...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Big%20Da...</td>
    </tr>
    <tr>
      <th>125</th>
      <td>Financial Analyst I, CCRU</td>
      <td>University Health Network</td>
      <td>Experience with financial and cost accounting...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Financial%20Analy...</td>
    </tr>
    <tr>
      <th>123</th>
      <td>Junior Business Analyst</td>
      <td>Genpact</td>
      <td>Expertise in Excel and PowerPoint including P...</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business...</td>
    </tr>
    <tr>
      <th>119</th>
      <td>Business Analyst I #Remote</td>
      <td>PointClickCare</td>
      <td>Experience with modeling tools relating to pr...</td>
      <td>Mississauga, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Business%20Analys...</td>
    </tr>
    <tr>
      <th>118</th>
      <td>Data Scientist I (Quants)</td>
      <td>TD Bank</td>
      <td>Provide technical expertise across a broad ra...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Scientist%...</td>
    </tr>
    <tr>
      <th>117</th>
      <td>Biostatistician I</td>
      <td>University Health Network</td>
      <td>Familiarity in the methods of missing data is...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Biostatistician%2...</td>
    </tr>
    <tr>
      <th>115</th>
      <td>Jr. Business Analyst</td>
      <td>Intimate Interactive Advertising</td>
      <td>Monitor reports and analyze data to identify ...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Business%20...</td>
    </tr>
    <tr>
      <th>113</th>
      <td>Data I/O Coordinator</td>
      <td>FuseFX</td>
      <td>Identifying discrepancies, and errors in data...</td>
      <td>Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Data%20I/O%20Coor...</td>
    </tr>
    <tr>
      <th>112</th>
      <td>Junior Financial Analyst</td>
      <td>Community Natural Foods</td>
      <td>Distribute incoming mail (inter office &amp;amp; ...</td>
      <td>Calgary, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financia...</td>
    </tr>
    <tr>
      <th>108</th>
      <td>Junior Engineer - Logistics Simulation &amp; Busin...</td>
      <td>Ausenco</td>
      <td>Many of the projects will employ logistics si...</td>
      <td>Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Engineer...</td>
    </tr>
    <tr>
      <th>107</th>
      <td>Junior Pricing/ Program Analyst</td>
      <td>Brandt</td>
      <td>Extract and manipulate large data sets to reg...</td>
      <td>Regina, SK</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Pricing/...</td>
    </tr>
    <tr>
      <th>106</th>
      <td>Toronto - Junior Technical Business Analyst/ J...</td>
      <td>FDM Group</td>
      <td>These roles are crucial in helping organizati...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Toronto%20-%20Jun...</td>
    </tr>
    <tr>
      <th>104</th>
      <td>Junior Pricing Analyst</td>
      <td>Bélanger UPT</td>
      <td>Collects data and maintains the database. Pre...</td>
      <td>Mississauga, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Pricing%...</td>
    </tr>
    <tr>
      <th>103</th>
      <td>Junior Marketing Associate - Internship</td>
      <td>AltaML</td>
      <td>As the Junior Marketing Associate, you will l...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Marketin...</td>
    </tr>
    <tr>
      <th>100</th>
      <td>Junior Financial Analyst, Consulting</td>
      <td>BDO</td>
      <td>Strong data collection and analytical skills ...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financia...</td>
    </tr>
    <tr>
      <th>193</th>
      <td>MARKETING SPECIALIST</td>
      <td>ABI - Allstream Business Inc</td>
      <td>This is a junior marketing role with experien...</td>
      <td>Mississauga, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=MARKETING%20SPECI...</td>
    </tr>
    <tr>
      <th>93</th>
      <td>Junior Sales Data Coordinator</td>
      <td>Bélanger UPT</td>
      <td>Reporting to the National Sales &amp;amp; Marketi...</td>
      <td>Mississauga, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Sales%20...</td>
    </tr>
    <tr>
      <th>89</th>
      <td>Junior Database Analyst</td>
      <td>HealthHub Solutions</td>
      <td>Maintain reliability, stability and data inte...</td>
      <td>Mississauga, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Database...</td>
    </tr>
    <tr>
      <th>77</th>
      <td>Junior Business Intelligence Analyst</td>
      <td>Secure Energy</td>
      <td>Inform data integrity and tool availability. ...</td>
      <td>Calgary, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business...</td>
    </tr>
    <tr>
      <th>76</th>
      <td>Junior Business Analyst</td>
      <td>Miller Paving Limited</td>
      <td>Analyzing and summarizing various sales and o...</td>
      <td>Whitby, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business...</td>
    </tr>
    <tr>
      <th>74</th>
      <td>Junior Data Engineer – Client Innovation Cente...</td>
      <td>Groom &amp; Associes</td>
      <td>Knowledge of tools to perform data quality, d...</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20E...</td>
    </tr>
    <tr>
      <th>73</th>
      <td>Junior Power Analyst</td>
      <td>Dynasty Power Inc.</td>
      <td>Analyze data to look for profitable trading s...</td>
      <td>Calgary, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Power%20...</td>
    </tr>
    <tr>
      <th>69</th>
      <td>Jr. Data Scientist</td>
      <td>SimpTek Technologies</td>
      <td>Integration with 3rd party API’s for data col...</td>
      <td>Fredericton, NB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data%20Scie...</td>
    </tr>
    <tr>
      <th>66</th>
      <td>Data Analyst</td>
      <td>WorkTango</td>
      <td>Manage our ETL process for client data transf...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Analyst%20...</td>
    </tr>
    <tr>
      <th>58</th>
      <td>Junior Data Analyst / IT Support Technician</td>
      <td>The Stevens Company Limited</td>
      <td>In-depth knowledge of applicable data privacy...</td>
      <td>Brampton, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20A...</td>
    </tr>
    <tr>
      <th>194</th>
      <td>Junior Quantitative Analyst</td>
      <td>Société Générale</td>
      <td>Assessing data quality and consistency betwee...</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Quantita...</td>
    </tr>
  </tbody>
</table>
</div>




```python
_
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
      <th>34</th>
      <td>Junior Business Analyst intern</td>
      <td>Jonar</td>
      <td>As a Junior Business Analyst, you’ll learn ho...</td>
      <td>Montréal, QC</td>
      <td>Just posted</td>
      <td>0</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business...</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Junior Machine Learning Scientist</td>
      <td>Ecoation</td>
      <td>Analyzing customer horticultural data to prov...</td>
      <td>North Vancouver, BC</td>
      <td>Today</td>
      <td>0</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Machine%...</td>
    </tr>
    <tr>
      <th>94</th>
      <td>Data Scientist I</td>
      <td>TD Bank</td>
      <td>Capture and analyze information or data on cu...</td>
      <td>Toronto, ON</td>
      <td>Today</td>
      <td>0</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Scientist%...</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Junior Data Analyst</td>
      <td>FlightHub</td>
      <td>Analyzing data sets and identifying trends an...</td>
      <td>Montréal, QC</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20A...</td>
    </tr>
    <tr>
      <th>80</th>
      <td>Jr. Data Analyst</td>
      <td>Flex Surveys</td>
      <td>Translating complex data and research outcome...</td>
      <td>Greater Toronto Area, ON</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data%20Anal...</td>
    </tr>
    <tr>
      <th>78</th>
      <td>Data Engineer - Level I</td>
      <td>Swift Medical</td>
      <td>As the world leader in digital wound care man...</td>
      <td>Toronto, ON</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Engineer%2...</td>
    </tr>
    <tr>
      <th>98</th>
      <td>I/O R.O. Enrolment Data Quality Assurance Officer</td>
      <td>George Brown College</td>
      <td>Experience with data mining and reporting uti...</td>
      <td>Toronto, ON</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=I/O%20R.O.%20Enro...</td>
    </tr>
    <tr>
      <th>72</th>
      <td>SAS Developer</td>
      <td>MSi Corp (Bell Canada)</td>
      <td>Document data mapping diagrams and data dicti...</td>
      <td>Ottawa, ON</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=SAS%20Developer%2...</td>
    </tr>
    <tr>
      <th>61</th>
      <td>Analyste PMO junior - Junior PMO Analyst</td>
      <td>Gameloft</td>
      <td>Being responsible for the regular data analyt...</td>
      <td>Montréal, QC</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Analyste%20PMO%20...</td>
    </tr>
    <tr>
      <th>116</th>
      <td>Analyst, Client Data I</td>
      <td>Mosaic North America</td>
      <td>Intermediate knowledge of data cleansing and ...</td>
      <td>Toronto, ON</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Analyst%2C%20Clie...</td>
    </tr>
    <tr>
      <th>105</th>
      <td>Engineering Analyst I</td>
      <td>TES - The Employment Solution</td>
      <td>Knowledge of statistical, mathematical and da...</td>
      <td>Markham, ON</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Engineering%20Ana...</td>
    </tr>
    <tr>
      <th>121</th>
      <td>Research Analyst I, Commercialization</td>
      <td>University Health Network</td>
      <td>Advanced skills in statistical analysis and d...</td>
      <td>Toronto, ON</td>
      <td>4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Research%20Analys...</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Junior Data Analyst</td>
      <td>OSL Retail Services Inc</td>
      <td>Acquire data from primary or secondary data s...</td>
      <td>Mississauga, ON</td>
      <td>4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20A...</td>
    </tr>
    <tr>
      <th>109</th>
      <td>Junior Financial Analyst (FT)</td>
      <td>Part Time CFO Services Inc.</td>
      <td>The Junior Financial Analyst position will be...</td>
      <td>Peterborough, ON</td>
      <td>4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financia...</td>
    </tr>
    <tr>
      <th>148</th>
      <td>Junior Agile Developer- SAP Analytics Cloud</td>
      <td>SAP</td>
      <td>Contribute to hands-on coding, design and tes...</td>
      <td>Vancouver, BC</td>
      <td>4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Agile%20...</td>
    </tr>
    <tr>
      <th>33</th>
      <td>Junior Data Engineer</td>
      <td>Kora</td>
      <td>Help maintain and update the company-level da...</td>
      <td>Toronto, ON</td>
      <td>4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20E...</td>
    </tr>
    <tr>
      <th>48</th>
      <td>Junior Asset Management Consultant and Data An...</td>
      <td>GM BluePlan Engineering</td>
      <td>Develop and analyze asset data to support ass...</td>
      <td>Vaughan, ON</td>
      <td>4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Asset%20...</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Jr. Data Analyst</td>
      <td>Ratehub</td>
      <td>Support in developing and maintaining our dat...</td>
      <td>Toronto, ON</td>
      <td>4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data%20Anal...</td>
    </tr>
    <tr>
      <th>39</th>
      <td>IT Support – Junior Data Coordinator</td>
      <td>Wellsite Masters</td>
      <td>Coordinate and manipulate all data that is de...</td>
      <td>Calgary, AB</td>
      <td>5 days ago</td>
      <td>5</td>
      <td>https://ca.indeed.com/jobs?q=IT%20Support%20%E...</td>
    </tr>
    <tr>
      <th>81</th>
      <td>Jr. Business Analyst</td>
      <td>The Portage Mutual Insurance Company</td>
      <td>Someone who enjoys working with data and solv...</td>
      <td>Winnipeg, MB</td>
      <td>5 days ago</td>
      <td>5</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Business%20...</td>
    </tr>
    <tr>
      <th>139</th>
      <td>OPÉRATRICE OU OPÉRATEUR EN INFORMATIQUE CLASSE...</td>
      <td>Riverside School Board</td>
      <td>They make backup copies, copy compressor dest...</td>
      <td>Saint-Hubert, QC</td>
      <td>5 days ago</td>
      <td>5</td>
      <td>https://ca.indeed.com/jobs?q=OP%C3%89RATRICE%2...</td>
    </tr>
    <tr>
      <th>177</th>
      <td>Laboratory Assistant I - Virology Pre-analytics</td>
      <td>Alberta Precision Laboratories</td>
      <td>You may be required to perform data entry and...</td>
      <td>Edmonton, AB</td>
      <td>5 days ago</td>
      <td>5</td>
      <td>https://ca.indeed.com/jobs?q=Laboratory%20Assi...</td>
    </tr>
    <tr>
      <th>191</th>
      <td>Laboratory Assistant I - Virology Pre-analytics</td>
      <td>Alberta Precision Labs</td>
      <td>You may be required to perform data entry and...</td>
      <td>Edmonton, AB</td>
      <td>5 days ago</td>
      <td>5</td>
      <td>https://ca.indeed.com/jobs?q=Laboratory%20Assi...</td>
    </tr>
    <tr>
      <th>83</th>
      <td>Jr. Business Intelligence Developer, Enterpris...</td>
      <td>Southlake Regional Health Centre</td>
      <td>Develop ETL procedures, SSIS packages and mai...</td>
      <td>Newmarket, ON</td>
      <td>6 days ago</td>
      <td>6</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Business%20...</td>
    </tr>
    <tr>
      <th>68</th>
      <td>IT Analyst I - IT Data Protection Admin</td>
      <td>Alberta Health Services</td>
      <td>Experience with reporting, monitoring, alerti...</td>
      <td>Calgary, AB</td>
      <td>6 days ago</td>
      <td>6</td>
      <td>https://ca.indeed.com/jobs?q=IT%20Analyst%20I%...</td>
    </tr>
    <tr>
      <th>154</th>
      <td>Junior Financial Analyst, Billing /Analyste fi...</td>
      <td>Estruxture Data Centers</td>
      <td>Solid computer skills: good knowledge of Exce...</td>
      <td>Montréal, QC</td>
      <td>6 days ago</td>
      <td>6</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financia...</td>
    </tr>
    <tr>
      <th>95</th>
      <td>Junior Marketing Specialist</td>
      <td>RV SnapPad</td>
      <td>Using formulas to parse data and create visua...</td>
      <td>Calgary, AB</td>
      <td>6 days ago</td>
      <td>6</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Marketin...</td>
    </tr>
    <tr>
      <th>65</th>
      <td>Junior Business Intelligence Specialist (RQ02143)</td>
      <td>Amanst Inc</td>
      <td>Report development and data management. Prepa...</td>
      <td>Greater Toronto Area, ON</td>
      <td>6 days ago</td>
      <td>6</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business...</td>
    </tr>
    <tr>
      <th>67</th>
      <td>Junior MS Database Developer</td>
      <td>Blue North Strategies</td>
      <td>Data management: 3 years (preferred). &amp;gt; Co...</td>
      <td>Guelph, ON</td>
      <td>7 days ago</td>
      <td>7</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20MS%20Dat...</td>
    </tr>
    <tr>
      <th>162</th>
      <td>Analyste fonctionnel I (BI/Analytique)</td>
      <td>Hydro Québec</td>
      <td>Analyser les besoins informatiques et techniq...</td>
      <td>Chicoutimi, QC</td>
      <td>7 days ago</td>
      <td>7</td>
      <td>https://ca.indeed.com/jobs?q=Analyste%20foncti...</td>
    </tr>
    <tr>
      <th>46</th>
      <td>Analyste de l’exploitation des données – Nivea...</td>
      <td>Equifax</td>
      <td>Ensure receipt of data and performs data qual...</td>
      <td>Montréal, QC</td>
      <td>7 days ago</td>
      <td>7</td>
      <td>https://ca.indeed.com/jobs?q=Analyste%20de%20l...</td>
    </tr>
    <tr>
      <th>168</th>
      <td>Analyste fonctionnel I (Applicatif - atout BI)</td>
      <td>Hydro Québec</td>
      <td>Analyser les besoins informatiques et techniq...</td>
      <td>Chicoutimi, QC</td>
      <td>7 days ago</td>
      <td>7</td>
      <td>https://ca.indeed.com/jobs?q=Analyste%20foncti...</td>
    </tr>
    <tr>
      <th>44</th>
      <td>Junior Customer Service and Data Entry</td>
      <td>Pinnacle Fibres Inc.</td>
      <td>Handles quality documentation entry and onlin...</td>
      <td>Saint-Lambert, QC</td>
      <td>10 days ago</td>
      <td>10</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Customer...</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Junior Data Analyst</td>
      <td>Scandinavian Building Services</td>
      <td>Previous experience with large scale data ana...</td>
      <td>Edmonton, AB</td>
      <td>10 days ago</td>
      <td>10</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20A...</td>
    </tr>
    <tr>
      <th>145</th>
      <td>Business Analyst I</td>
      <td>Global Excel Management</td>
      <td>Knowledge of process and data modeling; As a ...</td>
      <td>Sherbrooke, QC</td>
      <td>10 days ago</td>
      <td>10</td>
      <td>https://ca.indeed.com/jobs?q=Business%20Analys...</td>
    </tr>
    <tr>
      <th>189</th>
      <td>Analytics Product Owner I</td>
      <td>TD Bank</td>
      <td>Manage workload of analytics team; assigning ...</td>
      <td>Toronto, ON</td>
      <td>10 days ago</td>
      <td>10</td>
      <td>https://ca.indeed.com/jobs?q=Analytics%20Produ...</td>
    </tr>
    <tr>
      <th>150</th>
      <td>Analyste tarifaire junior (support administrat...</td>
      <td>GLS Canada</td>
      <td>Relevant experience in data manipulation. Nou...</td>
      <td>Dorval, QC</td>
      <td>10 days ago</td>
      <td>10</td>
      <td>https://ca.indeed.com/jobs?q=Analyste%20tarifa...</td>
    </tr>
    <tr>
      <th>146</th>
      <td>Data Steward I</td>
      <td>TD Bank</td>
      <td>Complete metadata and data quality tasks. Ide...</td>
      <td>Toronto, ON</td>
      <td>11 days ago</td>
      <td>11</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Steward%20...</td>
    </tr>
    <tr>
      <th>132</th>
      <td>Financial Analyst I</td>
      <td>Vancouver Drydock</td>
      <td>Perform reconciliations and resolve data disc...</td>
      <td>North Vancouver, BC</td>
      <td>11 days ago</td>
      <td>11</td>
      <td>https://ca.indeed.com/jobs?q=Financial%20Analy...</td>
    </tr>
    <tr>
      <th>47</th>
      <td>Junior Business Intelligence Analyst</td>
      <td>Great Canadian Casinos</td>
      <td>Ensures compliance with all data management p...</td>
      <td>Richmond, BC</td>
      <td>11 days ago</td>
      <td>11</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business...</td>
    </tr>
    <tr>
      <th>32</th>
      <td>JUNIOR FINANCIAL ANALYST</td>
      <td>Ministry of Colleges and Universities</td>
      <td>Research and analyze statistical data from a ...</td>
      <td>Toronto, ON</td>
      <td>12 days ago</td>
      <td>12</td>
      <td>https://ca.indeed.com/jobs?q=JUNIOR%20FINANCIA...</td>
    </tr>
    <tr>
      <th>102</th>
      <td>Jr Business Data Analyst</td>
      <td>Youth Services Bureau of Ottawa</td>
      <td>Analyze, review, extract and summarize pertin...</td>
      <td>Ottawa, ON</td>
      <td>12 days ago</td>
      <td>12</td>
      <td>https://ca.indeed.com/jobs?q=Jr%20Business%20D...</td>
    </tr>
    <tr>
      <th>187</th>
      <td>Data Steward I, ITSS Data Governance</td>
      <td>TD Bank</td>
      <td>Complete metadata and data quality tasks. Ide...</td>
      <td>Toronto, ON</td>
      <td>12 days ago</td>
      <td>12</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Steward%20...</td>
    </tr>
    <tr>
      <th>41</th>
      <td>Junior Financial Analyst</td>
      <td>Sault Area Hospital Foundation</td>
      <td>Create and design reports and spreadsheets to...</td>
      <td>Sault Ste. Marie, ON</td>
      <td>12 days ago</td>
      <td>12</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financia...</td>
    </tr>
    <tr>
      <th>71</th>
      <td>Junior Business Analyst</td>
      <td>FYidoctors</td>
      <td>Provide data administration and pipeline trac...</td>
      <td>Calgary, AB</td>
      <td>12 days ago</td>
      <td>12</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business...</td>
    </tr>
    <tr>
      <th>54</th>
      <td>Junior Business Analyst - OpenRoad Head Office</td>
      <td>OpenRoad Auto Group</td>
      <td>Identifying opportunities that improve data a...</td>
      <td>Richmond, BC</td>
      <td>13 days ago</td>
      <td>13</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business...</td>
    </tr>
    <tr>
      <th>184</th>
      <td>Junior Financial Analyst</td>
      <td>The Group Master</td>
      <td>Reporting to the assistant controller, the ju...</td>
      <td>Boucherville, QC</td>
      <td>13 days ago</td>
      <td>13</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financia...</td>
    </tr>
    <tr>
      <th>101</th>
      <td>Business Intelligence Reports Developer I</td>
      <td>Global Excel Management</td>
      <td>Work with all areas to resolve data issues an...</td>
      <td>Sherbrooke, QC</td>
      <td>13 days ago</td>
      <td>13</td>
      <td>https://ca.indeed.com/jobs?q=Business%20Intell...</td>
    </tr>
    <tr>
      <th>99</th>
      <td>Analyst I, Security Advisory and Data Security</td>
      <td>Moneris Solutions Corporation</td>
      <td>Knowledge of data classification and data los...</td>
      <td>Etobicoke, ON</td>
      <td>13 days ago</td>
      <td>13</td>
      <td>https://ca.indeed.com/jobs?q=Analyst%20I%2C%20...</td>
    </tr>
    <tr>
      <th>176</th>
      <td>Analyst, Client Business I</td>
      <td>Mosaic North America</td>
      <td>Interpret data, formulate reports, and make r...</td>
      <td>Toronto, ON</td>
      <td>13 days ago</td>
      <td>13</td>
      <td>https://ca.indeed.com/jobs?q=Analyst%2C%20Clie...</td>
    </tr>
    <tr>
      <th>114</th>
      <td>Junior Financial Analyst</td>
      <td>HUB International</td>
      <td>Assist in organizing building lease data and ...</td>
      <td>Chilliwack, BC</td>
      <td>13 days ago</td>
      <td>13</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financia...</td>
    </tr>
    <tr>
      <th>57</th>
      <td>Jr Data Analyst</td>
      <td>JELD-WEN, inc</td>
      <td>Strong knowledge of using multiple query tool...</td>
      <td>Woodbridge, ON</td>
      <td>13 days ago</td>
      <td>13</td>
      <td>https://ca.indeed.com/jobs?q=Jr%20Data%20Analy...</td>
    </tr>
    <tr>
      <th>124</th>
      <td>Business Analyst I</td>
      <td>TD Bank</td>
      <td>Knowledge of system analysis process and tech...</td>
      <td>Toronto, ON</td>
      <td>13 days ago</td>
      <td>13</td>
      <td>https://ca.indeed.com/jobs?q=Business%20Analys...</td>
    </tr>
    <tr>
      <th>52</th>
      <td>Junior Research Analyst</td>
      <td>Simcoe County District School Board</td>
      <td>Research and/or data analysis; In building da...</td>
      <td>Midhurst, ON</td>
      <td>13 days ago</td>
      <td>13</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Research...</td>
    </tr>
    <tr>
      <th>45</th>
      <td>Junior EA &amp; Data Entry Associate</td>
      <td>Redwood Classics Apparel</td>
      <td>Facilitates/attends special working group mee...</td>
      <td>Toronto, ON</td>
      <td>13 days ago</td>
      <td>13</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20EA%20%26...</td>
    </tr>
    <tr>
      <th>62</th>
      <td>Junior Business Analyst</td>
      <td>Pivotree</td>
      <td>Prototyping - Create wireframes of potential ...</td>
      <td>Toronto, ON</td>
      <td>14 days ago</td>
      <td>14</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business...</td>
    </tr>
    <tr>
      <th>122</th>
      <td>RESEARCH/DATABASE COORDINATOR I (Data Custodian)</td>
      <td>Centre for Global Health Research</td>
      <td>Experience working with GIS/spatial data, hea...</td>
      <td>Toronto, ON</td>
      <td>14 days ago</td>
      <td>14</td>
      <td>https://ca.indeed.com/jobs?q=RESEARCH/DATABASE...</td>
    </tr>
    <tr>
      <th>60</th>
      <td>Financial Analyst (Program), Junior</td>
      <td>General Dynamics Missions Systems-Canada</td>
      <td>Support program audit requirements and reques...</td>
      <td>Ottawa, ON</td>
      <td>14 days ago</td>
      <td>14</td>
      <td>https://ca.indeed.com/jobs?q=Financial%20Analy...</td>
    </tr>
    <tr>
      <th>70</th>
      <td>Jr. Data Engineer - Vancouver</td>
      <td>Randstad</td>
      <td>Proactively monitor data flow across systems ...</td>
      <td>Vancouver, BC</td>
      <td>17 days ago</td>
      <td>17</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data%20Engi...</td>
    </tr>
    <tr>
      <th>190</th>
      <td>Financial Analyst I (Contract)</td>
      <td>Duca</td>
      <td>As part of the Financial Planning &amp;amp; Analy...</td>
      <td>Toronto, ON</td>
      <td>17 days ago</td>
      <td>17</td>
      <td>https://ca.indeed.com/jobs?q=Financial%20Analy...</td>
    </tr>
    <tr>
      <th>192</th>
      <td>Financial Analyst I (Contract)</td>
      <td>DUCA Financial Services Credit Union Ltd.</td>
      <td>As part of the Financial Planning &amp;amp; Analy...</td>
      <td>Toronto, ON</td>
      <td>17 days ago</td>
      <td>17</td>
      <td>https://ca.indeed.com/jobs?q=Financial%20Analy...</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Junior Data Analyst</td>
      <td>The Mustard Seed</td>
      <td>Analyze donor and volunteer data to ensure th...</td>
      <td>Calgary, AB</td>
      <td>18 days ago</td>
      <td>18</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20A...</td>
    </tr>
    <tr>
      <th>149</th>
      <td>Jr. Murex Business Analyst</td>
      <td>CPQi</td>
      <td>Knowledge and understanding of Murex features...</td>
      <td>Halifax, NS</td>
      <td>18 days ago</td>
      <td>18</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Murex%20Bus...</td>
    </tr>
    <tr>
      <th>75</th>
      <td>Trading Desk Analyst</td>
      <td>Aquanow</td>
      <td>Daily processing of transactions and key cont...</td>
      <td>Vancouver, BC</td>
      <td>19 days ago</td>
      <td>19</td>
      <td>https://ca.indeed.com/jobs?q=Trading%20Desk%20...</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Junior Research Analyst</td>
      <td>Carleton University</td>
      <td>?experience organizing and validating data. ?...</td>
      <td>Ottawa, ON</td>
      <td>19 days ago</td>
      <td>19</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Research...</td>
    </tr>
    <tr>
      <th>59</th>
      <td>Jr. Quality Assurance Analyst (Manufacturing)</td>
      <td>MDA</td>
      <td>Implementing approved sampling, reporting and...</td>
      <td>Kanata, ON</td>
      <td>20 days ago</td>
      <td>20</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Quality%20A...</td>
    </tr>
    <tr>
      <th>110</th>
      <td>Business Analyst I, Wireless Fulfillment (Logi...</td>
      <td>TELUS</td>
      <td>Manage and monitor data and inputs required f...</td>
      <td>Scarborough, ON</td>
      <td>20 days ago</td>
      <td>20</td>
      <td>https://ca.indeed.com/jobs?q=Business%20Analys...</td>
    </tr>
    <tr>
      <th>79</th>
      <td>Junior Financial Analyst</td>
      <td>Axis Auto Finance</td>
      <td>Advanced Excel and data mining skills. Assist...</td>
      <td>Mississauga, ON</td>
      <td>20 days ago</td>
      <td>20</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financia...</td>
    </tr>
    <tr>
      <th>127</th>
      <td>Finance Ops Analyst I</td>
      <td>TD Bank</td>
      <td>Support the collection of meaningful data and...</td>
      <td>Dieppe, NB</td>
      <td>24 days ago</td>
      <td>24</td>
      <td>https://ca.indeed.com/jobs?q=Finance%20Ops%20A...</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Junior Data Analyst</td>
      <td>O2E Brands</td>
      <td>Passion for data visualization with Tableau. ...</td>
      <td>Vancouver, BC</td>
      <td>24 days ago</td>
      <td>24</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20A...</td>
    </tr>
    <tr>
      <th>120</th>
      <td>Junior Financial Analyst /Bookkeeper</td>
      <td>Process Fusion Inc.</td>
      <td>Collect, interpret, and report on financial d...</td>
      <td>Toronto, ON</td>
      <td>25 days ago</td>
      <td>25</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financia...</td>
    </tr>
    <tr>
      <th>170</th>
      <td>Analyst, Business I</td>
      <td>Mosaic North America</td>
      <td>Interpret data, formulate reports, and make r...</td>
      <td>Toronto, ON</td>
      <td>25 days ago</td>
      <td>25</td>
      <td>https://ca.indeed.com/jobs?q=Analyst%2C%20Busi...</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Junior Business Analyst</td>
      <td>Eastwood and Cleef</td>
      <td>\*Tasks include, but are not limited to: clie...</td>
      <td>Toronto, ON</td>
      <td>26 days ago</td>
      <td>26</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business...</td>
    </tr>
    <tr>
      <th>63</th>
      <td>CT Data Engineer I - Power BI</td>
      <td>EY</td>
      <td>Reviewing and understanding complex data sets...</td>
      <td>Toronto, ON</td>
      <td>27 days ago</td>
      <td>27</td>
      <td>https://ca.indeed.com/jobs?q=CT%20Data%20Engin...</td>
    </tr>
    <tr>
      <th>111</th>
      <td>Junior Data Scientist</td>
      <td>Providence Health Care</td>
      <td>Reviews clinical data at aggregate levels on ...</td>
      <td>Vancouver, BC</td>
      <td>28 days ago</td>
      <td>28</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20S...</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Junior Data Analysis Assistant</td>
      <td>Universal Rehabilitation Service Agency</td>
      <td>Support the Program Director to create proces...</td>
      <td>Calgary, AB</td>
      <td>28 days ago</td>
      <td>28</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20A...</td>
    </tr>
    <tr>
      <th>96</th>
      <td>Jr. Data Analyst (supply chain and demand plan...</td>
      <td>Noya Cannabis Inc.</td>
      <td>Perform data analysis to identify data integr...</td>
      <td>Hamilton, ON</td>
      <td>28 days ago</td>
      <td>28</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data%20Anal...</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Junior Machine Learning Engineer / Data Scientist</td>
      <td>Virtus Groups</td>
      <td>Candidates must be a Canadian Citizen or Perm...</td>
      <td>Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Machine%...</td>
    </tr>
    <tr>
      <th>134</th>
      <td>Jr Financial Analyst</td>
      <td>Rogers Insurance Ltd</td>
      <td>Strong attention to detail while maintaining ...</td>
      <td>Calgary, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr%20Financial%20...</td>
    </tr>
    <tr>
      <th>160</th>
      <td>Business Analyst I</td>
      <td>TES - The Employment Solution</td>
      <td>Errors are generally related to user data/pro...</td>
      <td>Edmonton, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Business%20Analys...</td>
    </tr>
    <tr>
      <th>147</th>
      <td>MES Business Analyst</td>
      <td>SyLogix Consulting Inc.</td>
      <td>Prior experience with OSIsoft PI or another d...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=MES%20Business%20...</td>
    </tr>
    <tr>
      <th>151</th>
      <td>Financial Business Analyst / Junior Accountant</td>
      <td>Cam Clark Auto Group</td>
      <td>Experience with interactive data visualizatio...</td>
      <td>Airdrie, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Financial%20Busin...</td>
    </tr>
    <tr>
      <th>152</th>
      <td>Jr Financial Analyst - Rogers Insurance</td>
      <td>Sharp Insurance</td>
      <td>Strong attention to detail while maintaining ...</td>
      <td>Calgary, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr%20Financial%20...</td>
    </tr>
    <tr>
      <th>129</th>
      <td>Montreal - Analyste Technique Junior ou chef d...</td>
      <td>FDM Group</td>
      <td>Certains postes courants dans lesquels vous p...</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Montreal%20-%20An...</td>
    </tr>
    <tr>
      <th>97</th>
      <td>Junior Online Marketing Analyst</td>
      <td>Core Online Marketing</td>
      <td>Analytical Skills to interpret data and prese...</td>
      <td>Oakville, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Online%2...</td>
    </tr>
    <tr>
      <th>126</th>
      <td>Clinical Data Manager I</td>
      <td>Labcorp</td>
      <td>Perform reconciliation of the clinical databa...</td>
      <td>Canada</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Clinical%20Data%2...</td>
    </tr>
    <tr>
      <th>49</th>
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
      <td>Junior Business Analyst – CPM/BI</td>
      <td>Corporate Renaissance Group</td>
      <td>Assist in data transformation and validation....</td>
      <td>Ottawa, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business...</td>
    </tr>
    <tr>
      <th>38</th>
      <td>Junior Business Analyst</td>
      <td>RPM TECHNOLOGIES CORP</td>
      <td>Documenting and analyzing the required inform...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business...</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Jr. Data/Reporting Analyst</td>
      <td>Scarsin</td>
      <td>Data management, data analysis and ETL proces...</td>
      <td>Markham, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data/Report...</td>
    </tr>
    <tr>
      <th>36</th>
      <td>Data Analytics Junior Technologist B</td>
      <td>St. Clair College</td>
      <td>Previous experience working with large data s...</td>
      <td>Windsor, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Analytics%...</td>
    </tr>
    <tr>
      <th>50</th>
      <td>Field Data Scientist I / Junior Field Data Sci...</td>
      <td>ThinkData Works</td>
      <td>Conducting research to identify data sources ...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Field%20Data%20Sc...</td>
    </tr>
    <tr>
      <th>128</th>
      <td>Ingénieur de données I / Data Engineer I</td>
      <td>CAE Inc.</td>
      <td>Build the infrastructure required for optimal...</td>
      <td>Saint-Laurent, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Ing%C3%A9nieur%20...</td>
    </tr>
    <tr>
      <th>51</th>
      <td>Junior Analyst Intern, Data &amp; Technology (4-mo...</td>
      <td>University Pension Plan</td>
      <td>Experience with basic data querying (SQL Serv...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Analyst%...</td>
    </tr>
    <tr>
      <th>64</th>
      <td>Junior Big Data Engineer, Business Intelligenc...</td>
      <td>CBC/Radio-Canada</td>
      <td>Batch-processed data as well as streaming dat...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Big%20Da...</td>
    </tr>
    <tr>
      <th>125</th>
      <td>Financial Analyst I, CCRU</td>
      <td>University Health Network</td>
      <td>Experience with financial and cost accounting...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Financial%20Analy...</td>
    </tr>
    <tr>
      <th>123</th>
      <td>Junior Business Analyst</td>
      <td>Genpact</td>
      <td>Expertise in Excel and PowerPoint including P...</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business...</td>
    </tr>
    <tr>
      <th>119</th>
      <td>Business Analyst I #Remote</td>
      <td>PointClickCare</td>
      <td>Experience with modeling tools relating to pr...</td>
      <td>Mississauga, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Business%20Analys...</td>
    </tr>
    <tr>
      <th>118</th>
      <td>Data Scientist I (Quants)</td>
      <td>TD Bank</td>
      <td>Provide technical expertise across a broad ra...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Scientist%...</td>
    </tr>
    <tr>
      <th>117</th>
      <td>Biostatistician I</td>
      <td>University Health Network</td>
      <td>Familiarity in the methods of missing data is...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Biostatistician%2...</td>
    </tr>
    <tr>
      <th>115</th>
      <td>Jr. Business Analyst</td>
      <td>Intimate Interactive Advertising</td>
      <td>Monitor reports and analyze data to identify ...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Business%20...</td>
    </tr>
    <tr>
      <th>113</th>
      <td>Data I/O Coordinator</td>
      <td>FuseFX</td>
      <td>Identifying discrepancies, and errors in data...</td>
      <td>Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Data%20I/O%20Coor...</td>
    </tr>
    <tr>
      <th>112</th>
      <td>Junior Financial Analyst</td>
      <td>Community Natural Foods</td>
      <td>Distribute incoming mail (inter office &amp;amp; ...</td>
      <td>Calgary, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financia...</td>
    </tr>
    <tr>
      <th>108</th>
      <td>Junior Engineer - Logistics Simulation &amp; Busin...</td>
      <td>Ausenco</td>
      <td>Many of the projects will employ logistics si...</td>
      <td>Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Engineer...</td>
    </tr>
    <tr>
      <th>107</th>
      <td>Junior Pricing/ Program Analyst</td>
      <td>Brandt</td>
      <td>Extract and manipulate large data sets to reg...</td>
      <td>Regina, SK</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Pricing/...</td>
    </tr>
    <tr>
      <th>106</th>
      <td>Toronto - Junior Technical Business Analyst/ J...</td>
      <td>FDM Group</td>
      <td>These roles are crucial in helping organizati...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Toronto%20-%20Jun...</td>
    </tr>
    <tr>
      <th>104</th>
      <td>Junior Pricing Analyst</td>
      <td>Bélanger UPT</td>
      <td>Collects data and maintains the database. Pre...</td>
      <td>Mississauga, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Pricing%...</td>
    </tr>
    <tr>
      <th>103</th>
      <td>Junior Marketing Associate - Internship</td>
      <td>AltaML</td>
      <td>As the Junior Marketing Associate, you will l...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Marketin...</td>
    </tr>
    <tr>
      <th>100</th>
      <td>Junior Financial Analyst, Consulting</td>
      <td>BDO</td>
      <td>Strong data collection and analytical skills ...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financia...</td>
    </tr>
    <tr>
      <th>193</th>
      <td>MARKETING SPECIALIST</td>
      <td>ABI - Allstream Business Inc</td>
      <td>This is a junior marketing role with experien...</td>
      <td>Mississauga, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=MARKETING%20SPECI...</td>
    </tr>
    <tr>
      <th>93</th>
      <td>Junior Sales Data Coordinator</td>
      <td>Bélanger UPT</td>
      <td>Reporting to the National Sales &amp;amp; Marketi...</td>
      <td>Mississauga, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Sales%20...</td>
    </tr>
    <tr>
      <th>89</th>
      <td>Junior Database Analyst</td>
      <td>HealthHub Solutions</td>
      <td>Maintain reliability, stability and data inte...</td>
      <td>Mississauga, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Database...</td>
    </tr>
    <tr>
      <th>77</th>
      <td>Junior Business Intelligence Analyst</td>
      <td>Secure Energy</td>
      <td>Inform data integrity and tool availability. ...</td>
      <td>Calgary, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business...</td>
    </tr>
    <tr>
      <th>76</th>
      <td>Junior Business Analyst</td>
      <td>Miller Paving Limited</td>
      <td>Analyzing and summarizing various sales and o...</td>
      <td>Whitby, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business...</td>
    </tr>
    <tr>
      <th>74</th>
      <td>Junior Data Engineer – Client Innovation Cente...</td>
      <td>Groom &amp; Associes</td>
      <td>Knowledge of tools to perform data quality, d...</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20E...</td>
    </tr>
    <tr>
      <th>73</th>
      <td>Junior Power Analyst</td>
      <td>Dynasty Power Inc.</td>
      <td>Analyze data to look for profitable trading s...</td>
      <td>Calgary, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Power%20...</td>
    </tr>
    <tr>
      <th>69</th>
      <td>Jr. Data Scientist</td>
      <td>SimpTek Technologies</td>
      <td>Integration with 3rd party API’s for data col...</td>
      <td>Fredericton, NB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data%20Scie...</td>
    </tr>
    <tr>
      <th>66</th>
      <td>Data Analyst</td>
      <td>WorkTango</td>
      <td>Manage our ETL process for client data transf...</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Analyst%20...</td>
    </tr>
    <tr>
      <th>58</th>
      <td>Junior Data Analyst / IT Support Technician</td>
      <td>The Stevens Company Limited</td>
      <td>In-depth knowledge of applicable data privacy...</td>
      <td>Brampton, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20A...</td>
    </tr>
    <tr>
      <th>194</th>
      <td>Junior Quantitative Analyst</td>
      <td>Société Générale</td>
      <td>Assessing data quality and consistency betwee...</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Quantita...</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.set_option("display.max_colwidth", None)
_.head()
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    /tmp/ipykernel_77671/884399833.py in <module>
    ----> 1 pd.set_option('display.max_colwidth', None)
          2 _.head()


    NameError: name 'pd' is not defined



```python

```

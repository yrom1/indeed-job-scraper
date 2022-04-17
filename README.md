```python
import pandas as pd
import subprocess
from pathlib import Path
```


```python
subprocess.run(["git", "pull", "--ff-only"])
```

    Already up to date.





    CompletedProcess(args=['git', 'pull', '--ff-only'], returncode=0)




```python
data, sql, py = [], [], []
pickles = list(Path('.').glob('./archive/*'))
for pickle in pickles:
    stem = pickle.stem
    if 'data' in stem:
        data.append(stem)
    if 'sql' in stem:
        sql.append(stem)
    if 'python' in stem:
        py.append(stem)
```


```python
newest_pickles = ['./archive/' + sorted(x)[-1] + '.p' for x in (data, sql, py)]

```


```python
dfs = [pd.read_pickle(pickle) for pickle in newest_pickles]
pd.set_option("display.max_colwidth", None)
pd.set_option("display.max_rows", 999)
```


```python
pd.concat(dfs).drop_duplicates(subset=['titles', 'companyNames'], ignore_index=True).sort_values('clean_dates')
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
      <td>Financial Analyst I</td>
      <td>BGIS</td>
      <td>Enters data to sub ledger systems. Gathers audit support data upon request. Prepares and gathers data to support proper transaction reporting.</td>
      <td>Toronto, ON</td>
      <td>Today</td>
      <td>0</td>
      <td>https://ca.indeed.com/jobs?q=Financial%20Analyst%20I%20BGIS</td>
    </tr>
    <tr>
      <th>107</th>
      <td>Junior DevOps Developer</td>
      <td>Checkfront</td>
      <td>Your daily work will include CI systems, Kubernetes, GCP cloud, maintaining Data Infrastructure like Postgresql and Kafka, and writing Infrastructure as Code…</td>
      <td>Remote in Victoria, BC</td>
      <td>1 day ago</td>
      <td>1</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20DevOps%20Developer%20Checkfront</td>
    </tr>
    <tr>
      <th>108</th>
      <td>Junior Java Developer</td>
      <td>CEO FOUNDRY</td>
      <td>Experience with Core &amp;amp; Advance Java / J2EE. Experience with front-end development technologies such as Angular is helpful as well.</td>
      <td>Remote in Toronto, ON</td>
      <td>Active 1 day ago</td>
      <td>1</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Java%20Developer%20CEO%20FOUNDRY</td>
    </tr>
    <tr>
      <th>218</th>
      <td>Junior Systems Administrator</td>
      <td>PSD</td>
      <td>Functionally rich, technically advanced and user friendly, PSD’s CityWide Enterprise systems are configurable for clients to deal with the current and future…</td>
      <td>Remote in London, ON</td>
      <td>1 day ago</td>
      <td>1</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Systems%20Administrator%20PSD</td>
    </tr>
    <tr>
      <th>106</th>
      <td>Junior Android Developer</td>
      <td>Goopter eCommerce Solutions</td>
      <td>As an Android Mobile Application Developer, you will participate in full-cycle mobile application development. Part-time hours: 40 per week.</td>
      <td>Burnaby, BC</td>
      <td>Active 1 day ago</td>
      <td>1</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Android%20Developer%20Goopter%20eCommerce%20Solutions</td>
    </tr>
    <tr>
      <th>105</th>
      <td>Junior Developer</td>
      <td>Silver Icing Inc</td>
      <td>We are a team of motivated people who believe in inspiring confidence through fashion. The combination of our multi-talented and highly organized group has made…</td>
      <td>Surrey, BC</td>
      <td>1 day ago</td>
      <td>1</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Developer%20Silver%20Icing%20Inc</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Jr. SQL BI Developer</td>
      <td>Vox Mobile</td>
      <td>This role will play an integral role in supporting Vox Mobile business and operations strategy by providing consultative and engineering services in the areas…</td>
      <td>Remote in Waterloo, ON</td>
      <td>1 day ago</td>
      <td>1</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20SQL%20BI%20Developer%20Vox%20Mobile</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Junior Financial Analyst (8 MONTH CONTRACT)</td>
      <td>Cineplex</td>
      <td>Key contact for Ad-hoc business unit and functional are support (modeling, reporting, analysis, data gathering). Bachelor’s degree or equivalent.</td>
      <td>Toronto, ON</td>
      <td>1 day ago</td>
      <td>1</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financial%20Analyst%20%288%20MONTH%20CONTRACT%29%20Cineplex</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Junior Research Analyst</td>
      <td>Altrio Inc.</td>
      <td>Accurate typing and data entry skills. Ad-hoc data and research projects. Data entry: 1 year (preferred). Collect, normalize, validate and structure incoming…</td>
      <td>Toronto, ON</td>
      <td>Active 1 day ago</td>
      <td>1</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Research%20Analyst%20Altrio%20Inc.</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Junior Data Engineer</td>
      <td>Paper</td>
      <td>Develop test plans for source data, analytics/reports, and data pipeline. Analyze upcoming data requirements and perform risk analysis.</td>
      <td>Remote in Montréal, QC</td>
      <td>1 day ago</td>
      <td>1</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Engineer%20Paper</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Junior Financial Analyst, Treasury</td>
      <td>Definity</td>
      <td>Support monthly capital management activities including monitoring and analyzing regular financial reports, investment data, and other information sources to…</td>
      <td>Hybrid remote in Toronto, ON</td>
      <td>2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financial%20Analyst%2C%20Treasury%20Definity</td>
    </tr>
    <tr>
      <th>223</th>
      <td>Software Developer I, Performance Advertising</td>
      <td>Amazon Dev Centre Canada ULC</td>
      <td>Experience coaching junior software development engineers including code review and design review. Programming experience with at least one modern language such…</td>
      <td>Toronto, ON</td>
      <td>2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Software%20Developer%20I%2C%20Performance%20Advertising%20Amazon%20Dev%20Centre%20Canada%20ULC</td>
    </tr>
    <tr>
      <th>222</th>
      <td>Junior Software Engineer</td>
      <td>ORBCOMM</td>
      <td>Experience with multiple software languages, such as C++, C#, Java and dynamic scripting languages such as Lua or python is an asset.</td>
      <td>Remote in Kanata, ON</td>
      <td>Active 2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Engineer%20ORBCOMM</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Junior Data Analytics Engineer</td>
      <td>Tier1 Financial Solutions</td>
      <td>Use large data sets to address business issues. Understanding of data warehousing concepts and NoSQL Databases. BS or MS in Computer Science or related fields.</td>
      <td>Remote in Ontario</td>
      <td>2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Analytics%20Engineer%20Tier1%20Financial%20Solutions</td>
    </tr>
    <tr>
      <th>220</th>
      <td>Junior Linux Administrator</td>
      <td>British Columbia Institute of Technology (BCIT)</td>
      <td>BCIT’s Information Technology Services Department is seeking a regular, junior full-time Linux Administrator to join our Enterprise Systems team.</td>
      <td>Hybrid remote in Burnaby, BC</td>
      <td>2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Linux%20Administrator%20British%20Columbia%20Institute%20of%20Technology%20%28BCIT%29</td>
    </tr>
    <tr>
      <th>219</th>
      <td>Junior C/C++ &amp; Fortran Compiler Developer</td>
      <td>IBM</td>
      <td>Software Developers at IBM are the backbone of our strategic initiatives to design, code, test, and provide industry-leading solutions that make the world run…</td>
      <td>Markham, ON</td>
      <td>2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20C/C%2B%2B%20%26%20Fortran%20Compiler%20Developer%20IBM</td>
    </tr>
    <tr>
      <th>121</th>
      <td>Junior Lead Generator</td>
      <td>Allied Technical Solutions</td>
      <td>ATS is the industry leader in using technology to revolutionize engineering and design processes. Learn and become the expert on data sources, uses, and ways to…</td>
      <td>Toronto, ON</td>
      <td>2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Lead%20Generator%20Allied%20Technical%20Solutions</td>
    </tr>
    <tr>
      <th>120</th>
      <td>Analyste Développeur spécialisé en sécurité applicative (jun...</td>
      <td>CGI</td>
      <td>Analyste Développeur spécialisé en sécurité applicative (junior). Le candidat choisi agira à titre d’analyste-développeur spécialisé en sécurité applicative …</td>
      <td>Montréal, QC</td>
      <td>2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Analyste%20D%C3%A9veloppeur%20sp%C3%A9cialis%C3%A9%20en%20s%C3%A9curit%C3%A9%20applicative%20%28jun...%20CGI</td>
    </tr>
    <tr>
      <th>119</th>
      <td>Software Engineer I (Python)</td>
      <td>Tripadvisor</td>
      <td>An ideal candidate will have experience building and operating one or more web frameworks such as Django or Flask in a cloud environment.</td>
      <td>Remote in Ottawa, ON</td>
      <td>2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Software%20Engineer%20I%20%28Python%29%20Tripadvisor</td>
    </tr>
    <tr>
      <th>118</th>
      <td>Junior Java Developer</td>
      <td>Skythinking Technology Co.Ltd</td>
      <td>Mentor and coach junior developers; Gather and document users' requirements from clients; Translate development requirements and specifications into high…</td>
      <td>Vancouver, BC</td>
      <td>Active 2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Java%20Developer%20Skythinking%20Technology%20Co.Ltd</td>
    </tr>
    <tr>
      <th>117</th>
      <td>Junior Software Developer</td>
      <td>NCM Associates</td>
      <td>The Junior Software Developer is responsible to work within an Agile team to evolve and support our web based reporting platform by creating and enhancing…</td>
      <td>Moncton, NB</td>
      <td>2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20NCM%20Associates</td>
    </tr>
    <tr>
      <th>116</th>
      <td>Junior .Net Developer</td>
      <td>Whistleblower Security</td>
      <td>We have the product, the development processes (CI/CD/Automation) and a solid roadmap in place and need someone who can start to pick up tactical analysis and…</td>
      <td>Temporarily Remote in West Vancouver, BC</td>
      <td>Active 2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20.Net%20Developer%20Whistleblower%20Security</td>
    </tr>
    <tr>
      <th>115</th>
      <td>Junior Software Developer</td>
      <td>Payfirma Corporation</td>
      <td>MerrcoPayfirma is looking for a junior software developer with background in building web and mobile applications. Junior Software Developer / Data Developer.</td>
      <td>&lt;span&gt;Remote&lt;/span&gt;</td>
      <td>2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20Payfirma%20Corporation</td>
    </tr>
    <tr>
      <th>114</th>
      <td>Junior Software Developer</td>
      <td>StarGarden Corporation</td>
      <td>Do you thrive in a fast-paced technical environment and have strong attention to detail? Are you eager to have a career where you are encouraged and supported…</td>
      <td>Vancouver, BC</td>
      <td>2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20StarGarden%20Corporation</td>
    </tr>
    <tr>
      <th>113</th>
      <td>Junior Developer/Backend developer</td>
      <td>Avant Techno Solutions</td>
      <td>Contributes to the overall success of the Global Payment Technology globally by designing, developing, and supporting applications using Shell Scripting, C/C++,…</td>
      <td>Toronto, ON</td>
      <td>Active 2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Developer/Backend%20developer%20Avant%20Techno%20Solutions</td>
    </tr>
    <tr>
      <th>112</th>
      <td>Développeur PHP Junior / Junior PHP Developer</td>
      <td>AppDirect</td>
      <td>IT Cloud est à la recherche d'un programmeur web Full Stack pour un poste permanent. Ce que vous ferez et ce qui vous fera briller. AEC or DEC in programming,.</td>
      <td>Remote in Trois-Rivières, QC</td>
      <td>2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20PHP%20Junior%20/%20Junior%20PHP%20Developer%20AppDirect</td>
    </tr>
    <tr>
      <th>111</th>
      <td>Junior IT Support Specialist</td>
      <td>The Aurum Group</td>
      <td>You are a team player with strong technical, communication, organizational, planning, planning, problem solving, and analytical skills.</td>
      <td>Calgary, AB</td>
      <td>Active 2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20IT%20Support%20Specialist%20The%20Aurum%20Group</td>
    </tr>
    <tr>
      <th>110</th>
      <td>Jr. Java Developer</td>
      <td>Apex Consulting Services</td>
      <td>Experience in Coding using Java, C++, or Python. Strong fundamentals in Core java and data structures. Knowledge in front end technologies like HTML, CSS,…</td>
      <td>McKinley Landing, BC</td>
      <td>Active 2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Java%20Developer%20Apex%20Consulting%20Services</td>
    </tr>
    <tr>
      <th>109</th>
      <td>Junior Production Specialist/SQL Programmer</td>
      <td>Professional Targeted Marketing</td>
      <td>Main/Primary Responsibilities (80% of the time). Handle e-mail, fax and mail broadcasts. Create selection logic using Oracle 11g SQL from production database.</td>
      <td>Markham, ON</td>
      <td>Active 2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Production%20Specialist/SQL%20Programmer%20Professional%20Targeted%20Marketing</td>
    </tr>
    <tr>
      <th>225</th>
      <td>Junior Computer Programmer - Summer Student</td>
      <td>Kobold Corporation</td>
      <td>We are currently looking for a Junior Computer Programmer Summer Student to join our Real-time Information Gathering System (RIGS) project team in Calgary,…</td>
      <td>Calgary, AB</td>
      <td>Active 2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Computer%20Programmer%20-%20Summer%20Student%20Kobold%20Corporation</td>
    </tr>
    <tr>
      <th>226</th>
      <td>Junior Process Engineer- (Downstream) New Grad-2022</td>
      <td>Hatch</td>
      <td>Work on problems and gain experience in the office and on project sites. Participate in local lunch and learns, Student Showcase, Sustainability Week,…</td>
      <td>Mississauga, ON</td>
      <td>2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Process%20Engineer-%20%28Downstream%29%20New%20Grad-2022%20Hatch</td>
    </tr>
    <tr>
      <th>221</th>
      <td>Jr. Analyst, Global Cyber Security</td>
      <td>International Justice Mission</td>
      <td>Technician, Cyber Security to take an active role as an individual contributor in security operations and incident response at IJM.</td>
      <td>Remote in Headquarters, BC</td>
      <td>2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Analyst%2C%20Global%20Cyber%20Security%20International%20Justice%20Mission</td>
    </tr>
    <tr>
      <th>224</th>
      <td>Junior Software Developer - Local Candidates Only</td>
      <td>PK Sound</td>
      <td>Develop and maintain new and existing software products. Analyze, design, and develop tests and test-automation suites. Web development experience with Angular.</td>
      <td>Calgary, AB</td>
      <td>Active 2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20-%20Local%20Candidates%20Only%20PK%20Sound</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Jr Data Scientist</td>
      <td>Olds College</td>
      <td>1-3 years experience in a data scientist or analyst role. Experience with agricultural and environmental research, including involvement on research teams, data…</td>
      <td>Olds, AB</td>
      <td>2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Jr%20Data%20Scientist%20Olds%20College</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Junior Data Analyst / Data Entry</td>
      <td>Strategy Institute</td>
      <td>Conducting data profiling to analyze quality of incoming data &amp;amp; advising on any data cleansing rules. Perform data maintenance tasks when required to ensure…</td>
      <td>Toronto, ON</td>
      <td>Active 2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20/%20Data%20Entry%20Strategy%20Institute</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Data Scientist I</td>
      <td>Northbridge Financial Corporation</td>
      <td>They have a strong sense of ownership and eagerness to solve high-impact business problems using data science. Programming; preferably with R, Python, and SQL.</td>
      <td>Hybrid remote in Toronto, ON</td>
      <td>2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Scientist%20I%20Northbridge%20Financial%20Corporation</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Jr. Data Analyst</td>
      <td>Canadian College</td>
      <td>Maintain confidentiality regarding all student data and information. Minimum 1 year’s experience in data management or analysis. Bachelor's Degree in any field.</td>
      <td>Metro Vancouver Regional District, BC</td>
      <td>Active 2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data%20Analyst%20Canadian%20College</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Junior Financial Analyst</td>
      <td>Credit Valley Conservation</td>
      <td>Support the Finance team in producing meaningful data/analysis. Comfortable working with reports in different formats from various information systems to ensure…</td>
      <td>Mississauga, ON</td>
      <td>2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financial%20Analyst%20Credit%20Valley%20Conservation</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Junior Treasury Analyst</td>
      <td>ETG Commodities Inc.</td>
      <td>Advanced MS Excel and Access skills for reporting and data analysis. Assess accuracy and completeness of data records and conformance with company procedures.</td>
      <td>Mississauga, ON</td>
      <td>Active 2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Treasury%20Analyst%20ETG%20Commodities%20Inc.</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Junior Data Analytics Engineer</td>
      <td>CaseWare RCM</td>
      <td>Use large data sets to address business issues. Understanding of data warehousing concepts and NoSQL Databases. BS or MS in Computer Science or related fields.</td>
      <td>Toronto, ON</td>
      <td>2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Analytics%20Engineer%20CaseWare%20RCM</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Junior Social Media Marketing &amp; Engagement Specialist</td>
      <td>ConsidraCare</td>
      <td>Keeping track of data analyzing the performance of social media campaigns. We are seeking a passionate and creative in-house Social Media Specialist to…</td>
      <td>Brampton, ON</td>
      <td>Active 2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Social%20Media%20Marketing%20%26%20Engagement%20Specialist%20ConsidraCare</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Clinical Data Manager I / Gestionnaire de données cliniques...</td>
      <td>Innovaderm Research</td>
      <td>Develops data transfer agreements and specifications with vendors providing external data (e.g. laboratory results). B.Sc. or in a related field of study;</td>
      <td>&lt;span&gt;Remote&lt;/span&gt;</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Clinical%20Data%20Manager%20I%20/%20Gestionnaire%20de%20donn%C3%A9es%20cliniques...%20Innovaderm%20Research</td>
    </tr>
    <tr>
      <th>122</th>
      <td>Junior Full Stack Developer</td>
      <td>Integrated Sustainability</td>
      <td>As a Junior Full Stack Developer with Random Acronym (a division of Integrated Sustainability), your experience and skills will enable you to make a difference…</td>
      <td>Remote in Calgary, AB</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20Integrated%20Sustainability</td>
    </tr>
    <tr>
      <th>123</th>
      <td>Junior Python Developer</td>
      <td>Leap Tools</td>
      <td>You have a passion for solving complex problems and working on products that people will use on a daily basis. Our game nights are legendary.*.</td>
      <td>Remote in Toronto, ON</td>
      <td>Active 3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Python%20Developer%20Leap%20Tools</td>
    </tr>
    <tr>
      <th>124</th>
      <td>Junior Software Developer</td>
      <td>Keywords Studios</td>
      <td>In this role you will be able to provide technical insights and expertise to support comprehensive automated verification. Fix bugs on existing scripts.</td>
      <td>Temporarily Remote in Vancouver, BC</td>
      <td>Active 3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20Keywords%20Studios</td>
    </tr>
    <tr>
      <th>129</th>
      <td>Junior Backend Developer</td>
      <td>Royal Bank of Canada</td>
      <td>Wealth Management Applied Analytics and Innovation (WMAI) is responsible for developing and implementing a data and analytics strategy that delivers key…</td>
      <td>Toronto, ON</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Backend%20Developer%20Royal%20Bank%20of%20Canada</td>
    </tr>
    <tr>
      <th>126</th>
      <td>Junior Front End Developer</td>
      <td>Leap Tools</td>
      <td>You love the satisfaction that comes from building software that strikes the perfect balance between simplicity, flexibility, and functionality.</td>
      <td>Remote in Toronto, ON</td>
      <td>Active 3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Front%20End%20Developer%20Leap%20Tools</td>
    </tr>
    <tr>
      <th>127</th>
      <td>Junior to Intermediate QA Engineer (Web application, Seleniu...</td>
      <td>Marine Learning Systems</td>
      <td>While our Vancouver office is located on Granville Island, this role will be fully remote (work-from-home), with the option of working at the office if the…</td>
      <td>Remote in Vancouver, BC</td>
      <td>Active 3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20to%20Intermediate%20QA%20Engineer%20%28Web%20application%2C%20Seleniu...%20Marine%20Learning%20Systems</td>
    </tr>
    <tr>
      <th>128</th>
      <td>Junior System Administrator</td>
      <td>VAC Developments Ltd</td>
      <td>Providing first and second-level technical support of current information systems locally. Maintaining, testing, and resolution of issues of all PC hardware and…</td>
      <td>Oakville, ON</td>
      <td>Active 3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20System%20Administrator%20VAC%20Developments%20Ltd</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Junior Business Analyst</td>
      <td>Pride Mobility Products Company</td>
      <td>A passion about organizing data and bringing order to chaos, while also being able to analyze and provide actionable insights. Job Types: Full-time, Permanent.</td>
      <td>Remote in Beamsville, ON</td>
      <td>Active 3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20Pride%20Mobility%20Products%20Company</td>
    </tr>
    <tr>
      <th>125</th>
      <td>Junior Software Developer-AQE</td>
      <td>Keywords Studios</td>
      <td>In this role you will be able to provide technical insights and expertise to support comprehensive automated verification. Previous experience in software QA.</td>
      <td>Temporarily Remote in Vancouver, BC</td>
      <td>Active 3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer-AQE%20Keywords%20Studios</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Junior Accounting Clerk / Financial Analyst</td>
      <td>GUARDIAN PERSONNEL</td>
      <td>This position will involve preparing/generating accounting reports, data entry of accounting information, and preparation for month-end Financial Statements as…</td>
      <td>Edmonton, AB</td>
      <td>Active 3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Accounting%20Clerk%20/%20Financial%20Analyst%20GUARDIAN%20PERSONNEL</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Junior Investment Analyst (Equity Research / Reconciliation)</td>
      <td>Applied Research Investment</td>
      <td>Responsible for ongoing data management; Possess strong research and data analysis skills. Demonstrated passion for research, and investment, data analysis.</td>
      <td>Montréal, QC</td>
      <td>Active 3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Investment%20Analyst%20%28Equity%20Research%20/%20Reconciliation%29%20Applied%20Research%20Investment</td>
    </tr>
    <tr>
      <th>229</th>
      <td>Junior Python programmer</td>
      <td>Visual Defence Inc</td>
      <td>You will work with Visual Defence’s Research and Development team under the guidance of the company’s Director of Research and Development.</td>
      <td>Richmond Hill, ON</td>
      <td>Active 3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Python%20programmer%20Visual%20Defence%20Inc</td>
    </tr>
    <tr>
      <th>18</th>
      <td>GIS Technician and Jr Data Engineer</td>
      <td>QSP Geographics Inc.</td>
      <td>Are Customer-centric – they understand and embrace the role of delivering exemplary service. Lead – they lead by example through their actions and attitudes.</td>
      <td>Toronto, ON</td>
      <td>Active 3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=GIS%20Technician%20and%20Jr%20Data%20Engineer%20QSP%20Geographics%20Inc.</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Business Analyst I - DC IS</td>
      <td>Columbia Sportswear Company</td>
      <td>Moderate to advanced knowledge of data processing and general business practices. This will include providing support and maintenance for computer hardware,…</td>
      <td>London, ON</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Business%20Analyst%20I%20-%20DC%20IS%20Columbia%20Sportswear%20Company</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Junior Business Analyst, Data Management – MS Excel - 337002</td>
      <td>Procom</td>
      <td>Performing new lender/borrower set up and static data validation and maintenance. Maintain Tax Module for maintenances of IRS tax static data for Loan…</td>
      <td>Toronto, ON</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%2C%20Data%20Management%20%E2%80%93%20MS%20Excel%20-%20337002%20Procom</td>
    </tr>
    <tr>
      <th>227</th>
      <td>Jr. Nuage/Cloud 2LS CS Engineer</td>
      <td>NOKIA</td>
      <td>Ability to write scripts at a Unix/Linux level (bash, python). Provide Remote Technical Support (RTS) for the Nuage SDN solutions and associated network…</td>
      <td>Remote in Ottawa, ON</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Nuage/Cloud%202LS%20CS%20Engineer%20NOKIA</td>
    </tr>
    <tr>
      <th>228</th>
      <td>Engineer I</td>
      <td>TD Bank</td>
      <td>We are looking for a developer to support short term surge in demand to enhance and deploy new functionality with DRUM KPI. University or Post-Graduate Degree.</td>
      <td>Toronto, ON</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Engineer%20I%20TD%20Bank</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Junior Business Analyst – Data Mapping/System Integrations -...</td>
      <td>Procom</td>
      <td>Prepares intuitive documentation for data validation purposes. Document data mapping and data fields between source system and candidate system (Process Unity…</td>
      <td>Toronto, ON</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20%E2%80%93%20Data%20Mapping/System%20Integrations%20-...%20Procom</td>
    </tr>
    <tr>
      <th>230</th>
      <td>Junior Technical Project Manager</td>
      <td>Leap Tools</td>
      <td>You have your finger on the pulse of all activities in your domain, no matter the complexity or the timelines. Our game nights are legendary.*.</td>
      <td>Remote in Toronto, ON</td>
      <td>Active 3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Technical%20Project%20Manager%20Leap%20Tools</td>
    </tr>
    <tr>
      <th>132</th>
      <td>Junior Systems Administrator</td>
      <td>Vicinity Motor Corporation</td>
      <td>No experience is necessary, you will be trained by the IT Manager directly. Develop knowledge base and content. Develop IT procedures and policies.</td>
      <td>Langley, BC</td>
      <td>4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Systems%20Administrator%20Vicinity%20Motor%20Corporation</td>
    </tr>
    <tr>
      <th>131</th>
      <td>DevOps Specialist I</td>
      <td>PortfolioAid Inc.</td>
      <td>Category: Permanent, Full Time, Monday-Friday, Regular Hours. § Implement release processes across development, test, and production environments.</td>
      <td>Toronto, ON</td>
      <td>Active 4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=DevOps%20Specialist%20I%20PortfolioAid%20Inc.</td>
    </tr>
    <tr>
      <th>130</th>
      <td>Junior Programmer</td>
      <td>Express Employment Professionals - Red Deer</td>
      <td>In this role you will meet customer’s needs by programming application specific solutions including a broad line of touchscreen and keypad user interfaces,…</td>
      <td>Lacombe, AB</td>
      <td>Active 4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Programmer%20Express%20Employment%20Professionals%20-%20Red%20Deer</td>
    </tr>
    <tr>
      <th>233</th>
      <td>Junior Python /Go Developer</td>
      <td>National Bank of Canada</td>
      <td>In order to start new initiatives, we are looking for three more developers, with intermediate to senior levels. Good collaboration attitude and autonomy.</td>
      <td>Montréal, QC</td>
      <td>4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Python%20/Go%20Developer%20National%20Bank%20of%20Canada</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Junior Data Analyst</td>
      <td>Beta-Calco</td>
      <td>Gain and update job knowledge to remain informed about innovation in the field, explore and implement use cases for data science/data analytics to improve…</td>
      <td>Remote in Toronto, ON</td>
      <td>Active 4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20Beta-Calco</td>
    </tr>
    <tr>
      <th>231</th>
      <td>Python Developer - Junior</td>
      <td>Alithya</td>
      <td>Candidates must have an eligible work permit for Canada and be fluent in French. Analyze customer and user requirements and propose an IT solution adapted to…</td>
      <td>Remote in Montréal, QC</td>
      <td>4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Python%20Developer%20-%20Junior%20Alithya</td>
    </tr>
    <tr>
      <th>133</th>
      <td>Junior Programmer</td>
      <td>FirstService Residential</td>
      <td>As the leading and largest residential property management company in North America, FirstService provides full-service, professional community management…</td>
      <td>Hybrid remote in Mississauga, ON</td>
      <td>4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Programmer%20FirstService%20Residential</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Junior Data Scientist - Deep Learning</td>
      <td>ASL Environmental Sciences Inc.</td>
      <td>Knowledge of geomatics tools and remote sensing data. Work with geospatial tools and data including multispectral and SAR imagery.</td>
      <td>Victoria, BC</td>
      <td>4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Scientist%20-%20Deep%20Learning%20ASL%20Environmental%20Sciences%20Inc.</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Junior Business Analyst</td>
      <td>Beyond Bilingual Inc.</td>
      <td>Collaborate with development and support teams to answer business questions using data and business analysis best practices.</td>
      <td>Thornhill, ON</td>
      <td>Active 4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20Beyond%20Bilingual%20Inc.</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Jr. Financial Analyst</td>
      <td>realtor.com</td>
      <td>Resourceful/able to find or develop compelling data. Analyze data and prepare KPI reports for distribution to senior management.</td>
      <td>Vancouver, BC</td>
      <td>4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Financial%20Analyst%20realtor.com</td>
    </tr>
    <tr>
      <th>232</th>
      <td>Information Security Analyst I (Terrace)</td>
      <td>Coast Mountain College</td>
      <td>Coast Mountain College (CMTN), Terrace campus, invites applications for a continuing full-time Information Security Analyst I. This position requires a flexible…</td>
      <td>Terrace, BC</td>
      <td>4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Information%20Security%20Analyst%20I%20%28Terrace%29%20Coast%20Mountain%20College</td>
    </tr>
    <tr>
      <th>134</th>
      <td>Junior Developer</td>
      <td>Norima Consulting</td>
      <td>A bachelor's degree in Computer Science, Engineering or similar. A minimum of 1-2 years of proven work experience in software development.</td>
      <td>Remote in Winnipeg, MB</td>
      <td>Active 5 days ago</td>
      <td>5</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Developer%20Norima%20Consulting</td>
    </tr>
    <tr>
      <th>141</th>
      <td>Développeur Python/Go junior</td>
      <td>Banque Nationale du Canada</td>
      <td>Nous sommes une équipe multidisciplinaire de six développeurs au sein d’un groupe de transformation DevOps et d’adoption du Cloud. Une expérience avec un Cloud.</td>
      <td>Remote in Montréal, QC</td>
      <td>5 days ago</td>
      <td>5</td>
      <td>https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20Python/Go%20junior%20Banque%20Nationale%20du%20Canada</td>
    </tr>
    <tr>
      <th>136</th>
      <td>Jr. Developer</td>
      <td>taq</td>
      <td>The Jr. Developer will participate in all phases of the software development life cycle including design, development, enhancement, and maintenance.</td>
      <td>Markham, ON</td>
      <td>Active 5 days ago</td>
      <td>5</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Developer%20taq</td>
    </tr>
    <tr>
      <th>137</th>
      <td>Linux Support Engineer (Junior)</td>
      <td>LinuxMagic</td>
      <td>Front line product support via email and phone. Troubleshooting a variety of technical issues our valued customers may have with their Linux systems.</td>
      <td>Vancouver, BC</td>
      <td>Active 5 days ago</td>
      <td>5</td>
      <td>https://ca.indeed.com/jobs?q=Linux%20Support%20Engineer%20%28Junior%29%20LinuxMagic</td>
    </tr>
    <tr>
      <th>138</th>
      <td>Junior Resource Analyst</td>
      <td>Ecora</td>
      <td>Data manipulation, forest estate modelling, and resource planning; and. Contribute to projects managed by project teams in areas such as, but not limited to,…</td>
      <td>Vancouver, BC</td>
      <td>Active 5 days ago</td>
      <td>5</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Resource%20Analyst%20Ecora</td>
    </tr>
    <tr>
      <th>139</th>
      <td>Jr Software Developer (Remote/Hybrid)</td>
      <td>CADdetails Ltd.</td>
      <td>Assisting the development manager with all aspects of software design and coding. Attending and contributing to company development meetings.</td>
      <td>Remote in London, ON</td>
      <td>Active 5 days ago</td>
      <td>5</td>
      <td>https://ca.indeed.com/jobs?q=Jr%20Software%20Developer%20%28Remote/Hybrid%29%20CADdetails%20Ltd.</td>
    </tr>
    <tr>
      <th>140</th>
      <td>Junior or Intermediate Quality Assurance Analyst</td>
      <td>LBMX Inc</td>
      <td>We are looking for a Junior or Intermediate Quality Assurance Analyst to work with our QA team, conducting testing of our web and desktop applications.</td>
      <td>Temporarily Remote in London, ON</td>
      <td>Active 5 days ago</td>
      <td>5</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20or%20Intermediate%20Quality%20Assurance%20Analyst%20LBMX%20Inc</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Junior Business Analyst - 336705</td>
      <td>Procom</td>
      <td>Synthetizing large amounts of data and identifying trends, potentials risks and developing remediation plans; Managing and tracking budget activities;</td>
      <td>Montréal, QC</td>
      <td>5 days ago</td>
      <td>5</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20-%20336705%20Procom</td>
    </tr>
    <tr>
      <th>142</th>
      <td>Junior Developer</td>
      <td>The Corner Office</td>
      <td>The Corner Office is a growing professional services firm providing out-sourced accounting services. The Junior Developer would partner with the Senior Data…</td>
      <td>Regina, SK</td>
      <td>Active 5 days ago</td>
      <td>5</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Developer%20The%20Corner%20Office</td>
    </tr>
    <tr>
      <th>234</th>
      <td>Compositor - Junior</td>
      <td>Tryptyc Theory</td>
      <td>Great artistic sense and aesthetic a must. Strong Nuke proficiency, including good organization of scripts and workflow. Knowledge of Python coding is a bonus.</td>
      <td>Remote in Toronto, ON</td>
      <td>5 days ago</td>
      <td>5</td>
      <td>https://ca.indeed.com/jobs?q=Compositor%20-%20Junior%20Tryptyc%20Theory</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Junior Global Business Analyst</td>
      <td>ZOOK Canada Inc</td>
      <td>Conduct data mining and executes queries to process data from multiple sources. Analyze data and prepare reports/dashboards that show key trends and metrics.</td>
      <td>Burlington, ON</td>
      <td>5 days ago</td>
      <td>5</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Global%20Business%20Analyst%20ZOOK%20Canada%20Inc</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Junior Fiscal Policy Analyst</td>
      <td>Validus Healthcare Economics Inc.</td>
      <td>Knowledge of computer languages useful for data analysis, such as R or Python, considered an asset. Experience researching and analyzing complex Canadian public…</td>
      <td>Remote in Winnipeg, MB</td>
      <td>Active 5 days ago</td>
      <td>5</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Fiscal%20Policy%20Analyst%20Validus%20Healthcare%20Economics%20Inc.</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Jr. and Sr. Analytics Consultant</td>
      <td>Advanced Analytics and Research Lab</td>
      <td>Has experiences in data visualization, such as Tableau or Qlik. Attend analytics, data science, AI and industry conferences and workshops, developing your own…</td>
      <td>Toronto, ON</td>
      <td>5 days ago</td>
      <td>5</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20and%20Sr.%20Analytics%20Consultant%20Advanced%20Analytics%20and%20Research%20Lab</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Junior Financial Analyst</td>
      <td>Thomas, Large &amp; Singer</td>
      <td>Payable and Accounts Receivable data entry. Reporting the Senior Director, Finance &amp;amp; Client Services, the Junior Financial Analyst is responsible for preparing…</td>
      <td>Hybrid remote in Markham, ON</td>
      <td>Active 5 days ago</td>
      <td>5</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financial%20Analyst%20Thomas%2C%20Large%20%26%20Singer</td>
    </tr>
    <tr>
      <th>135</th>
      <td>Junior System Administrator</td>
      <td>GNK Holdings Inc.</td>
      <td>As a Junior System Administrator, you will provide technical support of HW/SW, corporate system/server/network management, consultation, and procurement for all…</td>
      <td>Vaughan, ON</td>
      <td>5 days ago</td>
      <td>5</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20System%20Administrator%20GNK%20Holdings%20Inc.</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Junior Business Analyst (AP)</td>
      <td>Staffmax</td>
      <td>Collaborate with our development and support teams to answer business questions using data and business analysis best practices.</td>
      <td>Thornhill, ON</td>
      <td>Active 6 days ago</td>
      <td>6</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20%28AP%29%20Staffmax</td>
    </tr>
    <tr>
      <th>143</th>
      <td>IT Analyst I</td>
      <td>Alberta Health Services</td>
      <td>Reporting to the Manager – Alberta Netcare Portal, the IT Analyst is responsible for the support, development and configuration for the Alberta Netcare Portal,…</td>
      <td>Edmonton, AB</td>
      <td>7 days ago</td>
      <td>7</td>
      <td>https://ca.indeed.com/jobs?q=IT%20Analyst%20I%20Alberta%20Health%20Services</td>
    </tr>
    <tr>
      <th>235</th>
      <td>Junior Software Developer (DataHub Team)</td>
      <td>Pason Systems Corp</td>
      <td>You love solving problems and enjoy getting to the root cause of issues. You enjoy exploring new technologies to deliver a reliable, secure, and highly…</td>
      <td>Hybrid remote in Calgary, AB</td>
      <td>7 days ago</td>
      <td>7</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20%28DataHub%20Team%29%20Pason%20Systems%20Corp</td>
    </tr>
    <tr>
      <th>33</th>
      <td>Junior Business Analyst</td>
      <td>Colas</td>
      <td>The Analyst will assist in analyzing the data and preparing summary notes and dashboards/graphs/charts that will be shared with the sales &amp;amp; operations teams.</td>
      <td>Remote in Scarborough, ON</td>
      <td>7 days ago</td>
      <td>7</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20Colas</td>
    </tr>
    <tr>
      <th>147</th>
      <td>Junior Field Service Specialist</td>
      <td>Thales Group</td>
      <td>Thales people architect solutions that enable two-thirds of planes to take off and land safely. This includes Software, Hardware, Systems Design, Verification &amp;amp;…</td>
      <td>Toronto, ON</td>
      <td>8 days ago</td>
      <td>8</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Field%20Service%20Specialist%20Thales%20Group</td>
    </tr>
    <tr>
      <th>146</th>
      <td>Junior .NET Developer- (remote)</td>
      <td>Avesdo</td>
      <td>Net Core (C#) to help our software development teams execute high-impact initiatives that fuel Avesdo's growth. Translate user stories to design to code.</td>
      <td>Remote in Vancouver, BC</td>
      <td>8 days ago</td>
      <td>8</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20.NET%20Developer-%20%28remote%29%20Avesdo</td>
    </tr>
    <tr>
      <th>145</th>
      <td>Junior Business Systems Analyst (Application Life Cycle)</td>
      <td>Maximus</td>
      <td>Maximus Canada offers competitive market-based salaries, comprehensive employer-paid benefits and a defined-benefit pension plan or a Group RSP with employer…</td>
      <td>Remote in Victoria, BC</td>
      <td>8 days ago</td>
      <td>8</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Systems%20Analyst%20%28Application%20Life%20Cycle%29%20Maximus</td>
    </tr>
    <tr>
      <th>144</th>
      <td>Junior Analyst - GCLP (Toronto, ON)</td>
      <td>Guardian Capital Group Limited</td>
      <td>Of clients within the financial services sector. Institutional investment management services are provided by. This will entail reviewing and developing data.</td>
      <td>Toronto, ON</td>
      <td>8 days ago</td>
      <td>8</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Analyst%20-%C2%A0GCLP%20%28Toronto%2C%20ON%29%20Guardian%20Capital%20Group%20Limited</td>
    </tr>
    <tr>
      <th>236</th>
      <td>DevOps Junior / Junior DevOps</td>
      <td>Opal-RT</td>
      <td>À propos d’OPAL-RT Technologies. OPAL-RT s’est donné comme ambitieux défi de démocratiser la simulation temps réel afin de la rendre accessible à chaque…</td>
      <td>Remote in Montréal, QC</td>
      <td>8 days ago</td>
      <td>8</td>
      <td>https://ca.indeed.com/jobs?q=DevOps%20Junior%20/%20Junior%20DevOps%20Opal-RT</td>
    </tr>
    <tr>
      <th>237</th>
      <td>Junior Full Stack Developer</td>
      <td>Helcim</td>
      <td>Helcim is searching for an Junior Full Stack Developer to be responsible for helping develop a wide variety of features including both frontend and backend…</td>
      <td>Hybrid remote in Calgary, AB</td>
      <td>8 days ago</td>
      <td>8</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20Helcim</td>
    </tr>
    <tr>
      <th>36</th>
      <td>Junior Business Analyst - Reporting &amp; Analytics</td>
      <td>TripArc</td>
      <td>Recommend and develop automation solutions for our data and reporting needs. Collaborate with our development, database and support teams to answer business…</td>
      <td>Toronto, ON</td>
      <td>8 days ago</td>
      <td>8</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20-%20Reporting%20%26%20Analytics%20TripArc</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Junior Data Analyst</td>
      <td>OSL Retail Services Inc</td>
      <td>Acquire data from primary or secondary data sources and maintain databases/data systems. Proven working experience as a data analyst or business data analyst.</td>
      <td>Mississauga, ON</td>
      <td>8 days ago</td>
      <td>8</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20OSL%20Retail%20Services%20Inc</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Junior Business Analyst, Strategic Partnerships and Performa...</td>
      <td>Vancouver Coastal Health</td>
      <td>Practices diligence and care when maintaining, monitoring, calculating and summarizing data, records and confidential information.</td>
      <td>Vancouver, BC</td>
      <td>8 days ago</td>
      <td>8</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%2C%20Strategic%20Partnerships%20and%20Performa...%20Vancouver%20Coastal%20Health</td>
    </tr>
    <tr>
      <th>148</th>
      <td>Développeur .Net Junior</td>
      <td>Logient</td>
      <td>Vous êtes de ceux qui croient qu’apprendre, ça garde jeune. Logient est à la recherche d’un* Développeur . NET Junior*, qui se joindra à son équipe de virtuoses…</td>
      <td>Montréal, QC</td>
      <td>9 days ago</td>
      <td>9</td>
      <td>https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20.Net%20Junior%20Logient</td>
    </tr>
    <tr>
      <th>238</th>
      <td>Junior ASIC Verification Engineer</td>
      <td>NETINT Technologies Inc.</td>
      <td>You will work closely with ASIC design and verification engineers to verify SOC function features, close function &amp;amp; code coverage holes.</td>
      <td>Markham, ON</td>
      <td>9 days ago</td>
      <td>9</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20ASIC%20Verification%20Engineer%20NETINT%20Technologies%20Inc.</td>
    </tr>
    <tr>
      <th>149</th>
      <td>Développeur Junior / Intermédiaire (1 à 4 ans d’expérience)</td>
      <td>DECIMAL</td>
      <td>Notre expertise en gestion de performance, reconnue depuis plus de 30 ans, nous permet aujourd’hui de nous définir comme des créateurs d’informations de gestion…</td>
      <td>Longueuil, QC</td>
      <td>9 days ago</td>
      <td>9</td>
      <td>https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20Junior%20/%20Interm%C3%A9diaire%20%281%20%C3%A0%204%20ans%20d%E2%80%99exp%C3%A9rience%29%20DECIMAL</td>
    </tr>
    <tr>
      <th>151</th>
      <td>Junior Systems Developer</td>
      <td>Queen's University</td>
      <td>The Information Technology Services department at Queen's University requires a Junior Systems Developer to design, develop, implement and troubleshoot web…</td>
      <td>Kingston, ON</td>
      <td>9 days ago</td>
      <td>9</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Systems%20Developer%20Queen%27s%20University</td>
    </tr>
    <tr>
      <th>150</th>
      <td>Junior Software Developer (Co-op/Contract) - AI Project</td>
      <td>Binary Stream</td>
      <td>Binary Stream is an award-winning, Microsoft Gold certified partner that develops enterprise-grade software to enhance Microsoft Dynamics 365.</td>
      <td>Burnaby, BC</td>
      <td>9 days ago</td>
      <td>9</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20%28Co-op/Contract%29%20-%20AI%20Project%20Binary%20Stream</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Electrical EIT, Data Centres</td>
      <td>WSP</td>
      <td>Basic knowledge of power distribution topologies for data centres and familiarity with redundancy concepts; Provide support in preparation of engineering design…</td>
      <td>Markham, ON</td>
      <td>9 days ago</td>
      <td>9</td>
      <td>https://ca.indeed.com/jobs?q=Electrical%20EIT%2C%20Data%20Centres%20WSP</td>
    </tr>
    <tr>
      <th>38</th>
      <td>Business Analyst I</td>
      <td>TES - The Employment Solution</td>
      <td>Analyze financial data for decision support. Extensive experience in analyzing and evaluating data. MS Skills: Must have advanced MS Excel skills.</td>
      <td>North York, ON</td>
      <td>9 days ago</td>
      <td>9</td>
      <td>https://ca.indeed.com/jobs?q=Business%20Analyst%20I%20TES%20-%20The%20Employment%20Solution</td>
    </tr>
    <tr>
      <th>39</th>
      <td>Business Analyst I - TELUS Health</td>
      <td>TELUS</td>
      <td>Experience analysing and reporting on performance and utilisation data. The successful candidate must be a strong creative and analytical thinker with strong…</td>
      <td>Toronto, ON</td>
      <td>9 days ago</td>
      <td>9</td>
      <td>https://ca.indeed.com/jobs?q=Business%20Analyst%20I%20-%20TELUS%20Health%20TELUS</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Inventory Analysts - Remote</td>
      <td>Hunt Personnel Temporarily Yours</td>
      <td>Analyze previous sales data, forecast future sales. The other is a senior position requiring a minimum of 6 years’ experience. Degree or diploma in business.</td>
      <td>Remote in Richmond, BC</td>
      <td>Active 9 days ago</td>
      <td>9</td>
      <td>https://ca.indeed.com/jobs?q=Inventory%20Analysts%20-%20Remote%20Hunt%20Personnel%20Temporarily%20Yours</td>
    </tr>
    <tr>
      <th>41</th>
      <td>Business Analyst I, OPL</td>
      <td>Intact</td>
      <td>Please note that for positions with access to financial data or funds, your credit must be in good standing. Obtain requirements from business communities using…</td>
      <td>Remote in Quebec City, QC</td>
      <td>9 days ago</td>
      <td>9</td>
      <td>https://ca.indeed.com/jobs?q=Business%20Analyst%20I%2C%20OPL%20Intact</td>
    </tr>
    <tr>
      <th>42</th>
      <td>Mechanical EIT, Data Centres</td>
      <td>WSP</td>
      <td>Basic knowledge of building mechanical systems to support data centres (DCs); Reporting directly to the Mechanical Engineering Team Lead or Manager, works under…</td>
      <td>Markham, ON</td>
      <td>9 days ago</td>
      <td>9</td>
      <td>https://ca.indeed.com/jobs?q=Mechanical%20EIT%2C%20Data%20Centres%20WSP</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Junior Database Analyst</td>
      <td>HealthHub Solutions</td>
      <td>Maintain reliability, stability and data integrity of the databases. 1-2 years of experience as a data administrator in SQL server environment.</td>
      <td>Mississauga, ON</td>
      <td>9 days ago</td>
      <td>9</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Database%20Analyst%20HealthHub%20Solutions</td>
    </tr>
    <tr>
      <th>154</th>
      <td>Junior Automation Specialist</td>
      <td>Roberts Onsite Inc</td>
      <td>The Junior Automation Specialist position is located in Kitchener, Ontario and reports directly to the Automation Controls &amp;amp; Engineering Manager.</td>
      <td>Kitchener, ON</td>
      <td>10 days ago</td>
      <td>10</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Automation%20Specialist%20Roberts%20Onsite%20Inc</td>
    </tr>
    <tr>
      <th>240</th>
      <td>Jr Django REST/Python Developer</td>
      <td>focal</td>
      <td>Fully fluent in python + javascript. Canadian Citizen or Permanent Resident. Currently Enrolled Post Secondary Student. Co-op students are welcome.</td>
      <td>Victoria, BC</td>
      <td>Active 10 days ago</td>
      <td>10</td>
      <td>https://ca.indeed.com/jobs?q=Jr%20Django%20REST/Python%20Developer%20focal</td>
    </tr>
    <tr>
      <th>239</th>
      <td>Junior Electronics Engineer - Integration and Testing</td>
      <td>Preciseley Microtechnology</td>
      <td>Basic programming skills in C, Labview or python. Salary starting at $55,000 depending on experience. Training and development opportunities in a growing…</td>
      <td>Burnaby, BC</td>
      <td>10 days ago</td>
      <td>10</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Electronics%20Engineer%20-%20Integration%20and%20Testing%20Preciseley%20Microtechnology</td>
    </tr>
    <tr>
      <th>153</th>
      <td>Junior Oracle DBA</td>
      <td>AstraNorth</td>
      <td>Defines and administers data base organization, standards, controls, procedures, and documentation. Provides experienced technical consulting in the definition,…</td>
      <td>Toronto, ON</td>
      <td>10 days ago</td>
      <td>10</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Oracle%20DBA%20AstraNorth</td>
    </tr>
    <tr>
      <th>152</th>
      <td>Junior Analyst</td>
      <td>BCAA</td>
      <td>Work at an award-winning top employer! If you are looking for an empowering and progressive place to shape your future, then you’ve landed in the right place at…</td>
      <td>Canada</td>
      <td>10 days ago</td>
      <td>10</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Analyst%20BCAA</td>
    </tr>
    <tr>
      <th>44</th>
      <td>Junior Business Analyst</td>
      <td>SMART TRADE TECHNOLOGIES</td>
      <td>Exposure and/or interest in data science or mathematics is a plus. SmartTrade Technologies is a software company specialising in the trading and finance sector.</td>
      <td>Toronto, ON</td>
      <td>Active 10 days ago</td>
      <td>10</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20SMART%20TRADE%20TECHNOLOGIES</td>
    </tr>
    <tr>
      <th>45</th>
      <td>Junior Business Analyst</td>
      <td>Norsat International Inc.</td>
      <td>Develop and monitor data quality metrics and ensure business data and reporting needs are met. You are responsible for developing and monitoring data quality…</td>
      <td>Richmond, BC</td>
      <td>11 days ago</td>
      <td>11</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20Norsat%20International%20Inc.</td>
    </tr>
    <tr>
      <th>157</th>
      <td>Junior Full Stack Developer</td>
      <td>Plan de Vol</td>
      <td>&amp;gt; Willingness and experience to mentor junior developers. To be eligible for this funding, candidates must be Canadian Citizens, Permanent Residents, and under…</td>
      <td>Temporarily Remote in Toronto, ON</td>
      <td>Active 11 days ago</td>
      <td>11</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20Plan%20de%20Vol</td>
    </tr>
    <tr>
      <th>156</th>
      <td>Junior Java Developer</td>
      <td>AstraNorth</td>
      <td>Undergraduate Degree or Technical Certificate. 1-2 years relevant experience. Good knowledge on various programming languages like Java, JavaScript, Python,…</td>
      <td>Toronto, ON</td>
      <td>11 days ago</td>
      <td>11</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Java%20Developer%20AstraNorth</td>
    </tr>
    <tr>
      <th>159</th>
      <td>Quality Engineer I</td>
      <td>TD Bank</td>
      <td>Provides foundational testing, automation and / or process support, research, and design input within a well-defined functional area to support the delivery of…</td>
      <td>Toronto, ON</td>
      <td>11 days ago</td>
      <td>11</td>
      <td>https://ca.indeed.com/jobs?q=Quality%20Engineer%20I%20TD%20Bank</td>
    </tr>
    <tr>
      <th>155</th>
      <td>Junior Application Developer - Web</td>
      <td>Western Financial Group</td>
      <td>Reporting to the Service Delivery Manager, you will be will be responsible for designing, coding, and modifying applications and or related web platforms.</td>
      <td>Winnipeg, MB</td>
      <td>11 days ago</td>
      <td>11</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Application%20Developer%20-%20Web%20Western%20Financial%20Group</td>
    </tr>
    <tr>
      <th>158</th>
      <td>Application Analyst I</td>
      <td>Edmonton Catholic Schools</td>
      <td>Under direction, and based on a beginner level analyst skill set, the job participates in the planning for and then participates in the development/re…</td>
      <td>Edmonton, AB</td>
      <td>11 days ago</td>
      <td>11</td>
      <td>https://ca.indeed.com/jobs?q=Application%20Analyst%20I%20Edmonton%20Catholic%20Schools</td>
    </tr>
    <tr>
      <th>48</th>
      <td>CT Data Engineer I - Power BI</td>
      <td>EY</td>
      <td>Reviewing and understanding complex data sets to establish data quality and highlighting where data cleansing is required to remediate the data.</td>
      <td>Toronto, ON</td>
      <td>11 days ago</td>
      <td>11</td>
      <td>https://ca.indeed.com/jobs?q=CT%20Data%20Engineer%20I%20-%20Power%20BI%20EY</td>
    </tr>
    <tr>
      <th>47</th>
      <td>Junior Data Engineer - OpenRoad Auto Group</td>
      <td>OpenRoad Auto Group</td>
      <td>Ensure high data integrity and quality from various data sources that are aligned to industry best practices. The Data Engineer is responsible for implementing …</td>
      <td>Richmond, BC</td>
      <td>11 days ago</td>
      <td>11</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Engineer%20-%20OpenRoad%20Auto%20Group%20OpenRoad%20Auto%20Group</td>
    </tr>
    <tr>
      <th>46</th>
      <td>Jr. Cyber Security Analyst</td>
      <td>Wellington Catholic DSB</td>
      <td>Excellent computer and technical skills including the use of excel for data analysis. 100% Temporary – JUNIOR CYBER SECURITY ANALYST*.</td>
      <td>Guelph, ON</td>
      <td>Active 11 days ago</td>
      <td>11</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Cyber%20Security%20Analyst%20Wellington%20Catholic%20DSB</td>
    </tr>
    <tr>
      <th>49</th>
      <td>Software Developer/Database Manager, Web Applications</td>
      <td>NeuroRx Research</td>
      <td>Designing and developing quality test plans, scenarios, and test data. The candidate will be responsible for providing support to the users on the ongoing…</td>
      <td>Temporarily Remote in Montréal, QC</td>
      <td>Active 12 days ago</td>
      <td>12</td>
      <td>https://ca.indeed.com/jobs?q=Software%20Developer/Database%20Manager%2C%20Web%20Applications%20NeuroRx%20Research</td>
    </tr>
    <tr>
      <th>160</th>
      <td>Junior Network Administrator</td>
      <td>Florists Supply Ltd.</td>
      <td>This individual will work closely with the Network Administrator and together they will be responsible for serving as the first point of contact for IT services…</td>
      <td>Remote in Winnipeg, MB</td>
      <td>Active 12 days ago</td>
      <td>12</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Network%20Administrator%20Florists%20Supply%20Ltd.</td>
    </tr>
    <tr>
      <th>50</th>
      <td>Junior Data Analytics Developer</td>
      <td>Tantalus</td>
      <td>Strong visual orientation for presenting data and analytics. You will work on data analytics tools related to the improvement of the electric, water and gas…</td>
      <td>Remote in Burnaby, BC</td>
      <td>14 days ago</td>
      <td>14</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Analytics%20Developer%20Tantalus</td>
    </tr>
    <tr>
      <th>242</th>
      <td>Administrateur.trice d'operations reseau TI Junior-(H/F)</td>
      <td>Société Générale</td>
      <td>Communication des rapports de contrôle quotidiens du matin. Détection et communication pendant les heures de bureau. O Cisco ACI ou vous êtes prêt à apprendre.</td>
      <td>Montréal, QC</td>
      <td>14 days ago</td>
      <td>14</td>
      <td>https://ca.indeed.com/jobs?q=Administrateur.trice%20d%27operations%20reseau%20TI%20Junior-%28H/F%29%20Soci%C3%A9t%C3%A9%20G%C3%A9n%C3%A9rale</td>
    </tr>
    <tr>
      <th>161</th>
      <td>Junior Software Developer</td>
      <td>Martello Technologies</td>
      <td>You will make a difference in how our customers interact with our products and conduct business. Your knowledge of all layers in software will help us re-think…</td>
      <td>Kanata, ON</td>
      <td>14 days ago</td>
      <td>14</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20Martello%20Technologies</td>
    </tr>
    <tr>
      <th>241</th>
      <td>Junior Network Operations Administrator</td>
      <td>Société Générale</td>
      <td>Supporting technical projects including involvement from local and global application, infrastructure, governance, and client teams.</td>
      <td>Montréal, QC</td>
      <td>14 days ago</td>
      <td>14</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Network%20Operations%20Administrator%20Soci%C3%A9t%C3%A9%20G%C3%A9n%C3%A9rale</td>
    </tr>
    <tr>
      <th>54</th>
      <td>Junior Database Administrator</td>
      <td>Questrade Financial Group</td>
      <td>They act as strategic partners with each business unit to help Questrade leverage technology to gain competitive advantage. You have experience with GIT/GitLab.</td>
      <td>Hybrid remote in Ontario</td>
      <td>15 days ago</td>
      <td>15</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Database%20Administrator%20Questrade%20Financial%20Group</td>
    </tr>
    <tr>
      <th>163</th>
      <td>Junior Software Developer (Rigsite &amp; EDR Team)</td>
      <td>Pason Systems Corp</td>
      <td>The team is seeking a junior full stack software developer with demonstrated skill in Java, Python, web-based technologies and frameworks, and Linux while…</td>
      <td>Calgary, AB</td>
      <td>15 days ago</td>
      <td>15</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20%28Rigsite%20%26%20EDR%20Team%29%20Pason%20Systems%20Corp</td>
    </tr>
    <tr>
      <th>53</th>
      <td>Junior/Intermediate Advanced Analytics Professional</td>
      <td>Definity</td>
      <td>Apply professional experience with data science software to prepare, analyze, and model data. 1+ years of professional work experience in a data analysis…</td>
      <td>Hybrid remote in Vancouver, BC</td>
      <td>15 days ago</td>
      <td>15</td>
      <td>https://ca.indeed.com/jobs?q=Junior/Intermediate%20Advanced%20Analytics%20Professional%20Definity</td>
    </tr>
    <tr>
      <th>55</th>
      <td>Junior Business Analyst</td>
      <td>The Skyline Group of Companies</td>
      <td>Extract data, compile reports, and develop customized reporting as required by users and management. Analyze, identify and validate key business requirements.</td>
      <td>Guelph, ON</td>
      <td>15 days ago</td>
      <td>15</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20The%20Skyline%20Group%20of%20Companies</td>
    </tr>
    <tr>
      <th>51</th>
      <td>Analyst Shipping Channel I</td>
      <td>Purolator</td>
      <td>Demonstrated skill in data analysis with exposure to a variety of data file formats. Test shipping software for compliance with Purolator’s technical…</td>
      <td>Mississauga, ON</td>
      <td>15 days ago</td>
      <td>15</td>
      <td>https://ca.indeed.com/jobs?q=Analyst%20Shipping%20Channel%20I%20Purolator</td>
    </tr>
    <tr>
      <th>162</th>
      <td>Junior Software Development Engineer in Test</td>
      <td>Global Relay</td>
      <td>As a Junior Software Development Engineer in Test (Jr. SDET), you will be part of a small, highly focused team responsible for delivery of highly scalable and…</td>
      <td>Hybrid remote in Vancouver, BC</td>
      <td>15 days ago</td>
      <td>15</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Development%20Engineer%20in%20Test%20Global%20Relay</td>
    </tr>
    <tr>
      <th>164</th>
      <td>Junior Software Development Engineer in Test (C#)</td>
      <td>Global Relay</td>
      <td>As a Software Development Engineer in Test (SDET), you will be part of a small, highly focused team responsible for delivery of highly scalable and robust…</td>
      <td>Hybrid remote in Vancouver, BC</td>
      <td>15 days ago</td>
      <td>15</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Development%20Engineer%20in%20Test%20%28C%23%29%20Global%20Relay</td>
    </tr>
    <tr>
      <th>52</th>
      <td>Junior Data Engineer</td>
      <td>CGI</td>
      <td>Ensure the quality and integrity of data. Candidates must have strong collaboration skills to work with cross-functional teams and stakeholders to ensure…</td>
      <td>Toronto, ON</td>
      <td>15 days ago</td>
      <td>15</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Engineer%20CGI</td>
    </tr>
    <tr>
      <th>57</th>
      <td>Research Analyst I - Cancer Rehabilitation &amp; Survivorship Pr...</td>
      <td>University Health Network</td>
      <td>At minimum, one (1) to three (3) years of related research experience preferred (e.g., study coordination experience; database design/set-up; data collection…</td>
      <td>Toronto, ON</td>
      <td>16 days ago</td>
      <td>16</td>
      <td>https://ca.indeed.com/jobs?q=Research%20Analyst%20I%20-%20Cancer%20Rehabilitation%20%26%20Survivorship%20Pr...%20University%20Health%20Network</td>
    </tr>
    <tr>
      <th>165</th>
      <td>Junior Applications Analyst</td>
      <td>Parkland Corporation</td>
      <td>The Junior Applications Analyst - Integration plays a critical role in delivering high quality customer service and support to clients.</td>
      <td>Dartmouth, NS</td>
      <td>16 days ago</td>
      <td>16</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Applications%20Analyst%20Parkland%20Corporation</td>
    </tr>
    <tr>
      <th>243</th>
      <td>Jr. Web Application Tester</td>
      <td>Vistek LTD</td>
      <td>For more than 40 years, Vistek has been a Canadian Success story, retailing photo, video and digital professional equipment solutions. Basic knowledge of T-SQL.</td>
      <td>Toronto, ON</td>
      <td>16 days ago</td>
      <td>16</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Web%20Application%20Tester%20Vistek%20LTD</td>
    </tr>
    <tr>
      <th>166</th>
      <td>Junior Software Developer</td>
      <td>Makeship</td>
      <td>Makeship exists to empower influencers, creators, and brands of all sizes to develop and launch limited edition products that matter to their fans.</td>
      <td>Remote in Vancouver, BC</td>
      <td>16 days ago</td>
      <td>16</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20Makeship</td>
    </tr>
    <tr>
      <th>56</th>
      <td>Junior Business Intelligence Developer</td>
      <td>Colliers Project Leaders</td>
      <td>Processes data extracts and configures data source connections using standard and custom data interfaces and APIs.</td>
      <td>Ottawa, ON</td>
      <td>16 days ago</td>
      <td>16</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Intelligence%20Developer%20Colliers%20Project%20Leaders</td>
    </tr>
    <tr>
      <th>58</th>
      <td>Junior DBA (Database Administrator)</td>
      <td>Dawn InfoTek Inc.</td>
      <td>Provide DB2 Administrative services to application development team. Design/develop/test/support DB2 LUW database. Performance tuning and trouble shooting.</td>
      <td>Toronto, ON</td>
      <td>Active 16 days ago</td>
      <td>16</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20DBA%20%28Database%20Administrator%29%20Dawn%20InfoTek%20Inc.</td>
    </tr>
    <tr>
      <th>167</th>
      <td>Junior Software Developer - New Grad (Azure, C#) - Calgary</td>
      <td>Peloton</td>
      <td>The Junior Software Developer will be responsible for building a set of web-based, real-time data visualization and analysis tools.</td>
      <td>Calgary, AB</td>
      <td>16 days ago</td>
      <td>16</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20-%20New%20Grad%20%28Azure%2C%20C%23%29%20-%20Calgary%20Peloton</td>
    </tr>
    <tr>
      <th>170</th>
      <td>Junior Software Developer, Paediatrics, Cumming School of Me...</td>
      <td>The University of Calgary</td>
      <td>The Department of Paediatrics in the Cumming School of Medicine invites applications for a Junior Software Developer.</td>
      <td>Calgary, AB</td>
      <td>17 days ago</td>
      <td>17</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%2C%20Paediatrics%2C%20Cumming%20School%20of%20Me...%20The%20University%20of%20Calgary</td>
    </tr>
    <tr>
      <th>168</th>
      <td>Junior Cloud Infrastructure Engineer</td>
      <td>Neo Financial</td>
      <td>Neo Financial is looking for a full-time Junior Cloud Infrastructure Engineer (AWS) in Calgary, AB. Successful candidates make continuous improvements through a…</td>
      <td>Calgary, AB</td>
      <td>17 days ago</td>
      <td>17</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Cloud%20Infrastructure%20Engineer%20Neo%20Financial</td>
    </tr>
    <tr>
      <th>169</th>
      <td>Technology Analyst I</td>
      <td>TELUS</td>
      <td>As a Technology Analyst within our Pharmacy Operations team, you will leverage your technical acumen, creative problem-solving, collaboration and interpersonal…</td>
      <td>Toronto, ON</td>
      <td>17 days ago</td>
      <td>17</td>
      <td>https://ca.indeed.com/jobs?q=Technology%20Analyst%20I%20TELUS</td>
    </tr>
    <tr>
      <th>171</th>
      <td>Développeur(euse) .Net junior | Junior .NET Developer</td>
      <td>Paysafe</td>
      <td>Chef de file dans le secteur des jeux d’argent en ligne depuis plus de 15 ans, Income Access est un fournisseur de logiciels primés de suivi et de création de…</td>
      <td>Remote in Westmount, QC</td>
      <td>18 days ago</td>
      <td>18</td>
      <td>https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%28euse%29%20.Net%20junior%20%7C%20Junior%20.NET%20Developer%20Paysafe</td>
    </tr>
    <tr>
      <th>246</th>
      <td>Junior Software Engineer</td>
      <td>OpenBet</td>
      <td>Develop new features and functionality for large scale highly performant transactional sites. Participate in all phases of the Software Development Life Cycle …</td>
      <td>Montréal, QC</td>
      <td>18 days ago</td>
      <td>18</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Engineer%20OpenBet</td>
    </tr>
    <tr>
      <th>60</th>
      <td>Programmeur(euse) débutant en SQL / SQL Junior Programmer</td>
      <td>Ove décors ULC</td>
      <td>Experience working with enterprise data. Knowledge of ETL and BI data warehouse architecture is an asset. Solid computer science fundamentals such as algorithms…</td>
      <td>Laval, QC</td>
      <td>18 days ago</td>
      <td>18</td>
      <td>https://ca.indeed.com/jobs?q=Programmeur%28euse%29%20d%C3%A9butant%20en%20SQL%20/%20SQL%20Junior%20Programmer%20Ove%20d%C3%A9cors%20ULC</td>
    </tr>
    <tr>
      <th>245</th>
      <td>Software Engineer I</td>
      <td>Twitter</td>
      <td>We own the development tools distribution and configuration management for Twitter’s software engineering workstations! Work in an Agile, CI/CD environment.</td>
      <td>Toronto, ON</td>
      <td>18 days ago</td>
      <td>18</td>
      <td>https://ca.indeed.com/jobs?q=Software%20Engineer%20I%20Twitter</td>
    </tr>
    <tr>
      <th>244</th>
      <td>Junior Cloud Engineer OTW</td>
      <td>Ericsson</td>
      <td>Our CI/CD and System integration department plays a strategic role in making sure that the Cloud RAN solutions meet our customers’ expectations.</td>
      <td>Remote in Ottawa, ON</td>
      <td>18 days ago</td>
      <td>18</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Cloud%20Engineer%20OTW%20Ericsson</td>
    </tr>
    <tr>
      <th>59</th>
      <td>Junior Project Finance Analyst (Montreal or Laval)</td>
      <td>Kiewit Corporation</td>
      <td>0 - 5 years of financial/data analysis experience. The primary focuses of this position include: evaluating construction job cost, data reporting/analysis for…</td>
      <td>Montréal, QC</td>
      <td>18 days ago</td>
      <td>18</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Project%20Finance%20Analyst%20%28Montreal%20or%20Laval%29%20Kiewit%20Corporation</td>
    </tr>
    <tr>
      <th>247</th>
      <td>BIOINFORMATICS SCIENTIST I - CA</td>
      <td>Luminex</td>
      <td>This position is responsible for in-depth in-silico bioinformatics analysis required for development of sequencing and other molecular methods, bio surveillance…</td>
      <td>Toronto, ON</td>
      <td>Active 19 days ago</td>
      <td>19</td>
      <td>https://ca.indeed.com/jobs?q=BIOINFORMATICS%20SCIENTIST%20I%20-%20CA%20Luminex</td>
    </tr>
    <tr>
      <th>249</th>
      <td>Junior Verification Engineer - Kanata</td>
      <td>Randstad</td>
      <td>** 8-hour day*** you have the option to work overtime and you get paid for every hour you work! Opportunity Yearly Bonus, Signing Bonus, Stock Bonus, RRSP…</td>
      <td>Remote in Kanata, ON</td>
      <td>21 days ago</td>
      <td>21</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Verification%20Engineer%20-%20Kanata%20Randstad</td>
    </tr>
    <tr>
      <th>248</th>
      <td>22-39 Software Engineer I</td>
      <td>Technical Safety BC</td>
      <td>The Software Engineer I is responsible for working with the Application Designer to understand the scope of the project and to configure and/or develop…</td>
      <td>Vancouver, BC</td>
      <td>21 days ago</td>
      <td>21</td>
      <td>https://ca.indeed.com/jobs?q=22-39%20Software%20Engineer%20I%20Technical%20Safety%20BC</td>
    </tr>
    <tr>
      <th>61</th>
      <td>Credit Analyst Trainee, Business Banking, Courtney Park, Mis...</td>
      <td>BMO Financial Group</td>
      <td>Coordinates the management of databases; ensures alignment and integration of data in adherence with data governance standards.</td>
      <td>Mississauga, ON</td>
      <td>22 days ago</td>
      <td>22</td>
      <td>https://ca.indeed.com/jobs?q=Credit%20Analyst%20Trainee%2C%20Business%20Banking%2C%20Courtney%20Park%2C%20Mis...%20BMO%20Financial%20Group</td>
    </tr>
    <tr>
      <th>250</th>
      <td>Développeur Python junior</td>
      <td>Alithya</td>
      <td>Veuillez noter que ce poste est en télétravail. Téléphone, Microsoft Teams ou Zoom, comme vous préférez ! Analyser les exigences des clients et des utilisateurs…</td>
      <td>Remote in Montréal, QC</td>
      <td>22 days ago</td>
      <td>22</td>
      <td>https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20Python%20junior%20Alithya</td>
    </tr>
    <tr>
      <th>172</th>
      <td>Junior Quality Assurance Analyst</td>
      <td>TC Transcontinental</td>
      <td>Junior QA analyst will be working on legacy web applications testing and testing of newly created solutions in various environments, from .</td>
      <td>Mississauga, ON</td>
      <td>22 days ago</td>
      <td>22</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Quality%20Assurance%20Analyst%20TC%20Transcontinental</td>
    </tr>
    <tr>
      <th>173</th>
      <td>Junior Analyst - Regulatory Services (AEOI)</td>
      <td>Maples Group</td>
      <td>The Junior Analyst - Regulatory Services reports to a Senior Vice President and supports the Structured Finance Team. Fluency in English is required.</td>
      <td>Montréal, QC</td>
      <td>22 days ago</td>
      <td>22</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Analyst%20-%20Regulatory%20Services%20%28AEOI%29%20Maples%20Group</td>
    </tr>
    <tr>
      <th>174</th>
      <td>Junior Analyst (Securities)</td>
      <td>Vincent Associates Inc.</td>
      <td>Job Type: Full-time permanent position. When on site, all associated government COVID-19 requirements and restrictions must be adhered to.</td>
      <td>Toronto, ON</td>
      <td>22 days ago</td>
      <td>22</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Analyst%20%28Securities%29%20Vincent%20Associates%20Inc.</td>
    </tr>
    <tr>
      <th>64</th>
      <td>Jr. Data Strategist</td>
      <td>Publicis Groupe</td>
      <td>Familiarity with data metrics &amp;amp; terminology. The Jr. Data Strategist will ingest data from search, social, and other primary/secondary data sources to formulate…</td>
      <td>Toronto, ON</td>
      <td>23 days ago</td>
      <td>23</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data%20Strategist%20Publicis%20Groupe</td>
    </tr>
    <tr>
      <th>62</th>
      <td>Junior Marketing Associate</td>
      <td>Source Atlantic</td>
      <td>Improve new campaigns using data and feedback from existing and previous projects. Reporting to the Marketing Manager, the Marketing Associate’s is primarily…</td>
      <td>Saint John, NB</td>
      <td>23 days ago</td>
      <td>23</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Marketing%20Associate%20Source%20Atlantic</td>
    </tr>
    <tr>
      <th>63</th>
      <td>IT Support – Junior Data Coordinator</td>
      <td>Wellsite Masters</td>
      <td>Coordinate and manipulate all data that is derived from WM Systems. Create reports in Microsoft Excel, Word and PowerPoint as required.</td>
      <td>Calgary, AB</td>
      <td>23 days ago</td>
      <td>23</td>
      <td>https://ca.indeed.com/jobs?q=IT%20Support%20%E2%80%93%20Junior%20Data%20Coordinator%20Wellsite%20Masters</td>
    </tr>
    <tr>
      <th>252</th>
      <td>Analyste junior autochtone (Poste pouvant être situé n'impor...</td>
      <td>CMHC</td>
      <td>La diversité et l’inclusion guident tout ce que nous faisons à la SCHL. Vous aurez également à utiliser les outils appropriés (y compris R ou Python) pour…</td>
      <td>Temporarily Remote in Ottawa, ON</td>
      <td>24 days ago</td>
      <td>24</td>
      <td>https://ca.indeed.com/jobs?q=Analyste%20junior%20autochtone%20%28Poste%20pouvant%20%C3%AAtre%20situ%C3%A9%20n%27impor...%20CMHC</td>
    </tr>
    <tr>
      <th>253</th>
      <td>Junior Software Engineer - Full Stack</td>
      <td>RideCo</td>
      <td>Collaborate with team members to get a better understanding of your user stories. Develop elegant features and solutions for our web and mobile platforms.</td>
      <td>Waterloo, ON</td>
      <td>Active 24 days ago</td>
      <td>24</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Engineer%20-%20Full%20Stack%20RideCo</td>
    </tr>
    <tr>
      <th>251</th>
      <td>Software Engineer I/II</td>
      <td>Microsoft</td>
      <td>You will have opportunities to work on multiple layers of the technology stack, ranging from customer-focused user experience work, building scalable…</td>
      <td>Vancouver, BC</td>
      <td>24 days ago</td>
      <td>24</td>
      <td>https://ca.indeed.com/jobs?q=Software%20Engineer%20I/II%20Microsoft</td>
    </tr>
    <tr>
      <th>65</th>
      <td>Business Analyst I, AWS Commerce Platform Business Operation...</td>
      <td>Amazon Dev Centre Canada ULC</td>
      <td>At least 1+ years of experience with data warehousing and reporting. At least 1+ years of professional working experience in related occupations of Business…</td>
      <td>Vancouver, BC</td>
      <td>24 days ago</td>
      <td>24</td>
      <td>https://ca.indeed.com/jobs?q=Business%20Analyst%20I%2C%20AWS%20Commerce%20Platform%20Business%20Operation...%20Amazon%20Dev%20Centre%20Canada%20ULC</td>
    </tr>
    <tr>
      <th>254</th>
      <td>Junior Research Developer</td>
      <td>C-CORE</td>
      <td>Initially these include research into applications that rely on numerical analysis, signal processing and statistical and machine learning.</td>
      <td>Ottawa, ON</td>
      <td>Active 25 days ago</td>
      <td>25</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Research%20Developer%20C-CORE</td>
    </tr>
    <tr>
      <th>66</th>
      <td>Jr. Data Systems Manager</td>
      <td>Nelson Education LTD</td>
      <td>Providing technical expertise in data storage structures, data mining, and data cleansing as needed. Supporting initiatives for data integrity and normalization…</td>
      <td>Toronto, ON</td>
      <td>25 days ago</td>
      <td>25</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data%20Systems%20Manager%20Nelson%20Education%20LTD</td>
    </tr>
    <tr>
      <th>175</th>
      <td>Junior Developer</td>
      <td>Insurance Corporation of British Columbia</td>
      <td>This mandate will be fulfilled by using technology solutions such as Robotics Process Automation (RPA). Perform application development and system configuration…</td>
      <td>Hybrid remote in North Vancouver, BC</td>
      <td>Active 25 days ago</td>
      <td>25</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Developer%20Insurance%20Corporation%20of%20British%20Columbia</td>
    </tr>
    <tr>
      <th>176</th>
      <td>Junior Algorithmic Trading Developer with C++.</td>
      <td>Scotiabank</td>
      <td>The position will be a primary technical resource for the ETF trading desk. Enhancing our low latency trading framework, optimizing handling of market data,…</td>
      <td>Toronto, ON</td>
      <td>25 days ago</td>
      <td>25</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Algorithmic%20Trading%20Developer%20with%20C%2B%2B.%20Scotiabank</td>
    </tr>
    <tr>
      <th>177</th>
      <td>Junior C# Developer [#3902]</td>
      <td>Alteo</td>
      <td>Develop and write high quality code that adheres to the documented software quality standards. Maintain and manage existing source bases. Good skills in C# ASP.</td>
      <td>Montréal, QC</td>
      <td>26 days ago</td>
      <td>26</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20C%23%20Developer%20%5B%233902%5D%20Alteo</td>
    </tr>
    <tr>
      <th>255</th>
      <td>Junior Developer</td>
      <td>ICBC</td>
      <td>Location: North Vancouver Employment Type: Permanent Full Time. Business to improve customer responsiveness. This mandate will be fulfilled by using technology…</td>
      <td>Hybrid remote in North Vancouver, BC</td>
      <td>26 days ago</td>
      <td>26</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Developer%20ICBC</td>
    </tr>
    <tr>
      <th>178</th>
      <td>Junior Full Stack Developer</td>
      <td>Steelhaus Technologies</td>
      <td>We are seeking for a Junior Full Stack Developer to join our team who will be responsible for participating in all phases of the development life-cycle,…</td>
      <td>Calgary, AB</td>
      <td>28 days ago</td>
      <td>28</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20Steelhaus%20Technologies</td>
    </tr>
    <tr>
      <th>282</th>
      <td>Junior DevOps Engineer</td>
      <td>Hellbent Games</td>
      <td>This job involves development and maintenance of scalable, secure and highly-available services and infrastructure for online gaming such as player progression,…</td>
      <td>Burnaby, BC</td>
      <td>30 days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20DevOps%20Engineer%20Hellbent%20Games</td>
    </tr>
    <tr>
      <th>281</th>
      <td>Junior Software Developer</td>
      <td>Prolucid Technologies</td>
      <td>We encourage cross functional developers to not only learn programming languages, but also the related tools and supporting systems.</td>
      <td>Mississauga, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20Prolucid%20Technologies</td>
    </tr>
    <tr>
      <th>283</th>
      <td>Développeur Python/Django [Junior]</td>
      <td>FJNR's a Judicious New Reference</td>
      <td>Si vous êtes passionné par le développement logiciel et que vous avez le goût de rejoindre une équipe qui met l’apprentissage continu au centre de toute chose,…</td>
      <td>Remote in Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20Python/Django%20%5BJunior%5D%20FJNR%27s%20a%20Judicious%20New%20Reference</td>
    </tr>
    <tr>
      <th>264</th>
      <td>Developer Advocate - Remote (Canada)</td>
      <td>Vonage</td>
      <td>As businesses continue to shift to a real-time, customer-centric communications model, we are experiencing a time of impressive growth.</td>
      <td>Remote in Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Developer%20Advocate%20-%20Remote%20%28Canada%29%20Vonage</td>
    </tr>
    <tr>
      <th>285</th>
      <td>Junior Power System Consultant- Remote Canada</td>
      <td>Siemens Canada Limited</td>
      <td>Rewarding vacation entitlement with the opportunity to buy and sell your vacation depending on your lifestyle. Provide support to project teams as required.</td>
      <td>Remote in Fredericton, NB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Power%20System%20Consultant-%20Remote%20Canada%20Siemens%20Canada%20Limited</td>
    </tr>
    <tr>
      <th>299</th>
      <td>Software Developer (Junior)</td>
      <td>STEP Software</td>
      <td>NET), C/C++, Python, Java, Swift, Objective C, PHP &amp;amp; Delphi on Windows, Linux, Mac, iPhone, Android and Embedded Devices.</td>
      <td>London, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Software%20Developer%20%28Junior%29%20STEP%20Software</td>
    </tr>
    <tr>
      <th>298</th>
      <td>Junior Python Solution Developer for Jeppesen - a Boeing Com...</td>
      <td>Sigma Software</td>
      <td>As a Junior Software Solution Developer, you will work on our various software solutions for commercial airlines. 2+ years of working in software development.</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Python%20Solution%20Developer%20for%20Jeppesen%20-%20a%20Boeing%20Com...%20Sigma%20Software</td>
    </tr>
    <tr>
      <th>297</th>
      <td>Junior Full Stack Developer - DevOps</td>
      <td>Lockheed Martin Corporation</td>
      <td>Support the Canadian Surface Combatant (CSC) Tactical Operating Environment (TOE). Act as the Subject Matter Expert (SME) for relevant system design areas.</td>
      <td>Halifax, NS</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20-%20DevOps%20Lockheed%20Martin%20Corporation</td>
    </tr>
    <tr>
      <th>296</th>
      <td>Junior Cybersecurity Analyst</td>
      <td>Richter</td>
      <td>They will support the delivery and execution of white-glove cyber security services to an exclusive set of clients. Strong analytical and investigative skills.</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Cybersecurity%20Analyst%20Richter</td>
    </tr>
    <tr>
      <th>295</th>
      <td>Reporting Analyst I (Canada Remote)</td>
      <td>Fullscript</td>
      <td>The Reporting team is a core function of the Fullscript Data team, responsible for helping our team understand performance and drive effective planning and…</td>
      <td>Remote in Ottawa, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Reporting%20Analyst%20I%20%28Canada%20Remote%29%20Fullscript</td>
    </tr>
    <tr>
      <th>294</th>
      <td>Junior Software Engineer</td>
      <td>Symend</td>
      <td>The Junior Software Engineer is responsible for producing and implementing functional software solutions that align with the client needs and business goals.</td>
      <td>Remote in Calgary, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Engineer%20Symend</td>
    </tr>
    <tr>
      <th>284</th>
      <td>Junior Electrical Engineer</td>
      <td>BBA</td>
      <td>Work collaboratively with clients, project managers, engineers, designers and drafters in the preparation of deliverables to BBA and client standards.</td>
      <td>Trail, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Electrical%20Engineer%20BBA</td>
    </tr>
    <tr>
      <th>293</th>
      <td>Junior Water Resources Engineer or Engineer-in-Training</td>
      <td>CBCL Limited</td>
      <td>Development of numerical models for multiple hydraulic systems including rivers, stormwater/sanitary systems, dams, wetlands, weirs and channels as well as…</td>
      <td>Hybrid remote in Halifax, NS</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Water%20Resources%20Engineer%20or%20Engineer-in-Training%20CBCL%20Limited</td>
    </tr>
    <tr>
      <th>291</th>
      <td>Développeur(se) de logiciels junior</td>
      <td>French Canadian Instance</td>
      <td>Maritime International, une division de L3Harris, est un fournisseur mondial de premier plan de contrôles-commandes non ITAR et de solutions de simulation pour…</td>
      <td>Ottawa, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%28se%29%20de%20logiciels%20junior%20French%20Canadian%20Instance</td>
    </tr>
    <tr>
      <th>290</th>
      <td>Junior Web Developer</td>
      <td>Scribendi</td>
      <td>You will work with cutting-edge technologies, learn how they are applied in the ecommerce sector, and collaborate extensively with stakeholders and the…</td>
      <td>Chatham-Kent, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Web%20Developer%20Scribendi</td>
    </tr>
    <tr>
      <th>289</th>
      <td>Jr. / Int. Software Engineering (12mo fixed term)</td>
      <td>Magellan Aerospace</td>
      <td>Magellan Aerospace, Winnipeg is looking for a high performing Entry Level (or Intermediate) Software Engineering/Developer to join our development team.</td>
      <td>Winnipeg, MB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20/%20Int.%20Software%20Engineering%20%2812mo%20fixed%20term%29%20Magellan%20Aerospace</td>
    </tr>
    <tr>
      <th>288</th>
      <td>Junior Solution Architect</td>
      <td>Stealth Monitoring</td>
      <td>NET Framework, javascript, python, T-SQL. Stealth Monitoring Development is looking for a highly motivated and experienced solutions architect who can help…</td>
      <td>Mississauga, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Solution%20Architect%20Stealth%20Monitoring</td>
    </tr>
    <tr>
      <th>287</th>
      <td>Matchmove Artist - Junior</td>
      <td>Track Visual Effects</td>
      <td>You will be working with artists with a wealth of experience on various productions. It is important to have basic knowledge of Syntheyes and matchmove.</td>
      <td>Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Matchmove%20Artist%20-%20Junior%20Track%20Visual%20Effects</td>
    </tr>
    <tr>
      <th>286</th>
      <td>Junior Systems Engineer (New Graduate)</td>
      <td>Aviya Aerospace Systems</td>
      <td>Aviya provides expertise in program management, systems, software, mechanical, and hardware engineering to many of the top-tier Aerospace and Defense…</td>
      <td>Mississauga, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Systems%20Engineer%20%28New%20Graduate%29%20Aviya%20Aerospace%20Systems</td>
    </tr>
    <tr>
      <th>292</th>
      <td>Junior Software Developer</td>
      <td>S&amp;P Global</td>
      <td>Financial Risk Analytics is part of the IHS Markit group and provides industry leading risk analytics solutions to sell side institutions within the financial…</td>
      <td>Calgary, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20S%26P%20Global</td>
    </tr>
    <tr>
      <th>280</th>
      <td>Junior Python Developer</td>
      <td>ReDefine</td>
      <td>As an Juniour Python Developer (internally called ATD) you will perform a variety of tasks to assist the Pipeline Technical Directors (Pipeline TDs) to ensure…</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Python%20Developer%20ReDefine</td>
    </tr>
    <tr>
      <th>259</th>
      <td>Junior Firmware Engineer</td>
      <td>Corinex Communications</td>
      <td>Participate in the development of next-generation smart grid communication devices and equipment. Involve in system design discussions and provide comprehensive…</td>
      <td>Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Firmware%20Engineer%20Corinex%20Communications</td>
    </tr>
    <tr>
      <th>256</th>
      <td>Analog Design Engr, I</td>
      <td>Synopsys</td>
      <td>You will be working with a cross functional team of analog and mixed signal circuit designers from a wide variety of backgrounds on our latest DDR and HBM IP…</td>
      <td>Kanata, ON</td>
      <td>30 days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Analog%20Design%20Engr%2C%20I%20Synopsys</td>
    </tr>
    <tr>
      <th>263</th>
      <td>Junior Pipeline TD -- Développeur du Pipeline Junior</td>
      <td>Cinesite-Montreal</td>
      <td>Cinesite is recruiting a Junior Pipeline TD who will be responsible to maintain and advance the Cinesite pipeline on our animated movies and VFX shows.</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Pipeline%20TD%20--%20D%C3%A9veloppeur%20du%20Pipeline%20Junior%20Cinesite-Montreal</td>
    </tr>
    <tr>
      <th>266</th>
      <td>Junior Software Control Engineer</td>
      <td>SNC-Lavalin</td>
      <td>Candu Energy Inc. is a leading full-service nuclear technology company and committed to design and deliver state-of-the-art CANDU® reactors, carry out life…</td>
      <td>Courtice, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Control%20Engineer%20SNC-Lavalin</td>
    </tr>
    <tr>
      <th>267</th>
      <td>Junior Actuarial Associate - Corporate Actuarial</td>
      <td>SCOR</td>
      <td>This position is part of the Canadian Corporate Actuarial Team, which is responsible for actuarial activities associated with SCORâ€™s Canada Life &amp;amp; Health…</td>
      <td>Canada</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Actuarial%20Associate%20-%20Corporate%20Actuarial%20SCOR</td>
    </tr>
    <tr>
      <th>268</th>
      <td>Jr. NSP Software Tester</td>
      <td>NOKIA</td>
      <td>Define the test strategy, design test plans, and carry out the validation of various features, emphasizing automated tests.</td>
      <td>Hybrid remote in Ottawa, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20NSP%20Software%20Tester%20NOKIA</td>
    </tr>
    <tr>
      <th>269</th>
      <td>Junior Software Solution Developer for Jeppesen – a Boeing C...</td>
      <td>Sigma Software</td>
      <td>As a Junior Software Solution Developer, you will work on our various software solutions for commercial airlines. 2+ years of working in software development.</td>
      <td>Canada</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Solution%20Developer%20for%20Jeppesen%20%E2%80%93%20a%20Boeing%20C...%20Sigma%20Software</td>
    </tr>
    <tr>
      <th>270</th>
      <td>Junior Software Developers</td>
      <td>David Aplin Group</td>
      <td>This position is responsible for the development, evaluation, implementation and maintenance of new software solutions, including maintenance and development of…</td>
      <td>Winnipeg, MB</td>
      <td>30 days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developers%20David%20Aplin%20Group</td>
    </tr>
    <tr>
      <th>271</th>
      <td>Software Engineering - Engineer I</td>
      <td>Live Nation</td>
      <td>The candidate would be directly involved from POC to production deployment of a set of components that are well tested, fully automated, well designed, highly…</td>
      <td>Quebec City, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Software%20Engineering%20-%20Engineer%20I%20Live%20Nation</td>
    </tr>
    <tr>
      <th>272</th>
      <td>Junior Java Developer - REMOTE</td>
      <td>Software International</td>
      <td>University or College degree in Computer Science or equivalent. Minimum 2 years Java development. Working knowledge of JavaScript programming.</td>
      <td>Remote in Canada</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Java%20Developer%20-%20REMOTE%20Software%20International</td>
    </tr>
    <tr>
      <th>273</th>
      <td>Pipeline TD (JR)</td>
      <td>Bardel Entertainment</td>
      <td>Working closely with all Technology teams, this role is responsible for the successful creation of the company's pipeline software tools, supporting Production…</td>
      <td>Remote in Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Pipeline%20TD%20%28JR%29%20Bardel%20Entertainment</td>
    </tr>
    <tr>
      <th>279</th>
      <td>Ingénieur(e) junior en mécanique des roches</td>
      <td>Golder Associates</td>
      <td>Réduire les données et analyser des données d’enquête; Préparer et utiliser des modèles 2D et 3D; Participer à la caractérisation géotechnique et aux…</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Ing%C3%A9nieur%28e%29%20junior%20en%20m%C3%A9canique%20des%20roches%20Golder%20Associates</td>
    </tr>
    <tr>
      <th>274</th>
      <td>Full Stack Engineer (Junior)</td>
      <td>Sangoma</td>
      <td>At least 1 years of experience python TurboGears framework and celery library. As a FullStack Engineer, you will be responsible for implementing real-time and…</td>
      <td>Markham, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Full%20Stack%20Engineer%20%28Junior%29%20Sangoma</td>
    </tr>
    <tr>
      <th>276</th>
      <td>Jr Embedded Software Engineer</td>
      <td>MDA</td>
      <td>Software development in Python, C++. Development of test environments and tools. Write test plans for verification of software modules.</td>
      <td>Richmond, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr%20Embedded%20Software%20Engineer%20MDA</td>
    </tr>
    <tr>
      <th>277</th>
      <td>HYDROGÉOLOGUE JUNIOR/INTERMÉDIAIRE (INGÉNIEUR OU GÉOLOGUE) M...</td>
      <td>WSP</td>
      <td>WSP est l’une des plus importantes firmes de services professionnels à travers le monde. Nous accordons une grande valeur à nos employés et à notre réputation.</td>
      <td>Remote in Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=HYDROG%C3%89OLOGUE%20JUNIOR/INTERM%C3%89DIAIRE%20%28ING%C3%89NIEUR%20OU%20G%C3%89OLOGUE%29%20M...%20WSP</td>
    </tr>
    <tr>
      <th>278</th>
      <td>DevSecOps Engineer</td>
      <td>CarbonCure Technologies</td>
      <td>We are seeking a Junior Data Science Developer to assist with the overall execution of our digital strategy to maximize usage of our full suite of CO2…</td>
      <td>Remote in Ontario</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=DevSecOps%20Engineer%20CarbonCure%20Technologies</td>
    </tr>
    <tr>
      <th>262</th>
      <td>Junior Developer</td>
      <td>Vaco Lannick</td>
      <td>This role will mostly work with C# and VB. NET on backend applications and APIs (REST), MySQL and some Python, AWS. NET backend development - C# and VB.NET.</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Developer%20Vaco%20Lannick</td>
    </tr>
    <tr>
      <th>261</th>
      <td>Pipeline Technical Director, Level I Vancouver, BC</td>
      <td>Industrial Light &amp; Magic</td>
      <td>The Pipeline TD develops and maintains software tools, providing front-line support to artists, and general troubleshooting of the CG pipeline in a fast-paced,…</td>
      <td>Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Pipeline%20Technical%20Director%2C%20Level%20I%20Vancouver%2C%20BC%20Industrial%20Light%20%26%20Magic</td>
    </tr>
    <tr>
      <th>260</th>
      <td>SCIENTIFIQUE JUNIOR – TRAITEMENT AUTOMATIQUE DU LANGAGE NATU...</td>
      <td>Centre de recherche informatique de Montréal...</td>
      <td>Pour réussir à ce poste, le candidat retenu devra combiner des passions pour la linguistique, l’informatique ainsi que pour l’apprentissage automatique.</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=SCIENTIFIQUE%20JUNIOR%20%E2%80%93%20TRAITEMENT%20AUTOMATIQUE%20DU%20LANGAGE%20NATU...%20Centre%20de%20recherche%20informatique%20de%20Montr%C3%A9al...</td>
    </tr>
    <tr>
      <th>265</th>
      <td>Technical Assistant, Level I Vancouver, BC</td>
      <td>Industrial Light &amp; Magic</td>
      <td>The Technical Assistant I (TA) provides front line rendering and data management support for ILM VFX Production teams and the facility.</td>
      <td>Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Technical%20Assistant%2C%20Level%20I%20Vancouver%2C%20BC%20Industrial%20Light%20%26%20Magic</td>
    </tr>
    <tr>
      <th>258</th>
      <td>Research Associate I/II, Assay Development</td>
      <td>BlueRock Therapeutics</td>
      <td>BlueRock Therapeutics is seeking a Research Associate I/II, Assay Development in Toronto ON. The successful candidate will support the development of cell…</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Research%20Associate%20I/II%2C%20Assay%20Development%20BlueRock%20Therapeutics</td>
    </tr>
    <tr>
      <th>257</th>
      <td>Junior Pipeline TD/ Software Engineer</td>
      <td>Stellar Creative Lab</td>
      <td>Stellar Creative Lab is hiring a Junior Pipeline TD, who can bring his or her talent and brains to the design and development of a facility-wide CG-Animation…</td>
      <td>&lt;span&gt;Temporarily Remote&lt;/span&gt;</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Pipeline%20TD/%20Software%20Engineer%20Stellar%20Creative%20Lab</td>
    </tr>
    <tr>
      <th>275</th>
      <td>Junior Software Developer</td>
      <td>Wedge Networks</td>
      <td>Wedge Networks is seeking candidates to fill a junior software development position on our research and development team, developing software for our network…</td>
      <td>Calgary, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20Wedge%20Networks</td>
    </tr>
    <tr>
      <th>103</th>
      <td>Data Architect I - Analytics Solutions</td>
      <td>Electronic Arts</td>
      <td>Understanding of data modelling, design and architecture principles and techniques across master data, transaction data and derived data.</td>
      <td>Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Architect%20I%20-%20Analytics%20Solutions%20Electronic%20Arts</td>
    </tr>
    <tr>
      <th>203</th>
      <td>Junior Developer</td>
      <td>E-By Design</td>
      <td>We are seeking an entry-level . NET developer responsible for building . NET applications using C#, SQL, and SSRS. Skill for writing reusable libraries.</td>
      <td>Alberta</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Developer%20E-By%20Design</td>
    </tr>
    <tr>
      <th>216</th>
      <td>Junior Water Resources Engineer</td>
      <td>Kerr Wood Leidal</td>
      <td>Design of engineering infrastructure including, but not limited to, dikes, fish habitat enhancement, dams, intakes, and hazard mitigation structures.</td>
      <td>Burnaby, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Water%20Resources%20Engineer%20Kerr%20Wood%20Leidal</td>
    </tr>
    <tr>
      <th>82</th>
      <td>Junior Online Marketing Analyst</td>
      <td>Core Online Marketing</td>
      <td>Analytical Skills to interpret data and present recommendations. Ensure data from all sources is accurate and being captured appropriately.</td>
      <td>Oakville, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Online%20Marketing%20Analyst%20Core%20Online%20Marketing</td>
    </tr>
    <tr>
      <th>81</th>
      <td>Développeur BI junior | Junior Business Intelligence Develop...</td>
      <td>Delmar International Inc.</td>
      <td>Participating to data quality checks. Developing data models, working conjointly with senior developers. 1 to 3 years' experience in data analysis developing…</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20BI%20junior%20%7C%20Junior%20Business%20Intelligence%20Develop...%20Delmar%20International%20Inc.</td>
    </tr>
    <tr>
      <th>80</th>
      <td>Junior Financial Analyst (Business Case)</td>
      <td>Questrade Financial Group</td>
      <td>Support the Finance team in producing meaningful data/analysis. Perform reconciliation processes for various reports and systems to ensure data integrity.</td>
      <td>&lt;span class="more_loc_container"&gt;&lt;a aria-label="Same Junior Financial Analyst (Business Case) job in 1 other location" class="more_loc" href="/addlLoc/redirect?tk=1g0qf29hbsaaa800&amp;amp;jk=7a0f15e1520a9fd8&amp;amp;dest=%2Fjobs%3Fq%3Ddata%2Bjunior%26l%3DCanada%26grpKey%3DkAP8mP0gmAPY0dHpAqADAfIHA3RjbA%253D%253D" rel="nofollow"&gt;+1 location&lt;/a&gt;&lt;/span&gt;</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financial%20Analyst%20%28Business%20Case%29%20Questrade%20Financial%20Group</td>
    </tr>
    <tr>
      <th>79</th>
      <td>Jr Financial Analyst</td>
      <td>MCAP</td>
      <td>Focus on detail and accuracy with respect to data integrity while working with large volumes of data. Collect all relevant data to prepare monthly GST/HST/QST…</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr%20Financial%20Analyst%20MCAP</td>
    </tr>
    <tr>
      <th>78</th>
      <td>Associate Product Manager, Data</td>
      <td>Lightspeed Commerce</td>
      <td>Collaborate with stakeholders to define their big data needs for the business. You will help define and execute the vision for Big Data at Lightspeed.</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Associate%20Product%20Manager%2C%20Data%20Lightspeed%20Commerce</td>
    </tr>
    <tr>
      <th>77</th>
      <td>Junior Asset Management Consultant and Data Analyst</td>
      <td>GM BluePlan Engineering</td>
      <td>Develop and analyze asset data to support asset management planning. Create and manage asset inventories and data structures, including the development of…</td>
      <td>Vaughan, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Asset%20Management%20Consultant%20and%20Data%20Analyst%20GM%20BluePlan%20Engineering</td>
    </tr>
    <tr>
      <th>76</th>
      <td>Data Steward I</td>
      <td>TD Bank</td>
      <td>Complete metadata and data quality tasks. Identify and monitor the quality of critical data elements. Manage data work activities requiring coordination across…</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Steward%20I%20TD%20Bank</td>
    </tr>
    <tr>
      <th>75</th>
      <td>Junior Business Analyst</td>
      <td>RPM TECHNOLOGIES CORP</td>
      <td>Documenting and analyzing the required information and data to determine potential solutions from a technical and business perspective.</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20RPM%20TECHNOLOGIES%20CORP</td>
    </tr>
    <tr>
      <th>74</th>
      <td>Financial Analyst I</td>
      <td>University Health Network</td>
      <td>Skill in performing detailed numerical computations and accurate data entry. Hours: 37.5 hours per week. As an integral member of the Grant Operations team…</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Financial%20Analyst%20I%20University%20Health%20Network</td>
    </tr>
    <tr>
      <th>73</th>
      <td>Jr. Business Intelligence Developer, Enterprise Analytics</td>
      <td>Southlake Regional Health Centre</td>
      <td>Develop ETL procedures, SSIS packages and maintain data flow processes. Advanced understanding of data warehousing concepts and best practices required.</td>
      <td>Newmarket, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Business%20Intelligence%20Developer%2C%20Enterprise%20Analytics%20Southlake%20Regional%20Health%20Centre</td>
    </tr>
    <tr>
      <th>72</th>
      <td>Junior Sales Data Coordinator</td>
      <td>Bélanger UPT</td>
      <td>Reporting to the National Sales &amp;amp; Marketing Director, the Junior Sales Data Coordinator will be internal link between the pricing analyst and inside sales.</td>
      <td>Mississauga, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Sales%20Data%20Coordinator%20B%C3%A9langer%20UPT</td>
    </tr>
    <tr>
      <th>71</th>
      <td>Jr. Email Marketing Implementation Specialist at Digital Age...</td>
      <td>Arctic Leaf Inc.</td>
      <td>Measure campaign results and optimize based on data. Analyzing campaign and email performance data to develop insights and make recommendations on areas for…</td>
      <td>&lt;span&gt;Remote&lt;/span&gt;</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Email%20Marketing%20Implementation%20Specialist%20at%20Digital%20Age...%20Arctic%20Leaf%20Inc.</td>
    </tr>
    <tr>
      <th>70</th>
      <td>Scientist I/II, Process Development Analytics</td>
      <td>BlueRock Therapeutics</td>
      <td>Strong practical knowledge of experimental design, and statistical analysis of data. Train and supervise junior staff members in supporting analytical…</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Scientist%20I/II%2C%20Process%20Development%20Analytics%20BlueRock%20Therapeutics</td>
    </tr>
    <tr>
      <th>69</th>
      <td>Junior Business Analyst</td>
      <td>Dokainish &amp; Company</td>
      <td>Work closely with IT team to satisfy data sampling, project analysis, testing verification, and other user requests from existing client databases.</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20Dokainish%20%26%20Company</td>
    </tr>
    <tr>
      <th>68</th>
      <td>Junior Analyst, Indirect Tax</td>
      <td>KPMG</td>
      <td>Work with advanced information technology for electronic data query and analysis. Perform In-depth data analysis to identify areas of risk, opportunities and…</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Analyst%2C%20Indirect%20Tax%20KPMG</td>
    </tr>
    <tr>
      <th>83</th>
      <td>Jr. Data Scientist</td>
      <td>SimpTek Technologies</td>
      <td>Integration with 3rd party API’s for data collection and analysis, including weather data, time-series data, and event-based data sets.</td>
      <td>Fredericton, NB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data%20Scientist%20SimpTek%20Technologies</td>
    </tr>
    <tr>
      <th>84</th>
      <td>Junior CRM Business Analyst</td>
      <td>Educators Financial Group</td>
      <td>Assists in analytics with need-based support on reports data extraction, compiling and manipulation. CRM Business Analyst with the delivery of CRM initiatives,…</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20CRM%20Business%20Analyst%20Educators%20Financial%20Group</td>
    </tr>
    <tr>
      <th>85</th>
      <td>Junior Pricing Analyst</td>
      <td>Bélanger UPT</td>
      <td>Collects data and maintains the database. Prepares financial and sku analysis reports, analyses margins and competitive market data.</td>
      <td>Mississauga, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Pricing%20Analyst%20B%C3%A9langer%20UPT</td>
    </tr>
    <tr>
      <th>86</th>
      <td>Data Processing Analyst I - 1 year contract (2)</td>
      <td>ERIS Info.</td>
      <td>Very good with data, numbers and patterns. Follow set instructions and run different scripts to extract data from images. Perform quality control of results.</td>
      <td>Temporarily Remote in Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Processing%20Analyst%20I%20-%201%20year%20contract%20%282%29%20ERIS%20Info.</td>
    </tr>
    <tr>
      <th>102</th>
      <td>Jr. Data/Reporting Analyst</td>
      <td>Scarsin</td>
      <td>Data management, data analysis and ETL process skills and concepts including data modeling and transformations. Required Knowledge, Skills and Experience.</td>
      <td>Markham, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data/Reporting%20Analyst%20Scarsin</td>
    </tr>
    <tr>
      <th>101</th>
      <td>Jr. Data Analyst</td>
      <td>Blackstone Energy</td>
      <td>Familiarity with data mining techniques. Reporting to the Director of Analytics, you will collect, clean, organize and analyze data for the organization.</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data%20Analyst%20Blackstone%20Energy</td>
    </tr>
    <tr>
      <th>100</th>
      <td>Junior Business Analyst (remote)</td>
      <td>Software International</td>
      <td>Analyzes and evaluates complex data processing systems both current and proposed, translating business area customer information systems requirements into…</td>
      <td>Remote in Mississauga, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20%28remote%29%20Software%20International</td>
    </tr>
    <tr>
      <th>99</th>
      <td>Junior Developer – Test Data</td>
      <td>CGI Inc</td>
      <td>Develop, maintain knowledge of data available from upstream sources and data within various platforms. Support data profiling using TD tooling and ad hoc system…</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Developer%20%E2%80%93%20Test%20Data%20CGI%20Inc</td>
    </tr>
    <tr>
      <th>98</th>
      <td>Field Data Scientist I / Junior Field Data Scientist</td>
      <td>ThinkData Works</td>
      <td>Conducting research to identify data sources and data products for specific client requirements. Design and build data products.</td>
      <td>Hybrid remote in Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Field%20Data%20Scientist%20I%20/%20Junior%20Field%20Data%20Scientist%20ThinkData%20Works</td>
    </tr>
    <tr>
      <th>97</th>
      <td>Junior Business Analyst</td>
      <td>Centrecorp Management Services Limited</td>
      <td>Management of Excel spreadsheets, including updating and editing data as required. The Business Analysis team is seeking a full-time Junior Business Analyst…</td>
      <td>Markham, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20Centrecorp%20Management%20Services%20Limited</td>
    </tr>
    <tr>
      <th>96</th>
      <td>Junior Data Analyst</td>
      <td>Blend HRM Internal</td>
      <td>Able to analyze data and interpret the results. Assist in enforcing proper data collection in team engagement trackers. Create, update and maintain trackers.</td>
      <td>Remote in Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20Blend%20HRM%20Internal</td>
    </tr>
    <tr>
      <th>67</th>
      <td>Junior Business Analyst</td>
      <td>Pivotree</td>
      <td>Roles &amp;amp; Responsibilities: • Elicits and documents requirements using a variety of methods, such as interviews, document analysis, requirements workshops,…</td>
      <td>Remote in Ottawa, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20Pivotree</td>
    </tr>
    <tr>
      <th>95</th>
      <td>Business Intelligence Analyst I</td>
      <td>Finning International Inc.</td>
      <td>Basic ability to mine data, profile data and derive business solutions using data. Critically evaluate information gathered from multiple data sources and…</td>
      <td>Edmonton, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Business%20Intelligence%20Analyst%20I%20Finning%20International%20Inc.</td>
    </tr>
    <tr>
      <th>93</th>
      <td>Junior Data Scientist</td>
      <td>Providence Health Care</td>
      <td>Reviews clinical data at aggregate levels on a regular basis using analytical reporting tools to support the identification of risks and data patterns or trends…</td>
      <td>Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Scientist%20Providence%20Health%20Care</td>
    </tr>
    <tr>
      <th>92</th>
      <td>Junior Data Analyst</td>
      <td>Canadian Niagara Hotels</td>
      <td>Investigate data quality issues identified by data stakeholders as well as those detected by data quality monitoring rules.</td>
      <td>Niagara Falls, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20Canadian%20Niagara%20Hotels</td>
    </tr>
    <tr>
      <th>91</th>
      <td>Junior Biostatistician</td>
      <td>Amaris</td>
      <td>Preparing analysis datasets and explore data prior to statistical analyses. Interpreting data within the context of the project.</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Biostatistician%20Amaris</td>
    </tr>
    <tr>
      <th>90</th>
      <td>FL Junior Data Analyst</td>
      <td>Fujitsu</td>
      <td>Perform data integrity and quality checks. Experience with data repositories and advance Excel skills. Junior/Intermediate Data Analyst requirement for minimum…</td>
      <td>Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=FL%20Junior%20Data%20Analyst%20Fujitsu</td>
    </tr>
    <tr>
      <th>89</th>
      <td>Data Processing Analyst I</td>
      <td>ERIS Environmental Risk Information Services</td>
      <td>Very good with data, numbers and patterns. Follow set instructions and run different scripts to extract data from images. Perform quality control of results.</td>
      <td>Temporarily Remote in Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Processing%20Analyst%20I%20ERIS%20Environmental%20Risk%20Information%20Services</td>
    </tr>
    <tr>
      <th>88</th>
      <td>Junior Power Analyst</td>
      <td>Dynasty Power Inc.</td>
      <td>Analyze data to look for profitable trading strategies. Passion for trading, financial derivatives and financial data analysis considered an asset.</td>
      <td>Calgary, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Power%20Analyst%20Dynasty%20Power%20Inc.</td>
    </tr>
    <tr>
      <th>87</th>
      <td>Quality Assurance Specialist (Backend/Data) - Junior/Interme...</td>
      <td>Klick Health</td>
      <td>Perform data analysis using SQL to ensure data quality and quality of programs. Practical experience with manipulating test data &amp;amp; its validation techniques.</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Quality%20Assurance%20Specialist%20%28Backend/Data%29%20-%20Junior/Interme...%20Klick%20Health</td>
    </tr>
    <tr>
      <th>94</th>
      <td>Commercial Financial Analyst I</td>
      <td>Thermo Fisher Scientific</td>
      <td>Data management experience and the ability to manage large sets of data and accurate reports. As part of the commercial finance organization, your position will…</td>
      <td>Ottawa, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Commercial%20Financial%20Analyst%20I%20Thermo%20Fisher%20Scientific</td>
    </tr>
    <tr>
      <th>217</th>
      <td>MySQL DBA I</td>
      <td>Percona</td>
      <td>Percona is a leader in providing best-of-breed enterprise-class support, consulting, managed services, training and software for MySQL®, MariaDB®, MongoDB®,…</td>
      <td>Remote in Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=MySQL%20DBA%20I%20Percona</td>
    </tr>
    <tr>
      <th>300</th>
      <td>Junior IT Specialist</td>
      <td>Fortinet</td>
      <td>This position would represent a great fit for IT professionals with a combination of virtualization, Openstack, storage and networking experience.</td>
      <td>Burnaby, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20IT%20Specialist%20Fortinet</td>
    </tr>
    <tr>
      <th>180</th>
      <td>Junior Software Developer; AUI</td>
      <td>RPM TECHNOLOGIES CORP</td>
      <td>We offer product record keeping and distribution systems, supporting a full range of investments, accounts and regulatory bodies.</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%3B%20AUI%20RPM%20TECHNOLOGIES%20CORP</td>
    </tr>
    <tr>
      <th>201</th>
      <td>Junior Drupal Developer (Remote Friendly)</td>
      <td>Acro Media</td>
      <td>Acro Media is looking for a Drupal Software Developer to develop Drupal 8 and Commerce builds. If you’re desperate to break free from that office life where you…</td>
      <td>Remote in Kelowna, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Drupal%20Developer%20%28Remote%20Friendly%29%20Acro%20Media</td>
    </tr>
    <tr>
      <th>202</th>
      <td>Junior Software Quality Assurance Specialist</td>
      <td>Piicomm Inc.</td>
      <td>Review development specifications, technical documentations, and user stories to build and execute appropriate test plans. Job Type: Full-time, Permanent.</td>
      <td>Plantagenet, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Quality%20Assurance%20Specialist%20Piicomm%20Inc.</td>
    </tr>
    <tr>
      <th>104</th>
      <td>Junior Buyer (Data Entry)</td>
      <td>Insurance Corporation of British Columbia</td>
      <td>Our Strategic Sourcing department is currently seeking a Junior Buyer (Supply Analyst I) to join our growing team. Job Types: Full-time, Permanent.</td>
      <td>Hybrid remote in North Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Buyer%20%28Data%20Entry%29%20Insurance%20Corporation%20of%20British%20Columbia</td>
    </tr>
    <tr>
      <th>204</th>
      <td>Junior Settlement / Financial / Risk Analyst</td>
      <td>Dynasty Power Inc.</td>
      <td>Dynasty Power is currently looking to hire a Junior Settlement / Financial / Risk Analyst. This position will be accountable for settlements of trading…</td>
      <td>Calgary, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Settlement%20/%20Financial%20/%20Risk%20Analyst%20Dynasty%20Power%20Inc.</td>
    </tr>
    <tr>
      <th>205</th>
      <td>Junior Developer</td>
      <td>Coconut Software</td>
      <td>In this role, you will work on a platform that facilitates connections between businesses and their customers, through a combination of appointments, lobby…</td>
      <td>Canada</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Developer%20Coconut%20Software</td>
    </tr>
    <tr>
      <th>206</th>
      <td>Junior Developer</td>
      <td>University of Alberta Students' Union</td>
      <td>As part of an information technology team, the Junior Developer creates efficient and effective technology based solutions to meet the operational needs of…</td>
      <td>Edmonton, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Developer%20University%20of%20Alberta%20Students%27%20Union</td>
    </tr>
    <tr>
      <th>207</th>
      <td>Junior Web Developer</td>
      <td>Outshinery Creative</td>
      <td>Do you love tinkering with super geeky things? Are you technically creative and a natural problem solver? Do you love learning new technologies and stepping…</td>
      <td>&lt;span&gt;Remote&lt;/span&gt;</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Web%20Developer%20Outshinery%20Creative</td>
    </tr>
    <tr>
      <th>208</th>
      <td>Junior Systems Administrator</td>
      <td>Athennian</td>
      <td>Our products help legal, finance, and tax teams be transaction and audit-ready by organizing business entity and corporate structure information.</td>
      <td>Hybrid remote in Calgary, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Systems%20Administrator%20Athennian</td>
    </tr>
    <tr>
      <th>209</th>
      <td>Développeur junior, OutilsDev (C# et Jenkins)</td>
      <td>GIRO</td>
      <td>L'équipe Outils est responsable d’optimiser le pipeline de livraison de fonctionnalités et de technologies à nos clients à travers la conception et le…</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20junior%2C%20OutilsDev%20%28C%23%20et%20Jenkins%29%20GIRO</td>
    </tr>
    <tr>
      <th>210</th>
      <td>Analyste d'affaires, junior</td>
      <td>Caisse de dépôt et placement du Québec</td>
      <td>/ Carry out projects with potential returns and economic benefits for Quebecers. / Collaborate on dynamic teams with high-level professionals committed to…</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Analyste%20d%27affaires%2C%20junior%20Caisse%20de%20d%C3%A9p%C3%B4t%20et%20placement%20du%20Qu%C3%A9bec</td>
    </tr>
    <tr>
      <th>211</th>
      <td>Scientifique de données junior</td>
      <td>Robert Half</td>
      <td>Notre client recherche un scientifique de données junior. Fondée en tant qu'entreprise axée sur la création de nouvelles opportunités de vente nettes pour les…</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Scientifique%20de%20donn%C3%A9es%20junior%20Robert%20Half</td>
    </tr>
    <tr>
      <th>212</th>
      <td>Junior Web Developer</td>
      <td>Trellis</td>
      <td>Provide programming supports to lead developer on an Seed to Sale Cannabis Enterprise Software project. Develop documentation and assistance tools to support…</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Web%20Developer%20Trellis</td>
    </tr>
    <tr>
      <th>213</th>
      <td>Junior Trader</td>
      <td>Questrade Financial Group</td>
      <td>And we swear by that every single day. They efficiently and accurately process client trade requests according to the directions received from clients.</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Trader%20Questrade%20Financial%20Group</td>
    </tr>
    <tr>
      <th>214</th>
      <td>Junior Software Engineer</td>
      <td>Optima Tele.com, Inc.</td>
      <td>Engineering focus areas for this position include wireless gateways, LAN/WAN switches, IoT nodes, interface units and sensors.</td>
      <td>Remote in Markham, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Engineer%20Optima%20Tele.com%2C%20Inc.</td>
    </tr>
    <tr>
      <th>215</th>
      <td>Junior Guidewire Developer</td>
      <td>Ouest</td>
      <td>As a Business Technology Analyst, in Insurance Core Technology group within our Consulting Practice, you'll work within an engagement team and be responsible…</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Guidewire%20Developer%20Ouest</td>
    </tr>
    <tr>
      <th>200</th>
      <td>Jr. Software Engineer - Lighthouse</td>
      <td>KPMG</td>
      <td>Work closely with clients to understand key business issues. Gather and analyze requirements to develop impactful recommendations and solutions.</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Software%20Engineer%20-%20Lighthouse%20KPMG</td>
    </tr>
    <tr>
      <th>199</th>
      <td>Junior Java Developer [#3867]</td>
      <td>Alteo</td>
      <td>Alteo est à la recherche d'un Développeur Java junior pour un poste permanent basé à Québec. Design and develop React component.</td>
      <td>Hybrid remote in Quebec City, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Java%20Developer%20%5B%233867%5D%20Alteo</td>
    </tr>
    <tr>
      <th>198</th>
      <td>Junior Actuarial Analyst</td>
      <td>SCOR</td>
      <td>Participate in quarterly valuation processes involving the calculation of technical provisions and the analysis of results. 0 to 3 years of relevant experience.</td>
      <td>Canada</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Actuarial%20Analyst%20SCOR</td>
    </tr>
    <tr>
      <th>197</th>
      <td>Junior C++ Software Developer</td>
      <td>S&amp;P Global</td>
      <td>We need software engineers who can help us develop and maintain systems that are always online and can handle hundreds of thousands of transactions per second.</td>
      <td>Remote in London, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20C%2B%2B%20Software%20Developer%20S%26P%20Global</td>
    </tr>
    <tr>
      <th>181</th>
      <td>QA Analyst</td>
      <td>SHIPTRACK INC.</td>
      <td>Analyze, document, and prioritize bug reports. Define, implement, and maintain a testing suite. Create and document test scenarios.</td>
      <td>Plantagenet, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=QA%20Analyst%20SHIPTRACK%20INC.</td>
    </tr>
    <tr>
      <th>182</th>
      <td>Junior Software Developer</td>
      <td>i-Open Technologies</td>
      <td>You will be required to learn how to leverage HTML5 for use on tablets or developing smartphone apps with any number of development frameworks.</td>
      <td>Abbotsford, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20i-Open%20Technologies</td>
    </tr>
    <tr>
      <th>183</th>
      <td>Junior Research Consultant</td>
      <td>Arksum Results</td>
      <td>As this role is within the marketing and communications team, the ideal candidate for this position will have excellent writing skills, with a keen interest in…</td>
      <td>Etobicoke, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Research%20Consultant%20Arksum%20Results</td>
    </tr>
    <tr>
      <th>184</th>
      <td>Junior Analyst, Applications Support</td>
      <td>Lantic Inc.</td>
      <td>Pension plan with equivalent contribution from the company. Supplementary health insurance and dental care. Life insurance and accident insurance.</td>
      <td>Montréal, QC</td>
      <td>30 days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Analyst%2C%20Applications%20Support%20Lantic%20Inc.</td>
    </tr>
    <tr>
      <th>185</th>
      <td>Junior Devops Engineer</td>
      <td>Scribendi</td>
      <td>This role is for a fearless self-starter with good communication skills, a strong work ethic, and the ability to participate in all aspects of the software…</td>
      <td>Chatham-Kent, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Devops%20Engineer%20Scribendi</td>
    </tr>
    <tr>
      <th>186</th>
      <td>Jr. Software Developer (WinForms)</td>
      <td>MUNISIGHT</td>
      <td>We are a top-tier GovTech software and service company focused on helping Municipal Governments simplify. Full-stack developer, develop user-facing features…</td>
      <td>Hybrid remote in Edmonton, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Software%20Developer%20%28WinForms%29%20MUNISIGHT</td>
    </tr>
    <tr>
      <th>187</th>
      <td>Junior DevOps Engineer</td>
      <td>Navigator Games</td>
      <td>As a Junior DevOps Engineer, your main priorities will be to work with our developers to help us build and maintain our technology stack in support of the…</td>
      <td>Remote in Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20DevOps%20Engineer%20Navigator%20Games</td>
    </tr>
    <tr>
      <th>179</th>
      <td>Junior Software Developer</td>
      <td>Bioinformatics Solutions</td>
      <td>Work closely with other developers in an agile and collaborative environment to foster continuous improvement at the team and company level.</td>
      <td>Waterloo, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20Bioinformatics%20Solutions</td>
    </tr>
    <tr>
      <th>188</th>
      <td>Junior Full Stack Developer</td>
      <td>Visual Knowledge Share Ltd</td>
      <td>Visual Knowledge Share Ltd (VKS, vksapp.com) is looking for a talented, passionate, roll-up-your-sleeves, hands-on Junior Full Stack Developer.</td>
      <td>Remote in Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20Visual%20Knowledge%20Share%20Ltd</td>
    </tr>
    <tr>
      <th>190</th>
      <td>Junior Software Developer (Open to Remote)</td>
      <td>S&amp;P Global</td>
      <td>We need software developers who can help us develop and maintain systems that are always online and can handle hundreds of thousands of transactions per second.</td>
      <td>Remote in London, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20%28Open%20to%20Remote%29%20S%26P%20Global</td>
    </tr>
    <tr>
      <th>191</th>
      <td>Junior Developer - Quality Assurance</td>
      <td>Fortran Traffic Systems</td>
      <td>With the arrival of transportation technologies such as CAV and Vehicle-to-Everything (V2X). The Junior Developer / QA Engineer will be entrusted to both test…</td>
      <td>Remote in Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Developer%20-%20Quality%20Assurance%20Fortran%20Traffic%20Systems</td>
    </tr>
    <tr>
      <th>192</th>
      <td>Développeur(se) Junior, Intelligence d'affaires</td>
      <td>Caisse de dépôt et placement du Québec</td>
      <td>/ Carry out projects with potential returns and economic benefits for Quebecers. / Collaborate on dynamic teams with high-level professionals committed to…</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%28se%29%20Junior%2C%20Intelligence%20d%27affaires%20Caisse%20de%20d%C3%A9p%C3%B4t%20et%20placement%20du%20Qu%C3%A9bec</td>
    </tr>
    <tr>
      <th>193</th>
      <td>Service Technician I - Montreal</td>
      <td>NCR</td>
      <td>Localisation : Montréal (Rive-Sud), QC. Effectuer des travaux de niveau I sur les produits et services de moyenne-haute complexité ; produits de niveau I…</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Service%20Technician%20I%20-%20Montreal%20NCR</td>
    </tr>
    <tr>
      <th>194</th>
      <td>JUNIOR JAVA DEVELOPER</td>
      <td>Trailmark Systems Inc.</td>
      <td>For all positions we offer a competitive compensation package, including a health spending plan, along with a very flexible work schedule, an open and…</td>
      <td>Java, SK</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=JUNIOR%20JAVA%20DEVELOPER%20Trailmark%20Systems%20Inc.</td>
    </tr>
    <tr>
      <th>195</th>
      <td>Junior Programmer Analyst</td>
      <td>Advanis</td>
      <td>Successful businesses understand their customers and their competitors. World, as well as to all levels of government (from federal to municipal in Canada).</td>
      <td>Edmonton, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Programmer%20Analyst%20Advanis</td>
    </tr>
    <tr>
      <th>196</th>
      <td>Jr .Net</td>
      <td>Virtusa</td>
      <td>Strong on SQL server programming. T4 hire with option to train can be considered. 1 to 2 years of experience. Strong on SQL server programming.</td>
      <td>Halifax, NS</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr%20.Net%20Virtusa</td>
    </tr>
    <tr>
      <th>189</th>
      <td>Junior/Intermediate Ruby on Rails Developer</td>
      <td>ZayZoon</td>
      <td>You will work on customer- and admin-facing products, third party integrations both canned and bespoke, and help architect the system toward greater flexibility…</td>
      <td>&lt;span&gt;Remote&lt;/span&gt;</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior/Intermediate%20Ruby%20on%20Rails%20Developer%20ZayZoon</td>
    </tr>
    <tr>
      <th>301</th>
      <td>MRI Physicist, Junior</td>
      <td>Synaptive Medical Inc.</td>
      <td>The MRI Physicist position is an opportunity to develop applications on this novel system that leverage unique aspects of Synaptive MRI systems to address…</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=MRI%20Physicist%2C%20Junior%20Synaptive%20Medical%20Inc.</td>
    </tr>
  </tbody>
</table>
</div>



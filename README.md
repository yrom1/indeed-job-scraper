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
      <td>Junior Data Governance &amp; Data Quality Specialist - 336569</td>
      <td>Procom</td>
      <td>The candidate must be able to communicate effectively with team members and have an understanding of data analysis, data quality, data security, data movement,…</td>
      <td>Toronto, ON</td>
      <td>Today</td>
      <td>0</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Governance%20%26%20Data%20Quality%20Specialist%20-%20336569%20Procom</td>
    </tr>
    <tr>
      <th>102</th>
      <td>Junior Full Stack Developer New Graduate Opportunities</td>
      <td>Helcim</td>
      <td>Building smart and efficient code that works well within a service-based system architecture. Developing new features and systems, as well as maintaining…</td>
      <td>Hybrid remote in Calgary, AB</td>
      <td>Today</td>
      <td>0</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20New%20Graduate%20Opportunities%20Helcim</td>
    </tr>
    <tr>
      <th>101</th>
      <td>Junior .NET Developer- (remote)</td>
      <td>Avesdo</td>
      <td>Net Core (C#) to help our software development teams execute high-impact initiatives that fuel Avesdo's growth. Translate user stories to design to code.</td>
      <td>Remote in Vancouver, BC</td>
      <td>Just posted</td>
      <td>0</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20.NET%20Developer-%20%28remote%29%20Avesdo</td>
    </tr>
    <tr>
      <th>100</th>
      <td>Junior Field Service Specialist</td>
      <td>Thales Group</td>
      <td>Thales people architect solutions that enable two-thirds of planes to take off and land safely. This includes Software, Hardware, Systems Design, Verification &amp;amp;…</td>
      <td>Toronto, ON</td>
      <td>Today</td>
      <td>0</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Field%20Service%20Specialist%20Thales%20Group</td>
    </tr>
    <tr>
      <th>105</th>
      <td>Jr. Product Owner</td>
      <td>Labatt Breweries Canada</td>
      <td>The Jr. Product Owner at Labatt requires a technical expertise to create, deliver and support a product roadmap for our custom internal Ordering tool built on…</td>
      <td>Montréal, QC</td>
      <td>Just posted</td>
      <td>0</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Product%20Owner%20Labatt%20Breweries%20Canada</td>
    </tr>
    <tr>
      <th>106</th>
      <td>Junior Analyst - GCLP (Toronto, ON)</td>
      <td>Guardian Capital Group Limited</td>
      <td>Of clients within the financial services sector. Institutional investment management services are provided by. This will entail reviewing and developing data.</td>
      <td>Toronto, ON</td>
      <td>Just posted</td>
      <td>0</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Analyst%20-%C2%A0GCLP%20%28Toronto%2C%20ON%29%20Guardian%20Capital%20Group%20Limited</td>
    </tr>
    <tr>
      <th>217</th>
      <td>DevOps Junior / Junior DevOps</td>
      <td>Opal-RT</td>
      <td>À propos d’OPAL-RT Technologies. OPAL-RT s’est donné comme ambitieux défi de démocratiser la simulation temps réel afin de la rendre accessible à chaque…</td>
      <td>Remote in Montréal, QC</td>
      <td>Today</td>
      <td>0</td>
      <td>https://ca.indeed.com/jobs?q=DevOps%20Junior%20/%20Junior%20DevOps%20Opal-RT</td>
    </tr>
    <tr>
      <th>103</th>
      <td>Software Engineer I</td>
      <td>KAR Global</td>
      <td>Experience conducting code reviews and mentoring junior developers. With 20 years of industry leadership, OPENLANE has a proven track record of delivering the…</td>
      <td>Remote in Toronto, ON</td>
      <td>Today</td>
      <td>0</td>
      <td>https://ca.indeed.com/jobs?q=Software%20Engineer%20I%20KAR%20Global</td>
    </tr>
    <tr>
      <th>219</th>
      <td>SOC Analyst I</td>
      <td>eSentire</td>
      <td>Analyze incoming security signals in real time with a balance of accuracy and speed using a variety of forensic tools.</td>
      <td>&lt;span class="more_loc_container"&gt;&lt;a aria-label="Same SOC Analyst I job in 1 other location" class="more_loc" href="/addlLoc/redirect?tk=1g05rn5gbo258801&amp;amp;jk=262b55d86901268b&amp;amp;dest=%2Fjobs%3Fq%3Dpython%2Bjunior%26l%3DCanada%26grpKey%3DkAOlg7MKmAO09%252FgqoAMB8gcDdGNs" rel="nofollow"&gt;+1 location&lt;/a&gt;&lt;/span&gt;</td>
      <td>Today</td>
      <td>0</td>
      <td>https://ca.indeed.com/jobs?q=SOC%20Analyst%20I%20eSentire</td>
    </tr>
    <tr>
      <th>220</th>
      <td>Junior Software Engineer</td>
      <td>ORBCOMM</td>
      <td>Experience with multiple software languages, such as C++, C#, Java and dynamic scripting languages such as Lua or python is an asset.</td>
      <td>Remote in Kanata, ON</td>
      <td>Today</td>
      <td>0</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Engineer%20ORBCOMM</td>
    </tr>
    <tr>
      <th>218</th>
      <td>Junior Python programmer</td>
      <td>Visual Defence Inc</td>
      <td>You will work with Visual Defence’s Research and Development team under the guidance of the company’s Director of Research and Development.</td>
      <td>Richmond Hill, ON</td>
      <td>Today</td>
      <td>0</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Python%20programmer%20Visual%20Defence%20Inc</td>
    </tr>
    <tr>
      <th>104</th>
      <td>Junior Developer - Co-op</td>
      <td>Aequilibrium Software Inc.</td>
      <td>You have good communication, analysis and problem-solved skills. You're adaptable, flexible and willing to embrace change.</td>
      <td>&lt;span&gt;Remote&lt;/span&gt;</td>
      <td>Today</td>
      <td>0</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Developer%20-%20Co-op%20Aequilibrium%20Software%20Inc.</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Junior Data Analyst</td>
      <td>OSL Retail Services Inc</td>
      <td>Acquire data from primary or secondary data sources and maintain databases/data systems. Proven working experience as a data analyst or business data analyst.</td>
      <td>Mississauga, ON</td>
      <td>Today</td>
      <td>0</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20OSL%20Retail%20Services%20Inc</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Business Analyst - Junior - 336548</td>
      <td>Procom</td>
      <td>Research, analytical and problem-solving skills to investigate issues pertinent to the program, ability to find trends in program data, identify options, and…</td>
      <td>Toronto, ON</td>
      <td>Today</td>
      <td>0</td>
      <td>https://ca.indeed.com/jobs?q=Business%20Analyst%20-%20Junior%20-%20336548%20Procom</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Junior Business Analyst - Reporting &amp; Analytics</td>
      <td>TripArc</td>
      <td>Recommend and develop automation solutions for our data and reporting needs. Collaborate with our development, database and support teams to answer business…</td>
      <td>Toronto, ON</td>
      <td>Today</td>
      <td>0</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20-%20Reporting%20%26%20Analytics%20TripArc</td>
    </tr>
    <tr>
      <th>223</th>
      <td>Junior ASIC Verification Engineer</td>
      <td>NETINT Technologies Inc.</td>
      <td>You will work closely with ASIC design and verification engineers to verify SOC function features, close function &amp;amp; code coverage holes.</td>
      <td>Markham, ON</td>
      <td>1 day ago</td>
      <td>1</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20ASIC%20Verification%20Engineer%20NETINT%20Technologies%20Inc.</td>
    </tr>
    <tr>
      <th>222</th>
      <td>Junior Software Developer</td>
      <td>CardinalChain Software, Inc.</td>
      <td>Maintain and enhance enterprise financial system ( crypto-currency trading system, token-exchange system, financial modelling system), developing test programs,…</td>
      <td>Vancouver, BC</td>
      <td>Active 1 day ago</td>
      <td>1</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20CardinalChain%20Software%2C%20Inc.</td>
    </tr>
    <tr>
      <th>221</th>
      <td>QA Analyst I</td>
      <td>Milk Moovement</td>
      <td>As part of tracking milk from cow to carton, the Milk Moovement platform provides our clients with all the tools they need to manage their supply chain while…</td>
      <td>Remote in Halifax, NS</td>
      <td>1 day ago</td>
      <td>1</td>
      <td>https://ca.indeed.com/jobs?q=QA%20Analyst%20I%20Milk%20Moovement</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Electrical EIT, Data Centres</td>
      <td>WSP</td>
      <td>Basic knowledge of power distribution topologies for data centres and familiarity with redundancy concepts; Provide support in preparation of engineering design…</td>
      <td>Markham, ON</td>
      <td>1 day ago</td>
      <td>1</td>
      <td>https://ca.indeed.com/jobs?q=Electrical%20EIT%2C%20Data%20Centres%20WSP</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Business Analyst I - TELUS Health</td>
      <td>TELUS</td>
      <td>Experience analysing and reporting on performance and utilisation data. The successful candidate must be a strong creative and analytical thinker with strong…</td>
      <td>Toronto, ON</td>
      <td>1 day ago</td>
      <td>1</td>
      <td>https://ca.indeed.com/jobs?q=Business%20Analyst%20I%20-%20TELUS%20Health%20TELUS</td>
    </tr>
    <tr>
      <th>224</th>
      <td>Développeur SAP Junior/intermédiaire</td>
      <td>Createch</td>
      <td>Participer à des projets d’implémentation SAP chez nos clients, soit comme nouvelle implémentation ou pour un ajout spécifique géré par le contexte du projet.</td>
      <td>Hybrid remote in Montréal, QC</td>
      <td>1 day ago</td>
      <td>1</td>
      <td>https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20SAP%20Junior/interm%C3%A9diaire%20Createch</td>
    </tr>
    <tr>
      <th>116</th>
      <td>Junior Database Analyst</td>
      <td>HealthHub Solutions</td>
      <td>Reporting to the Senior Analyst, Business Intelligence the successful candidate will be responsible for monitoring, maintenance and operational support of our…</td>
      <td>Mississauga, ON</td>
      <td>1 day ago</td>
      <td>1</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Database%20Analyst%20HealthHub%20Solutions</td>
    </tr>
    <tr>
      <th>115</th>
      <td>Junior Business Analyst (AP)</td>
      <td>Staffmax</td>
      <td>This is a Full Time Permanent Job. Support the on-going maintenance and continuous improvement of products. Conduct needs assessments with clients to identify…</td>
      <td>Thornhill, ON</td>
      <td>1 day ago</td>
      <td>1</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20%28AP%29%20Staffmax</td>
    </tr>
    <tr>
      <th>114</th>
      <td>Junior Software Developer (Co-op/Contract) - AI Project</td>
      <td>Binary Stream</td>
      <td>Binary Stream is an award-winning, Microsoft Gold certified partner that develops enterprise-grade software to enhance Microsoft Dynamics 365.</td>
      <td>Burnaby, BC</td>
      <td>1 day ago</td>
      <td>1</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20%28Co-op/Contract%29%20-%20AI%20Project%20Binary%20Stream</td>
    </tr>
    <tr>
      <th>225</th>
      <td>Jr. Photonic System Test Specialist</td>
      <td>NOKIA</td>
      <td>Our Advanced Optics Team within the Fixed Networks Broadband Networks organization is looking for a Photonics System Test Specialist in Ottawa.</td>
      <td>Hybrid remote in Ottawa, ON</td>
      <td>1 day ago</td>
      <td>1</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Photonic%20System%20Test%20Specialist%20NOKIA</td>
    </tr>
    <tr>
      <th>112</th>
      <td>Junior Front-End Software Developer</td>
      <td>Tantalus</td>
      <td>This role offers a competitive salary plus variable compensation tied to business unit scale objectives. Tantalus offers full health, dental and vision plans,…</td>
      <td>Remote in Burnaby, BC</td>
      <td>1 day ago</td>
      <td>1</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Front-End%20Software%20Developer%20Tantalus</td>
    </tr>
    <tr>
      <th>111</th>
      <td>Développeur Junior / Intermédiaire (1 à 4 ans d’expérience)</td>
      <td>DECIMAL</td>
      <td>Notre expertise en gestion de performance, reconnue depuis plus de 30 ans, nous permet aujourd’hui de nous définir comme des créateurs d’informations de gestion…</td>
      <td>Longueuil, QC</td>
      <td>1 day ago</td>
      <td>1</td>
      <td>https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20Junior%20/%20Interm%C3%A9diaire%20%281%20%C3%A0%204%20ans%20d%E2%80%99exp%C3%A9rience%29%20DECIMAL</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Product Engineer (JavaScript/SQL - Junior Level)</td>
      <td>DLT Labs Technologies Private Limited</td>
      <td>Document custom implementation, integrations, configuration, and data elements implemented inside platform/product framework. Must have knowledge about SQL.</td>
      <td>Toronto, ON</td>
      <td>1 day ago</td>
      <td>1</td>
      <td>https://ca.indeed.com/jobs?q=Product%20Engineer%20%28JavaScript/SQL%20-%20Junior%20Level%29%20DLT%20Labs%20Technologies%20Private%20Limited</td>
    </tr>
    <tr>
      <th>110</th>
      <td>Junior Software Developer (Co-op/Contract)- DevOps Project</td>
      <td>Binary Stream</td>
      <td>Binary Stream is an award-winning, Microsoft Gold certified partner that develops enterprise-grade software to enhance Microsoft Dynamics 365.</td>
      <td>Burnaby, BC</td>
      <td>1 day ago</td>
      <td>1</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20%28Co-op/Contract%29-%20DevOps%20Project%20Binary%20Stream</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Mechanical EIT, Data Centres</td>
      <td>WSP</td>
      <td>Basic knowledge of building mechanical systems to support data centres (DCs); This position is focused on data centres, telecom COs and other mission-critical…</td>
      <td>Markham, ON</td>
      <td>1 day ago</td>
      <td>1</td>
      <td>https://ca.indeed.com/jobs?q=Mechanical%20EIT%2C%20Data%20Centres%20WSP</td>
    </tr>
    <tr>
      <th>107</th>
      <td>Junior Systems Developer</td>
      <td>Queen's University</td>
      <td>The Information Technology Services department at Queen's University requires a Junior Systems Developer to design, develop, implement and troubleshoot web…</td>
      <td>Kingston, ON</td>
      <td>1 day ago</td>
      <td>1</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Systems%20Developer%20Queen%27s%20University</td>
    </tr>
    <tr>
      <th>108</th>
      <td>Junior Field Service Specialist</td>
      <td>Thales Canada Inc., Defence and Security</td>
      <td>Thales people architect solutions that enable two-thirds of planes to take off and land safely. This includes Software, Hardware, Systems Design, Verification &amp;amp;…</td>
      <td>Toronto, ON</td>
      <td>1 day ago</td>
      <td>1</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Field%20Service%20Specialist%20Thales%20Canada%20Inc.%2C%20Defence%20and%20Security</td>
    </tr>
    <tr>
      <th>109</th>
      <td>Junior or Intermediate Web Developer</td>
      <td>Resource Software International Ltd.</td>
      <td>The position involves working as part of a small close knit and highly motivated development team. You will be involved in all aspects of product development…</td>
      <td>Oshawa, ON</td>
      <td>1 day ago</td>
      <td>1</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20or%20Intermediate%20Web%20Developer%20Resource%20Software%20International%20Ltd.</td>
    </tr>
    <tr>
      <th>113</th>
      <td>GBP - Junior Programmer / Analyst, Client Services &amp; Solutio...</td>
      <td>Scotiabank</td>
      <td>Global Banking &amp;amp; Markets provides a full range of investment banking, credit and risk management products and services relevant to the financing and strategic…</td>
      <td>Toronto, ON</td>
      <td>1 day ago</td>
      <td>1</td>
      <td>https://ca.indeed.com/jobs?q=GBP%20-%20Junior%20Programmer%20/%20Analyst%2C%20Client%20Services%20%26%20Solutio...%20Scotiabank</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Financial Analyst I</td>
      <td>TELUS</td>
      <td>Manual data entry with 100% accuracy. Manual data validation with 100% accuracy. Tracking and analysis of contractors hours, working patterns, patient ratings,…</td>
      <td>Vancouver, BC</td>
      <td>2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Financial%20Analyst%20I%20TELUS</td>
    </tr>
    <tr>
      <th>8</th>
      <td>DATA PROCESSING OPERATOR CLASS I</td>
      <td>Kativik School Board</td>
      <td>Make backup copies, copy, compress or destroy files on various media and transfer data from one. POSITION: DATA PROCESSING OPERATOR CLASS I*.</td>
      <td>Montréal, QC</td>
      <td>2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=DATA%20PROCESSING%20OPERATOR%20CLASS%20I%20Kativik%20School%20Board</td>
    </tr>
    <tr>
      <th>125</th>
      <td>Junior Programmer Analyst</td>
      <td>MDG Computers Canada Inc</td>
      <td>The successful candidate will work with various stakeholders to develop, test, implement and maintain application systems. Job Types: Full-time, Permanent.</td>
      <td>Oakville, ON</td>
      <td>2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Programmer%20Analyst%20MDG%20Computers%20Canada%20Inc</td>
    </tr>
    <tr>
      <th>124</th>
      <td>Junior Analyst</td>
      <td>BCAA</td>
      <td>A successful candidate offered employment at BCAA will need to provide proof of full vaccination prior to commencing employment.</td>
      <td>Canada</td>
      <td>2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Analyst%20BCAA</td>
    </tr>
    <tr>
      <th>123</th>
      <td>Junior Oracle DBA</td>
      <td>AstraNorth</td>
      <td>Defines and administers data base organization, standards, controls, procedures, and documentation. Provides experienced technical consulting in the definition,…</td>
      <td>Toronto, ON</td>
      <td>2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Oracle%20DBA%20AstraNorth</td>
    </tr>
    <tr>
      <th>122</th>
      <td>Programmeur.e Web junior full-stack</td>
      <td>Revue Qui fait Quoi inc.</td>
      <td>Sous la responsabilité du rédacteur en chef et éditeur et d'un chargé de projet Web, votre rôle sera de collaborer à la programmation et au développement d'une…</td>
      <td>Remote in Montréal, QC</td>
      <td>Active 2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Programmeur.e%20Web%20junior%20full-stack%20Revue%20Qui%20fait%20Quoi%20inc.</td>
    </tr>
    <tr>
      <th>121</th>
      <td>Junior Software Developer-AQE</td>
      <td>Keywords Studios</td>
      <td>In this role you will be able to provide technical insights and expertise to support comprehensive automated verification. Previous experience in software QA.</td>
      <td>Temporarily Remote in Vancouver, BC</td>
      <td>2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer-AQE%20Keywords%20Studios</td>
    </tr>
    <tr>
      <th>120</th>
      <td>Junior Software Engineer</td>
      <td>SkiBig3</td>
      <td>SkiBig3 is currently seeking a full-time junior software engineer who will work on our software development and will be able to create reports used for business…</td>
      <td>Banff, AB</td>
      <td>2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Engineer%20SkiBig3</td>
    </tr>
    <tr>
      <th>119</th>
      <td>Junior Automation Specialist</td>
      <td>Roberts Onsite Inc</td>
      <td>The Junior Automation Specialist position is located in Kitchener, Ontario and reports directly to the Automation Controls &amp;amp; Engineering Manager.</td>
      <td>Kitchener, ON</td>
      <td>2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Automation%20Specialist%20Roberts%20Onsite%20Inc</td>
    </tr>
    <tr>
      <th>117</th>
      <td>Junior Developer/Backend developer</td>
      <td>Avant Techno Solutions</td>
      <td>Contributes to the overall success of the Global Payment Technology globally by designing, developing, and supporting applications using Shell Scripting, C/C++,…</td>
      <td>Toronto, ON</td>
      <td>2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Developer/Backend%20developer%20Avant%20Techno%20Solutions</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Junior Business Analyst</td>
      <td>Pride Mobility Products Company</td>
      <td>A passion about organizing data and bringing order to chaos, while also being able to analyze and provide actionable insights. A desire to grow quickly.</td>
      <td>Remote in Beamsville, ON</td>
      <td>Active 2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20Pride%20Mobility%20Products%20Company</td>
    </tr>
    <tr>
      <th>118</th>
      <td>Technicien(ne) en support technique junior</td>
      <td>Les systèmes d'information ULLIX</td>
      <td>ULLIX offre des solutions spécialisées pour la passation de tests d’aptitudes, psychométriques ou de connaissances visant à supporter les efforts de recrutement…</td>
      <td>Montréal, QC</td>
      <td>Active 2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Technicien%28ne%29%20en%20support%20technique%20junior%20Les%20syst%C3%A8mes%20d%27information%20ULLIX</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Junior Data Analyst</td>
      <td>Beta-Calco</td>
      <td>Gain and update job knowledge to remain informed about innovation in the field, explore and implement use cases for data science/data analytics to improve…</td>
      <td>Remote in Toronto, ON</td>
      <td>Active 2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20Beta-Calco</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Junior Data Analyst / Data Entry</td>
      <td>Strategy Institute</td>
      <td>Conducting data profiling to analyze quality of incoming data &amp;amp; advising on any data cleansing rules. Perform data maintenance tasks when required to ensure…</td>
      <td>Toronto, ON</td>
      <td>2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20/%20Data%20Entry%20Strategy%20Institute</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Junior Back-end Developer / Data-entry</td>
      <td>eMotors Direct</td>
      <td>Assist with writing of data entry guidelines, data validation plans and data review. Data management and data quality assurance.</td>
      <td>Remote in Edmonton, AB</td>
      <td>Active 2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Back-end%20Developer%20/%20Data-entry%20eMotors%20Direct</td>
    </tr>
    <tr>
      <th>226</th>
      <td>Junior Electronics Engineer - Integration and Testing</td>
      <td>Preciseley Microtechnology</td>
      <td>Basic programming skills in C, Labview or python. Salary starting at $55,000 depending on experience. Training and development opportunities in a growing…</td>
      <td>Burnaby, BC</td>
      <td>2 days ago</td>
      <td>2</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Electronics%20Engineer%20-%20Integration%20and%20Testing%20Preciseley%20Microtechnology</td>
    </tr>
    <tr>
      <th>227</th>
      <td>Junior Software Developer - Local Candidates Only</td>
      <td>PK Sound</td>
      <td>Develop and maintain new and existing software products. Analyze, design, and develop tests and test-automation suites. Web development experience with Angular.</td>
      <td>Calgary, AB</td>
      <td>Active 3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20-%20Local%20Candidates%20Only%20PK%20Sound</td>
    </tr>
    <tr>
      <th>134</th>
      <td>Junior Java Developer</td>
      <td>AstraNorth</td>
      <td>Undergraduate Degree or Technical Certificate. 1-2 years relevant experience. Good knowledge on various programming languages like Java, JavaScript, Python,…</td>
      <td>Toronto, ON</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Java%20Developer%20AstraNorth</td>
    </tr>
    <tr>
      <th>133</th>
      <td>Junior Software Developer (Vancouver)</td>
      <td>Eigen Development Ltd.</td>
      <td>Software Engineering or Computer Science university degree; or. Related University Degree (math, physics etc) with software development experience.</td>
      <td>Remote in Vancouver, BC</td>
      <td>Active 3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20%28Vancouver%29%20Eigen%20Development%20Ltd.</td>
    </tr>
    <tr>
      <th>132</th>
      <td>Junior Embedded Engineer/Developer</td>
      <td>Ecosystem Informatics Inc.</td>
      <td>The junior developer will work in a team to design and manufacture embedded system solutions, perform testing and debugging of hardware, and deploy them for…</td>
      <td>Mississauga, ON</td>
      <td>Active 3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Embedded%20Engineer/Developer%20Ecosystem%20Informatics%20Inc.</td>
    </tr>
    <tr>
      <th>131</th>
      <td>Junior IT Support Specialist</td>
      <td>The Aurum Group</td>
      <td>You are a team player with strong technical, communication, organizational, planning, planning, problem solving, and analytical skills.</td>
      <td>Calgary, AB</td>
      <td>Active 3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20IT%20Support%20Specialist%20The%20Aurum%20Group</td>
    </tr>
    <tr>
      <th>130</th>
      <td>Junior Application Developer - Web</td>
      <td>Western Financial Group</td>
      <td>Reporting to the Service Delivery Manager, you will be will be responsible for designing, coding, and modifying applications and or related web platforms.</td>
      <td>Winnipeg, MB</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Application%20Developer%20-%20Web%20Western%20Financial%20Group</td>
    </tr>
    <tr>
      <th>128</th>
      <td>Junior Developer</td>
      <td>LEARNstyle Ltd</td>
      <td>LEARNstyle Ltd is looking for a talented junior web developer for a full-time permanent position. *. As a full stack developer your day to day responsibilities…</td>
      <td>Greater Toronto Area, ON</td>
      <td>Active 3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Developer%20LEARNstyle%20Ltd</td>
    </tr>
    <tr>
      <th>127</th>
      <td>Junior Software Developer</td>
      <td>Keywords Studios</td>
      <td>In this role you will be able to provide technical insights and expertise to support comprehensive automated verification. Fix bugs on existing scripts.</td>
      <td>Temporarily Remote in Vancouver, BC</td>
      <td>Active 3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20Keywords%20Studios</td>
    </tr>
    <tr>
      <th>126</th>
      <td>Junior Full Stack Developer</td>
      <td>Plan de Vol</td>
      <td>&amp;gt; Willingness and experience to mentor junior developers. To be eligible for this funding, candidates must be Canadian Citizens, Permanent Residents, and under…</td>
      <td>Temporarily Remote in Toronto, ON</td>
      <td>Active 3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20Plan%20de%20Vol</td>
    </tr>
    <tr>
      <th>20</th>
      <td>GIS Technician and Jr Data Engineer</td>
      <td>QSP Geographics Inc.</td>
      <td>Are Customer-centric – they understand and embrace the role of delivering exemplary service. Lead – they lead by example through their actions and attitudes.</td>
      <td>Toronto, ON</td>
      <td>Active 3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=GIS%20Technician%20and%20Jr%20Data%20Engineer%20QSP%20Geographics%20Inc.</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Junior Data Analyst</td>
      <td>DeVry Greenhouses Ltd.</td>
      <td>Collect, clean and verify data. Aptitude for quantitative analysis and data driven decision making. Experience with managing or working with data.</td>
      <td>Chilliwack, BC</td>
      <td>Active 3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20DeVry%20Greenhouses%20Ltd.</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Junior Fiscal Policy Analyst</td>
      <td>Validus Healthcare Economics Inc.</td>
      <td>Knowledge of computer languages useful for data analysis, such as R or Python, considered an asset. Experience researching and analyzing complex Canadian public…</td>
      <td>Remote in Winnipeg, MB</td>
      <td>Active 3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Fiscal%20Policy%20Analyst%20Validus%20Healthcare%20Economics%20Inc.</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Junior Treasury Analyst</td>
      <td>ETG Commodities Inc.</td>
      <td>Advanced MS Excel and Access skills for reporting and data analysis. Assess accuracy and completeness of data records and conformance with company procedures.</td>
      <td>Mississauga, ON</td>
      <td>Active 3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Treasury%20Analyst%20ETG%20Commodities%20Inc.</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Junior Data Engineer - OpenRoad Auto Group</td>
      <td>OpenRoad Auto Group</td>
      <td>Ensure high data integrity and quality from various data sources that are aligned to industry best practices. The Data Engineer is responsible for implementing …</td>
      <td>Richmond, BC</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Engineer%20-%20OpenRoad%20Auto%20Group%20OpenRoad%20Auto%20Group</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Junior Business Analyst</td>
      <td>Norsat International Inc.</td>
      <td>Develop and monitor data quality metrics and ensure business data and reporting needs are met. You are responsible for developing and monitoring data quality…</td>
      <td>Richmond, BC</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20Norsat%20International%20Inc.</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Jr. Cyber Security Analyst</td>
      <td>Wellington Catholic DSB</td>
      <td>Excellent computer and technical skills including the use of excel for data analysis. 100% Temporary – JUNIOR CYBER SECURITY ANALYST*.</td>
      <td>Guelph, ON</td>
      <td>Active 3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Cyber%20Security%20Analyst%20Wellington%20Catholic%20DSB</td>
    </tr>
    <tr>
      <th>135</th>
      <td>Junior Software Developer, C++ (remote)</td>
      <td>InterTalk Critical Information Systems Inc.</td>
      <td>You will spend time virtually with the team and remotely on your own. You will be expected to be detail-oriented and thorough in work processes, in addition to…</td>
      <td>Remote in Dartmouth, NS</td>
      <td>Active 3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%2C%20C%2B%2B%20%28remote%29%20InterTalk%20Critical%20Information%20Systems%20Inc.</td>
    </tr>
    <tr>
      <th>136</th>
      <td>Junior Front End Developer</td>
      <td>Leap Tools</td>
      <td>Collaborate with team members to review requirements and interface and application design specifications. Design beautiful interfaces with an elegant simplicity…</td>
      <td>Remote in Toronto, ON</td>
      <td>Active 3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Front%20End%20Developer%20Leap%20Tools</td>
    </tr>
    <tr>
      <th>129</th>
      <td>DevOps Specialist I</td>
      <td>PortfolioAid Inc.</td>
      <td>Category: Permanent, Full Time, Monday-Friday, Regular Hours. § Implement release processes across development, test, and production environments.</td>
      <td>Toronto, ON</td>
      <td>3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=DevOps%20Specialist%20I%20PortfolioAid%20Inc.</td>
    </tr>
    <tr>
      <th>137</th>
      <td>Junior Developer</td>
      <td>The Corner Office</td>
      <td>The Junior Developer would partner with the Senior Data Analyst to support internal applications, perform maintenance on existing deployments of software tools,…</td>
      <td>Regina, SK</td>
      <td>Active 3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Developer%20The%20Corner%20Office</td>
    </tr>
    <tr>
      <th>228</th>
      <td>Junior Full Stack Developer</td>
      <td>Leap Tools</td>
      <td>Craft scalable TypeScript and Python code to integrate with customer websites, apps, and APIs. Flex your TypeScript muscle to design/develop single page web…</td>
      <td>Remote in Toronto, ON</td>
      <td>Active 3 days ago</td>
      <td>3</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20Leap%20Tools</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Junior Financial Analyst</td>
      <td>Thomas, Large &amp; Singer</td>
      <td>Payable and Accounts Receivable data entry. Reporting the Senior Director, Finance &amp;amp; Client Services, the Junior Financial Analyst is responsible for preparing…</td>
      <td>Hybrid remote in Markham, ON</td>
      <td>Active 4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financial%20Analyst%20Thomas%2C%20Large%20%26%20Singer</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Junior Business Analyst - Special Project (Apr. 2022 - Mar....</td>
      <td>Mohawk College</td>
      <td>Organize and analyze this information and data. Gather benchmarking information and data on a variety of topic areas as assigned.</td>
      <td>Temporarily Remote in Hamilton, ON</td>
      <td>4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20-%20Special%20Project%20%28Apr.%202022%20-%20Mar....%20Mohawk%20College</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Junior Data Engineer</td>
      <td>Canadian Niagara Hotels</td>
      <td>Build and maintain data pipeline architecture required for optimal extraction, transformation, and loading of data from a wide variety of data sources.</td>
      <td>Niagara Falls, ON</td>
      <td>Active 4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Engineer%20Canadian%20Niagara%20Hotels</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Junior Big Data Engineer - 336165</td>
      <td>Procom</td>
      <td>Capability to architect highly scalable distributed data pipelines using open-source tools and big data technologies such as Hadoop, HBase, Spark, Storm, ELK,…</td>
      <td>Toronto, ON</td>
      <td>4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Big%20Data%20Engineer%20-%20336165%20Procom</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Software Developer/Database Manager, Web Applications</td>
      <td>NeuroRx Research</td>
      <td>Designing and developing quality test plans, scenarios, and test data. The candidate will be responsible for providing support to the users on the ongoing…</td>
      <td>Temporarily Remote in Montréal, QC</td>
      <td>Active 4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Software%20Developer/Database%20Manager%2C%20Web%20Applications%20NeuroRx%20Research</td>
    </tr>
    <tr>
      <th>138</th>
      <td>Junior Network Administrator</td>
      <td>Florists Supply Ltd.</td>
      <td>This individual will work closely with the Network Administrator and together they will be responsible for serving as the first point of contact for IT services…</td>
      <td>Remote in Winnipeg, MB</td>
      <td>Active 4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Network%20Administrator%20Florists%20Supply%20Ltd.</td>
    </tr>
    <tr>
      <th>230</th>
      <td>Junior Software Developer</td>
      <td>Good Chemistry</td>
      <td>The Junior Software Developer will contribute to Good Chemistry's QEMIST Cloud, a cloud-based quantum chemistry simulation service.</td>
      <td>Remote in Vancouver, BC</td>
      <td>4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20Good%20Chemistry</td>
    </tr>
    <tr>
      <th>229</th>
      <td>Junior Backend Developer - Summer Student Internship</td>
      <td>myMarketing.io</td>
      <td>MyMarketing is a unique digital marketing agency that provides businesses with a comprehensive, no-commitment digital marketing monthly subscription.</td>
      <td>Ottawa, ON</td>
      <td>Active 4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Backend%20Developer%20-%20Summer%20Student%20Internship%20myMarketing.io</td>
    </tr>
    <tr>
      <th>139</th>
      <td>Junior Python Developer</td>
      <td>Track Revenue Ltd.</td>
      <td>Work as part of a small engineer team to be the interconnect between business and tech divisions. Maintain uptime of some backend servers for internal use.</td>
      <td>Toronto, ON</td>
      <td>Active 4 days ago</td>
      <td>4</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Python%20Developer%20Track%20Revenue%20Ltd.</td>
    </tr>
    <tr>
      <th>231</th>
      <td>Jr Django REST/Python Developer</td>
      <td>focal</td>
      <td>Fully fluent in python + javascript. Canadian Citizen or Permanent Resident. Currently Enrolled Post Secondary Student. Co-op students are welcome.</td>
      <td>Victoria, BC</td>
      <td>Active 5 days ago</td>
      <td>5</td>
      <td>https://ca.indeed.com/jobs?q=Jr%20Django%20REST/Python%20Developer%20focal</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Jr. Analyst / Analyst, Development</td>
      <td>Graywood Group</td>
      <td>Continuous buildout and improvement on Graywood’s existing project data and costs database. Direct experience related to real estate development, data analysis,…</td>
      <td>Toronto, ON</td>
      <td>6 days ago</td>
      <td>6</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Analyst%20/%20Analyst%2C%20Development%20Graywood%20Group</td>
    </tr>
    <tr>
      <th>140</th>
      <td>Jr. Data Analyst</td>
      <td>Virtusa</td>
      <td>3 to 5 years of relevant experience in data analysis or analytics in the banking industry. Extract, Transform, Load ETL processes for understanding and building…</td>
      <td>Halifax, NS</td>
      <td>6 days ago</td>
      <td>6</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data%20Analyst%20Virtusa</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Junior Data Analytics Developer</td>
      <td>Tantalus</td>
      <td>Strong visual orientation for presenting data and analytics. You will work on data analytics tools related to the improvement of the electric, water and gas…</td>
      <td>Remote in Burnaby, BC</td>
      <td>6 days ago</td>
      <td>6</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Analytics%20Developer%20Tantalus</td>
    </tr>
    <tr>
      <th>232</th>
      <td>Administrateur.trice d'operations reseau TI Junior-(H/F)</td>
      <td>Société Générale</td>
      <td>Communication des rapports de contrôle quotidiens du matin. Détection et communication pendant les heures de bureau. O Cisco ACI ou vous êtes prêt à apprendre.</td>
      <td>Montréal, QC</td>
      <td>6 days ago</td>
      <td>6</td>
      <td>https://ca.indeed.com/jobs?q=Administrateur.trice%20d%27operations%20reseau%20TI%20Junior-%28H/F%29%20Soci%C3%A9t%C3%A9%20G%C3%A9n%C3%A9rale</td>
    </tr>
    <tr>
      <th>233</th>
      <td>Junior Network Operations Administrator</td>
      <td>Société Générale</td>
      <td>Supporting technical projects including involvement from local and global application, infrastructure, governance, and client teams.</td>
      <td>Montréal, QC</td>
      <td>6 days ago</td>
      <td>6</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Network%20Operations%20Administrator%20Soci%C3%A9t%C3%A9%20G%C3%A9n%C3%A9rale</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Analyst Shipping Channel I</td>
      <td>Purolator</td>
      <td>Open up to the Possibilities! At Purolator, you’ll be proud knowing you’re working for a Canadian company that truly values its employees. And it’s community.…</td>
      <td>Mississauga, ON</td>
      <td>7 days ago</td>
      <td>7</td>
      <td>https://ca.indeed.com/jobs?q=Analyst%20Shipping%20Channel%20I%20Purolator</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Junior/Intermediate Advanced Analytics Professional</td>
      <td>Definity</td>
      <td>Apply professional experience with data science software to prepare, analyze, and model data. 1+ years of professional work experience in a data analysis…</td>
      <td>Hybrid remote in Vancouver, BC</td>
      <td>7 days ago</td>
      <td>7</td>
      <td>https://ca.indeed.com/jobs?q=Junior/Intermediate%20Advanced%20Analytics%20Professional%20Definity</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Junior Database Administrator</td>
      <td>Questrade Financial Group</td>
      <td>They act as strategic partners with each business unit to help Questrade leverage technology to gain competitive advantage. You have experience with GIT/GitLab.</td>
      <td>Hybrid remote in Ontario</td>
      <td>7 days ago</td>
      <td>7</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Database%20Administrator%20Questrade%20Financial%20Group</td>
    </tr>
    <tr>
      <th>141</th>
      <td>Junior Software Developer</td>
      <td>Pason Systems Corp</td>
      <td>The team is seeking a junior full stack software developer with demonstrated skill in Java, Python, web-based technologies and frameworks, and Linux while…</td>
      <td>Calgary, AB</td>
      <td>7 days ago</td>
      <td>7</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20Pason%20Systems%20Corp</td>
    </tr>
    <tr>
      <th>142</th>
      <td>Junior Java Developer</td>
      <td>CEO FOUNDRY</td>
      <td>Experience with Core &amp;amp; Advance Java / J2EE. Experience with front-end development technologies such as Angular is helpful as well.</td>
      <td>Remote in Toronto, ON</td>
      <td>Active 7 days ago</td>
      <td>7</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Java%20Developer%20CEO%20FOUNDRY</td>
    </tr>
    <tr>
      <th>143</th>
      <td>Junior Software Development Engineer in Test</td>
      <td>Global Relay</td>
      <td>As a Junior Software Development Engineer in Test (Jr. SDET), you will be part of a small, highly focused team responsible for delivery of highly scalable and…</td>
      <td>Hybrid remote in Vancouver, BC</td>
      <td>7 days ago</td>
      <td>7</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Development%20Engineer%20in%20Test%20Global%20Relay</td>
    </tr>
    <tr>
      <th>144</th>
      <td>Junior Business Analyst</td>
      <td>The Skyline Group of Companies</td>
      <td>You will support Skyline users with day to day troubleshooting activities and assist with documenting software requirements for technology initiatives for…</td>
      <td>Guelph, ON</td>
      <td>7 days ago</td>
      <td>7</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20The%20Skyline%20Group%20of%20Companies</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Junior Data Engineer</td>
      <td>CGI</td>
      <td>Ensure the quality and integrity of data. Candidates must have strong collaboration skills to work with cross-functional teams and stakeholders to ensure…</td>
      <td>Toronto, ON</td>
      <td>7 days ago</td>
      <td>7</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Engineer%20CGI</td>
    </tr>
    <tr>
      <th>145</th>
      <td>Junior Underwriter</td>
      <td>Benecaid</td>
      <td>We enable employers to provide their employees with the health care they need and want more comprehensively and cost-effectively than traditional health…</td>
      <td>Hybrid remote in Etobicoke, ON</td>
      <td>Active 8 days ago</td>
      <td>8</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Underwriter%20Benecaid</td>
    </tr>
    <tr>
      <th>146</th>
      <td>Junior / Intermediate Analyst, Information Services</td>
      <td>Heartland Generation</td>
      <td>Reporting to the Director, IS, and working alongside a dynamic IS team, the Analyst is responsible for helping support and expand Heartland’s portfolio of…</td>
      <td>Calgary, AB</td>
      <td>Active 8 days ago</td>
      <td>8</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20/%20Intermediate%20Analyst%2C%20Information%20Services%20Heartland%20Generation</td>
    </tr>
    <tr>
      <th>147</th>
      <td>Junior Software Developer</td>
      <td>Makeship</td>
      <td>Design and implement high-impact changes. Build our dashboard to enable our creators to launch new product campaigns. Bonus points if you have....*.</td>
      <td>Remote in Vancouver, BC</td>
      <td>8 days ago</td>
      <td>8</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20Makeship</td>
    </tr>
    <tr>
      <th>148</th>
      <td>Junior Applications Analyst</td>
      <td>Parkland Corporation</td>
      <td>The Junior Applications Analyst - Integration plays a critical role in delivering high quality customer service and support to clients.</td>
      <td>Dartmouth, NS</td>
      <td>8 days ago</td>
      <td>8</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Applications%20Analyst%20Parkland%20Corporation</td>
    </tr>
    <tr>
      <th>234</th>
      <td>Jr. Web Application Tester</td>
      <td>Vistek LTD</td>
      <td>For more than 40 years, Vistek has been a Canadian Success story, retailing photo, video and digital professional equipment solutions. Basic knowledge of T-SQL.</td>
      <td>Toronto, ON</td>
      <td>8 days ago</td>
      <td>8</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Web%20Application%20Tester%20Vistek%20LTD</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Junior DBA (Database Administrator)</td>
      <td>Dawn InfoTek Inc.</td>
      <td>Dawn InfoTek Inc. is a professional IT consulting team that partners with major financial institutions, investment firms and government sectors.</td>
      <td>Toronto, ON</td>
      <td>Active 8 days ago</td>
      <td>8</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20DBA%20%28Database%20Administrator%29%20Dawn%20InfoTek%20Inc.</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Research Analyst I</td>
      <td>University Health Network</td>
      <td>Experience with data management and/or database design. You will design statistical analysis plans, perform data quality control, conduct analyses and report…</td>
      <td>Remote in Toronto, ON</td>
      <td>8 days ago</td>
      <td>8</td>
      <td>https://ca.indeed.com/jobs?q=Research%20Analyst%20I%20University%20Health%20Network</td>
    </tr>
    <tr>
      <th>33</th>
      <td>Junior Business Intelligence Developer</td>
      <td>Colliers Project Leaders</td>
      <td>Processes data extracts and configures data source connections using standard and custom data interfaces and APIs.</td>
      <td>Ottawa, ON</td>
      <td>8 days ago</td>
      <td>8</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Intelligence%20Developer%20Colliers%20Project%20Leaders</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Research Analyst I - Cancer Rehabilitation &amp; Survivorship Pr...</td>
      <td>University Health Network</td>
      <td>At minimum, one (1) to three (3) years of related research experience preferred (e.g., study coordination experience; database design/set-up; data collection…</td>
      <td>Toronto, ON</td>
      <td>8 days ago</td>
      <td>8</td>
      <td>https://ca.indeed.com/jobs?q=Research%20Analyst%20I%20-%20Cancer%20Rehabilitation%20%26%20Survivorship%20Pr...%20University%20Health%20Network</td>
    </tr>
    <tr>
      <th>151</th>
      <td>Junior PHP Full-Stack Developer</td>
      <td>Katipult</td>
      <td>Katipult is a white-label investor management software that enables companies to design, setup, and manage equity and debt investments and funds across multiple…</td>
      <td>Remote in Toronto, ON</td>
      <td>9 days ago</td>
      <td>9</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20PHP%20Full-Stack%20Developer%20Katipult</td>
    </tr>
    <tr>
      <th>150</th>
      <td>Junior Solutions Specialist</td>
      <td>Method:CRM</td>
      <td>This person will also provide paid training sessions and work as a dedicated consultant to our customers. Unlike other CRMs, the combination of Method’s deep…</td>
      <td>Temporarily Remote in Toronto, ON</td>
      <td>9 days ago</td>
      <td>9</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Solutions%20Specialist%20Method%3ACRM</td>
    </tr>
    <tr>
      <th>149</th>
      <td>Junior or Intermediate Quality Assurance Analyst</td>
      <td>LBMX Inc</td>
      <td>We are looking for a Junior or Intermediate Quality Assurance Analyst to work with our QA team, conducting testing of our web and desktop applications.</td>
      <td>Temporarily Remote in London, ON</td>
      <td>Active 9 days ago</td>
      <td>9</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20or%20Intermediate%20Quality%20Assurance%20Analyst%20LBMX%20Inc</td>
    </tr>
    <tr>
      <th>36</th>
      <td>Programmeur(euse) débutant en SQL / SQL Junior Programmer</td>
      <td>Ove décors ULC</td>
      <td>Experience working with enterprise data. Knowledge of ETL and BI data warehouse architecture is an asset. Solid computer science fundamentals such as algorithms…</td>
      <td>Laval, QC</td>
      <td>10 days ago</td>
      <td>10</td>
      <td>https://ca.indeed.com/jobs?q=Programmeur%28euse%29%20d%C3%A9butant%20en%20SQL%20/%20SQL%20Junior%20Programmer%20Ove%20d%C3%A9cors%20ULC</td>
    </tr>
    <tr>
      <th>237</th>
      <td>Junior Cloud Engineer OTW</td>
      <td>Ericsson</td>
      <td>Our CI/CD and System integration department plays a strategic role in making sure that the Cloud RAN solutions meet our customers’ expectations.</td>
      <td>Remote in Ottawa, ON</td>
      <td>10 days ago</td>
      <td>10</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Cloud%20Engineer%20OTW%20Ericsson</td>
    </tr>
    <tr>
      <th>236</th>
      <td>Software Engineer I</td>
      <td>Twitter</td>
      <td>We own the development tools distribution and configuration management for Twitter’s software engineering workstations! Work in an Agile, CI/CD environment.</td>
      <td>Toronto, ON</td>
      <td>10 days ago</td>
      <td>10</td>
      <td>https://ca.indeed.com/jobs?q=Software%20Engineer%20I%20Twitter</td>
    </tr>
    <tr>
      <th>235</th>
      <td>Junior Software Engineer</td>
      <td>OpenBet</td>
      <td>Develop new features and functionality for large scale highly performant transactional sites. Participate in all phases of the Software Development Life Cycle …</td>
      <td>Montréal, QC</td>
      <td>10 days ago</td>
      <td>10</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Engineer%20OpenBet</td>
    </tr>
    <tr>
      <th>238</th>
      <td>BIOINFORMATICS SCIENTIST I - CA</td>
      <td>Luminex</td>
      <td>This position is responsible for in-depth in-silico bioinformatics analysis required for development of sequencing and other molecular methods, bio surveillance…</td>
      <td>Toronto, ON</td>
      <td>Active 11 days ago</td>
      <td>11</td>
      <td>https://ca.indeed.com/jobs?q=BIOINFORMATICS%20SCIENTIST%20I%20-%20CA%20Luminex</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Junior Global Business Analyst</td>
      <td>ZOOK Canada Inc</td>
      <td>Conduct data mining and executes queries to process data from multiple sources. Analyze data and prepare reports/dashboards that show key trends and metrics.</td>
      <td>Burlington, ON</td>
      <td>11 days ago</td>
      <td>11</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Global%20Business%20Analyst%20ZOOK%20Canada%20Inc</td>
    </tr>
    <tr>
      <th>152</th>
      <td>System Consultant I</td>
      <td>Simon Fraser University</td>
      <td>Administrative and Professional Staff (APSA). The Systems Consultant oversees the operational delivery of computing and technical services for the Faculty of…</td>
      <td>Burnaby, BC</td>
      <td>11 days ago</td>
      <td>11</td>
      <td>https://ca.indeed.com/jobs?q=System%20Consultant%20I%20Simon%20Fraser%20University</td>
    </tr>
    <tr>
      <th>153</th>
      <td>Junior Java Developer</td>
      <td>TEKsystems</td>
      <td>Strong full-stack developer with solid Back End (Java 8+) development experience. Development experience working with SQL database.</td>
      <td>Toronto, ON</td>
      <td>13 days ago</td>
      <td>13</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Java%20Developer%20TEKsystems</td>
    </tr>
    <tr>
      <th>38</th>
      <td>Junior Data Scientist (2022-0118)</td>
      <td>ICTC</td>
      <td>Ability to work collaboratively with team members and share data tools and techniques to help build ICTC’s data capabilities.</td>
      <td>Ottawa, ON</td>
      <td>13 days ago</td>
      <td>13</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Scientist%20%282022-0118%29%20ICTC</td>
    </tr>
    <tr>
      <th>240</th>
      <td>Junior C/C++ &amp; Fortran Compiler Developer</td>
      <td>IBM</td>
      <td>Software Developers at IBM are the backbone of our strategic initiatives to design, code, test, and provide industry-leading solutions that make the world run…</td>
      <td>Markham, ON</td>
      <td>14 days ago</td>
      <td>14</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20C/C%2B%2B%20%26%20Fortran%20Compiler%20Developer%20IBM</td>
    </tr>
    <tr>
      <th>239</th>
      <td>Développeur Python junior</td>
      <td>Alithya</td>
      <td>Veuillez noter que ce poste est en télétravail. Téléphone, Microsoft Teams ou Zoom, comme vous préférez ! Analyser les exigences des clients et des utilisateurs…</td>
      <td>Remote in Montréal, QC</td>
      <td>14 days ago</td>
      <td>14</td>
      <td>https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20Python%20junior%20Alithya</td>
    </tr>
    <tr>
      <th>156</th>
      <td>Junior Python Developer</td>
      <td>Leap Tools</td>
      <td>You have a passion for solving complex problems and working on products that people will use on a daily basis. Our game nights are legendary.*.</td>
      <td>Remote in Toronto, ON</td>
      <td>Active 14 days ago</td>
      <td>14</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Python%20Developer%20Leap%20Tools</td>
    </tr>
    <tr>
      <th>39</th>
      <td>Data Scientist I</td>
      <td>TD Bank</td>
      <td>Technical skills in multiple facets of data science: advanced analytics, statistical modelling, machine learning &amp;amp; data engineering.</td>
      <td>Toronto, ON</td>
      <td>14 days ago</td>
      <td>14</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Scientist%20I%20TD%20Bank</td>
    </tr>
    <tr>
      <th>155</th>
      <td>Junior Quality Assurance Analyst</td>
      <td>TC Transcontinental</td>
      <td>Junior QA analyst will be working on legacy web applications testing and testing of newly created solutions in various environments, from .</td>
      <td>Mississauga, ON</td>
      <td>14 days ago</td>
      <td>14</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Quality%20Assurance%20Analyst%20TC%20Transcontinental</td>
    </tr>
    <tr>
      <th>154</th>
      <td>Junior Analyst - Regulatory Services (AEOI)</td>
      <td>Maples Group</td>
      <td>The Junior Analyst - Regulatory Services reports to a Senior Vice President and supports the Structured Finance Team. Fluency in English is required.</td>
      <td>Montréal, QC</td>
      <td>14 days ago</td>
      <td>14</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Analyst%20-%20Regulatory%20Services%20%28AEOI%29%20Maples%20Group</td>
    </tr>
    <tr>
      <th>244</th>
      <td>ASNA Event – Junior Actuarial Analyst &amp; Co-op</td>
      <td>Definity</td>
      <td>In this role, you will have exposure to actuarial development work in auto and property &amp;amp; liability lines under Personal and Commercial Insurance;</td>
      <td>Toronto, ON</td>
      <td>15 days ago</td>
      <td>15</td>
      <td>https://ca.indeed.com/jobs?q=ASNA%20Event%20%E2%80%93%20Junior%20Actuarial%20Analyst%20%26%20Co-op%20Definity</td>
    </tr>
    <tr>
      <th>243</th>
      <td>Jr. Software Engineer</td>
      <td>Publicis Worldwide</td>
      <td>With a strong, active and familial culture, Pub United is the agency’s social club, hosting events as wide reaching as Curling, Trivia Nights and more.</td>
      <td>Toronto, ON</td>
      <td>15 days ago</td>
      <td>15</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Software%20Engineer%20Publicis%20Worldwide</td>
    </tr>
    <tr>
      <th>242</th>
      <td>Software Developer I</td>
      <td>Watts Water Technologies</td>
      <td>The individual is a junior software developer who works on mostly pre-defined software development, testing and lifecycle support projects with the intent of…</td>
      <td>Vernon, BC</td>
      <td>15 days ago</td>
      <td>15</td>
      <td>https://ca.indeed.com/jobs?q=Software%20Developer%20I%20Watts%20Water%20Technologies</td>
    </tr>
    <tr>
      <th>241</th>
      <td>Junior Product Owner</td>
      <td>NCR</td>
      <td>They know we have the best and brightest software developers – developers who write code that can survive under the pressure of hundreds of thousands of…</td>
      <td>Waterloo, ON</td>
      <td>15 days ago</td>
      <td>15</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Product%20Owner%20NCR</td>
    </tr>
    <tr>
      <th>157</th>
      <td>Junior Developer - Microsoft Dynamics 365, Managed Services</td>
      <td>KPMG</td>
      <td>Participate in implementation customization and configuration for D365 solutions. Code, test, debug and document software solutions using appropriate processes,…</td>
      <td>Calgary, AB</td>
      <td>15 days ago</td>
      <td>15</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Developer%20-%20Microsoft%20Dynamics%20365%2C%20Managed%20Services%20KPMG</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Junior Marketing Associate</td>
      <td>Source Atlantic</td>
      <td>Improve new campaigns using data and feedback from existing and previous projects. Reporting to the Marketing Manager, the Marketing Associate’s is primarily…</td>
      <td>Saint John, NB</td>
      <td>15 days ago</td>
      <td>15</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Marketing%20Associate%20Source%20Atlantic</td>
    </tr>
    <tr>
      <th>41</th>
      <td>IT Support – Junior Data Coordinator</td>
      <td>Wellsite Masters</td>
      <td>Coordinate and manipulate all data that is derived from WM Systems. Create reports in Microsoft Excel, Word and PowerPoint as required.</td>
      <td>Calgary, AB</td>
      <td>15 days ago</td>
      <td>15</td>
      <td>https://ca.indeed.com/jobs?q=IT%20Support%20%E2%80%93%20Junior%20Data%20Coordinator%20Wellsite%20Masters</td>
    </tr>
    <tr>
      <th>42</th>
      <td>Jr. Data Strategist</td>
      <td>Publicis Groupe</td>
      <td>Familiarity with data metrics &amp;amp; terminology. The Jr. Data Strategist will ingest data from search, social, and other primary/secondary data sources to formulate…</td>
      <td>Toronto, ON</td>
      <td>15 days ago</td>
      <td>15</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data%20Strategist%20Publicis%20Groupe</td>
    </tr>
    <tr>
      <th>158</th>
      <td>Junior Software Engineer - Full Stack</td>
      <td>RideCo</td>
      <td>Collaborate with team members to get a better understanding of your user stories. Develop elegant features and solutions for our web and mobile platforms.</td>
      <td>Waterloo, ON</td>
      <td>Active 16 days ago</td>
      <td>16</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Engineer%20-%20Full%20Stack%20RideCo</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Business Analyst I, AWS Commerce Platform Business Operation...</td>
      <td>Amazon Dev Centre Canada ULC</td>
      <td>At least 1+ years of experience with data warehousing and reporting. At least 1+ years of professional working experience in related occupations of Business…</td>
      <td>Vancouver, BC</td>
      <td>16 days ago</td>
      <td>16</td>
      <td>https://ca.indeed.com/jobs?q=Business%20Analyst%20I%2C%20AWS%20Commerce%20Platform%20Business%20Operation...%20Amazon%20Dev%20Centre%20Canada%20ULC</td>
    </tr>
    <tr>
      <th>44</th>
      <td>Junior Business Analyst</td>
      <td>SMART TRADE TECHNOLOGIES</td>
      <td>Exposure and/or interest in data science or mathematics is a plus. SmartTrade Technologies is a software company specialising in the trading and finance sector.</td>
      <td>Toronto, ON</td>
      <td>Active 16 days ago</td>
      <td>16</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20SMART%20TRADE%20TECHNOLOGIES</td>
    </tr>
    <tr>
      <th>245</th>
      <td>Junior Research Developer</td>
      <td>C-CORE</td>
      <td>Initially these include research into applications that rely on numerical analysis, signal processing and statistical and machine learning.</td>
      <td>Ottawa, ON</td>
      <td>Active 17 days ago</td>
      <td>17</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Research%20Developer%20C-CORE</td>
    </tr>
    <tr>
      <th>45</th>
      <td>Jr. Data Systems Manager</td>
      <td>Nelson Education LTD</td>
      <td>Providing technical expertise in data storage structures, data mining, and data cleansing as needed. Supporting initiatives for data integrity and normalization…</td>
      <td>Toronto, ON</td>
      <td>17 days ago</td>
      <td>17</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data%20Systems%20Manager%20Nelson%20Education%20LTD</td>
    </tr>
    <tr>
      <th>46</th>
      <td>Junior Data Analytics Engineer</td>
      <td>Tier1 Financial Solutions</td>
      <td>Use large data sets to address business issues. Understanding of data warehousing concepts and NoSQL Databases. BS or MS in Computer Science or related fields.</td>
      <td>Ottawa, ON</td>
      <td>17 days ago</td>
      <td>17</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Analytics%20Engineer%20Tier1%20Financial%20Solutions</td>
    </tr>
    <tr>
      <th>159</th>
      <td>Junior Systems Programmer</td>
      <td>Paladin Technologies</td>
      <td>Your work will focus on the programming components associated with the installation, service, and maintenance of integrated low voltage systems.</td>
      <td>Ottawa, ON</td>
      <td>17 days ago</td>
      <td>17</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Systems%20Programmer%20Paladin%20Technologies</td>
    </tr>
    <tr>
      <th>160</th>
      <td>Junior Algorithmic Trading Developer with C++.</td>
      <td>Scotiabank</td>
      <td>The position will be a primary technical resource for the ETF trading desk. Enhancing our low latency trading framework, optimizing handling of market data,…</td>
      <td>Toronto, ON</td>
      <td>17 days ago</td>
      <td>17</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Algorithmic%20Trading%20Developer%20with%20C%2B%2B.%20Scotiabank</td>
    </tr>
    <tr>
      <th>47</th>
      <td>JR. FINANCIAL ANALYST</td>
      <td>SSi Canada</td>
      <td>Able to summarize data into visual dashboards using charts, graphs, trend analysis. As a Jr. Financial Analyst at SSi Canada, you will report to the Director of…</td>
      <td>Kanata, ON</td>
      <td>Active 18 days ago</td>
      <td>18</td>
      <td>https://ca.indeed.com/jobs?q=JR.%20FINANCIAL%20ANALYST%20SSi%20Canada</td>
    </tr>
    <tr>
      <th>161</th>
      <td>Junior Developer</td>
      <td>ICBC</td>
      <td>Location: North Vancouver Employment Type: Permanent Full Time. Business to improve customer responsiveness. This mandate will be fulfilled by using technology…</td>
      <td>Hybrid remote in North Vancouver, BC</td>
      <td>18 days ago</td>
      <td>18</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Developer%20ICBC</td>
    </tr>
    <tr>
      <th>162</th>
      <td>Junior Full Stack Developer</td>
      <td>Steelhaus Technologies</td>
      <td>We are seeking for a Junior Full Stack Developer to join our team who will be responsible for participating in all phases of the development life-cycle,…</td>
      <td>Calgary, AB</td>
      <td>20 days ago</td>
      <td>20</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20Steelhaus%20Technologies</td>
    </tr>
    <tr>
      <th>48</th>
      <td>Jr. Business Operations Analyst</td>
      <td>Vessi</td>
      <td>Ability to analyze a company’s big-picture data needs such as supporting in data analytics projects, supporting functional groups to review their data…</td>
      <td>Vancouver, BC</td>
      <td>21 days ago</td>
      <td>21</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Business%20Operations%20Analyst%20Vessi</td>
    </tr>
    <tr>
      <th>246</th>
      <td>Junior Electrical Engineer</td>
      <td>BBA inc.</td>
      <td>Work collaboratively with clients, project managers, engineers, designers and drafters in the preparation of deliverables to BBA and client standards.</td>
      <td>Trail, BC</td>
      <td>21 days ago</td>
      <td>21</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Electrical%20Engineer%20BBA%20inc.</td>
    </tr>
    <tr>
      <th>163</th>
      <td>Junior Analyst, Applications Support</td>
      <td>Lantic Inc.</td>
      <td>Pension plan with equivalent contribution from the company. Supplementary health insurance and dental care. Life insurance and accident insurance.</td>
      <td>Montréal, QC</td>
      <td>22 days ago</td>
      <td>22</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Analyst%2C%20Applications%20Support%20Lantic%20Inc.</td>
    </tr>
    <tr>
      <th>250</th>
      <td>Junior DevOps Engineer</td>
      <td>Hellbent Games</td>
      <td>This job involves development and maintenance of scalable, secure and highly-available services and infrastructure for online gaming such as player progression,…</td>
      <td>Burnaby, BC</td>
      <td>22 days ago</td>
      <td>22</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20DevOps%20Engineer%20Hellbent%20Games</td>
    </tr>
    <tr>
      <th>49</th>
      <td>Junior Buyer (Data Entry)</td>
      <td>Insurance Corporation of British Columbia</td>
      <td>Our Strategic Sourcing department is currently seeking a Junior Buyer (Supply Analyst I) to join our growing team. Job Types: Full-time, Permanent.</td>
      <td>Hybrid remote in North Vancouver, BC</td>
      <td>Active 22 days ago</td>
      <td>22</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Buyer%20%28Data%20Entry%29%20Insurance%20Corporation%20of%20British%20Columbia</td>
    </tr>
    <tr>
      <th>247</th>
      <td>Junior Software Developers</td>
      <td>David Aplin Group</td>
      <td>This position is responsible for the development, evaluation, implementation and maintenance of new software solutions, including maintenance and development of…</td>
      <td>Winnipeg, MB</td>
      <td>22 days ago</td>
      <td>22</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developers%20David%20Aplin%20Group</td>
    </tr>
    <tr>
      <th>248</th>
      <td>Junior Software Developer (Job Req. #2022-235)</td>
      <td>Ross Video</td>
      <td>You will help develop, deploy, and automate the Virtualized Switcher product to AWS and other cloud platforms.</td>
      <td>Remote in Ottawa, ON</td>
      <td>22 days ago</td>
      <td>22</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20%28Job%20Req.%20%232022-235%29%20Ross%20Video</td>
    </tr>
    <tr>
      <th>249</th>
      <td>Analog Design Engr, I</td>
      <td>Synopsys</td>
      <td>You will be working with a cross functional team of analog and mixed signal circuit designers from a wide variety of backgrounds on our latest DDR and HBM IP…</td>
      <td>Kanata, ON</td>
      <td>22 days ago</td>
      <td>22</td>
      <td>https://ca.indeed.com/jobs?q=Analog%20Design%20Engr%2C%20I%20Synopsys</td>
    </tr>
    <tr>
      <th>50</th>
      <td>Credit Analyst Trainee, Business Banking - King Street, Toro...</td>
      <td>BMO Financial Group</td>
      <td>Coordinates the management of databases; ensures alignment and integration of data in adherence with data governance standards.</td>
      <td>Toronto, ON</td>
      <td>23 days ago</td>
      <td>23</td>
      <td>https://ca.indeed.com/jobs?q=Credit%20Analyst%20Trainee%2C%20Business%20Banking%20-%20King%20Street%2C%20Toro...%20BMO%20Financial%20Group</td>
    </tr>
    <tr>
      <th>53</th>
      <td>Data Processing Analyst I</td>
      <td>ERIS Environmental Risk Information Services</td>
      <td>Very good with data, numbers and patterns. Follow set instructions and run different scripts to extract data from images. Perform quality control of results.</td>
      <td>Temporarily Remote in Toronto, ON</td>
      <td>23 days ago</td>
      <td>23</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Processing%20Analyst%20I%20ERIS%20Environmental%20Risk%20Information%20Services</td>
    </tr>
    <tr>
      <th>52</th>
      <td>Junior Financial Analyst</td>
      <td>Powell Group of Companies</td>
      <td>Support the team by gathering, analyzing and interpreting financial data and information. With over 50 years experience, we are the industry leader in providing…</td>
      <td>Aurora, ON</td>
      <td>23 days ago</td>
      <td>23</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financial%20Analyst%20Powell%20Group%20of%20Companies</td>
    </tr>
    <tr>
      <th>51</th>
      <td>Data Processing Analyst I - 1 year contract (2)</td>
      <td>ERIS Info.</td>
      <td>Very good with data, numbers and patterns. Follow set instructions and run different scripts to extract data from images. Perform quality control of results.</td>
      <td>Temporarily Remote in Toronto, ON</td>
      <td>23 days ago</td>
      <td>23</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Processing%20Analyst%20I%20-%201%20year%20contract%20%282%29%20ERIS%20Info.</td>
    </tr>
    <tr>
      <th>254</th>
      <td>Manager I - RF Amplifier engineer</td>
      <td>Capgemini</td>
      <td>Designing &amp;amp; developing high-power amplifiers modules (10W to 1000W) in the 400 MHz to 4000 MHz frequency range and will support their higher-level integration…</td>
      <td>Ottawa, ON</td>
      <td>23 days ago</td>
      <td>23</td>
      <td>https://ca.indeed.com/jobs?q=Manager%20I%20-%20RF%20Amplifier%20engineer%20Capgemini</td>
    </tr>
    <tr>
      <th>253</th>
      <td>Junior Water Resources Engineer or Engineer-in-Training</td>
      <td>CBCL Limited</td>
      <td>Development of numerical models for multiple hydraulic systems including rivers, stormwater/sanitary systems, dams, wetlands, weirs and channels as well as…</td>
      <td>Hybrid remote in Halifax, NS</td>
      <td>23 days ago</td>
      <td>23</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Water%20Resources%20Engineer%20or%20Engineer-in-Training%20CBCL%20Limited</td>
    </tr>
    <tr>
      <th>255</th>
      <td>Junior Frontend Software Developer</td>
      <td>Bruker</td>
      <td>All our systems and instruments are designed to improve safety of products, accelerate time-to-market and support industries in successfully enhancing quality…</td>
      <td>Remote in Canada</td>
      <td>23 days ago</td>
      <td>23</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Frontend%20Software%20Developer%20Bruker</td>
    </tr>
    <tr>
      <th>251</th>
      <td>Software Tools Developer I</td>
      <td>BlackBerry</td>
      <td>Develop automation pipelines/frameworks to facilitate CI/CD. Develop analysis tools to analyze and interpret data. Develop and maintain automated test cases.</td>
      <td>Waterloo, ON</td>
      <td>23 days ago</td>
      <td>23</td>
      <td>https://ca.indeed.com/jobs?q=Software%20Tools%20Developer%20I%20BlackBerry</td>
    </tr>
    <tr>
      <th>252</th>
      <td>Junior Full Stack Developer - DevOps</td>
      <td>Lockheed Martin Corporation</td>
      <td>Support the Canadian Surface Combatant (CSC) Tactical Operating Environment (TOE). Act as the Subject Matter Expert (SME) for relevant system design areas.</td>
      <td>Halifax, NS</td>
      <td>23 days ago</td>
      <td>23</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20-%20DevOps%20Lockheed%20Martin%20Corporation</td>
    </tr>
    <tr>
      <th>256</th>
      <td>Junior IT Specialist</td>
      <td>Fortinet</td>
      <td>This position would represent a great fit for IT professionals with a combination of virtualization, Openstack, storage and networking experience.</td>
      <td>Burnaby, BC</td>
      <td>24 days ago</td>
      <td>24</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20IT%20Specialist%20Fortinet</td>
    </tr>
    <tr>
      <th>164</th>
      <td>Fullstack développeur Junior</td>
      <td>Fairstone</td>
      <td>La Financière Fairstone est la première institution financière dont les opérations se déroulent entièrement dans le nuage AWS.</td>
      <td>Temporarily Remote in Montréal, QC</td>
      <td>25 days ago</td>
      <td>25</td>
      <td>https://ca.indeed.com/jobs?q=Fullstack%20d%C3%A9veloppeur%20Junior%20Fairstone</td>
    </tr>
    <tr>
      <th>54</th>
      <td>Junior Data Analyst</td>
      <td>Canadian Niagara Hotels</td>
      <td>Investigate data quality issues identified by data stakeholders as well as those detected by data quality monitoring rules.</td>
      <td>Niagara Falls, ON</td>
      <td>25 days ago</td>
      <td>25</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20Canadian%20Niagara%20Hotels</td>
    </tr>
    <tr>
      <th>55</th>
      <td>Junior Developer – Test Data</td>
      <td>CGI Inc</td>
      <td>Develop, maintain knowledge of data available from upstream sources and data within various platforms. Support data profiling using TD tooling and ad hoc system…</td>
      <td>Toronto, ON</td>
      <td>25 days ago</td>
      <td>25</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Developer%20%E2%80%93%20Test%20Data%20CGI%20Inc</td>
    </tr>
    <tr>
      <th>165</th>
      <td>Junior Full Stack Developer</td>
      <td>Navitas</td>
      <td>Our ideal developer will be comfortable with both backend (primarily PHP) and frontend (JS/CSS/HTML) development, along with associated activities such as…</td>
      <td>Burnaby, BC</td>
      <td>27 days ago</td>
      <td>27</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20Navitas</td>
    </tr>
    <tr>
      <th>257</th>
      <td>DevSecOps Engineer</td>
      <td>CarbonCure Technologies</td>
      <td>We are seeking a Junior Data Science Developer to assist with the overall execution of our digital strategy to maximize usage of our full suite of CO2…</td>
      <td>Remote in Ontario</td>
      <td>27 days ago</td>
      <td>27</td>
      <td>https://ca.indeed.com/jobs?q=DevSecOps%20Engineer%20CarbonCure%20Technologies</td>
    </tr>
    <tr>
      <th>56</th>
      <td>Junior Specialist, Marketing, 12 Month Contract</td>
      <td>Abbvie</td>
      <td>Support the commercial teams with data analysis, to elevate understanding of brand performance and insights. In this exciting role, you will be responsible for…</td>
      <td>Saint-Laurent, QC</td>
      <td>28 days ago</td>
      <td>28</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Specialist%2C%20Marketing%2C%2012%20Month%20Contract%20Abbvie</td>
    </tr>
    <tr>
      <th>57</th>
      <td>Sales Operations Analyst - Mat-Leave Coverage</td>
      <td>Teranet</td>
      <td>You have at least 1 year of experience in data analysis, financial and sales reporting, and database administration an asset.</td>
      <td>Toronto, ON</td>
      <td>28 days ago</td>
      <td>28</td>
      <td>https://ca.indeed.com/jobs?q=Sales%20Operations%20Analyst%20-%20Mat-Leave%20Coverage%20Teranet</td>
    </tr>
    <tr>
      <th>58</th>
      <td>Jr. Data Analyst</td>
      <td>Blackstone Energy</td>
      <td>Familiarity with data mining techniques. Reporting to the Director of Analytics, you will collect, clean, organize and analyze data for the organization.</td>
      <td>Toronto, ON</td>
      <td>28 days ago</td>
      <td>28</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data%20Analyst%20Blackstone%20Energy</td>
    </tr>
    <tr>
      <th>166</th>
      <td>Junior DevOps Engineer</td>
      <td>Navigator Games</td>
      <td>As a Junior DevOps Engineer, your main priorities will be to work with our developers to help us build and maintain our technology stack in support of the…</td>
      <td>Remote in Vancouver, BC</td>
      <td>28 days ago</td>
      <td>28</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20DevOps%20Engineer%20Navigator%20Games</td>
    </tr>
    <tr>
      <th>258</th>
      <td>Junior Python Solution Developer for Jeppesen - a Boeing Com...</td>
      <td>Sigma Software</td>
      <td>As a Junior Software Solution Developer, you will work on our various software solutions for commercial airlines. 2+ years of working in software development.</td>
      <td>Montréal, QC</td>
      <td>28 days ago</td>
      <td>28</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Python%20Solution%20Developer%20for%20Jeppesen%20-%20a%20Boeing%20Com...%20Sigma%20Software</td>
    </tr>
    <tr>
      <th>259</th>
      <td>MRI Physicist, Junior</td>
      <td>Synaptive Medical Inc.</td>
      <td>The MRI Physicist position is an opportunity to develop applications on this novel system that leverage unique aspects of Synaptive MRI systems to address…</td>
      <td>Toronto, ON</td>
      <td>29 days ago</td>
      <td>29</td>
      <td>https://ca.indeed.com/jobs?q=MRI%20Physicist%2C%20Junior%20Synaptive%20Medical%20Inc.</td>
    </tr>
    <tr>
      <th>59</th>
      <td>Financial Analyst I</td>
      <td>University Health Network</td>
      <td>Skill in performing detailed numerical computations and accurate data entry. Hours: 37.5 hours per week. As an integral member of the Grant Operations team…</td>
      <td>Toronto, ON</td>
      <td>29 days ago</td>
      <td>29</td>
      <td>https://ca.indeed.com/jobs?q=Financial%20Analyst%20I%20University%20Health%20Network</td>
    </tr>
    <tr>
      <th>167</th>
      <td>Junior Web Developer</td>
      <td>PayShepherd</td>
      <td>Our software is a cloud-based billing validation platform that automates the previously manual onerous review of paper based vendor billing.</td>
      <td>Vancouver, BC</td>
      <td>29 days ago</td>
      <td>29</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Web%20Developer%20PayShepherd</td>
    </tr>
    <tr>
      <th>168</th>
      <td>Développeur C# junior</td>
      <td>Harris Computer Systems</td>
      <td>Hopem, une division de Harris Computer, offre un environnement dynamique et stimulant où tu pourras te démarquer et réaliser tes objectifs professionnels.</td>
      <td>Remote in Quebec City, QC</td>
      <td>29 days ago</td>
      <td>29</td>
      <td>https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20C%23%20junior%20Harris%20Computer%20Systems</td>
    </tr>
    <tr>
      <th>169</th>
      <td>Java+SQL Developer I</td>
      <td>TD Bank</td>
      <td>Transform business requirements and research into winning delivery solutions that meet performance goals. Rigorously build and test applications.</td>
      <td>London, ON</td>
      <td>29 days ago</td>
      <td>29</td>
      <td>https://ca.indeed.com/jobs?q=Java%2BSQL%20Developer%20I%20TD%20Bank</td>
    </tr>
    <tr>
      <th>170</th>
      <td>Développeur C# junior</td>
      <td>System Innovators</td>
      <td>Hopem, une division de Harris Computer, offre un environnement dynamique et stimulant où tu pourras te démarquer et réaliser tes objectifs professionnels.</td>
      <td>Remote in Quebec City, QC</td>
      <td>29 days ago</td>
      <td>29</td>
      <td>https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20C%23%20junior%20System%20Innovators</td>
    </tr>
    <tr>
      <th>60</th>
      <td>Junior Business Analyst</td>
      <td>Colas</td>
      <td>The Analyst will assist in analyzing the data and preparing summary notes and dashboards/graphs/charts that will be shared with the sales &amp;amp; operations teams.</td>
      <td>Remote in Scarborough, ON</td>
      <td>29 days ago</td>
      <td>29</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20Colas</td>
    </tr>
    <tr>
      <th>98</th>
      <td>Scientist I/II, Process Development Analytics</td>
      <td>BlueRock Therapeutics</td>
      <td>Strong practical knowledge of experimental design, and statistical analysis of data. Train and supervise junior staff members in supporting analytical…</td>
      <td>Toronto, ON</td>
      <td>30 days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Scientist%20I/II%2C%20Process%20Development%20Analytics%20BlueRock%20Therapeutics</td>
    </tr>
    <tr>
      <th>260</th>
      <td>Junior Python Solution Developer (FT)</td>
      <td>Sigma Software</td>
      <td>As a Junior Python Solution Developer, you will work on our various software solutions for commercial airlines. 2+ years of working in software development.</td>
      <td>Montréal, QC</td>
      <td>30 days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Python%20Solution%20Developer%20%28FT%29%20Sigma%20Software</td>
    </tr>
    <tr>
      <th>281</th>
      <td>Jr. NSP Software Tester</td>
      <td>NOKIA</td>
      <td>Define the test strategy, design test plans, and carry out the validation of various features, emphasizing automated tests.</td>
      <td>Hybrid remote in Ottawa, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20NSP%20Software%20Tester%20NOKIA</td>
    </tr>
    <tr>
      <th>282</th>
      <td>Software Engineering - Engineer I</td>
      <td>Live Nation</td>
      <td>The candidate would be directly involved from POC to production deployment of a set of components that are well tested, fully automated, well designed, highly…</td>
      <td>Quebec City, QC</td>
      <td>30 days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Software%20Engineering%20-%20Engineer%20I%20Live%20Nation</td>
    </tr>
    <tr>
      <th>283</th>
      <td>Junior Embedded Software Developer</td>
      <td>FLYHT</td>
      <td>Previous experience in this area is awesome but isn’t required (it’s contagious once you get here). You have appropriate technical training and previous work…</td>
      <td>Calgary, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Embedded%20Software%20Developer%20FLYHT</td>
    </tr>
    <tr>
      <th>284</th>
      <td>Junior Software Engineer</td>
      <td>Symend</td>
      <td>The Junior Software Engineer is responsible for producing and implementing functional software solutions that align with the client needs and business goals.</td>
      <td>Remote in Calgary, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Engineer%20Symend</td>
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
      <th>286</th>
      <td>Junior Cybersecurity Analyst</td>
      <td>Richter</td>
      <td>They will support the delivery and execution of white-glove cyber security services to an exclusive set of clients. Strong analytical and investigative skills.</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Cybersecurity%20Analyst%20Richter</td>
    </tr>
    <tr>
      <th>287</th>
      <td>Junior Software Developer</td>
      <td>Prolucid Technologies</td>
      <td>We encourage cross functional developers to not only learn programming languages, but also the related tools and supporting systems.</td>
      <td>Mississauga, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20Prolucid%20Technologies</td>
    </tr>
    <tr>
      <th>280</th>
      <td>Junior Systems Engineer (New Graduate)</td>
      <td>Aviya Aerospace Systems</td>
      <td>Aviya provides expertise in program management, systems, software, mechanical, and hardware engineering to many of the top-tier Aerospace and Defense…</td>
      <td>Mississauga, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Systems%20Engineer%20%28New%20Graduate%29%20Aviya%20Aerospace%20Systems</td>
    </tr>
    <tr>
      <th>288</th>
      <td>Research Associate I/II, Assay Development</td>
      <td>BlueRock Therapeutics</td>
      <td>BlueRock Therapeutics is seeking a Research Associate I/II, Assay Development in Toronto ON. The successful candidate will support the development of cell…</td>
      <td>Toronto, ON</td>
      <td>30 days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Research%20Associate%20I/II%2C%20Assay%20Development%20BlueRock%20Therapeutics</td>
    </tr>
    <tr>
      <th>290</th>
      <td>Scientifique de données junior</td>
      <td>Robert Half</td>
      <td>Notre client recherche un scientifique de données junior. 1 an d'expérience pratique avec python ou R dans un cadre d'apprentissage automatique moderne tel que…</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Scientifique%20de%20donn%C3%A9es%20junior%20Robert%20Half</td>
    </tr>
    <tr>
      <th>291</th>
      <td>Junior Software Developer</td>
      <td>S&amp;P Global</td>
      <td>Financial Risk Analytics is part of the IHS Markit group and provides industry leading risk analytics solutions to sell side institutions within the financial…</td>
      <td>Calgary, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20S%26P%20Global</td>
    </tr>
    <tr>
      <th>292</th>
      <td>Junior Aeronautical/Systems Engineer</td>
      <td>Sander Geophysics</td>
      <td>Exercise knowledge concerning the specification, design, integration, test, and certification of aeronautical systems; Generate applicable drawings and reports;</td>
      <td>Ottawa, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Aeronautical/Systems%20Engineer%20Sander%20Geophysics</td>
    </tr>
    <tr>
      <th>293</th>
      <td>Junior DevOps Engineer</td>
      <td>Global Relay</td>
      <td>As a development team member, you will be responsible for ensuring the smooth operation of production systems and development/test environments.</td>
      <td>Hybrid remote in Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20DevOps%20Engineer%20Global%20Relay</td>
    </tr>
    <tr>
      <th>294</th>
      <td>Junior Software QA Specialist (FortiOS GUI)</td>
      <td>Fortinet</td>
      <td>As a team member, you will be responsible for testing the FortiOS GUI for managing FortiGate firewall appliances. 1 - 2 years of relevant working experience.</td>
      <td>Burnaby, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20QA%20Specialist%20%28FortiOS%20GUI%29%20Fortinet</td>
    </tr>
    <tr>
      <th>295</th>
      <td>Junior Developer - Quality Assurance</td>
      <td>Fortran Traffic Systems</td>
      <td>With the arrival of transportation technologies such as CAV and Vehicle-to-Everything (V2X). The Junior Developer / QA Engineer will be entrusted to both test…</td>
      <td>Remote in Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Developer%20-%20Quality%20Assurance%20Fortran%20Traffic%20Systems</td>
    </tr>
    <tr>
      <th>296</th>
      <td>Junior Software Control Engineer</td>
      <td>SNC-Lavalin</td>
      <td>Candu Energy Inc. is a leading full-service nuclear technology company and committed to design and deliver state-of-the-art CANDU® reactors, carry out life…</td>
      <td>Courtice, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Control%20Engineer%20SNC-Lavalin</td>
    </tr>
    <tr>
      <th>289</th>
      <td>Junior Electrical Engineer</td>
      <td>BBA</td>
      <td>Work collaboratively with clients, project managers, engineers, designers and drafters in the preparation of deliverables to BBA and client standards.</td>
      <td>Trail, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Electrical%20Engineer%20BBA</td>
    </tr>
    <tr>
      <th>216</th>
      <td>Junior Developer/Programmer</td>
      <td>SimplyCast</td>
      <td>Maintain software design consistency, aesthetics, and functionality of web application pages, communications systems, and data processing.</td>
      <td>Remote in Dartmouth, NS</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Developer/Programmer%20SimplyCast</td>
    </tr>
    <tr>
      <th>279</th>
      <td>Consultant I</td>
      <td>f5</td>
      <td>You can help our best in-class customers improve application delivery, access, security, and data management for their infrastructure.</td>
      <td>Hybrid remote in Canada</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Consultant%20I%20f5</td>
    </tr>
    <tr>
      <th>277</th>
      <td>Full Stack Engineer (Junior)</td>
      <td>Sangoma</td>
      <td>At least 1 years of experience python TurboGears framework and celery library. As a FullStack Engineer, you will be responsible for implementing real-time and…</td>
      <td>Markham, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Full%20Stack%20Engineer%20%28Junior%29%20Sangoma</td>
    </tr>
    <tr>
      <th>261</th>
      <td>Junior Developer</td>
      <td>Vaco Lannick</td>
      <td>This role will mostly work with C# and VB. NET on backend applications and APIs (REST), MySQL and some Python, AWS. NET backend development - C# and VB.NET.</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Developer%20Vaco%20Lannick</td>
    </tr>
    <tr>
      <th>262</th>
      <td>Développeur(se) de logiciels junior</td>
      <td>French Canadian Instance</td>
      <td>Maritime International, une division de L3Harris, est un fournisseur mondial de premier plan de contrôles-commandes non ITAR et de solutions de simulation pour…</td>
      <td>Ottawa, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%28se%29%20de%20logiciels%20junior%20French%20Canadian%20Instance</td>
    </tr>
    <tr>
      <th>263</th>
      <td>Junior Software Engineer - Cloud Networking QA (Vancouver, B...</td>
      <td>Aviatrix</td>
      <td>ABOUT THE ROLE: Member of Technical Staff – QA (Full Time). We're looking for ideas and skills from every area of computer science, networking, security, large…</td>
      <td>Vancouver, BC</td>
      <td>30 days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Engineer%20-%20Cloud%20Networking%20QA%20%28Vancouver%2C%20B...%20Aviatrix</td>
    </tr>
    <tr>
      <th>264</th>
      <td>Junior Pipeline TD/ Software Engineer</td>
      <td>Stellar Creative Lab</td>
      <td>Stellar Creative Lab is hiring a Junior Pipeline TD, who can bring his or her talent and brains to the design and development of a facility-wide CG-Animation…</td>
      <td>&lt;span&gt;Temporarily Remote&lt;/span&gt;</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Pipeline%20TD/%20Software%20Engineer%20Stellar%20Creative%20Lab</td>
    </tr>
    <tr>
      <th>265</th>
      <td>Junior Web Developer</td>
      <td>Scribendi</td>
      <td>You will work with cutting-edge technologies, learn how they are applied in the ecommerce sector, and collaborate extensively with stakeholders and the…</td>
      <td>Chatham-Kent, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Web%20Developer%20Scribendi</td>
    </tr>
    <tr>
      <th>266</th>
      <td>Junior Transportation Engineer/Planner (EIT)</td>
      <td>Wood Plc</td>
      <td>Wood’s Infrastructure Planning Solutions group is seeking a highly motivated Junior Traffic Engineer/Planner (EIT) for either our Burlington, ON or Richmond…</td>
      <td>Remote in Burlington, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Transportation%20Engineer/Planner%20%28EIT%29%20Wood%20Plc</td>
    </tr>
    <tr>
      <th>267</th>
      <td>System Integration Engineer, Junior/Intermediate</td>
      <td>General Dynamics Missions Systems-Canada</td>
      <td>This role will be working on the Land Command Support System (LCSS) which primarily supports the Canadian Army operations by providing the information services…</td>
      <td>Ottawa, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=System%20Integration%20Engineer%2C%20Junior/Intermediate%20General%20Dynamics%20Missions%20Systems-Canada</td>
    </tr>
    <tr>
      <th>278</th>
      <td>Jr. / Int. Software Engineering (12mo fixed term)</td>
      <td>Magellan Aerospace</td>
      <td>Magellan Aerospace, Winnipeg is looking for a high performing Entry Level (or Intermediate) Software Engineering/Developer to join our development team.</td>
      <td>Winnipeg, MB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20/%20Int.%20Software%20Engineering%20%2812mo%20fixed%20term%29%20Magellan%20Aerospace</td>
    </tr>
    <tr>
      <th>268</th>
      <td>AV Systems Engineer/Junior Crestron Programmer</td>
      <td>TMX Group Limited</td>
      <td>Creating and adjusting Biamp Audio DSP systems, as well as modifying Shure MXA910/410 microphone configurations should be something firmly in your wheelhouse.</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=AV%20Systems%20Engineer/Junior%20Crestron%20Programmer%20TMX%20Group%20Limited</td>
    </tr>
    <tr>
      <th>270</th>
      <td>Junior Python Developer</td>
      <td>ReDefine</td>
      <td>As an Juniour Python Developer (internally called ATD) you will perform a variety of tasks to assist the Pipeline Technical Directors (Pipeline TDs) to ensure…</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Python%20Developer%20ReDefine</td>
    </tr>
    <tr>
      <th>271</th>
      <td>SCIENTIFIQUE JUNIOR – TRAITEMENT AUTOMATIQUE DU LANGAGE NATU...</td>
      <td>Centre de recherche informatique de Montréal...</td>
      <td>Pour réussir à ce poste, le candidat retenu devra combiner des passions pour la linguistique, l’informatique ainsi que pour l’apprentissage automatique.</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=SCIENTIFIQUE%20JUNIOR%20%E2%80%93%20TRAITEMENT%20AUTOMATIQUE%20DU%20LANGAGE%20NATU...%20Centre%20de%20recherche%20informatique%20de%20Montr%C3%A9al...</td>
    </tr>
    <tr>
      <th>272</th>
      <td>Ingénieur(e) junior en mécanique des roches</td>
      <td>Golder Associates</td>
      <td>Réduire les données et analyser des données d’enquête; Préparer et utiliser des modèles 2D et 3D; Participer à la caractérisation géotechnique et aux…</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Ing%C3%A9nieur%28e%29%20junior%20en%20m%C3%A9canique%20des%20roches%20Golder%20Associates</td>
    </tr>
    <tr>
      <th>273</th>
      <td>QA Analyst</td>
      <td>SHIPTRACK INC.</td>
      <td>Analyze, document, and prioritize bug reports. Define, implement, and maintain a testing suite. Create and document test scenarios.</td>
      <td>Plantagenet, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=QA%20Analyst%20SHIPTRACK%20INC.</td>
    </tr>
    <tr>
      <th>274</th>
      <td>Developer Advocate - Remote (Canada)</td>
      <td>Vonage</td>
      <td>As businesses continue to shift to a real-time, customer-centric communications model, we are experiencing a time of impressive growth.</td>
      <td>Remote in Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Developer%20Advocate%20-%20Remote%20%28Canada%29%20Vonage</td>
    </tr>
    <tr>
      <th>275</th>
      <td>Junior Python Developer</td>
      <td>DNEG</td>
      <td>Production Technology is an umbrella term used to describe the group of people supporting, developing and improving the tools and technologies that artists use…</td>
      <td>Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Python%20Developer%20DNEG</td>
    </tr>
    <tr>
      <th>276</th>
      <td>Design Specialist I</td>
      <td>TELUS</td>
      <td>Understanding and gathering RF engineering requirements and providing data analytics, web applications and scripting tools to help the Engineers in their day to…</td>
      <td>Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Design%20Specialist%20I%20TELUS</td>
    </tr>
    <tr>
      <th>269</th>
      <td>Junior Actuarial Associate - Corporate Actuarial</td>
      <td>SCOR</td>
      <td>This position is part of the Canadian Corporate Actuarial Team, which is responsible for actuarial activities associated with SCORâ€™s Canada Life &amp;amp; Health…</td>
      <td>Canada</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Actuarial%20Associate%20-%20Corporate%20Actuarial%20SCOR</td>
    </tr>
    <tr>
      <th>215</th>
      <td>Junior/Intermediate Ruby on Rails Developer</td>
      <td>ZayZoon</td>
      <td>You will work on customer- and admin-facing products, third party integrations both canned and bespoke, and help architect the system toward greater flexibility…</td>
      <td>&lt;span&gt;Remote&lt;/span&gt;</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior/Intermediate%20Ruby%20on%20Rails%20Developer%20ZayZoon</td>
    </tr>
    <tr>
      <th>202</th>
      <td>Junior Research Consultant</td>
      <td>Arksum Results</td>
      <td>As this role is within the marketing and communications team, the ideal candidate for this position will have excellent writing skills, with a keen interest in…</td>
      <td>Etobicoke, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Research%20Consultant%20Arksum%20Results</td>
    </tr>
    <tr>
      <th>213</th>
      <td>Junior Developer</td>
      <td>University of Alberta Students' Union</td>
      <td>As part of an information technology team, the Junior Developer creates efficient and effective technology based solutions to meet the operational needs of…</td>
      <td>Edmonton, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Developer%20University%20of%20Alberta%20Students%27%20Union</td>
    </tr>
    <tr>
      <th>76</th>
      <td>Associate Product Manager, Data</td>
      <td>Lightspeed Commerce</td>
      <td>Collaborate with stakeholders to define their big data needs for the business. You will help define and execute the vision for Big Data at Lightspeed.</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Associate%20Product%20Manager%2C%20Data%20Lightspeed%20Commerce</td>
    </tr>
    <tr>
      <th>75</th>
      <td>Junior Pricing Analyst</td>
      <td>Bélanger UPT</td>
      <td>Collects data and maintains the database. Prepares financial and sku analysis reports, analyses margins and competitive market data.</td>
      <td>Mississauga, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Pricing%20Analyst%20B%C3%A9langer%20UPT</td>
    </tr>
    <tr>
      <th>74</th>
      <td>Junior Sales Data Coordinator</td>
      <td>Bélanger UPT</td>
      <td>Reporting to the National Sales &amp;amp; Marketing Director, the Junior Sales Data Coordinator will be internal link between the pricing analyst and inside sales.</td>
      <td>Mississauga, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Sales%20Data%20Coordinator%20B%C3%A9langer%20UPT</td>
    </tr>
    <tr>
      <th>73</th>
      <td>Junior Online Marketing Analyst</td>
      <td>Core Online Marketing</td>
      <td>Analytical Skills to interpret data and present recommendations. Ensure data from all sources is accurate and being captured appropriately.</td>
      <td>Oakville, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Online%20Marketing%20Analyst%20Core%20Online%20Marketing</td>
    </tr>
    <tr>
      <th>72</th>
      <td>Software Engineer, Junior - Principal (Web/Data Back-End)-Re...</td>
      <td>Arista Networks</td>
      <td>Mentor new and junior engineers to bring them up to speed in Arista's software development environment. Experience with network monitoring, network protocols,…</td>
      <td>Remote in Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Software%20Engineer%2C%20Junior%20-%20Principal%20%28Web/Data%20Back-End%29-Re...%20Arista%20Networks</td>
    </tr>
    <tr>
      <th>71</th>
      <td>Junior Analyst, Indirect Tax</td>
      <td>KPMG</td>
      <td>Work with advanced information technology for electronic data query and analysis. Perform In-depth data analysis to identify areas of risk, opportunities and…</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Analyst%2C%20Indirect%20Tax%20KPMG</td>
    </tr>
    <tr>
      <th>70</th>
      <td>Junior Marketing Specialist</td>
      <td>Contractor Compliance</td>
      <td>Monitor top of funnel channels and evaluate data, create reports and keep track of key metrics in order to monitor campaign efficiency and analyze trends with…</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Marketing%20Specialist%20Contractor%20Compliance</td>
    </tr>
    <tr>
      <th>69</th>
      <td>Data Steward I</td>
      <td>TD Bank</td>
      <td>Complete metadata and data quality tasks. Identify and monitor the quality of critical data elements. Manage data work activities requiring coordination across…</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Steward%20I%20TD%20Bank</td>
    </tr>
    <tr>
      <th>68</th>
      <td>Junior Settlement / Financial / Risk Analyst</td>
      <td>Dynasty Power Inc.</td>
      <td>Programming and data science skills are a definite plus. Dynasty Power is currently looking to hire a Junior Settlement / Financial / Risk Analyst.</td>
      <td>Calgary, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Settlement%20/%20Financial%20/%20Risk%20Analyst%20Dynasty%20Power%20Inc.</td>
    </tr>
    <tr>
      <th>67</th>
      <td>Clinical Data Manager I - REMOTE</td>
      <td>Precision for Medicine</td>
      <td>Actively cleaning data, managing CRF and query trends and data reporting to ensure a clean database lock ready for analysis.</td>
      <td>Remote in Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Clinical%20Data%20Manager%20I%20-%20REMOTE%20Precision%20for%20Medicine</td>
    </tr>
    <tr>
      <th>66</th>
      <td>Junior Power Analyst</td>
      <td>Dynasty Power Inc.</td>
      <td>Analyze data to look for profitable trading strategies. Passion for trading, financial derivatives and financial data analysis considered an asset.</td>
      <td>Calgary, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Power%20Analyst%20Dynasty%20Power%20Inc.</td>
    </tr>
    <tr>
      <th>65</th>
      <td>Jr. Data Scientist</td>
      <td>SimpTek Technologies</td>
      <td>Integration with 3rd party API’s for data collection and analysis, including weather data, time-series data, and event-based data sets.</td>
      <td>Fredericton, NB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data%20Scientist%20SimpTek%20Technologies</td>
    </tr>
    <tr>
      <th>64</th>
      <td>Business Intelligence Analyst I</td>
      <td>Finning International Inc.</td>
      <td>Basic ability to mine data, profile data and derive business solutions using data. Critically evaluate information gathered from multiple data sources and…</td>
      <td>Edmonton, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Business%20Intelligence%20Analyst%20I%20Finning%20International%20Inc.</td>
    </tr>
    <tr>
      <th>63</th>
      <td>Commercial Financial Analyst I</td>
      <td>Thermo Fisher Scientific</td>
      <td>Data management experience and the ability to manage large sets of data and accurate reports. As part of the commercial finance organization, your position will…</td>
      <td>Ottawa, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Commercial%20Financial%20Analyst%20I%20Thermo%20Fisher%20Scientific</td>
    </tr>
    <tr>
      <th>62</th>
      <td>Développeur BI junior | Junior Business Intelligence Develop...</td>
      <td>Delmar International Inc.</td>
      <td>Participating to data quality checks. Developing data models, working conjointly with senior developers. 1 to 3 years' experience in data analysis developing…</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20BI%20junior%20%7C%20Junior%20Business%20Intelligence%20Develop...%20Delmar%20International%20Inc.</td>
    </tr>
    <tr>
      <th>61</th>
      <td>Software Engineer, Junior - Principal (Web/Data Frontend)-Re...</td>
      <td>Arista Networks</td>
      <td>Experience with UI/UX design, network monitoring, data visualization, or data analytics is a plus. Mentor new and junior engineers to bring them up to speed in…</td>
      <td>Remote in Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Software%20Engineer%2C%20Junior%20-%20Principal%20%28Web/Data%20Frontend%29-Re...%20Arista%20Networks</td>
    </tr>
    <tr>
      <th>297</th>
      <td>Junior Firmware Engineer</td>
      <td>Corinex Communications</td>
      <td>Participate in the development of next-generation smart grid communication devices and equipment. Involve in system design discussions and provide comprehensive…</td>
      <td>Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Firmware%20Engineer%20Corinex%20Communications</td>
    </tr>
    <tr>
      <th>77</th>
      <td>Quality Assurance Specialist (Backend/Data) - Junior/Interme...</td>
      <td>Klick Health</td>
      <td>Perform data analysis using SQL to ensure data quality and quality of programs. Practical experience with manipulating test data &amp;amp; its validation techniques.</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Quality%20Assurance%20Specialist%20%28Backend/Data%29%20-%20Junior/Interme...%20Klick%20Health</td>
    </tr>
    <tr>
      <th>171</th>
      <td>Junior Software Quality Assurance Specialist</td>
      <td>Piicomm Inc.</td>
      <td>Review development specifications, technical documentations, and user stories to build and execute appropriate test plans. Job Type: Full-time, Permanent.</td>
      <td>Plantagenet, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Quality%20Assurance%20Specialist%20Piicomm%20Inc.</td>
    </tr>
    <tr>
      <th>78</th>
      <td>Junior Data Engineer</td>
      <td>Altus Group</td>
      <td>You will contribute to the integration of new data, the improvement of existing data, and the integration of machine learning and data science efforts.</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Engineer%20Altus%20Group</td>
    </tr>
    <tr>
      <th>80</th>
      <td>Junior Data Scientist</td>
      <td>Providence Health Care</td>
      <td>Reviews clinical data at aggregate levels on a regular basis using analytical reporting tools to support the identification of risks and data patterns or trends…</td>
      <td>Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Scientist%20Providence%20Health%20Care</td>
    </tr>
    <tr>
      <th>97</th>
      <td>Junior Financial Analyst (Business Case)</td>
      <td>Questrade Financial Group</td>
      <td>Support the Finance team in producing meaningful data/analysis. Perform reconciliation processes for various reports and systems to ensure data integrity.</td>
      <td>Remote in Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financial%20Analyst%20%28Business%20Case%29%20Questrade%20Financial%20Group</td>
    </tr>
    <tr>
      <th>96</th>
      <td>Jr. Business Intelligence Developer, Enterprise Analytics</td>
      <td>Southlake Regional Health Centre</td>
      <td>Develop ETL procedures, SSIS packages and maintain data flow processes. Advanced understanding of data warehousing concepts and best practices required.</td>
      <td>Newmarket, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Business%20Intelligence%20Developer%2C%20Enterprise%20Analytics%20Southlake%20Regional%20Health%20Centre</td>
    </tr>
    <tr>
      <th>95</th>
      <td>Jr. Email Marketing Implementation Specialist at Digital Age...</td>
      <td>Arctic Leaf Inc.</td>
      <td>Measure campaign results and optimize based on data. Analyzing campaign and email performance data to develop insights and make recommendations on areas for…</td>
      <td>&lt;span&gt;Remote&lt;/span&gt;</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Email%20Marketing%20Implementation%20Specialist%20at%20Digital%20Age...%20Arctic%20Leaf%20Inc.</td>
    </tr>
    <tr>
      <th>94</th>
      <td>Graduate Trainee Assistant Analyst - GTA</td>
      <td>Kinectrics</td>
      <td>Ability to utilize computer software programs for data management, such as Microsoft Excel. Work independently and as a part of engineering and technical teams…</td>
      <td>Greater Toronto Area, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Graduate%20Trainee%20Assistant%20Analyst%20-%20GTA%20Kinectrics</td>
    </tr>
    <tr>
      <th>93</th>
      <td>Junior Asset Management Consultant and Data Analyst</td>
      <td>GM BluePlan Engineering</td>
      <td>Develop and analyze asset data to support asset management planning. Create and manage asset inventories and data structures, including the development of…</td>
      <td>Vaughan, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Asset%20Management%20Consultant%20and%20Data%20Analyst%20GM%20BluePlan%20Engineering</td>
    </tr>
    <tr>
      <th>92</th>
      <td>Jr. Data/Reporting Analyst</td>
      <td>Scarsin</td>
      <td>Data management, data analysis and ETL process skills and concepts including data modeling and transformations. Create / maintain all Production Documentation.</td>
      <td>Markham, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Data/Reporting%20Analyst%20Scarsin</td>
    </tr>
    <tr>
      <th>91</th>
      <td>Junior Data Integration Engineer</td>
      <td>Mogo</td>
      <td>Ensure integrity of all data sources. Experience building ETLs, working with data integration tools. Using data collected from multiple sources, you will…</td>
      <td>Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Integration%20Engineer%20Mogo</td>
    </tr>
    <tr>
      <th>90</th>
      <td>Junior Business Analyst</td>
      <td>Pivotree</td>
      <td>Roles &amp;amp; Responsibilities: • Elicits and documents requirements using a variety of methods, such as interviews, document analysis, requirements workshops,…</td>
      <td>Remote in Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20Pivotree</td>
    </tr>
    <tr>
      <th>89</th>
      <td>Junior Financial Analyst</td>
      <td>Questrade Financial Group</td>
      <td>Support the Finance team in producing meaningful data/analysis. Perform reconciliation processes for various reports and systems to ensure data integrity.</td>
      <td>Remote in Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financial%20Analyst%20Questrade%20Financial%20Group</td>
    </tr>
    <tr>
      <th>88</th>
      <td>Junior Pavement Data Analyst</td>
      <td>Stantec</td>
      <td>The Junior Technician will reside within the IMPE Data Analytics Group (DAG), which is responsible for managing field data acquisition, data quality control and…</td>
      <td>Waterloo, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Pavement%20Data%20Analyst%20Stantec</td>
    </tr>
    <tr>
      <th>87</th>
      <td>Junior Data Engineer</td>
      <td>Sobeys</td>
      <td>In this exciting role, you will help design and build the data platforms needed for optimal data usage and results. Career Group: Corporate Office Careers.</td>
      <td>Hybrid remote in Mississauga, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Engineer%20Sobeys</td>
    </tr>
    <tr>
      <th>86</th>
      <td>Junior Data Integration Engineer</td>
      <td>Mogo Finance Technology Inc.</td>
      <td>Ensure integrity of all data sources. Experience building ETLs, working with data integration tools. Using data collected from multiple sources, you will…</td>
      <td>Remote in Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Integration%20Engineer%20Mogo%20Finance%20Technology%20Inc.</td>
    </tr>
    <tr>
      <th>85</th>
      <td>Field Data Scientist I / Junior Field Data Scientist</td>
      <td>ThinkData Works</td>
      <td>Conducting research to identify data sources and data products for specific client requirements. Design and build data products. What You’ll be Doing.</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Field%20Data%20Scientist%20I%20/%20Junior%20Field%20Data%20Scientist%20ThinkData%20Works</td>
    </tr>
    <tr>
      <th>84</th>
      <td>FL Junior Data Analyst</td>
      <td>Fujitsu</td>
      <td>Perform data integrity and quality checks. Experience with data repositories and advance Excel skills. Junior/Intermediate Data Analyst requirement for minimum…</td>
      <td>Vancouver, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=FL%20Junior%20Data%20Analyst%20Fujitsu</td>
    </tr>
    <tr>
      <th>83</th>
      <td>Junior Business Analyst (remote)</td>
      <td>Software International</td>
      <td>Analyzes and evaluates complex data processing systems both current and proposed, translating business area customer information systems requirements into…</td>
      <td>Remote in Mississauga, ON</td>
      <td>30 days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20%28remote%29%20Software%20International</td>
    </tr>
    <tr>
      <th>82</th>
      <td>Junior Data Analyst</td>
      <td>Blend HRM Internal</td>
      <td>Able to analyze data and interpret the results. Assist in enforcing proper data collection in team engagement trackers. Create, update and maintain trackers.</td>
      <td>Remote in Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20Blend%20HRM%20Internal</td>
    </tr>
    <tr>
      <th>81</th>
      <td>Junior Financial Analyst</td>
      <td>MindGeek Careers</td>
      <td>Collecting data and applying analytical techniques to generate statistics for our websites. Analyzing transaction data and preparing entries/reports for…</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Financial%20Analyst%20MindGeek%20Careers</td>
    </tr>
    <tr>
      <th>79</th>
      <td>Analyst I, Security Advisory and Data Security</td>
      <td>Moneris Solutions</td>
      <td>Knowledge of data classification and data loss prevention principles. Support the provision of data protection subject matter advice related to Moneris' data…</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Analyst%20I%2C%20Security%20Advisory%20and%20Data%20Security%20Moneris%20Solutions</td>
    </tr>
    <tr>
      <th>214</th>
      <td>Junior Software Developer (Open to Remote)</td>
      <td>S&amp;P Global</td>
      <td>We need software developers who can help us develop and maintain systems that are always online and can handle hundreds of thousands of transactions per second.</td>
      <td>Remote in London, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20%28Open%20to%20Remote%29%20S%26P%20Global</td>
    </tr>
    <tr>
      <th>172</th>
      <td>Junior Guidewire Developer</td>
      <td>Ouest</td>
      <td>As a Business Technology Analyst, in Insurance Core Technology group within our Consulting Practice, you'll work within an engagement team and be responsible…</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Guidewire%20Developer%20Ouest</td>
    </tr>
    <tr>
      <th>174</th>
      <td>Junior Devops Engineer</td>
      <td>Scribendi</td>
      <td>This role is for a fearless self-starter with good communication skills, a strong work ethic, and the ability to participate in all aspects of the software…</td>
      <td>Chatham-Kent, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Devops%20Engineer%20Scribendi</td>
    </tr>
    <tr>
      <th>196</th>
      <td>Junior PHP Developer</td>
      <td>Visual Knowledge Share Ltd</td>
      <td>Position: Part-time or permanent. Work schedule: Part-time position is 20 hours a week, permanent position is 40 hours/week, flexible.</td>
      <td>Remote in Châteauguay, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20PHP%20Developer%20Visual%20Knowledge%20Share%20Ltd</td>
    </tr>
    <tr>
      <th>197</th>
      <td>Junior Software Developer - Microsoft Dynamics F&amp;O Consultin...</td>
      <td>BDO</td>
      <td>BDO is looking for a full-time permanent Junior Software Developer to join our client-facing Microsoft Dynamics 365 for Finance and Operations Consulting…</td>
      <td>Remote in Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20-%20Microsoft%20Dynamics%20F%26O%20Consultin...%20BDO</td>
    </tr>
    <tr>
      <th>198</th>
      <td>Junior Full Stack Developer</td>
      <td>Visual Knowledge Share Ltd</td>
      <td>Visual Knowledge Share Ltd (VKS, vksapp.com) is looking for a talented, passionate, roll-up-your-sleeves, hands-on Junior Full Stack Developer.</td>
      <td>Remote in Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20Visual%20Knowledge%20Share%20Ltd</td>
    </tr>
    <tr>
      <th>199</th>
      <td>Junior Developer</td>
      <td>E-By Design</td>
      <td>We are seeking an entry-level . NET developer responsible for building . NET applications using C#, SQL, and SSRS. Skill for writing reusable libraries.</td>
      <td>Alberta</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Developer%20E-By%20Design</td>
    </tr>
    <tr>
      <th>200</th>
      <td>Junior Java Developer [#3867]</td>
      <td>Alteo</td>
      <td>Alteo est à la recherche d'un Développeur Java junior pour un poste permanent basé à Québec. Design and develop React component.</td>
      <td>Hybrid remote in Quebec City, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Java%20Developer%20%5B%233867%5D%20Alteo</td>
    </tr>
    <tr>
      <th>201</th>
      <td>Reporting Analyst I (Canada Remote)</td>
      <td>Fullscript</td>
      <td>The Reporting team is a core function of the Fullscript Data team, responsible for helping our team understand performance and drive effective planning and…</td>
      <td>Remote in Ottawa, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Reporting%20Analyst%20I%20%28Canada%20Remote%29%20Fullscript</td>
    </tr>
    <tr>
      <th>99</th>
      <td>Jr. Quality Assurance Analyst (Manufacturing)</td>
      <td>MDA</td>
      <td>Implementing approved sampling, reporting and data analysis as required. Assist in developing, maintaining, and evaluating the company Quality system meeting…</td>
      <td>Kanata, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Quality%20Assurance%20Analyst%20%28Manufacturing%29%20MDA</td>
    </tr>
    <tr>
      <th>203</th>
      <td>Junior C++ Software Developer</td>
      <td>S&amp;P Global</td>
      <td>We need software engineers who can help us develop and maintain systems that are always online and can handle hundreds of thousands of transactions per second.</td>
      <td>Remote in London, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20C%2B%2B%20Software%20Developer%20S%26P%20Global</td>
    </tr>
    <tr>
      <th>204</th>
      <td>Junior Software Engineer</td>
      <td>Optima Tele.com, Inc.</td>
      <td>Engineering focus areas for this position include wireless gateways, LAN/WAN switches, IoT nodes, interface units and sensors.</td>
      <td>Remote in Markham, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Engineer%20Optima%20Tele.com%2C%20Inc.</td>
    </tr>
    <tr>
      <th>205</th>
      <td>Junior Software Developer</td>
      <td>Bioinformatics Solutions</td>
      <td>Work closely with other developers in an agile and collaborative environment to foster continuous improvement at the team and company level.</td>
      <td>Waterloo, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20Bioinformatics%20Solutions</td>
    </tr>
    <tr>
      <th>206</th>
      <td>Développeur junior, OutilsDev (C# et Jenkins)</td>
      <td>GIRO</td>
      <td>L'équipe Outils est responsable d’optimiser le pipeline de livraison de fonctionnalités et de technologies à nos clients à travers la conception et le…</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20junior%2C%20OutilsDev%20%28C%23%20et%20Jenkins%29%20GIRO</td>
    </tr>
    <tr>
      <th>207</th>
      <td>Développeur PHP junior</td>
      <td>Serti Informatique</td>
      <td>Créer et entretenir du code propre, efficace, sécure, et bien architecturé qui se conforme aux normes établies; Expérience à utiliser des APIs;</td>
      <td>Canal de la Rive Sud, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20PHP%20junior%20Serti%20Informatique</td>
    </tr>
    <tr>
      <th>208</th>
      <td>Junior Drupal Developer (Remote Friendly)</td>
      <td>Acro Media</td>
      <td>Acro Media is looking for a Drupal Software Developer to develop Drupal 8 and Commerce builds. If you’re desperate to break free from that office life where you…</td>
      <td>Remote in Kelowna, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Drupal%20Developer%20%28Remote%20Friendly%29%20Acro%20Media</td>
    </tr>
    <tr>
      <th>209</th>
      <td>Junior Full Stack Developer</td>
      <td>Markdale Financial Management</td>
      <td>Markdale Financial Management is looking for a part-time Junior Full Stack Web Developer to join our team. Currently an undergrad in Computer Science.</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20Markdale%20Financial%20Management</td>
    </tr>
    <tr>
      <th>210</th>
      <td>Junior Developer</td>
      <td>Coconut Software</td>
      <td>In this role, you will work on a platform that facilitates connections between businesses and their customers, through a combination of appointments, lobby…</td>
      <td>Canada</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Developer%20Coconut%20Software</td>
    </tr>
    <tr>
      <th>211</th>
      <td>Analyste d'affaires, junior</td>
      <td>Caisse de dépôt et placement du Québec</td>
      <td>/ Carry out projects with potential returns and economic benefits for Quebecers. / Collaborate on dynamic teams with high-level professionals committed to…</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Analyste%20d%27affaires%2C%20junior%20Caisse%20de%20d%C3%A9p%C3%B4t%20et%20placement%20du%20Qu%C3%A9bec</td>
    </tr>
    <tr>
      <th>212</th>
      <td>Jr. Software Engineer - Lighthouse</td>
      <td>KPMG</td>
      <td>Work closely with clients to understand key business issues. Gather and analyze requirements to develop impactful recommendations and solutions.</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20Software%20Engineer%20-%20Lighthouse%20KPMG</td>
    </tr>
    <tr>
      <th>195</th>
      <td>Junior Web Developer</td>
      <td>Outshinery Creative</td>
      <td>You will work closely with our CTO on various projects, ranging from prototyping, developing and testing new product &amp;amp; service ideas to updates and changes to…</td>
      <td>&lt;span&gt;Remote&lt;/span&gt;</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Web%20Developer%20Outshinery%20Creative</td>
    </tr>
    <tr>
      <th>173</th>
      <td>Stage étudiant - Développeur Junior</td>
      <td>Jovaco</td>
      <td>Travailler avec des bases de données SQL Server.</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Stage%20%C3%A9tudiant%20-%20D%C3%A9veloppeur%20Junior%20Jovaco</td>
    </tr>
    <tr>
      <th>194</th>
      <td>Junior Trader</td>
      <td>Questrade Financial Group</td>
      <td>And we swear by that every single day. They efficiently and accurately process client trade requests according to the directions received from clients.</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Trader%20Questrade%20Financial%20Group</td>
    </tr>
    <tr>
      <th>192</th>
      <td>Junior Programmer Analyst</td>
      <td>Advanis</td>
      <td>Successful businesses understand their customers and their competitors. World, as well as to all levels of government (from federal to municipal in Canada).</td>
      <td>Edmonton, AB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Programmer%20Analyst%20Advanis</td>
    </tr>
    <tr>
      <th>175</th>
      <td>Junior Web Designer/Developer</td>
      <td>Search Gurus Inc</td>
      <td>2 Years experience required, portfolio required Qualifications: HTML5 HTML CSS Bootstrap 3+ Framework PHP MySQL JavaScript FTP Secure Shell Photoshop…</td>
      <td>Mississauga, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Web%20Designer/Developer%20Search%20Gurus%20Inc</td>
    </tr>
    <tr>
      <th>176</th>
      <td>Software Developer (Junior)</td>
      <td>STEP Software</td>
      <td>NET), C/C++, Python, Java, Swift, Objective C, PHP &amp;amp; Delphi on Windows, Linux, Mac, iPhone, Android and Embedded Devices.</td>
      <td>London, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Software%20Developer%20%28Junior%29%20STEP%20Software</td>
    </tr>
    <tr>
      <th>177</th>
      <td>Ingénieur logiciel junior</td>
      <td>Robert Half</td>
      <td>Aujourd'hui, leur empreinte mondiale englobe plus de 260 sites dans le monde. Relevant du responsable informatique des applications, l'ingénieur logiciel senior…</td>
      <td>Saint-Laurent, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Ing%C3%A9nieur%20logiciel%20junior%20Robert%20Half</td>
    </tr>
    <tr>
      <th>178</th>
      <td>Développeur(se) Junior, Intelligence d'affaires</td>
      <td>Caisse de dépôt et placement du Québec</td>
      <td>/ Carry out projects with potential returns and economic benefits for Quebecers. / Collaborate on dynamic teams with high-level professionals committed to…</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%28se%29%20Junior%2C%20Intelligence%20d%27affaires%20Caisse%20de%20d%C3%A9p%C3%B4t%20et%20placement%20du%20Qu%C3%A9bec</td>
    </tr>
    <tr>
      <th>179</th>
      <td>Junior Environmental Technical Administrator</td>
      <td>Parsons</td>
      <td>Contaminated Land Assessments and Management Programs (Phase I and II ESAs, Remediations, Risk Assessments),. Field work may involve travel (sometimes to remote…</td>
      <td>Oakville, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Environmental%20Technical%20Administrator%20Parsons</td>
    </tr>
    <tr>
      <th>180</th>
      <td>Jr .Net</td>
      <td>Virtusa</td>
      <td>Strong on SQL server programming. T4 hire with option to train can be considered. 1 to 2 years of experience. Strong on SQL server programming.</td>
      <td>Halifax, NS</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Jr%20.Net%20Virtusa</td>
    </tr>
    <tr>
      <th>181</th>
      <td>Junior Systems Administrator Fulltime- Permanent</td>
      <td>ProServeIT</td>
      <td>Moreover, this Junior Systems Administrator role will have elevated access within client environments, therefore, the added responsibility of ensuring the…</td>
      <td>Mississauga, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Systems%20Administrator%20Fulltime-%20Permanent%20ProServeIT</td>
    </tr>
    <tr>
      <th>182</th>
      <td>Junior Water Resources Engineer</td>
      <td>Kerr Wood Leidal</td>
      <td>Design of engineering infrastructure including, but not limited to, dikes, fish habitat enhancement, dams, intakes, and hazard mitigation structures.</td>
      <td>Burnaby, BC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Water%20Resources%20Engineer%20Kerr%20Wood%20Leidal</td>
    </tr>
    <tr>
      <th>183</th>
      <td>Conversion Analyst I</td>
      <td>Vertafore</td>
      <td>Vertafore Canada is looking for a Conversion Analyst who is passionate about meeting customer needs and has Insurance industry experience.</td>
      <td>Remote in Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Conversion%20Analyst%20I%20Vertafore</td>
    </tr>
    <tr>
      <th>184</th>
      <td>Junior Full Stack Developer</td>
      <td>Prolucid Technologies</td>
      <td>We deliver solutions to customers in markets ranging from Medical Devices, Aerospace &amp;amp; Defence, Nuclear &amp;amp; Energy, Transportation, and Advanced Manufacturing.</td>
      <td>Mississauga, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20Prolucid%20Technologies</td>
    </tr>
    <tr>
      <th>185</th>
      <td>Junior Business Systems Analyst</td>
      <td>Robert Half</td>
      <td>The ideal candidate will consider themselves a problem solver who is not scared to seek answers. Research, design, develop, deploy and maintain ERP operational…</td>
      <td>Cambridge, ON</td>
      <td>30 days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Business%20Systems%20Analyst%20Robert%20Half</td>
    </tr>
    <tr>
      <th>186</th>
      <td>Junior Developer</td>
      <td>Norima Consulting</td>
      <td>A bachelor's degree in Computer Science, Engineering or similar. A minimum of 1-2 years of proven work experience in software development.</td>
      <td>Remote in Winnipeg, MB</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Developer%20Norima%20Consulting</td>
    </tr>
    <tr>
      <th>187</th>
      <td>Junior Web Developer</td>
      <td>Trellis</td>
      <td>Provide programming supports to lead developer on an Seed to Sale Cannabis Enterprise Software project. Develop documentation and assistance tools to support…</td>
      <td>Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Web%20Developer%20Trellis</td>
    </tr>
    <tr>
      <th>188</th>
      <td>Junior IT Specialist</td>
      <td>Irving Tissue</td>
      <td>Focus on end-user support, wireless, software, and hardware management for our Toronto location. Maintain current anti-virus, anti-spam, and anti-spyware…</td>
      <td>Remote in Toronto, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20IT%20Specialist%20Irving%20Tissue</td>
    </tr>
    <tr>
      <th>189</th>
      <td>Junior Actuarial Analyst</td>
      <td>SCOR</td>
      <td>Participate in quarterly valuation processes involving the calculation of technical provisions and the analysis of results. 0 to 3 years of relevant experience.</td>
      <td>Canada</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Actuarial%20Analyst%20SCOR</td>
    </tr>
    <tr>
      <th>190</th>
      <td>Junior (Jr.) Developer (Canada Summer Jobs 2022)</td>
      <td>SimplyCast</td>
      <td>Canada Summer Jobs 2022 - Position is open to all youth aged 15 to 30 years. Position starts on May 2nd, 2022 and ends on June 27th, 2022.</td>
      <td>Remote in Dartmouth, NS</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20%28Jr.%29%20Developer%20%28Canada%20Summer%20Jobs%202022%29%20SimplyCast</td>
    </tr>
    <tr>
      <th>191</th>
      <td>Junior Software Developer</td>
      <td>COVNEX</td>
      <td>Through your knowledge of industry-proven technologies and methodologies (see below), you will be responsible for delivering high-quality, efficient code as…</td>
      <td>Ottawa, ON</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20COVNEX</td>
    </tr>
    <tr>
      <th>193</th>
      <td>Student Internship - Junior Developer</td>
      <td>Jovaco</td>
      <td>They solve complex issues related to scalability, growth, and usability, and are accountable for their own productivity. Work with SQL Server databases.</td>
      <td>Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=Student%20Internship%20-%20Junior%20Developer%20Jovaco</td>
    </tr>
    <tr>
      <th>298</th>
      <td>Développeur Python/Django [Junior]</td>
      <td>FJNR's a Judicious New Reference</td>
      <td>Si vous êtes passionné par le développement logiciel et que vous avez le goût de rejoindre une équipe qui met l’apprentissage continu au centre de toute chose,…</td>
      <td>Remote in Montréal, QC</td>
      <td>30+ days ago</td>
      <td>30</td>
      <td>https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20Python/Django%20%5BJunior%5D%20FJNR%27s%20a%20Judicious%20New%20Reference</td>
    </tr>
  </tbody>
</table>
</div>



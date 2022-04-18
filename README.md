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
df = pd.concat(dfs).drop_duplicates(subset=['titles', 'companyNames'], ignore_index=True).sort_values('clean_dates')

def filter_cols_by_strs(df, cols, strings):
    for col in cols:
        for string in strings:
            # to see the job postings this filters read:
            # print(df[df[col].str.contains(string) == True])
            df = df[df[col].str.contains(string) == False]
    return df

df = filter_cols_by_strs(df, ['titles', 'jobSnippets'], ['.NET', 'C#', 'Java'])
df.drop(columns=['locations','clean_dates', 'companyNames']).style.set_properties(**{'text-align': 'left'})
```





<table id="T_3f2a9">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_3f2a9_level0_col0" class="col_heading level0 col0" >titles</th>
      <th id="T_3f2a9_level0_col1" class="col_heading level0 col1" >jobSnippets</th>
      <th id="T_3f2a9_level0_col2" class="col_heading level0 col2" >dates</th>
      <th id="T_3f2a9_level0_col3" class="col_heading level0 col3" >links</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_3f2a9_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_3f2a9_row0_col0" class="data row0 col0" >Financial Analyst I</td>
      <td id="T_3f2a9_row0_col1" class="data row0 col1" > Enters data to sub ledger systems. Gathers audit support data upon request. Prepares and gathers data to support proper transaction reporting. </td>
      <td id="T_3f2a9_row0_col2" class="data row0 col2" >1 day ago</td>
      <td id="T_3f2a9_row0_col3" class="data row0 col3" >https://ca.indeed.com/jobs?q=Financial%20Analyst%20I%20BGIS</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row1" class="row_heading level0 row1" >217</th>
      <td id="T_3f2a9_row1_col0" class="data row1 col0" >Junior Software Developer</td>
      <td id="T_3f2a9_row1_col1" class="data row1 col1" > Maintain and enhance enterprise financial system ( crypto-currency trading system, token-exchange system, financial modelling system), developing test programs,… </td>
      <td id="T_3f2a9_row1_col2" class="data row1 col2" >Active 1 day ago</td>
      <td id="T_3f2a9_row1_col3" class="data row1 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20CardinalChain%20Software%2C%20Inc.</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row2" class="row_heading level0 row2" >100</th>
      <td id="T_3f2a9_row2_col0" class="data row2 col0" >Junior PHP backend developer</td>
      <td id="T_3f2a9_row2_col1" class="data row2 col1" > Hands on experience with PHP 7, Mysql, MongoDB, Redis, RabbitMQ, REST API, composer and cloud computing; Understand computer science fundamentals, algorithms,… </td>
      <td id="T_3f2a9_row2_col2" class="data row2 col2" >1 day ago</td>
      <td id="T_3f2a9_row2_col3" class="data row2 col3" >https://ca.indeed.com/jobs?q=Junior%20PHP%20backend%20developer%20Eversun%20Software%20Corp.</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row3" class="row_heading level0 row3" >218</th>
      <td id="T_3f2a9_row3_col0" class="data row3 col0" >Junior Systems Administrator</td>
      <td id="T_3f2a9_row3_col1" class="data row3 col1" > Functionally rich, technically advanced and user friendly, PSD’s CityWide Enterprise systems are configurable for clients to deal with the current and future… </td>
      <td id="T_3f2a9_row3_col2" class="data row3 col2" >2 days ago</td>
      <td id="T_3f2a9_row3_col3" class="data row3 col3" >https://ca.indeed.com/jobs?q=Junior%20Systems%20Administrator%20PSD</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row4" class="row_heading level0 row4" >101</th>
      <td id="T_3f2a9_row4_col0" class="data row4 col0" >Junior Android Developer</td>
      <td id="T_3f2a9_row4_col1" class="data row4 col1" > As an Android Mobile Application Developer, you will participate in full-cycle mobile application development. Part-time hours: 40 per week. </td>
      <td id="T_3f2a9_row4_col2" class="data row4 col2" >Active 2 days ago</td>
      <td id="T_3f2a9_row4_col3" class="data row4 col3" >https://ca.indeed.com/jobs?q=Junior%20Android%20Developer%20Goopter%20eCommerce%20Solutions</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row5" class="row_heading level0 row5" >102</th>
      <td id="T_3f2a9_row5_col0" class="data row5 col0" >Junior Developer/Backend developer</td>
      <td id="T_3f2a9_row5_col1" class="data row5 col1" > Contributes to the overall success of the Global Payment Technology globally by designing, developing, and supporting applications using Shell Scripting, C/C++,… </td>
      <td id="T_3f2a9_row5_col2" class="data row5 col2" >Active 2 days ago</td>
      <td id="T_3f2a9_row5_col3" class="data row5 col3" >https://ca.indeed.com/jobs?q=Junior%20Developer/Backend%20developer%20Avant%20Techno%20Solutions</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row6" class="row_heading level0 row6" >103</th>
      <td id="T_3f2a9_row6_col0" class="data row6 col0" >Junior Developer</td>
      <td id="T_3f2a9_row6_col1" class="data row6 col1" > As a Silver Icing Junior Developer, you have worked on a variety of projects with different technologies in school. Bonuses: Linux, Git, Docker, WordPress. </td>
      <td id="T_3f2a9_row6_col2" class="data row6 col2" >2 days ago</td>
      <td id="T_3f2a9_row6_col3" class="data row6 col3" >https://ca.indeed.com/jobs?q=Junior%20Developer%20Silver%20Icing%20Inc</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row7" class="row_heading level0 row7" >105</th>
      <td id="T_3f2a9_row7_col0" class="data row7 col0" >Junior DevOps Developer</td>
      <td id="T_3f2a9_row7_col1" class="data row7 col1" > Your daily work will include CI systems, Kubernetes, GCP cloud, maintaining Data Infrastructure like Postgresql and Kafka, and writing Infrastructure as Code… </td>
      <td id="T_3f2a9_row7_col2" class="data row7 col2" >2 days ago</td>
      <td id="T_3f2a9_row7_col3" class="data row7 col3" >https://ca.indeed.com/jobs?q=Junior%20DevOps%20Developer%20Checkfront</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row8" class="row_heading level0 row8" >4</th>
      <td id="T_3f2a9_row8_col0" class="data row8 col0" >Junior Financial Analyst (8 MONTH CONTRACT)</td>
      <td id="T_3f2a9_row8_col1" class="data row8 col1" > Key contact for Ad-hoc business unit and functional are support (modeling, reporting, analysis, data gathering). Bachelor’s degree or equivalent. </td>
      <td id="T_3f2a9_row8_col2" class="data row8 col2" >2 days ago</td>
      <td id="T_3f2a9_row8_col3" class="data row8 col3" >https://ca.indeed.com/jobs?q=Junior%20Financial%20Analyst%20%288%20MONTH%20CONTRACT%29%20Cineplex</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row9" class="row_heading level0 row9" >1</th>
      <td id="T_3f2a9_row9_col0" class="data row9 col0" >Junior Data Engineer</td>
      <td id="T_3f2a9_row9_col1" class="data row9 col1" > Develop test plans for source data, analytics/reports, and data pipeline. Analyze upcoming data requirements and perform risk analysis. </td>
      <td id="T_3f2a9_row9_col2" class="data row9 col2" >2 days ago</td>
      <td id="T_3f2a9_row9_col3" class="data row9 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Engineer%20Paper</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row10" class="row_heading level0 row10" >2</th>
      <td id="T_3f2a9_row10_col0" class="data row10 col0" >Jr. SQL BI Developer</td>
      <td id="T_3f2a9_row10_col1" class="data row10 col1" > This role will play an integral role in supporting Vox Mobile business and operations strategy by providing consultative and engineering services in the areas… </td>
      <td id="T_3f2a9_row10_col2" class="data row10 col2" >2 days ago</td>
      <td id="T_3f2a9_row10_col3" class="data row10 col3" >https://ca.indeed.com/jobs?q=Jr.%20SQL%20BI%20Developer%20Vox%20Mobile</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row11" class="row_heading level0 row11" >5</th>
      <td id="T_3f2a9_row11_col0" class="data row11 col0" >Junior Research Analyst</td>
      <td id="T_3f2a9_row11_col1" class="data row11 col1" > Accurate typing and data entry skills. Ad-hoc data and research projects. Data entry: 1 year (preferred). Collect, normalize, validate and structure incoming… </td>
      <td id="T_3f2a9_row11_col2" class="data row11 col2" >Active 2 days ago</td>
      <td id="T_3f2a9_row11_col3" class="data row11 col3" >https://ca.indeed.com/jobs?q=Junior%20Research%20Analyst%20Altrio%20Inc.</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row12" class="row_heading level0 row12" >3</th>
      <td id="T_3f2a9_row12_col0" class="data row12 col0" >Junior Fiscal Policy Analyst</td>
      <td id="T_3f2a9_row12_col1" class="data row12 col1" > Knowledge of computer languages useful for data analysis, such as R or Python, considered an asset. Experience researching and analyzing complex Canadian public… </td>
      <td id="T_3f2a9_row12_col2" class="data row12 col2" >Active 2 days ago</td>
      <td id="T_3f2a9_row12_col3" class="data row12 col3" >https://ca.indeed.com/jobs?q=Junior%20Fiscal%20Policy%20Analyst%20Validus%20Healthcare%20Economics%20Inc.</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row13" class="row_heading level0 row13" >224</th>
      <td id="T_3f2a9_row13_col0" class="data row13 col0" >Scientific Associate I</td>
      <td id="T_3f2a9_row13_col1" class="data row13 col1" > Salary Range: $65,091 - $81,354 per annum (Commensurate with experience and consistent with UHN Compensation Policy). </td>
      <td id="T_3f2a9_row13_col2" class="data row13 col2" >3 days ago</td>
      <td id="T_3f2a9_row13_col3" class="data row13 col3" >https://ca.indeed.com/jobs?q=Scientific%20Associate%20I%20University%20Health%20Network</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row14" class="row_heading level0 row14" >117</th>
      <td id="T_3f2a9_row14_col0" class="data row14 col0" >Junior Production Specialist/SQL Programmer</td>
      <td id="T_3f2a9_row14_col1" class="data row14 col1" > Main/Primary Responsibilities (80% of the time). Handle e-mail, fax and mail broadcasts. Create selection logic using Oracle 11g SQL from production database. </td>
      <td id="T_3f2a9_row14_col2" class="data row14 col2" >Active 3 days ago</td>
      <td id="T_3f2a9_row14_col3" class="data row14 col3" >https://ca.indeed.com/jobs?q=Junior%20Production%20Specialist/SQL%20Programmer%20Professional%20Targeted%20Marketing</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row15" class="row_heading level0 row15" >222</th>
      <td id="T_3f2a9_row15_col0" class="data row15 col0" >Jr. Analyst, Global Cyber Security</td>
      <td id="T_3f2a9_row15_col1" class="data row15 col1" > Technician, Cyber Security to take an active role as an individual contributor in security operations and incident response at IJM. </td>
      <td id="T_3f2a9_row15_col2" class="data row15 col2" >3 days ago</td>
      <td id="T_3f2a9_row15_col3" class="data row15 col3" >https://ca.indeed.com/jobs?q=Jr.%20Analyst%2C%20Global%20Cyber%20Security%20International%20Justice%20Mission</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row16" class="row_heading level0 row16" >221</th>
      <td id="T_3f2a9_row16_col0" class="data row16 col0" >Junior Linux Administrator</td>
      <td id="T_3f2a9_row16_col1" class="data row16 col1" > BCIT’s Information Technology Services Department is seeking a regular, junior full-time Linux Administrator to join our Enterprise Systems team. </td>
      <td id="T_3f2a9_row16_col2" class="data row16 col2" >3 days ago</td>
      <td id="T_3f2a9_row16_col3" class="data row16 col3" >https://ca.indeed.com/jobs?q=Junior%20Linux%20Administrator%20British%20Columbia%20Institute%20of%20Technology%20%28BCIT%29</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row17" class="row_heading level0 row17" >220</th>
      <td id="T_3f2a9_row17_col0" class="data row17 col0" >Junior C/C++ & Fortran Compiler Developer</td>
      <td id="T_3f2a9_row17_col1" class="data row17 col1" > Software Developers at IBM are the backbone of our strategic initiatives to design, code, test, and provide industry-leading solutions that make the world run… </td>
      <td id="T_3f2a9_row17_col2" class="data row17 col2" >3 days ago</td>
      <td id="T_3f2a9_row17_col3" class="data row17 col3" >https://ca.indeed.com/jobs?q=Junior%20C/C%2B%2B%20%26%20Fortran%20Compiler%20Developer%20IBM</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row18" class="row_heading level0 row18" >219</th>
      <td id="T_3f2a9_row18_col0" class="data row18 col0" >Technical Analyst I-II</td>
      <td id="T_3f2a9_row18_col1" class="data row18 col1" > Salary Range: $60,672 to $83,558 per annum commensurate with experience and consistent with UHN Compensation Policy. Reports To: KITE Operations Lead. </td>
      <td id="T_3f2a9_row18_col2" class="data row18 col2" >3 days ago</td>
      <td id="T_3f2a9_row18_col3" class="data row18 col3" >https://ca.indeed.com/jobs?q=Technical%20Analyst%20I-II%20University%20Health%20Network</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row19" class="row_heading level0 row19" >119</th>
      <td id="T_3f2a9_row19_col0" class="data row19 col0" >Programmeur.e Web junior full-stack</td>
      <td id="T_3f2a9_row19_col1" class="data row19 col1" > Sous la responsabilité du rédacteur en chef et éditeur et d'un chargé de projet Web, votre rôle sera de collaborer à la programmation et au développement d'une… </td>
      <td id="T_3f2a9_row19_col2" class="data row19 col2" >Active 3 days ago</td>
      <td id="T_3f2a9_row19_col3" class="data row19 col3" >https://ca.indeed.com/jobs?q=Programmeur.e%20Web%20junior%20full-stack%20Revue%20Qui%20fait%20Quoi%20inc.</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row20" class="row_heading level0 row20" >116</th>
      <td id="T_3f2a9_row20_col0" class="data row20 col0" >Junior Software Developer-AQE</td>
      <td id="T_3f2a9_row20_col1" class="data row20 col1" > In this role you will be able to provide technical insights and expertise to support comprehensive automated verification. Previous experience in software QA. </td>
      <td id="T_3f2a9_row20_col2" class="data row20 col2" >Active 3 days ago</td>
      <td id="T_3f2a9_row20_col3" class="data row20 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer-AQE%20Keywords%20Studios</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row21" class="row_heading level0 row21" >115</th>
      <td id="T_3f2a9_row21_col0" class="data row21 col0" >Junior Developer</td>
      <td id="T_3f2a9_row21_col1" class="data row21 col1" > The Junior Developer would partner with the Senior Data Analyst to support internal applications, perform maintenance on existing deployments of software tools,… </td>
      <td id="T_3f2a9_row21_col2" class="data row21 col2" >Active 3 days ago</td>
      <td id="T_3f2a9_row21_col3" class="data row21 col3" >https://ca.indeed.com/jobs?q=Junior%20Developer%20The%20Corner%20Office</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row22" class="row_heading level0 row22" >114</th>
      <td id="T_3f2a9_row22_col0" class="data row22 col0" >Développeur PHP Junior / Junior PHP Developer</td>
      <td id="T_3f2a9_row22_col1" class="data row22 col1" > IT Cloud est à la recherche d'un programmeur web Full Stack pour un poste permanent. Ce que vous ferez et ce qui vous fera briller. AEC or DEC in programming,. </td>
      <td id="T_3f2a9_row22_col2" class="data row22 col2" >3 days ago</td>
      <td id="T_3f2a9_row22_col3" class="data row22 col3" >https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20PHP%20Junior%20/%20Junior%20PHP%20Developer%20AppDirect</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row23" class="row_heading level0 row23" >225</th>
      <td id="T_3f2a9_row23_col0" class="data row23 col0" >Software Developer I, Performance Advertising</td>
      <td id="T_3f2a9_row23_col1" class="data row23 col1" > Experience coaching junior software development engineers including code review and design review. Programming experience with at least one modern language such… </td>
      <td id="T_3f2a9_row23_col2" class="data row23 col2" >3 days ago</td>
      <td id="T_3f2a9_row23_col3" class="data row23 col3" >https://ca.indeed.com/jobs?q=Software%20Developer%20I%2C%20Performance%20Advertising%20Amazon%20Dev%20Centre%20Canada%20ULC</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row24" class="row_heading level0 row24" >107</th>
      <td id="T_3f2a9_row24_col0" class="data row24 col0" >Junior IT Support Specialist</td>
      <td id="T_3f2a9_row24_col1" class="data row24 col1" > You are a team player with strong technical, communication, organizational, planning, planning, problem solving, and analytical skills. </td>
      <td id="T_3f2a9_row24_col2" class="data row24 col2" >Active 3 days ago</td>
      <td id="T_3f2a9_row24_col3" class="data row24 col3" >https://ca.indeed.com/jobs?q=Junior%20IT%20Support%20Specialist%20The%20Aurum%20Group</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row25" class="row_heading level0 row25" >108</th>
      <td id="T_3f2a9_row25_col0" class="data row25 col0" >Junior Software Developer</td>
      <td id="T_3f2a9_row25_col1" class="data row25 col1" > MerrcoPayfirma is looking for a junior software developer with background in building web and mobile applications. Experience working with REST APIs. </td>
      <td id="T_3f2a9_row25_col2" class="data row25 col2" >3 days ago</td>
      <td id="T_3f2a9_row25_col3" class="data row25 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20Payfirma%20Corporation</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row26" class="row_heading level0 row26" >109</th>
      <td id="T_3f2a9_row26_col0" class="data row26 col0" >Junior Lead Generator</td>
      <td id="T_3f2a9_row26_col1" class="data row26 col1" > ATS is the industry leader in using technology to revolutionize engineering and design processes. Learn and become the expert on data sources, uses, and ways to… </td>
      <td id="T_3f2a9_row26_col2" class="data row26 col2" >3 days ago</td>
      <td id="T_3f2a9_row26_col3" class="data row26 col3" >https://ca.indeed.com/jobs?q=Junior%20Lead%20Generator%20Allied%20Technical%20Solutions</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row27" class="row_heading level0 row27" >110</th>
      <td id="T_3f2a9_row27_col0" class="data row27 col0" >Analyste Développeur spécialisé en sécurité applicative (jun...</td>
      <td id="T_3f2a9_row27_col1" class="data row27 col1" > Analyste Développeur spécialisé en sécurité applicative (junior). Le candidat choisi agira à titre d’analyste-développeur spécialisé en sécurité applicative … </td>
      <td id="T_3f2a9_row27_col2" class="data row27 col2" >3 days ago</td>
      <td id="T_3f2a9_row27_col3" class="data row27 col3" >https://ca.indeed.com/jobs?q=Analyste%20D%C3%A9veloppeur%20sp%C3%A9cialis%C3%A9%20en%20s%C3%A9curit%C3%A9%20applicative%20%28jun...%20CGI</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row28" class="row_heading level0 row28" >111</th>
      <td id="T_3f2a9_row28_col0" class="data row28 col0" >Junior Software Developer</td>
      <td id="T_3f2a9_row28_col1" class="data row28 col1" > Develop high quality code, that delights our customers and stakeholders, using your knowledge of ASP. Net web application development and SQL databases. </td>
      <td id="T_3f2a9_row28_col2" class="data row28 col2" >3 days ago</td>
      <td id="T_3f2a9_row28_col3" class="data row28 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20NCM%20Associates</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row29" class="row_heading level0 row29" >113</th>
      <td id="T_3f2a9_row29_col0" class="data row29 col0" >Junior Front End Developer</td>
      <td id="T_3f2a9_row29_col1" class="data row29 col1" > Collaborate with team members to review requirements and interface and application design specifications. Design beautiful interfaces with an elegant simplicity… </td>
      <td id="T_3f2a9_row29_col2" class="data row29 col2" >Active 3 days ago</td>
      <td id="T_3f2a9_row29_col3" class="data row29 col3" >https://ca.indeed.com/jobs?q=Junior%20Front%20End%20Developer%20Leap%20Tools</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row30" class="row_heading level0 row30" >223</th>
      <td id="T_3f2a9_row30_col0" class="data row30 col0" >Junior Computer Programmer - Summer Student</td>
      <td id="T_3f2a9_row30_col1" class="data row30 col1" > We are currently looking for a Junior Computer Programmer Summer Student to join our Real-time Information Gathering System (RIGS) project team in Calgary,… </td>
      <td id="T_3f2a9_row30_col2" class="data row30 col2" >Active 3 days ago</td>
      <td id="T_3f2a9_row30_col3" class="data row30 col3" >https://ca.indeed.com/jobs?q=Junior%20Computer%20Programmer%20-%20Summer%20Student%20Kobold%20Corporation</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row31" class="row_heading level0 row31" >118</th>
      <td id="T_3f2a9_row31_col0" class="data row31 col0" >Software Engineer I (Python)</td>
      <td id="T_3f2a9_row31_col1" class="data row31 col1" > An ideal candidate will have experience building and operating one or more web frameworks such as Django or Flask in a cloud environment. </td>
      <td id="T_3f2a9_row31_col2" class="data row31 col2" >3 days ago</td>
      <td id="T_3f2a9_row31_col3" class="data row31 col3" >https://ca.indeed.com/jobs?q=Software%20Engineer%20I%20%28Python%29%20Tripadvisor</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row32" class="row_heading level0 row32" >6</th>
      <td id="T_3f2a9_row32_col0" class="data row32 col0" >Data Scientist I</td>
      <td id="T_3f2a9_row32_col1" class="data row32 col1" > They have a strong sense of ownership and eagerness to solve high-impact business problems using data science. Programming; preferably with R, Python, and SQL. </td>
      <td id="T_3f2a9_row32_col2" class="data row32 col2" >3 days ago</td>
      <td id="T_3f2a9_row32_col3" class="data row32 col3" >https://ca.indeed.com/jobs?q=Data%20Scientist%20I%20Northbridge%20Financial%20Corporation</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row33" class="row_heading level0 row33" >7</th>
      <td id="T_3f2a9_row33_col0" class="data row33 col0" >Junior Data Analytics Engineer</td>
      <td id="T_3f2a9_row33_col1" class="data row33 col1" > Use large data sets to address business issues. Understanding of data warehousing concepts and NoSQL Databases. BS or MS in Computer Science or related fields. </td>
      <td id="T_3f2a9_row33_col2" class="data row33 col2" >3 days ago</td>
      <td id="T_3f2a9_row33_col3" class="data row33 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Analytics%20Engineer%20Tier1%20Financial%20Solutions</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row34" class="row_heading level0 row34" >8</th>
      <td id="T_3f2a9_row34_col0" class="data row34 col0" >Jr Data Scientist</td>
      <td id="T_3f2a9_row34_col1" class="data row34 col1" > 1-3 years experience in a data scientist or analyst role. Experience with agricultural and environmental research, including involvement on research teams, data… </td>
      <td id="T_3f2a9_row34_col2" class="data row34 col2" >3 days ago</td>
      <td id="T_3f2a9_row34_col3" class="data row34 col3" >https://ca.indeed.com/jobs?q=Jr%20Data%20Scientist%20Olds%20College</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row35" class="row_heading level0 row35" >9</th>
      <td id="T_3f2a9_row35_col0" class="data row35 col0" >Junior Financial Analyst</td>
      <td id="T_3f2a9_row35_col1" class="data row35 col1" > Support the Finance team in producing meaningful data/analysis. Comfortable working with reports in different formats from various information systems to ensure… </td>
      <td id="T_3f2a9_row35_col2" class="data row35 col2" >3 days ago</td>
      <td id="T_3f2a9_row35_col3" class="data row35 col3" >https://ca.indeed.com/jobs?q=Junior%20Financial%20Analyst%20Credit%20Valley%20Conservation</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row36" class="row_heading level0 row36" >10</th>
      <td id="T_3f2a9_row36_col0" class="data row36 col0" >Junior Financial Analyst, Treasury</td>
      <td id="T_3f2a9_row36_col1" class="data row36 col1" > Support monthly capital management activities including monitoring and analyzing regular financial reports, investment data, and other information sources to… </td>
      <td id="T_3f2a9_row36_col2" class="data row36 col2" >3 days ago</td>
      <td id="T_3f2a9_row36_col3" class="data row36 col3" >https://ca.indeed.com/jobs?q=Junior%20Financial%20Analyst%2C%20Treasury%20Definity</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row37" class="row_heading level0 row37" >11</th>
      <td id="T_3f2a9_row37_col0" class="data row37 col0" >Junior Treasury Analyst</td>
      <td id="T_3f2a9_row37_col1" class="data row37 col1" > Advanced MS Excel and Access skills for reporting and data analysis. Assess accuracy and completeness of data records and conformance with company procedures. </td>
      <td id="T_3f2a9_row37_col2" class="data row37 col2" >Active 3 days ago</td>
      <td id="T_3f2a9_row37_col3" class="data row37 col3" >https://ca.indeed.com/jobs?q=Junior%20Treasury%20Analyst%20ETG%20Commodities%20Inc.</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row38" class="row_heading level0 row38" >12</th>
      <td id="T_3f2a9_row38_col0" class="data row38 col0" >Junior Data Analytics Engineer</td>
      <td id="T_3f2a9_row38_col1" class="data row38 col1" > Use large data sets to address business issues. Understanding of data warehousing concepts and NoSQL Databases. BS or MS in Computer Science or related fields. </td>
      <td id="T_3f2a9_row38_col2" class="data row38 col2" >3 days ago</td>
      <td id="T_3f2a9_row38_col3" class="data row38 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Analytics%20Engineer%20CaseWare%20RCM</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row39" class="row_heading level0 row39" >13</th>
      <td id="T_3f2a9_row39_col0" class="data row39 col0" >Junior Data Analyst / Data Entry</td>
      <td id="T_3f2a9_row39_col1" class="data row39 col1" > Conducting data profiling to analyze quality of incoming data &amp; advising on any data cleansing rules. Perform data maintenance tasks when required to ensure… </td>
      <td id="T_3f2a9_row39_col2" class="data row39 col2" >Active 3 days ago</td>
      <td id="T_3f2a9_row39_col3" class="data row39 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20/%20Data%20Entry%20Strategy%20Institute</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row40" class="row_heading level0 row40" >14</th>
      <td id="T_3f2a9_row40_col0" class="data row40 col0" >Jr. Data Analyst</td>
      <td id="T_3f2a9_row40_col1" class="data row40 col1" > Maintain confidentiality regarding all student data and information. Minimum 1 year’s experience in data management or analysis. Bachelor's Degree in any field. </td>
      <td id="T_3f2a9_row40_col2" class="data row40 col2" >Active 3 days ago</td>
      <td id="T_3f2a9_row40_col3" class="data row40 col3" >https://ca.indeed.com/jobs?q=Jr.%20Data%20Analyst%20Canadian%20College</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row41" class="row_heading level0 row41" >19</th>
      <td id="T_3f2a9_row41_col0" class="data row41 col0" >Clinical Data Manager I / Gestionnaire de données cliniques...</td>
      <td id="T_3f2a9_row41_col1" class="data row41 col1" > Develops data transfer agreements and specifications with vendors providing external data (e.g. laboratory results). B.Sc. or in a related field of study; </td>
      <td id="T_3f2a9_row41_col2" class="data row41 col2" >4 days ago</td>
      <td id="T_3f2a9_row41_col3" class="data row41 col3" >https://ca.indeed.com/jobs?q=Clinical%20Data%20Manager%20I%20/%20Gestionnaire%20de%20donn%C3%A9es%20cliniques...%20Innovaderm%20Research</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row42" class="row_heading level0 row42" >127</th>
      <td id="T_3f2a9_row42_col0" class="data row42 col0" >Junior Software Developer</td>
      <td id="T_3f2a9_row42_col1" class="data row42 col1" > In this role you will be able to provide technical insights and expertise to support comprehensive automated verification. Fix bugs on existing scripts. </td>
      <td id="T_3f2a9_row42_col2" class="data row42 col2" >Active 4 days ago</td>
      <td id="T_3f2a9_row42_col3" class="data row42 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20Keywords%20Studios</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row43" class="row_heading level0 row43" >126</th>
      <td id="T_3f2a9_row43_col0" class="data row43 col0" >Junior System Administrator</td>
      <td id="T_3f2a9_row43_col1" class="data row43 col1" > We manage the entire lifecycle of the finance receivable from credit adjudication through to contract administration, customer service, default management and… </td>
      <td id="T_3f2a9_row43_col2" class="data row43 col2" >Active 4 days ago</td>
      <td id="T_3f2a9_row43_col3" class="data row43 col3" >https://ca.indeed.com/jobs?q=Junior%20System%20Administrator%20Cancap%20Group%20Inc</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row44" class="row_heading level0 row44" >125</th>
      <td id="T_3f2a9_row44_col0" class="data row44 col0" >Junior Underwriter</td>
      <td id="T_3f2a9_row44_col1" class="data row44 col1" > We enable employers to provide their employees with the health care they need and want more comprehensively and cost-effectively than traditional health… </td>
      <td id="T_3f2a9_row44_col2" class="data row44 col2" >Active 4 days ago</td>
      <td id="T_3f2a9_row44_col3" class="data row44 col3" >https://ca.indeed.com/jobs?q=Junior%20Underwriter%20Benecaid</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row45" class="row_heading level0 row45" >21</th>
      <td id="T_3f2a9_row45_col0" class="data row45 col0" >Junior Business Analyst, Data Management – MS Excel - 337002</td>
      <td id="T_3f2a9_row45_col1" class="data row45 col1" > Performing new lender/borrower set up and static data validation and maintenance. Maintain Tax Module for maintenances of IRS tax static data for Loan… </td>
      <td id="T_3f2a9_row45_col2" class="data row45 col2" >4 days ago</td>
      <td id="T_3f2a9_row45_col3" class="data row45 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%2C%20Data%20Management%20%E2%80%93%20MS%20Excel%20-%20337002%20Procom</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row46" class="row_heading level0 row46" >123</th>
      <td id="T_3f2a9_row46_col0" class="data row46 col0" >Junior Full Stack Developer</td>
      <td id="T_3f2a9_row46_col1" class="data row46 col1" > As a Junior Full Stack Developer with Random Acronym (a division of Integrated Sustainability), your experience and skills will enable you to make a difference… </td>
      <td id="T_3f2a9_row46_col2" class="data row46 col2" >4 days ago</td>
      <td id="T_3f2a9_row46_col3" class="data row46 col3" >https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20Integrated%20Sustainability</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row47" class="row_heading level0 row47" >122</th>
      <td id="T_3f2a9_row47_col0" class="data row47 col0" >Junior Python Developer</td>
      <td id="T_3f2a9_row47_col1" class="data row47 col1" > You have a passion for solving complex problems and working on products that people will use on a daily basis. Our game nights are legendary.*. </td>
      <td id="T_3f2a9_row47_col2" class="data row47 col2" >Active 4 days ago</td>
      <td id="T_3f2a9_row47_col3" class="data row47 col3" >https://ca.indeed.com/jobs?q=Junior%20Python%20Developer%20Leap%20Tools</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row48" class="row_heading level0 row48" >20</th>
      <td id="T_3f2a9_row48_col0" class="data row48 col0" >GIS Technician and Jr Data Engineer</td>
      <td id="T_3f2a9_row48_col1" class="data row48 col1" > Are Customer-centric – they understand and embrace the role of delivering exemplary service. Lead – they lead by example through their actions and attitudes. </td>
      <td id="T_3f2a9_row48_col2" class="data row48 col2" >Active 4 days ago</td>
      <td id="T_3f2a9_row48_col3" class="data row48 col3" >https://ca.indeed.com/jobs?q=GIS%20Technician%20and%20Jr%20Data%20Engineer%20QSP%20Geographics%20Inc.</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row49" class="row_heading level0 row49" >18</th>
      <td id="T_3f2a9_row49_col0" class="data row49 col0" >Junior Business Analyst</td>
      <td id="T_3f2a9_row49_col1" class="data row49 col1" > A passion about organizing data and bringing order to chaos, while also being able to analyze and provide actionable insights. Job Types: Full-time, Permanent. </td>
      <td id="T_3f2a9_row49_col2" class="data row49 col2" >Active 4 days ago</td>
      <td id="T_3f2a9_row49_col3" class="data row49 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20Pride%20Mobility%20Products%20Company</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row50" class="row_heading level0 row50" >124</th>
      <td id="T_3f2a9_row50_col0" class="data row50 col0" >Engineer I</td>
      <td id="T_3f2a9_row50_col1" class="data row50 col1" > We are looking for a developer to support short term surge in demand to enhance and deploy new functionality with DRUM KPI. University or Post-Graduate Degree. </td>
      <td id="T_3f2a9_row50_col2" class="data row50 col2" >4 days ago</td>
      <td id="T_3f2a9_row50_col3" class="data row50 col3" >https://ca.indeed.com/jobs?q=Engineer%20I%20TD%20Bank</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row51" class="row_heading level0 row51" >17</th>
      <td id="T_3f2a9_row51_col0" class="data row51 col0" >Junior Investment Analyst (Equity Research / Reconciliation)</td>
      <td id="T_3f2a9_row51_col1" class="data row51 col1" > Responsible for ongoing data management; Possess strong research and data analysis skills. Demonstrated passion for research, and investment, data analysis. </td>
      <td id="T_3f2a9_row51_col2" class="data row51 col2" >Active 4 days ago</td>
      <td id="T_3f2a9_row51_col3" class="data row51 col3" >https://ca.indeed.com/jobs?q=Junior%20Investment%20Analyst%20%28Equity%20Research%20/%20Reconciliation%29%20Applied%20Research%20Investment</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row52" class="row_heading level0 row52" >230</th>
      <td id="T_3f2a9_row52_col0" class="data row52 col0" >Junior Python programmer</td>
      <td id="T_3f2a9_row52_col1" class="data row52 col1" > You will work with Visual Defence’s Research and Development team under the guidance of the company’s Director of Research and Development. </td>
      <td id="T_3f2a9_row52_col2" class="data row52 col2" >Active 4 days ago</td>
      <td id="T_3f2a9_row52_col3" class="data row52 col3" >https://ca.indeed.com/jobs?q=Junior%20Python%20programmer%20Visual%20Defence%20Inc</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row53" class="row_heading level0 row53" >227</th>
      <td id="T_3f2a9_row53_col0" class="data row53 col0" >Jr ITSM Analyst - jp 2193 - Markham</td>
      <td id="T_3f2a9_row53_col1" class="data row53 col1" > This role will provide assistance and support to the IT Service Management team. Assisting with tasks related to the Configuration Item registry and CMDB data… </td>
      <td id="T_3f2a9_row53_col2" class="data row53 col2" >4 days ago</td>
      <td id="T_3f2a9_row53_col3" class="data row53 col3" >https://ca.indeed.com/jobs?q=Jr%20ITSM%20Analyst%20-%20jp%202193%20-%20Markham%20Randstad</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row54" class="row_heading level0 row54" >228</th>
      <td id="T_3f2a9_row54_col0" class="data row54 col0" >Jr. Nuage/Cloud 2LS CS Engineer</td>
      <td id="T_3f2a9_row54_col1" class="data row54 col1" > Ability to write scripts at a Unix/Linux level (bash, python). Provide Remote Technical Support (RTS) for the Nuage SDN solutions and associated network… </td>
      <td id="T_3f2a9_row54_col2" class="data row54 col2" >4 days ago</td>
      <td id="T_3f2a9_row54_col3" class="data row54 col3" >https://ca.indeed.com/jobs?q=Jr.%20Nuage/Cloud%202LS%20CS%20Engineer%20NOKIA</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row55" class="row_heading level0 row55" >229</th>
      <td id="T_3f2a9_row55_col0" class="data row55 col0" >Junior to Intermediate QA Engineer (Web application, Seleniu...</td>
      <td id="T_3f2a9_row55_col1" class="data row55 col1" > While our Vancouver office is located on Granville Island, this role will be fully remote (work-from-home), with the option of working at the office if the… </td>
      <td id="T_3f2a9_row55_col2" class="data row55 col2" >Active 4 days ago</td>
      <td id="T_3f2a9_row55_col3" class="data row55 col3" >https://ca.indeed.com/jobs?q=Junior%20to%20Intermediate%20QA%20Engineer%20%28Web%20application%2C%20Seleniu...%20Marine%20Learning%20Systems</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row56" class="row_heading level0 row56" >128</th>
      <td id="T_3f2a9_row56_col0" class="data row56 col0" >Junior Backend Developer</td>
      <td id="T_3f2a9_row56_col1" class="data row56 col1" > Wealth Management Applied Analytics and Innovation (WMAI) is responsible for developing and implementing a data and analytics strategy that delivers key… </td>
      <td id="T_3f2a9_row56_col2" class="data row56 col2" >4 days ago</td>
      <td id="T_3f2a9_row56_col3" class="data row56 col3" >https://ca.indeed.com/jobs?q=Junior%20Backend%20Developer%20Royal%20Bank%20of%20Canada</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row57" class="row_heading level0 row57" >15</th>
      <td id="T_3f2a9_row57_col0" class="data row57 col0" >Business Analyst I - DC IS</td>
      <td id="T_3f2a9_row57_col1" class="data row57 col1" > Moderate to advanced knowledge of data processing and general business practices. This will include providing support and maintenance for computer hardware,… </td>
      <td id="T_3f2a9_row57_col2" class="data row57 col2" >4 days ago</td>
      <td id="T_3f2a9_row57_col3" class="data row57 col3" >https://ca.indeed.com/jobs?q=Business%20Analyst%20I%20-%20DC%20IS%20Columbia%20Sportswear%20Company</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row58" class="row_heading level0 row58" >16</th>
      <td id="T_3f2a9_row58_col0" class="data row58 col0" >Junior Social Media Marketing & Engagement Specialist</td>
      <td id="T_3f2a9_row58_col1" class="data row58 col1" > Keeping track of data analyzing the performance of social media campaigns. We are seeking a passionate and creative in-house Social Media Specialist to… </td>
      <td id="T_3f2a9_row58_col2" class="data row58 col2" >Active 4 days ago</td>
      <td id="T_3f2a9_row58_col3" class="data row58 col3" >https://ca.indeed.com/jobs?q=Junior%20Social%20Media%20Marketing%20%26%20Engagement%20Specialist%20ConsidraCare</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row59" class="row_heading level0 row59" >120</th>
      <td id="T_3f2a9_row59_col0" class="data row59 col0" >Junior System Administrator</td>
      <td id="T_3f2a9_row59_col1" class="data row59 col1" > Providing first and second-level technical support of current information systems locally. Maintaining, testing, and resolution of issues of all PC hardware and… </td>
      <td id="T_3f2a9_row59_col2" class="data row59 col2" >Active 4 days ago</td>
      <td id="T_3f2a9_row59_col3" class="data row59 col3" >https://ca.indeed.com/jobs?q=Junior%20System%20Administrator%20VAC%20Developments%20Ltd</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row60" class="row_heading level0 row60" >135</th>
      <td id="T_3f2a9_row60_col0" class="data row60 col0" >Jr Software Developer (Remote/Hybrid)</td>
      <td id="T_3f2a9_row60_col1" class="data row60 col1" > Assisting the development manager with all aspects of software design and coding. Attending and contributing to company development meetings. </td>
      <td id="T_3f2a9_row60_col2" class="data row60 col2" >Active 5 days ago</td>
      <td id="T_3f2a9_row60_col3" class="data row60 col3" >https://ca.indeed.com/jobs?q=Jr%20Software%20Developer%20%28Remote/Hybrid%29%20CADdetails%20Ltd.</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row61" class="row_heading level0 row61" >134</th>
      <td id="T_3f2a9_row61_col0" class="data row61 col0" >Junior Programmer</td>
      <td id="T_3f2a9_row61_col1" class="data row61 col1" > Under the supervision of the Director of Operations, this position provides direct assistance in all aspects of planning, organizing, implementing, monitoring,… </td>
      <td id="T_3f2a9_row61_col2" class="data row61 col2" >5 days ago</td>
      <td id="T_3f2a9_row61_col3" class="data row61 col3" >https://ca.indeed.com/jobs?q=Junior%20Programmer%20FirstService%20Residential</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row62" class="row_heading level0 row62" >133</th>
      <td id="T_3f2a9_row62_col0" class="data row62 col0" >Junior Software Developer</td>
      <td id="T_3f2a9_row62_col1" class="data row62 col1" > Reporting to the Director of Information Technology, the successful candidate must be able meet client needs by assessing current software systems and… </td>
      <td id="T_3f2a9_row62_col2" class="data row62 col2" >5 days ago</td>
      <td id="T_3f2a9_row62_col3" class="data row62 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20CanTalk%20Canada</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row63" class="row_heading level0 row63" >132</th>
      <td id="T_3f2a9_row63_col0" class="data row63 col0" >DevOps Specialist I</td>
      <td id="T_3f2a9_row63_col1" class="data row63 col1" > Category: Permanent, Full Time, Monday-Friday, Regular Hours. § Implement release processes across development, test, and production environments. </td>
      <td id="T_3f2a9_row63_col2" class="data row63 col2" >Active 5 days ago</td>
      <td id="T_3f2a9_row63_col3" class="data row63 col3" >https://ca.indeed.com/jobs?q=DevOps%20Specialist%20I%20PortfolioAid%20Inc.</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row64" class="row_heading level0 row64" >131</th>
      <td id="T_3f2a9_row64_col0" class="data row64 col0" >Junior Systems Administrator</td>
      <td id="T_3f2a9_row64_col1" class="data row64 col1" > No experience is necessary, you will be trained by the IT Manager directly. Develop knowledge base and content. Develop IT procedures and policies. </td>
      <td id="T_3f2a9_row64_col2" class="data row64 col2" >5 days ago</td>
      <td id="T_3f2a9_row64_col3" class="data row64 col3" >https://ca.indeed.com/jobs?q=Junior%20Systems%20Administrator%20Vicinity%20Motor%20Corporation</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row65" class="row_heading level0 row65" >129</th>
      <td id="T_3f2a9_row65_col0" class="data row65 col0" >Junior Programmer</td>
      <td id="T_3f2a9_row65_col1" class="data row65 col1" > In this role you will meet customer’s needs by programming application specific solutions including a broad line of touchscreen and keypad user interfaces,… </td>
      <td id="T_3f2a9_row65_col2" class="data row65 col2" >Active 5 days ago</td>
      <td id="T_3f2a9_row65_col3" class="data row65 col3" >https://ca.indeed.com/jobs?q=Junior%20Programmer%20Express%20Employment%20Professionals%20-%20Red%20Deer</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row66" class="row_heading level0 row66" >22</th>
      <td id="T_3f2a9_row66_col0" class="data row66 col0" >Jr. Financial Analyst</td>
      <td id="T_3f2a9_row66_col1" class="data row66 col1" > Resourceful/able to find or develop compelling data. Analyze data and prepare KPI reports for distribution to senior management. </td>
      <td id="T_3f2a9_row66_col2" class="data row66 col2" >5 days ago</td>
      <td id="T_3f2a9_row66_col3" class="data row66 col3" >https://ca.indeed.com/jobs?q=Jr.%20Financial%20Analyst%20realtor.com</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row67" class="row_heading level0 row67" >24</th>
      <td id="T_3f2a9_row67_col0" class="data row67 col0" >Junior Data Analyst</td>
      <td id="T_3f2a9_row67_col1" class="data row67 col1" > Gain and update job knowledge to remain informed about innovation in the field, explore and implement use cases for data science/data analytics to improve… </td>
      <td id="T_3f2a9_row67_col2" class="data row67 col2" >Active 5 days ago</td>
      <td id="T_3f2a9_row67_col3" class="data row67 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20Beta-Calco</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row68" class="row_heading level0 row68" >25</th>
      <td id="T_3f2a9_row68_col0" class="data row68 col0" >Junior Data Scientist - Deep Learning</td>
      <td id="T_3f2a9_row68_col1" class="data row68 col1" > Knowledge of geomatics tools and remote sensing data. Work with geospatial tools and data including multispectral and SAR imagery. </td>
      <td id="T_3f2a9_row68_col2" class="data row68 col2" >5 days ago</td>
      <td id="T_3f2a9_row68_col3" class="data row68 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Scientist%20-%20Deep%20Learning%20ASL%20Environmental%20Sciences%20Inc.</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row69" class="row_heading level0 row69" >130</th>
      <td id="T_3f2a9_row69_col0" class="data row69 col0" >JUNIOR SOFTWARE ENGINEER</td>
      <td id="T_3f2a9_row69_col1" class="data row69 col1" > Work closely with product managers and domain experts to distill complex business problems into elegant technical solutions. Experience with HTML and CSS. </td>
      <td id="T_3f2a9_row69_col2" class="data row69 col2" >5 days ago</td>
      <td id="T_3f2a9_row69_col3" class="data row69 col3" >https://ca.indeed.com/jobs?q=JUNIOR%20SOFTWARE%20ENGINEER%20OEC%20Group%20%28Canada%29</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row70" class="row_heading level0 row70" >233</th>
      <td id="T_3f2a9_row70_col0" class="data row70 col0" >Python Developer - Junior</td>
      <td id="T_3f2a9_row70_col1" class="data row70 col1" > Please note that this position is remote. Candidates must have an eligible work permit for Canada and be fluent in French. Come and work with us! </td>
      <td id="T_3f2a9_row70_col2" class="data row70 col2" >5 days ago</td>
      <td id="T_3f2a9_row70_col3" class="data row70 col3" >https://ca.indeed.com/jobs?q=Python%20Developer%20-%20Junior%20Alithya</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row71" class="row_heading level0 row71" >231</th>
      <td id="T_3f2a9_row71_col0" class="data row71 col0" >Information Security Analyst I (Terrace)</td>
      <td id="T_3f2a9_row71_col1" class="data row71 col1" > Coast Mountain College (CMTN), Terrace campus, invites applications for a continuing full-time Information Security Analyst I. This position requires a flexible… </td>
      <td id="T_3f2a9_row71_col2" class="data row71 col2" >5 days ago</td>
      <td id="T_3f2a9_row71_col3" class="data row71 col3" >https://ca.indeed.com/jobs?q=Information%20Security%20Analyst%20I%20%28Terrace%29%20Coast%20Mountain%20College</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row72" class="row_heading level0 row72" >232</th>
      <td id="T_3f2a9_row72_col0" class="data row72 col0" >Junior Python /Go Developer</td>
      <td id="T_3f2a9_row72_col1" class="data row72 col1" > In order to start new initiatives, we are looking for three more developers, with intermediate to senior levels. Good collaboration attitude and autonomy. </td>
      <td id="T_3f2a9_row72_col2" class="data row72 col2" >5 days ago</td>
      <td id="T_3f2a9_row72_col3" class="data row72 col3" >https://ca.indeed.com/jobs?q=Junior%20Python%20/Go%20Developer%20National%20Bank%20of%20Canada</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row73" class="row_heading level0 row73" >23</th>
      <td id="T_3f2a9_row73_col0" class="data row73 col0" >Junior Business Analyst</td>
      <td id="T_3f2a9_row73_col1" class="data row73 col1" > Collaborate with development and support teams to answer business questions using data and business analysis best practices. </td>
      <td id="T_3f2a9_row73_col2" class="data row73 col2" >Active 5 days ago</td>
      <td id="T_3f2a9_row73_col3" class="data row73 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20Beyond%20Bilingual%20Inc.</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row74" class="row_heading level0 row74" >235</th>
      <td id="T_3f2a9_row74_col0" class="data row74 col0" >Développeur Python/Go junior</td>
      <td id="T_3f2a9_row74_col1" class="data row74 col1" > Nous sommes une équipe multidisciplinaire de six développeurs au sein d’un groupe de transformation DevOps et d’adoption du Cloud. Une expérience avec un Cloud. </td>
      <td id="T_3f2a9_row74_col2" class="data row74 col2" >6 days ago</td>
      <td id="T_3f2a9_row74_col3" class="data row74 col3" >https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20Python/Go%20junior%20Banque%20Nationale%20du%20Canada</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row75" class="row_heading level0 row75" >234</th>
      <td id="T_3f2a9_row75_col0" class="data row75 col0" >Compositor - Junior</td>
      <td id="T_3f2a9_row75_col1" class="data row75 col1" > Great artistic sense and aesthetic a must. Strong Nuke proficiency, including good organization of scripts and workflow. Knowledge of Python coding is a bonus. </td>
      <td id="T_3f2a9_row75_col2" class="data row75 col2" >6 days ago</td>
      <td id="T_3f2a9_row75_col3" class="data row75 col3" >https://ca.indeed.com/jobs?q=Compositor%20-%20Junior%20Tryptyc%20Theory</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row76" class="row_heading level0 row76" >136</th>
      <td id="T_3f2a9_row76_col0" class="data row76 col0" >Junior Developer</td>
      <td id="T_3f2a9_row76_col1" class="data row76 col1" > A bachelor's degree in Computer Science, Engineering or similar. A minimum of 1-2 years of proven work experience in software development. </td>
      <td id="T_3f2a9_row76_col2" class="data row76 col2" >Active 6 days ago</td>
      <td id="T_3f2a9_row76_col3" class="data row76 col3" >https://ca.indeed.com/jobs?q=Junior%20Developer%20Norima%20Consulting</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row77" class="row_heading level0 row77" >138</th>
      <td id="T_3f2a9_row77_col0" class="data row77 col0" >Junior Resource Analyst</td>
      <td id="T_3f2a9_row77_col1" class="data row77 col1" > Data manipulation, forest estate modelling, and resource planning; and. Contribute to projects managed by project teams in areas such as, but not limited to,… </td>
      <td id="T_3f2a9_row77_col2" class="data row77 col2" >Active 6 days ago</td>
      <td id="T_3f2a9_row77_col3" class="data row77 col3" >https://ca.indeed.com/jobs?q=Junior%20Resource%20Analyst%20Ecora</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row78" class="row_heading level0 row78" >28</th>
      <td id="T_3f2a9_row78_col0" class="data row78 col0" >Jr. and Sr. Analytics Consultant</td>
      <td id="T_3f2a9_row78_col1" class="data row78 col1" > Has experiences in data visualization, such as Tableau or Qlik. Attend analytics, data science, AI and industry conferences and workshops, developing your own… </td>
      <td id="T_3f2a9_row78_col2" class="data row78 col2" >6 days ago</td>
      <td id="T_3f2a9_row78_col3" class="data row78 col3" >https://ca.indeed.com/jobs?q=Jr.%20and%20Sr.%20Analytics%20Consultant%20Advanced%20Analytics%20and%20Research%20Lab</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row79" class="row_heading level0 row79" >26</th>
      <td id="T_3f2a9_row79_col0" class="data row79 col0" >Junior Global Business Analyst</td>
      <td id="T_3f2a9_row79_col1" class="data row79 col1" > Conduct data mining and executes queries to process data from multiple sources. Analyze data and prepare reports/dashboards that show key trends and metrics. </td>
      <td id="T_3f2a9_row79_col2" class="data row79 col2" >6 days ago</td>
      <td id="T_3f2a9_row79_col3" class="data row79 col3" >https://ca.indeed.com/jobs?q=Junior%20Global%20Business%20Analyst%20ZOOK%20Canada%20Inc</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row80" class="row_heading level0 row80" >137</th>
      <td id="T_3f2a9_row80_col0" class="data row80 col0" >Junior System Administrator</td>
      <td id="T_3f2a9_row80_col1" class="data row80 col1" > As a Junior System Administrator, you will provide technical support of HW/SW, corporate system/server/network management, consultation, and procurement for all… </td>
      <td id="T_3f2a9_row80_col2" class="data row80 col2" >6 days ago</td>
      <td id="T_3f2a9_row80_col3" class="data row80 col3" >https://ca.indeed.com/jobs?q=Junior%20System%20Administrator%20GNK%20Holdings%20Inc.</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row81" class="row_heading level0 row81" >27</th>
      <td id="T_3f2a9_row81_col0" class="data row81 col0" >Junior Business Analyst - 336705</td>
      <td id="T_3f2a9_row81_col1" class="data row81 col1" > Synthetizing large amounts of data and identifying trends, potentials risks and developing remediation plans; Managing and tracking budget activities; </td>
      <td id="T_3f2a9_row81_col2" class="data row81 col2" >6 days ago</td>
      <td id="T_3f2a9_row81_col3" class="data row81 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20-%20336705%20Procom</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row82" class="row_heading level0 row82" >139</th>
      <td id="T_3f2a9_row82_col0" class="data row82 col0" >IT Analyst I</td>
      <td id="T_3f2a9_row82_col1" class="data row82 col1" > Reporting to the Manager – Alberta Netcare Portal, the IT Analyst is responsible for the support, development and configuration for the Alberta Netcare Portal,… </td>
      <td id="T_3f2a9_row82_col2" class="data row82 col2" >8 days ago</td>
      <td id="T_3f2a9_row82_col3" class="data row82 col3" >https://ca.indeed.com/jobs?q=IT%20Analyst%20I%20Alberta%20Health%20Services</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row83" class="row_heading level0 row83" >29</th>
      <td id="T_3f2a9_row83_col0" class="data row83 col0" >Junior Business Analyst</td>
      <td id="T_3f2a9_row83_col1" class="data row83 col1" > The Analyst will assist in analyzing the data and preparing summary notes and dashboards/graphs/charts that will be shared with the sales &amp; operations teams. </td>
      <td id="T_3f2a9_row83_col2" class="data row83 col2" >8 days ago</td>
      <td id="T_3f2a9_row83_col3" class="data row83 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20Colas</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row84" class="row_heading level0 row84" >236</th>
      <td id="T_3f2a9_row84_col0" class="data row84 col0" >Junior Software Developer (DataHub Team)</td>
      <td id="T_3f2a9_row84_col1" class="data row84 col1" > You love solving problems and enjoy getting to the root cause of issues. You enjoy exploring new technologies to deliver a reliable, secure, and highly… </td>
      <td id="T_3f2a9_row84_col2" class="data row84 col2" >8 days ago</td>
      <td id="T_3f2a9_row84_col3" class="data row84 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20%28DataHub%20Team%29%20Pason%20Systems%20Corp</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row85" class="row_heading level0 row85" >142</th>
      <td id="T_3f2a9_row85_col0" class="data row85 col0" >Junior Business Systems Analyst (Application Life Cycle)</td>
      <td id="T_3f2a9_row85_col1" class="data row85 col1" > Maximus Canada offers competitive market-based salaries, comprehensive employer-paid benefits and a defined-benefit pension plan or a Group RSP with employer… </td>
      <td id="T_3f2a9_row85_col2" class="data row85 col2" >9 days ago</td>
      <td id="T_3f2a9_row85_col3" class="data row85 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Systems%20Analyst%20%28Application%20Life%20Cycle%29%20Maximus</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row86" class="row_heading level0 row86" >141</th>
      <td id="T_3f2a9_row86_col0" class="data row86 col0" >Junior Analyst - GCLP (Toronto, ON)</td>
      <td id="T_3f2a9_row86_col1" class="data row86 col1" > Of clients within the financial services sector. Institutional investment management services are provided by. This will entail reviewing and developing data. </td>
      <td id="T_3f2a9_row86_col2" class="data row86 col2" >9 days ago</td>
      <td id="T_3f2a9_row86_col3" class="data row86 col3" >https://ca.indeed.com/jobs?q=Junior%20Analyst%20-%C2%A0GCLP%20%28Toronto%2C%20ON%29%20Guardian%20Capital%20Group%20Limited</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row87" class="row_heading level0 row87" >237</th>
      <td id="T_3f2a9_row87_col0" class="data row87 col0" >DevOps Junior / Junior DevOps</td>
      <td id="T_3f2a9_row87_col1" class="data row87 col1" > À propos d’OPAL-RT Technologies. OPAL-RT s’est donné comme ambitieux défi de démocratiser la simulation temps réel afin de la rendre accessible à chaque… </td>
      <td id="T_3f2a9_row87_col2" class="data row87 col2" >9 days ago</td>
      <td id="T_3f2a9_row87_col3" class="data row87 col3" >https://ca.indeed.com/jobs?q=DevOps%20Junior%20/%20Junior%20DevOps%20Opal-RT</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row88" class="row_heading level0 row88" >33</th>
      <td id="T_3f2a9_row88_col0" class="data row88 col0" >Junior Business Analyst, Strategic Partnerships and Performa...</td>
      <td id="T_3f2a9_row88_col1" class="data row88 col1" > Practices diligence and care when maintaining, monitoring, calculating and summarizing data, records and confidential information. </td>
      <td id="T_3f2a9_row88_col2" class="data row88 col2" >9 days ago</td>
      <td id="T_3f2a9_row88_col3" class="data row88 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%2C%20Strategic%20Partnerships%20and%20Performa...%20Vancouver%20Coastal%20Health</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row89" class="row_heading level0 row89" >32</th>
      <td id="T_3f2a9_row89_col0" class="data row89 col0" >Junior Data Governance & Data Quality Specialist - 336569</td>
      <td id="T_3f2a9_row89_col1" class="data row89 col1" > The candidate must be able to communicate effectively with team members and have an understanding of data analysis, data quality, data security, data movement,… </td>
      <td id="T_3f2a9_row89_col2" class="data row89 col2" >9 days ago</td>
      <td id="T_3f2a9_row89_col3" class="data row89 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Governance%20%26%20Data%20Quality%20Specialist%20-%20336569%20Procom</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row90" class="row_heading level0 row90" >30</th>
      <td id="T_3f2a9_row90_col0" class="data row90 col0" >Junior Business Analyst - Reporting & Analytics</td>
      <td id="T_3f2a9_row90_col1" class="data row90 col1" > Recommend and develop automation solutions for our data and reporting needs. Collaborate with our development, database and support teams to answer business… </td>
      <td id="T_3f2a9_row90_col2" class="data row90 col2" >9 days ago</td>
      <td id="T_3f2a9_row90_col3" class="data row90 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20-%20Reporting%20%26%20Analytics%20TripArc</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row91" class="row_heading level0 row91" >31</th>
      <td id="T_3f2a9_row91_col0" class="data row91 col0" >Junior Data Analyst</td>
      <td id="T_3f2a9_row91_col1" class="data row91 col1" > Acquire data from primary or secondary data sources and maintain databases/data systems. Proven working experience as a data analyst or business data analyst. </td>
      <td id="T_3f2a9_row91_col2" class="data row91 col2" >9 days ago</td>
      <td id="T_3f2a9_row91_col3" class="data row91 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20OSL%20Retail%20Services%20Inc</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row92" class="row_heading level0 row92" >238</th>
      <td id="T_3f2a9_row92_col0" class="data row92 col0" >Junior Analyst, Decision Support and Evaluation</td>
      <td id="T_3f2a9_row92_col1" class="data row92 col1" > Compensation: $42,000.00 to $50,000.00 per annum. Position Type: Full-time Permanent. The Junior Analyst, Decision Support and Evaluation supports quality… </td>
      <td id="T_3f2a9_row92_col2" class="data row92 col2" >10 days ago</td>
      <td id="T_3f2a9_row92_col3" class="data row92 col3" >https://ca.indeed.com/jobs?q=Junior%20Analyst%2C%20Decision%20Support%20and%20Evaluation%20Reconnect%20Community%20Health%20Services</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row93" class="row_heading level0 row93" >36</th>
      <td id="T_3f2a9_row93_col0" class="data row93 col0" >Business Analyst I, OPL</td>
      <td id="T_3f2a9_row93_col1" class="data row93 col1" > Please note that for positions with access to financial data or funds, your credit must be in good standing. Obtain requirements from business communities using… </td>
      <td id="T_3f2a9_row93_col2" class="data row93 col2" >10 days ago</td>
      <td id="T_3f2a9_row93_col3" class="data row93 col3" >https://ca.indeed.com/jobs?q=Business%20Analyst%20I%2C%20OPL%20Intact</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row94" class="row_heading level0 row94" >37</th>
      <td id="T_3f2a9_row94_col0" class="data row94 col0" >Business Analyst I - TELUS Health</td>
      <td id="T_3f2a9_row94_col1" class="data row94 col1" > Experience analysing and reporting on performance and utilisation data. The successful candidate must be a strong creative and analytical thinker with strong… </td>
      <td id="T_3f2a9_row94_col2" class="data row94 col2" >10 days ago</td>
      <td id="T_3f2a9_row94_col3" class="data row94 col3" >https://ca.indeed.com/jobs?q=Business%20Analyst%20I%20-%20TELUS%20Health%20TELUS</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row95" class="row_heading level0 row95" >38</th>
      <td id="T_3f2a9_row95_col0" class="data row95 col0" >Junior Database Analyst</td>
      <td id="T_3f2a9_row95_col1" class="data row95 col1" > Maintain reliability, stability and data integrity of the databases. 1-2 years of experience as a data administrator in SQL server environment. </td>
      <td id="T_3f2a9_row95_col2" class="data row95 col2" >10 days ago</td>
      <td id="T_3f2a9_row95_col3" class="data row95 col3" >https://ca.indeed.com/jobs?q=Junior%20Database%20Analyst%20HealthHub%20Solutions</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row96" class="row_heading level0 row96" >240</th>
      <td id="T_3f2a9_row96_col0" class="data row96 col0" >Junior ASIC Verification Engineer</td>
      <td id="T_3f2a9_row96_col1" class="data row96 col1" > You will work closely with ASIC design and verification engineers to verify SOC function features, close function &amp; code coverage holes. </td>
      <td id="T_3f2a9_row96_col2" class="data row96 col2" >10 days ago</td>
      <td id="T_3f2a9_row96_col3" class="data row96 col3" >https://ca.indeed.com/jobs?q=Junior%20ASIC%20Verification%20Engineer%20NETINT%20Technologies%20Inc.</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row97" class="row_heading level0 row97" >239</th>
      <td id="T_3f2a9_row97_col0" class="data row97 col0" >Jr. Photonic System Test Specialist</td>
      <td id="T_3f2a9_row97_col1" class="data row97 col1" > Come create the technology that helps the world act together. Nokia is committed to innovation and technology leadership across mobile, fixed and cloud networks… </td>
      <td id="T_3f2a9_row97_col2" class="data row97 col2" >10 days ago</td>
      <td id="T_3f2a9_row97_col3" class="data row97 col3" >https://ca.indeed.com/jobs?q=Jr.%20Photonic%20System%20Test%20Specialist%20NOKIA</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row98" class="row_heading level0 row98" >34</th>
      <td id="T_3f2a9_row98_col0" class="data row98 col0" >Mechanical EIT, Data Centres</td>
      <td id="T_3f2a9_row98_col1" class="data row98 col1" > Basic knowledge of building mechanical systems to support data centres (DCs); Reporting directly to the Mechanical Engineering Team Lead or Manager, works under… </td>
      <td id="T_3f2a9_row98_col2" class="data row98 col2" >10 days ago</td>
      <td id="T_3f2a9_row98_col3" class="data row98 col3" >https://ca.indeed.com/jobs?q=Mechanical%20EIT%2C%20Data%20Centres%20WSP</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row99" class="row_heading level0 row99" >143</th>
      <td id="T_3f2a9_row99_col0" class="data row99 col0" >Développeur Junior / Intermédiaire (1 à 4 ans d’expérience)</td>
      <td id="T_3f2a9_row99_col1" class="data row99 col1" > Notre expertise en gestion de performance, reconnue depuis plus de 30 ans, nous permet aujourd’hui de nous définir comme des créateurs d’informations de gestion… </td>
      <td id="T_3f2a9_row99_col2" class="data row99 col2" >10 days ago</td>
      <td id="T_3f2a9_row99_col3" class="data row99 col3" >https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20Junior%20/%20Interm%C3%A9diaire%20%281%20%C3%A0%204%20ans%20d%E2%80%99exp%C3%A9rience%29%20DECIMAL</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row100" class="row_heading level0 row100" >35</th>
      <td id="T_3f2a9_row100_col0" class="data row100 col0" >Electrical EIT, Data Centres</td>
      <td id="T_3f2a9_row100_col1" class="data row100 col1" > Basic knowledge of power distribution topologies for data centres and familiarity with redundancy concepts; Provide support in preparation of engineering design… </td>
      <td id="T_3f2a9_row100_col2" class="data row100 col2" >10 days ago</td>
      <td id="T_3f2a9_row100_col3" class="data row100 col3" >https://ca.indeed.com/jobs?q=Electrical%20EIT%2C%20Data%20Centres%20WSP</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row101" class="row_heading level0 row101" >145</th>
      <td id="T_3f2a9_row101_col0" class="data row101 col0" >Junior Field Service Specialist</td>
      <td id="T_3f2a9_row101_col1" class="data row101 col1" > Thales people architect solutions that enable two-thirds of planes to take off and land safely. This includes Software, Hardware, Systems Design, Verification &amp;… </td>
      <td id="T_3f2a9_row101_col2" class="data row101 col2" >10 days ago</td>
      <td id="T_3f2a9_row101_col3" class="data row101 col3" >https://ca.indeed.com/jobs?q=Junior%20Field%20Service%20Specialist%20Thales%20Canada%20Inc.%2C%20Defence%20and%20Security</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row102" class="row_heading level0 row102" >146</th>
      <td id="T_3f2a9_row102_col0" class="data row102 col0" >Junior Systems Developer</td>
      <td id="T_3f2a9_row102_col1" class="data row102 col1" > The Information Technology Services department at Queen's University requires a Junior Systems Developer to design, develop, implement and troubleshoot web… </td>
      <td id="T_3f2a9_row102_col2" class="data row102 col2" >10 days ago</td>
      <td id="T_3f2a9_row102_col3" class="data row102 col3" >https://ca.indeed.com/jobs?q=Junior%20Systems%20Developer%20Queen%27s%20University</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row103" class="row_heading level0 row103" >147</th>
      <td id="T_3f2a9_row103_col0" class="data row103 col0" >Junior Analyst</td>
      <td id="T_3f2a9_row103_col1" class="data row103 col1" > A successful candidate offered employment at BCAA will need to provide proof of full vaccination prior to commencing employment. </td>
      <td id="T_3f2a9_row103_col2" class="data row103 col2" >11 days ago</td>
      <td id="T_3f2a9_row103_col3" class="data row103 col3" >https://ca.indeed.com/jobs?q=Junior%20Analyst%20BCAA</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row104" class="row_heading level0 row104" >241</th>
      <td id="T_3f2a9_row104_col0" class="data row104 col0" >Junior Electronics Engineer - Integration and Testing</td>
      <td id="T_3f2a9_row104_col1" class="data row104 col1" > Basic programming skills in C, Labview or python. Salary starting at $55,000 depending on experience. Training and development opportunities in a growing… </td>
      <td id="T_3f2a9_row104_col2" class="data row104 col2" >11 days ago</td>
      <td id="T_3f2a9_row104_col3" class="data row104 col3" >https://ca.indeed.com/jobs?q=Junior%20Electronics%20Engineer%20-%20Integration%20and%20Testing%20Preciseley%20Microtechnology</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row105" class="row_heading level0 row105" >39</th>
      <td id="T_3f2a9_row105_col0" class="data row105 col0" >DATA PROCESSING OPERATOR CLASS I</td>
      <td id="T_3f2a9_row105_col1" class="data row105 col1" > Make backup copies, copy, compress or destroy files on various media and transfer data from one. Function of the operator is to assist users and resolve… </td>
      <td id="T_3f2a9_row105_col2" class="data row105 col2" >11 days ago</td>
      <td id="T_3f2a9_row105_col3" class="data row105 col3" >https://ca.indeed.com/jobs?q=DATA%20PROCESSING%20OPERATOR%20CLASS%20I%20Kativik%20School%20Board</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row106" class="row_heading level0 row106" >149</th>
      <td id="T_3f2a9_row106_col0" class="data row106 col0" >Junior Oracle DBA</td>
      <td id="T_3f2a9_row106_col1" class="data row106 col1" > Defines and administers data base organization, standards, controls, procedures, and documentation. Provides experienced technical consulting in the definition,… </td>
      <td id="T_3f2a9_row106_col2" class="data row106 col2" >11 days ago</td>
      <td id="T_3f2a9_row106_col3" class="data row106 col3" >https://ca.indeed.com/jobs?q=Junior%20Oracle%20DBA%20AstraNorth</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row107" class="row_heading level0 row107" >148</th>
      <td id="T_3f2a9_row107_col0" class="data row107 col0" >Junior Automation Specialist</td>
      <td id="T_3f2a9_row107_col1" class="data row107 col1" > The Junior Automation Specialist position is located in Kitchener, Ontario and reports directly to the Automation Controls &amp; Engineering Manager. </td>
      <td id="T_3f2a9_row107_col2" class="data row107 col2" >11 days ago</td>
      <td id="T_3f2a9_row107_col3" class="data row107 col3" >https://ca.indeed.com/jobs?q=Junior%20Automation%20Specialist%20Roberts%20Onsite%20Inc</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row108" class="row_heading level0 row108" >152</th>
      <td id="T_3f2a9_row108_col0" class="data row108 col0" >Application Analyst I</td>
      <td id="T_3f2a9_row108_col1" class="data row108 col1" > Under direction, and based on a beginner level analyst skill set, the job participates in the planning for and then participates in the development/re… </td>
      <td id="T_3f2a9_row108_col2" class="data row108 col2" >12 days ago</td>
      <td id="T_3f2a9_row108_col3" class="data row108 col3" >https://ca.indeed.com/jobs?q=Application%20Analyst%20I%20Edmonton%20Catholic%20Schools</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row109" class="row_heading level0 row109" >151</th>
      <td id="T_3f2a9_row109_col0" class="data row109 col0" >Quality Engineer I</td>
      <td id="T_3f2a9_row109_col1" class="data row109 col1" > Provides foundational testing, automation and / or process support, research, and design input within a well-defined functional area to support the delivery of… </td>
      <td id="T_3f2a9_row109_col2" class="data row109 col2" >12 days ago</td>
      <td id="T_3f2a9_row109_col3" class="data row109 col3" >https://ca.indeed.com/jobs?q=Quality%20Engineer%20I%20TD%20Bank</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row110" class="row_heading level0 row110" >150</th>
      <td id="T_3f2a9_row110_col0" class="data row110 col0" >Junior Business Analyst</td>
      <td id="T_3f2a9_row110_col1" class="data row110 col1" > Reports to: Director of Operations. As the Business Analyst, you are responsible for conducting market analyses, analyzing both product lines and the overall… </td>
      <td id="T_3f2a9_row110_col2" class="data row110 col2" >12 days ago</td>
      <td id="T_3f2a9_row110_col3" class="data row110 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20Norsat%20International%20Inc.</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row111" class="row_heading level0 row111" >40</th>
      <td id="T_3f2a9_row111_col0" class="data row111 col0" >Jr. Cyber Security Analyst</td>
      <td id="T_3f2a9_row111_col1" class="data row111 col1" > Excellent computer and technical skills including the use of excel for data analysis. _The Wellington Catholic DSB is committed to equity for all students and… </td>
      <td id="T_3f2a9_row111_col2" class="data row111 col2" >Active 12 days ago</td>
      <td id="T_3f2a9_row111_col3" class="data row111 col3" >https://ca.indeed.com/jobs?q=Jr.%20Cyber%20Security%20Analyst%20Wellington%20Catholic%20DSB</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row112" class="row_heading level0 row112" >42</th>
      <td id="T_3f2a9_row112_col0" class="data row112 col0" >CT Data Engineer I - Power BI</td>
      <td id="T_3f2a9_row112_col1" class="data row112 col1" > Reviewing and understanding complex data sets to establish data quality and highlighting where data cleansing is required to remediate the data. </td>
      <td id="T_3f2a9_row112_col2" class="data row112 col2" >12 days ago</td>
      <td id="T_3f2a9_row112_col3" class="data row112 col3" >https://ca.indeed.com/jobs?q=CT%20Data%20Engineer%20I%20-%20Power%20BI%20EY</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row113" class="row_heading level0 row113" >41</th>
      <td id="T_3f2a9_row113_col0" class="data row113 col0" >Junior Data Engineer - OpenRoad Auto Group</td>
      <td id="T_3f2a9_row113_col1" class="data row113 col1" > Ensure high data integrity and quality from various data sources that are aligned to industry best practices. The Data Engineer is responsible for implementing … </td>
      <td id="T_3f2a9_row113_col2" class="data row113 col2" >12 days ago</td>
      <td id="T_3f2a9_row113_col3" class="data row113 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Engineer%20-%20OpenRoad%20Auto%20Group%20OpenRoad%20Auto%20Group</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row114" class="row_heading level0 row114" >154</th>
      <td id="T_3f2a9_row114_col0" class="data row114 col0" >Junior Network Administrator</td>
      <td id="T_3f2a9_row114_col1" class="data row114 col1" > This individual will work closely with the Network Administrator and together they will be responsible for serving as the first point of contact for IT services… </td>
      <td id="T_3f2a9_row114_col2" class="data row114 col2" >Active 13 days ago</td>
      <td id="T_3f2a9_row114_col3" class="data row114 col3" >https://ca.indeed.com/jobs?q=Junior%20Network%20Administrator%20Florists%20Supply%20Ltd.</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row115" class="row_heading level0 row115" >43</th>
      <td id="T_3f2a9_row115_col0" class="data row115 col0" >Junior Data Analytics Developer</td>
      <td id="T_3f2a9_row115_col1" class="data row115 col1" > Strong visual orientation for presenting data and analytics. You will work on data analytics tools related to the improvement of the electric, water and gas… </td>
      <td id="T_3f2a9_row115_col2" class="data row115 col2" >15 days ago</td>
      <td id="T_3f2a9_row115_col3" class="data row115 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Analytics%20Developer%20Tantalus</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row116" class="row_heading level0 row116" >244</th>
      <td id="T_3f2a9_row116_col0" class="data row116 col0" >Junior Network Operations Administrator</td>
      <td id="T_3f2a9_row116_col1" class="data row116 col1" > Supporting technical projects including involvement from local and global application, infrastructure, governance, and client teams. </td>
      <td id="T_3f2a9_row116_col2" class="data row116 col2" >15 days ago</td>
      <td id="T_3f2a9_row116_col3" class="data row116 col3" >https://ca.indeed.com/jobs?q=Junior%20Network%20Operations%20Administrator%20Soci%C3%A9t%C3%A9%20G%C3%A9n%C3%A9rale</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row117" class="row_heading level0 row117" >243</th>
      <td id="T_3f2a9_row117_col0" class="data row117 col0" >Administrateur.trice d'operations reseau TI Junior-(H/F)</td>
      <td id="T_3f2a9_row117_col1" class="data row117 col1" > Communication des rapports de contrôle quotidiens du matin. Détection et communication pendant les heures de bureau. O Cisco ACI ou vous êtes prêt à apprendre. </td>
      <td id="T_3f2a9_row117_col2" class="data row117 col2" >15 days ago</td>
      <td id="T_3f2a9_row117_col3" class="data row117 col3" >https://ca.indeed.com/jobs?q=Administrateur.trice%20d%27operations%20reseau%20TI%20Junior-%28H/F%29%20Soci%C3%A9t%C3%A9%20G%C3%A9n%C3%A9rale</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row118" class="row_heading level0 row118" >155</th>
      <td id="T_3f2a9_row118_col0" class="data row118 col0" >Junior Software Developer</td>
      <td id="T_3f2a9_row118_col1" class="data row118 col1" > You will make a difference in how our customers interact with our products and conduct business. Your knowledge of all layers in software will help us re-think… </td>
      <td id="T_3f2a9_row118_col2" class="data row118 col2" >15 days ago</td>
      <td id="T_3f2a9_row118_col3" class="data row118 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20Martello%20Technologies</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row119" class="row_heading level0 row119" >48</th>
      <td id="T_3f2a9_row119_col0" class="data row119 col0" >Junior Database Administrator</td>
      <td id="T_3f2a9_row119_col1" class="data row119 col1" > Questrade Financial Group (QFG) of Companies is committed to helping Canadians become much more financially successful and secure. You are if you have…. </td>
      <td id="T_3f2a9_row119_col2" class="data row119 col2" >16 days ago</td>
      <td id="T_3f2a9_row119_col3" class="data row119 col3" >https://ca.indeed.com/jobs?q=Junior%20Database%20Administrator%20Questrade%20Financial%20Group</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row120" class="row_heading level0 row120" >44</th>
      <td id="T_3f2a9_row120_col0" class="data row120 col0" >Analyst Shipping Channel I</td>
      <td id="T_3f2a9_row120_col1" class="data row120 col1" > Demonstrated skill in data analysis with exposure to a variety of data file formats. Test shipping software for compliance with Purolator’s technical… </td>
      <td id="T_3f2a9_row120_col2" class="data row120 col2" >16 days ago</td>
      <td id="T_3f2a9_row120_col3" class="data row120 col3" >https://ca.indeed.com/jobs?q=Analyst%20Shipping%20Channel%20I%20Purolator</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row121" class="row_heading level0 row121" >45</th>
      <td id="T_3f2a9_row121_col0" class="data row121 col0" >Junior Data Engineer</td>
      <td id="T_3f2a9_row121_col1" class="data row121 col1" > Ensure the quality and integrity of data. Candidates must have strong collaboration skills to work with cross-functional teams and stakeholders to ensure… </td>
      <td id="T_3f2a9_row121_col2" class="data row121 col2" >16 days ago</td>
      <td id="T_3f2a9_row121_col3" class="data row121 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Engineer%20CGI</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row122" class="row_heading level0 row122" >46</th>
      <td id="T_3f2a9_row122_col0" class="data row122 col0" >Junior/Intermediate Advanced Analytics Professional</td>
      <td id="T_3f2a9_row122_col1" class="data row122 col1" > Apply professional experience with data science software to prepare, analyze, and model data. 1+ years of professional work experience in a data analysis… </td>
      <td id="T_3f2a9_row122_col2" class="data row122 col2" >16 days ago</td>
      <td id="T_3f2a9_row122_col3" class="data row122 col3" >https://ca.indeed.com/jobs?q=Junior/Intermediate%20Advanced%20Analytics%20Professional%20Definity</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row123" class="row_heading level0 row123" >47</th>
      <td id="T_3f2a9_row123_col0" class="data row123 col0" >Junior Business Analyst</td>
      <td id="T_3f2a9_row123_col1" class="data row123 col1" > Extract data, compile reports, and develop customized reporting as required by users and management. And looking a for passionate, driven and energetic… </td>
      <td id="T_3f2a9_row123_col2" class="data row123 col2" >16 days ago</td>
      <td id="T_3f2a9_row123_col3" class="data row123 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20The%20Skyline%20Group%20of%20Companies</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row124" class="row_heading level0 row124" >157</th>
      <td id="T_3f2a9_row124_col0" class="data row124 col0" >Junior Applications Analyst</td>
      <td id="T_3f2a9_row124_col1" class="data row124 col1" > The Junior Applications Analyst - Integration plays a critical role in delivering high quality customer service and support to clients. </td>
      <td id="T_3f2a9_row124_col2" class="data row124 col2" >17 days ago</td>
      <td id="T_3f2a9_row124_col3" class="data row124 col3" >https://ca.indeed.com/jobs?q=Junior%20Applications%20Analyst%20Parkland%20Corporation</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row125" class="row_heading level0 row125" >158</th>
      <td id="T_3f2a9_row125_col0" class="data row125 col0" >Junior Software Developer</td>
      <td id="T_3f2a9_row125_col1" class="data row125 col1" > Design and implement high-impact changes. Build our dashboard to enable our creators to launch new product campaigns. Bonus points if you have....*. </td>
      <td id="T_3f2a9_row125_col2" class="data row125 col2" >17 days ago</td>
      <td id="T_3f2a9_row125_col3" class="data row125 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20Makeship</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row126" class="row_heading level0 row126" >245</th>
      <td id="T_3f2a9_row126_col0" class="data row126 col0" >Jr. Web Application Tester</td>
      <td id="T_3f2a9_row126_col1" class="data row126 col1" > For more than 40 years, Vistek has been a Canadian Success story, retailing photo, video and digital professional equipment solutions. Basic knowledge of T-SQL. </td>
      <td id="T_3f2a9_row126_col2" class="data row126 col2" >17 days ago</td>
      <td id="T_3f2a9_row126_col3" class="data row126 col3" >https://ca.indeed.com/jobs?q=Jr.%20Web%20Application%20Tester%20Vistek%20LTD</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row127" class="row_heading level0 row127" >246</th>
      <td id="T_3f2a9_row127_col0" class="data row127 col0" >Actuarial Analyst I</td>
      <td id="T_3f2a9_row127_col1" class="data row127 col1" > GI Pricing oversees the overall pricing strategy of general insurance products that aligns with TD Insurance's business objectives in compliance with… </td>
      <td id="T_3f2a9_row127_col2" class="data row127 col2" >17 days ago</td>
      <td id="T_3f2a9_row127_col3" class="data row127 col3" >https://ca.indeed.com/jobs?q=Actuarial%20Analyst%20I%20TD%20Bank</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row128" class="row_heading level0 row128" >50</th>
      <td id="T_3f2a9_row128_col0" class="data row128 col0" >Junior DBA (Database Administrator)</td>
      <td id="T_3f2a9_row128_col1" class="data row128 col1" > Provide DB2 Administrative services to application development team. Design/develop/test/support DB2 LUW database. Performance tuning and trouble shooting. </td>
      <td id="T_3f2a9_row128_col2" class="data row128 col2" >Active 17 days ago</td>
      <td id="T_3f2a9_row128_col3" class="data row128 col3" >https://ca.indeed.com/jobs?q=Junior%20DBA%20%28Database%20Administrator%29%20Dawn%20InfoTek%20Inc.</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row129" class="row_heading level0 row129" >51</th>
      <td id="T_3f2a9_row129_col0" class="data row129 col0" >Junior Business Intelligence Developer</td>
      <td id="T_3f2a9_row129_col1" class="data row129 col1" > Processes data extracts and configures data source connections using standard and custom data interfaces and APIs. </td>
      <td id="T_3f2a9_row129_col2" class="data row129 col2" >17 days ago</td>
      <td id="T_3f2a9_row129_col3" class="data row129 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Intelligence%20Developer%20Colliers%20Project%20Leaders</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row130" class="row_heading level0 row130" >49</th>
      <td id="T_3f2a9_row130_col0" class="data row130 col0" >Research Analyst I - Cancer Rehabilitation & Survivorship Pr...</td>
      <td id="T_3f2a9_row130_col1" class="data row130 col1" > At minimum, one (1) to three (3) years of related research experience preferred (e.g., study coordination experience; database design/set-up; data collection… </td>
      <td id="T_3f2a9_row130_col2" class="data row130 col2" >17 days ago</td>
      <td id="T_3f2a9_row130_col3" class="data row130 col3" >https://ca.indeed.com/jobs?q=Research%20Analyst%20I%20-%20Cancer%20Rehabilitation%20%26%20Survivorship%20Pr...%20University%20Health%20Network</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row131" class="row_heading level0 row131" >160</th>
      <td id="T_3f2a9_row131_col0" class="data row131 col0" >Technology Analyst I</td>
      <td id="T_3f2a9_row131_col1" class="data row131 col1" > As a Technology Analyst within our Pharmacy Operations team, you will leverage your technical acumen, creative problem-solving, collaboration and interpersonal… </td>
      <td id="T_3f2a9_row131_col2" class="data row131 col2" >18 days ago</td>
      <td id="T_3f2a9_row131_col3" class="data row131 col3" >https://ca.indeed.com/jobs?q=Technology%20Analyst%20I%20TELUS</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row132" class="row_heading level0 row132" >159</th>
      <td id="T_3f2a9_row132_col0" class="data row132 col0" >Junior Cloud Infrastructure Engineer</td>
      <td id="T_3f2a9_row132_col1" class="data row132 col1" > Neo Financial is looking for a full-time Junior Cloud Infrastructure Engineer (AWS) in Calgary, AB. Successful candidates make continuous improvements through a… </td>
      <td id="T_3f2a9_row132_col2" class="data row132 col2" >18 days ago</td>
      <td id="T_3f2a9_row132_col3" class="data row132 col3" >https://ca.indeed.com/jobs?q=Junior%20Cloud%20Infrastructure%20Engineer%20Neo%20Financial</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row133" class="row_heading level0 row133" >53</th>
      <td id="T_3f2a9_row133_col0" class="data row133 col0" >Junior Project Finance Analyst (Montreal or Laval)</td>
      <td id="T_3f2a9_row133_col1" class="data row133 col1" > 0 - 5 years of financial/data analysis experience. The primary focuses of this position include: evaluating construction job cost, data reporting/analysis for… </td>
      <td id="T_3f2a9_row133_col2" class="data row133 col2" >19 days ago</td>
      <td id="T_3f2a9_row133_col3" class="data row133 col3" >https://ca.indeed.com/jobs?q=Junior%20Project%20Finance%20Analyst%20%28Montreal%20or%20Laval%29%20Kiewit%20Corporation</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row134" class="row_heading level0 row134" >248</th>
      <td id="T_3f2a9_row134_col0" class="data row134 col0" >Junior Software Engineer</td>
      <td id="T_3f2a9_row134_col1" class="data row134 col1" > Develop new features and functionality for large scale highly performant transactional sites. Participate in all phases of the Software Development Life Cycle … </td>
      <td id="T_3f2a9_row134_col2" class="data row134 col2" >19 days ago</td>
      <td id="T_3f2a9_row134_col3" class="data row134 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Engineer%20OpenBet</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row135" class="row_heading level0 row135" >249</th>
      <td id="T_3f2a9_row135_col0" class="data row135 col0" >Junior Cloud Engineer OTW</td>
      <td id="T_3f2a9_row135_col1" class="data row135 col1" > Our CI/CD and System integration department plays a strategic role in making sure that the Cloud RAN solutions meet our customers’ expectations. </td>
      <td id="T_3f2a9_row135_col2" class="data row135 col2" >19 days ago</td>
      <td id="T_3f2a9_row135_col3" class="data row135 col3" >https://ca.indeed.com/jobs?q=Junior%20Cloud%20Engineer%20OTW%20Ericsson</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row136" class="row_heading level0 row136" >52</th>
      <td id="T_3f2a9_row136_col0" class="data row136 col0" >Programmeur(euse) débutant en SQL / SQL Junior Programmer</td>
      <td id="T_3f2a9_row136_col1" class="data row136 col1" > Experience working with enterprise data. Knowledge of ETL and BI data warehouse architecture is an asset. Solid computer science fundamentals such as algorithms… </td>
      <td id="T_3f2a9_row136_col2" class="data row136 col2" >19 days ago</td>
      <td id="T_3f2a9_row136_col3" class="data row136 col3" >https://ca.indeed.com/jobs?q=Programmeur%28euse%29%20d%C3%A9butant%20en%20SQL%20/%20SQL%20Junior%20Programmer%20Ove%20d%C3%A9cors%20ULC</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row137" class="row_heading level0 row137" >161</th>
      <td id="T_3f2a9_row137_col0" class="data row137 col0" >Junior Software Developer</td>
      <td id="T_3f2a9_row137_col1" class="data row137 col1" > Contributing to design ideas-Developing optimal solutions with focus on quality. Adopting DevOps methods and tooling to improve productivity and supportability… </td>
      <td id="T_3f2a9_row137_col2" class="data row137 col2" >19 days ago</td>
      <td id="T_3f2a9_row137_col3" class="data row137 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20Michael%20Page%20CA</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row138" class="row_heading level0 row138" >247</th>
      <td id="T_3f2a9_row138_col0" class="data row138 col0" >Software Engineer I</td>
      <td id="T_3f2a9_row138_col1" class="data row138 col1" > We own the development tools distribution and configuration management for Twitter’s software engineering workstations! Work in an Agile, CI/CD environment. </td>
      <td id="T_3f2a9_row138_col2" class="data row138 col2" >19 days ago</td>
      <td id="T_3f2a9_row138_col3" class="data row138 col3" >https://ca.indeed.com/jobs?q=Software%20Engineer%20I%20Twitter</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row139" class="row_heading level0 row139" >250</th>
      <td id="T_3f2a9_row139_col0" class="data row139 col0" >BIOINFORMATICS SCIENTIST I - CA</td>
      <td id="T_3f2a9_row139_col1" class="data row139 col1" > Luminex, a DiaSorin Company is seeking dedicated and talented individuals with a proactive and positive ‘can-do’ attitude to join our team. </td>
      <td id="T_3f2a9_row139_col2" class="data row139 col2" >Active 20 days ago</td>
      <td id="T_3f2a9_row139_col3" class="data row139 col3" >https://ca.indeed.com/jobs?q=BIOINFORMATICS%20SCIENTIST%20I%20-%20CA%20Luminex</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row140" class="row_heading level0 row140" >55</th>
      <td id="T_3f2a9_row140_col0" class="data row140 col0" >Data Scientist I</td>
      <td id="T_3f2a9_row140_col1" class="data row140 col1" > Technical skills in multiple facets of data science: advanced analytics, statistical modelling, machine learning &amp; data engineering. </td>
      <td id="T_3f2a9_row140_col2" class="data row140 col2" >23 days ago</td>
      <td id="T_3f2a9_row140_col3" class="data row140 col3" >https://ca.indeed.com/jobs?q=Data%20Scientist%20I%20TD%20Bank</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row141" class="row_heading level0 row141" >164</th>
      <td id="T_3f2a9_row141_col0" class="data row141 col0" >Junior Analyst - Regulatory Services (AEOI)</td>
      <td id="T_3f2a9_row141_col1" class="data row141 col1" > The Junior Analyst - Regulatory Services reports to a Senior Vice President and supports the Structured Finance Team. Fluency in English is required. </td>
      <td id="T_3f2a9_row141_col2" class="data row141 col2" >23 days ago</td>
      <td id="T_3f2a9_row141_col3" class="data row141 col3" >https://ca.indeed.com/jobs?q=Junior%20Analyst%20-%20Regulatory%20Services%20%28AEOI%29%20Maples%20Group</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row142" class="row_heading level0 row142" >163</th>
      <td id="T_3f2a9_row142_col0" class="data row142 col0" >Junior Analyst (Securities)</td>
      <td id="T_3f2a9_row142_col1" class="data row142 col1" > Job Type: Full-time permanent position. When on site, all associated government COVID-19 requirements and restrictions must be adhered to. </td>
      <td id="T_3f2a9_row142_col2" class="data row142 col2" >23 days ago</td>
      <td id="T_3f2a9_row142_col3" class="data row142 col3" >https://ca.indeed.com/jobs?q=Junior%20Analyst%20%28Securities%29%20Vincent%20Associates%20Inc.</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row143" class="row_heading level0 row143" >251</th>
      <td id="T_3f2a9_row143_col0" class="data row143 col0" >Junior Solutions Architect</td>
      <td id="T_3f2a9_row143_col1" class="data row143 col1" > Provide technical leadership throughout the development life cycle and focus on delivery of quality solutions. Define standards to guide architectural designs. </td>
      <td id="T_3f2a9_row143_col2" class="data row143 col2" >23 days ago</td>
      <td id="T_3f2a9_row143_col3" class="data row143 col3" >https://ca.indeed.com/jobs?q=Junior%20Solutions%20Architect%20BIMM</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row144" class="row_heading level0 row144" >162</th>
      <td id="T_3f2a9_row144_col0" class="data row144 col0" >Junior Quality Assurance Analyst</td>
      <td id="T_3f2a9_row144_col1" class="data row144 col1" > Junior QA analyst will be working on legacy web applications testing and testing of newly created solutions in various environments, from . </td>
      <td id="T_3f2a9_row144_col2" class="data row144 col2" >23 days ago</td>
      <td id="T_3f2a9_row144_col3" class="data row144 col3" >https://ca.indeed.com/jobs?q=Junior%20Quality%20Assurance%20Analyst%20TC%20Transcontinental</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row145" class="row_heading level0 row145" >54</th>
      <td id="T_3f2a9_row145_col0" class="data row145 col0" >Credit Analyst Trainee, Business Banking, Courtney Park, Mis...</td>
      <td id="T_3f2a9_row145_col1" class="data row145 col1" > Coordinates the management of databases; ensures alignment and integration of data in adherence with data governance standards. </td>
      <td id="T_3f2a9_row145_col2" class="data row145 col2" >23 days ago</td>
      <td id="T_3f2a9_row145_col3" class="data row145 col3" >https://ca.indeed.com/jobs?q=Credit%20Analyst%20Trainee%2C%20Business%20Banking%2C%20Courtney%20Park%2C%20Mis...%20BMO%20Financial%20Group</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row146" class="row_heading level0 row146" >56</th>
      <td id="T_3f2a9_row146_col0" class="data row146 col0" >Jr. Data Strategist</td>
      <td id="T_3f2a9_row146_col1" class="data row146 col1" > Familiarity with data metrics &amp; terminology. The Jr. Data Strategist will ingest data from search, social, and other primary/secondary data sources to formulate… </td>
      <td id="T_3f2a9_row146_col2" class="data row146 col2" >24 days ago</td>
      <td id="T_3f2a9_row146_col3" class="data row146 col3" >https://ca.indeed.com/jobs?q=Jr.%20Data%20Strategist%20Publicis%20Groupe</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row147" class="row_heading level0 row147" >57</th>
      <td id="T_3f2a9_row147_col0" class="data row147 col0" >IT Support – Junior Data Coordinator</td>
      <td id="T_3f2a9_row147_col1" class="data row147 col1" > Coordinate and manipulate all data that is derived from WM Systems. Create reports in Microsoft Excel, Word and PowerPoint as required. </td>
      <td id="T_3f2a9_row147_col2" class="data row147 col2" >24 days ago</td>
      <td id="T_3f2a9_row147_col3" class="data row147 col3" >https://ca.indeed.com/jobs?q=IT%20Support%20%E2%80%93%20Junior%20Data%20Coordinator%20Wellsite%20Masters</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row148" class="row_heading level0 row148" >58</th>
      <td id="T_3f2a9_row148_col0" class="data row148 col0" >Junior Marketing Associate</td>
      <td id="T_3f2a9_row148_col1" class="data row148 col1" > Improve new campaigns using data and feedback from existing and previous projects. Reporting to the Marketing Manager, the Marketing Associate’s is primarily… </td>
      <td id="T_3f2a9_row148_col2" class="data row148 col2" >24 days ago</td>
      <td id="T_3f2a9_row148_col3" class="data row148 col3" >https://ca.indeed.com/jobs?q=Junior%20Marketing%20Associate%20Source%20Atlantic</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row149" class="row_heading level0 row149" >252</th>
      <td id="T_3f2a9_row149_col0" class="data row149 col0" >Junior Software Engineer - Full Stack</td>
      <td id="T_3f2a9_row149_col1" class="data row149 col1" > This is an opportunity in the exciting and fast-growing transportation technology industry. Public transit is being transformed from a system of static,… </td>
      <td id="T_3f2a9_row149_col2" class="data row149 col2" >Active 25 days ago</td>
      <td id="T_3f2a9_row149_col3" class="data row149 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Engineer%20-%20Full%20Stack%20RideCo</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row150" class="row_heading level0 row150" >255</th>
      <td id="T_3f2a9_row150_col0" class="data row150 col0" >Software Engineer I/II</td>
      <td id="T_3f2a9_row150_col1" class="data row150 col1" > You will have opportunities to work on multiple layers of the technology stack, ranging from customer-focused user experience work, building scalable… </td>
      <td id="T_3f2a9_row150_col2" class="data row150 col2" >25 days ago</td>
      <td id="T_3f2a9_row150_col3" class="data row150 col3" >https://ca.indeed.com/jobs?q=Software%20Engineer%20I/II%20Microsoft</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row151" class="row_heading level0 row151" >59</th>
      <td id="T_3f2a9_row151_col0" class="data row151 col0" >Business Analyst I, AWS Commerce Platform Business Operation...</td>
      <td id="T_3f2a9_row151_col1" class="data row151 col1" > At least 1+ years of experience with data warehousing and reporting. At least 1+ years of professional working experience in related occupations of Business… </td>
      <td id="T_3f2a9_row151_col2" class="data row151 col2" >25 days ago</td>
      <td id="T_3f2a9_row151_col3" class="data row151 col3" >https://ca.indeed.com/jobs?q=Business%20Analyst%20I%2C%20AWS%20Commerce%20Platform%20Business%20Operation...%20Amazon%20Dev%20Centre%20Canada%20ULC</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row152" class="row_heading level0 row152" >254</th>
      <td id="T_3f2a9_row152_col0" class="data row152 col0" >Python Developer (Consultant I)</td>
      <td id="T_3f2a9_row152_col1" class="data row152 col1" > Our delivery model provides market-leading business outcomes using EXL’s proprietary Business EXLerator Framework™, cutting-edge analytics, digital… </td>
      <td id="T_3f2a9_row152_col2" class="data row152 col2" >25 days ago</td>
      <td id="T_3f2a9_row152_col3" class="data row152 col3" >https://ca.indeed.com/jobs?q=Python%20Developer%20%28Consultant%20I%29%20EXL%20Services</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row153" class="row_heading level0 row153" >253</th>
      <td id="T_3f2a9_row153_col0" class="data row153 col0" >Analyste junior autochtone (Poste pouvant être situé n'impor...</td>
      <td id="T_3f2a9_row153_col1" class="data row153 col1" > La diversité et l’inclusion guident tout ce que nous faisons à la SCHL. Vous aurez également à utiliser les outils appropriés (y compris R ou Python) pour… </td>
      <td id="T_3f2a9_row153_col2" class="data row153 col2" >25 days ago</td>
      <td id="T_3f2a9_row153_col3" class="data row153 col3" >https://ca.indeed.com/jobs?q=Analyste%20junior%20autochtone%20%28Poste%20pouvant%20%C3%AAtre%20situ%C3%A9%20n%27impor...%20CMHC</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row154" class="row_heading level0 row154" >60</th>
      <td id="T_3f2a9_row154_col0" class="data row154 col0" >Jr. Data Systems Manager</td>
      <td id="T_3f2a9_row154_col1" class="data row154 col1" > Providing technical expertise in data storage structures, data mining, and data cleansing as needed. Supporting initiatives for data integrity and normalization… </td>
      <td id="T_3f2a9_row154_col2" class="data row154 col2" >26 days ago</td>
      <td id="T_3f2a9_row154_col3" class="data row154 col3" >https://ca.indeed.com/jobs?q=Jr.%20Data%20Systems%20Manager%20Nelson%20Education%20LTD</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row155" class="row_heading level0 row155" >166</th>
      <td id="T_3f2a9_row155_col0" class="data row155 col0" >Junior Systems Programmer</td>
      <td id="T_3f2a9_row155_col1" class="data row155 col1" > Your work will focus on the programming components associated with the installation, service, and maintenance of integrated low voltage systems. </td>
      <td id="T_3f2a9_row155_col2" class="data row155 col2" >26 days ago</td>
      <td id="T_3f2a9_row155_col3" class="data row155 col3" >https://ca.indeed.com/jobs?q=Junior%20Systems%20Programmer%20Paladin%20Technologies</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row156" class="row_heading level0 row156" >256</th>
      <td id="T_3f2a9_row156_col0" class="data row156 col0" >Junior Developer</td>
      <td id="T_3f2a9_row156_col1" class="data row156 col1" > At ICBC, it’s our job to make sure the car insurance system works for all British Columbians, today and in the future. A career at ICBC is an opportunity to be. </td>
      <td id="T_3f2a9_row156_col2" class="data row156 col2" >27 days ago</td>
      <td id="T_3f2a9_row156_col3" class="data row156 col3" >https://ca.indeed.com/jobs?q=Junior%20Developer%20ICBC</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row157" class="row_heading level0 row157" >168</th>
      <td id="T_3f2a9_row157_col0" class="data row157 col0" >Junior Full Stack Developer</td>
      <td id="T_3f2a9_row157_col1" class="data row157 col1" > We are seeking for a Junior Full Stack Developer to join our team who will be responsible for participating in all phases of the development life-cycle,… </td>
      <td id="T_3f2a9_row157_col2" class="data row157 col2" >29 days ago</td>
      <td id="T_3f2a9_row157_col3" class="data row157 col3" >https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20Steelhaus%20Technologies</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row158" class="row_heading level0 row158" >61</th>
      <td id="T_3f2a9_row158_col0" class="data row158 col0" >Junior Buyer (Data Entry)</td>
      <td id="T_3f2a9_row158_col1" class="data row158 col1" > Our Strategic Sourcing department is currently seeking a Junior Buyer (Supply Analyst I) to join our growing team. Job Types: Full-time, Permanent. </td>
      <td id="T_3f2a9_row158_col2" class="data row158 col2" >30+ days ago</td>
      <td id="T_3f2a9_row158_col3" class="data row158 col3" >https://ca.indeed.com/jobs?q=Junior%20Buyer%20%28Data%20Entry%29%20Insurance%20Corporation%20of%20British%20Columbia</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row159" class="row_heading level0 row159" >62</th>
      <td id="T_3f2a9_row159_col0" class="data row159 col0" >Junior Financial Analyst (Business Case)</td>
      <td id="T_3f2a9_row159_col1" class="data row159 col1" > Support the Finance team in producing meaningful data/analysis. Perform reconciliation processes for various reports and systems to ensure data integrity. </td>
      <td id="T_3f2a9_row159_col2" class="data row159 col2" >30+ days ago</td>
      <td id="T_3f2a9_row159_col3" class="data row159 col3" >https://ca.indeed.com/jobs?q=Junior%20Financial%20Analyst%20%28Business%20Case%29%20Questrade%20Financial%20Group</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row160" class="row_heading level0 row160" >257</th>
      <td id="T_3f2a9_row160_col0" class="data row160 col0" >Jr Embedded Software Engineer</td>
      <td id="T_3f2a9_row160_col1" class="data row160 col1" > Software development in Python, C++. Development of test environments and tools. Write test plans for verification of software modules. </td>
      <td id="T_3f2a9_row160_col2" class="data row160 col2" >30+ days ago</td>
      <td id="T_3f2a9_row160_col3" class="data row160 col3" >https://ca.indeed.com/jobs?q=Jr%20Embedded%20Software%20Engineer%20MDA</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row161" class="row_heading level0 row161" >258</th>
      <td id="T_3f2a9_row161_col0" class="data row161 col0" >Junior Software Developer</td>
      <td id="T_3f2a9_row161_col1" class="data row161 col1" > Financial Risk Analytics is part of the IHS Markit group and provides industry leading risk analytics solutions to sell side institutions within the financial… </td>
      <td id="T_3f2a9_row161_col2" class="data row161 col2" >30+ days ago</td>
      <td id="T_3f2a9_row161_col3" class="data row161 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20S%26P%20Global</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row162" class="row_heading level0 row162" >259</th>
      <td id="T_3f2a9_row162_col0" class="data row162 col0" >Junior DevOps Engineer</td>
      <td id="T_3f2a9_row162_col1" class="data row162 col1" > For more than 20 years Global Relay has set the standard and trends in compliant communications with our multi-award winning unified communications, data… </td>
      <td id="T_3f2a9_row162_col2" class="data row162 col2" >30+ days ago</td>
      <td id="T_3f2a9_row162_col3" class="data row162 col3" >https://ca.indeed.com/jobs?q=Junior%20DevOps%20Engineer%20Global%20Relay</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row163" class="row_heading level0 row163" >98</th>
      <td id="T_3f2a9_row163_col0" class="data row163 col0" >Jr. Technical Business Analyst</td>
      <td id="T_3f2a9_row163_col1" class="data row163 col1" > Understanding of data flow diagrams and technical specifications. 2-3 years of experience working with big data sets and ETL methodologies. </td>
      <td id="T_3f2a9_row163_col2" class="data row163 col2" >30+ days ago</td>
      <td id="T_3f2a9_row163_col3" class="data row163 col3" >https://ca.indeed.com/jobs?q=Jr.%20Technical%20Business%20Analyst%20Bond%20Brand%20Loyalty%20Inc</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row164" class="row_heading level0 row164" >261</th>
      <td id="T_3f2a9_row164_col0" class="data row164 col0" >Junior Actuarial Associate - Corporate Actuarial</td>
      <td id="T_3f2a9_row164_col1" class="data row164 col1" > This position is part of the Canadian Corporate Actuarial Team, which is responsible for actuarial activities associated with SCORâ€™s Canada Life &amp; Health… </td>
      <td id="T_3f2a9_row164_col2" class="data row164 col2" >30+ days ago</td>
      <td id="T_3f2a9_row164_col3" class="data row164 col3" >https://ca.indeed.com/jobs?q=Junior%20Actuarial%20Associate%20-%20Corporate%20Actuarial%20SCOR</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row165" class="row_heading level0 row165" >283</th>
      <td id="T_3f2a9_row165_col0" class="data row165 col0" >Junior Python Developer</td>
      <td id="T_3f2a9_row165_col1" class="data row165 col1" > As an Juniour Python Developer (internally called ATD) you will perform a variety of tasks to assist the Pipeline Technical Directors (Pipeline TDs) to ensure… </td>
      <td id="T_3f2a9_row165_col2" class="data row165 col2" >30+ days ago</td>
      <td id="T_3f2a9_row165_col3" class="data row165 col3" >https://ca.indeed.com/jobs?q=Junior%20Python%20Developer%20ReDefine</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row166" class="row_heading level0 row166" >284</th>
      <td id="T_3f2a9_row166_col0" class="data row166 col0" >Junior Trader</td>
      <td id="T_3f2a9_row166_col1" class="data row166 col1" > And we swear by that every single day. They efficiently and accurately process client trade requests according to the directions received from clients. </td>
      <td id="T_3f2a9_row166_col2" class="data row166 col2" >30+ days ago</td>
      <td id="T_3f2a9_row166_col3" class="data row166 col3" >https://ca.indeed.com/jobs?q=Junior%20Trader%20Questrade%20Financial%20Group</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row167" class="row_heading level0 row167" >285</th>
      <td id="T_3f2a9_row167_col0" class="data row167 col0" >MRI Physicist, Junior</td>
      <td id="T_3f2a9_row167_col1" class="data row167 col1" > The MRI Physicist position is an opportunity to develop applications on this novel system that leverage unique aspects of Synaptive MRI systems to address… </td>
      <td id="T_3f2a9_row167_col2" class="data row167 col2" >30+ days ago</td>
      <td id="T_3f2a9_row167_col3" class="data row167 col3" >https://ca.indeed.com/jobs?q=MRI%20Physicist%2C%20Junior%20Synaptive%20Medical%20Inc.</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row168" class="row_heading level0 row168" >286</th>
      <td id="T_3f2a9_row168_col0" class="data row168 col0" >Développeur Python/Django [Junior]</td>
      <td id="T_3f2a9_row168_col1" class="data row168 col1" > Si vous êtes passionné par le développement logiciel et que vous avez le goût de rejoindre une équipe qui met l’apprentissage continu au centre de toute chose,… </td>
      <td id="T_3f2a9_row168_col2" class="data row168 col2" >30+ days ago</td>
      <td id="T_3f2a9_row168_col3" class="data row168 col3" >https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20Python/Django%20%5BJunior%5D%20FJNR%27s%20a%20Judicious%20New%20Reference</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row169" class="row_heading level0 row169" >287</th>
      <td id="T_3f2a9_row169_col0" class="data row169 col0" >Matchmove Artist - Junior</td>
      <td id="T_3f2a9_row169_col1" class="data row169 col1" > You will be working with artists with a wealth of experience on various productions. It is important to have basic knowledge of Syntheyes and matchmove. </td>
      <td id="T_3f2a9_row169_col2" class="data row169 col2" >30+ days ago</td>
      <td id="T_3f2a9_row169_col3" class="data row169 col3" >https://ca.indeed.com/jobs?q=Matchmove%20Artist%20-%20Junior%20Track%20Visual%20Effects</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row170" class="row_heading level0 row170" >288</th>
      <td id="T_3f2a9_row170_col0" class="data row170 col0" >Junior Power System Consultant- Remote Canada</td>
      <td id="T_3f2a9_row170_col1" class="data row170 col1" > Rewarding vacation entitlement with the opportunity to buy and sell your vacation depending on your lifestyle. Provide support to project teams as required. </td>
      <td id="T_3f2a9_row170_col2" class="data row170 col2" >30+ days ago</td>
      <td id="T_3f2a9_row170_col3" class="data row170 col3" >https://ca.indeed.com/jobs?q=Junior%20Power%20System%20Consultant-%20Remote%20Canada%20Siemens%20Canada%20Limited</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row171" class="row_heading level0 row171" >289</th>
      <td id="T_3f2a9_row171_col0" class="data row171 col0" >DevSecOps Engineer</td>
      <td id="T_3f2a9_row171_col1" class="data row171 col1" > CarbonCure Technologies is an award-winning clean technology company leading a global mission to reduce the carbon footprint of concrete – the world’s most used… </td>
      <td id="T_3f2a9_row171_col2" class="data row171 col2" >30+ days ago</td>
      <td id="T_3f2a9_row171_col3" class="data row171 col3" >https://ca.indeed.com/jobs?q=DevSecOps%20Engineer%20CarbonCure%20Technologies</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row172" class="row_heading level0 row172" >290</th>
      <td id="T_3f2a9_row172_col0" class="data row172 col0" >Junior Electrical Engineer</td>
      <td id="T_3f2a9_row172_col1" class="data row172 col1" > Working for BBA means being part of a team of talented people who have the passion to succeed and the drive to excel in order to provide first-class service to… </td>
      <td id="T_3f2a9_row172_col2" class="data row172 col2" >30 days ago</td>
      <td id="T_3f2a9_row172_col3" class="data row172 col3" >https://ca.indeed.com/jobs?q=Junior%20Electrical%20Engineer%20BBA%20inc.</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row173" class="row_heading level0 row173" >291</th>
      <td id="T_3f2a9_row173_col0" class="data row173 col0" >Junior Web Developer</td>
      <td id="T_3f2a9_row173_col1" class="data row173 col1" > You will work with cutting-edge technologies, learn how they are applied in the ecommerce sector, and collaborate extensively with stakeholders and the… </td>
      <td id="T_3f2a9_row173_col2" class="data row173 col2" >30+ days ago</td>
      <td id="T_3f2a9_row173_col3" class="data row173 col3" >https://ca.indeed.com/jobs?q=Junior%20Web%20Developer%20Scribendi</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row174" class="row_heading level0 row174" >292</th>
      <td id="T_3f2a9_row174_col0" class="data row174 col0" >Junior Systems Engineer (New Graduate)</td>
      <td id="T_3f2a9_row174_col1" class="data row174 col1" > Aviya provides expertise in program management, systems, software, mechanical, and hardware engineering to many of the top-tier Aerospace and Defense… </td>
      <td id="T_3f2a9_row174_col2" class="data row174 col2" >30+ days ago</td>
      <td id="T_3f2a9_row174_col3" class="data row174 col3" >https://ca.indeed.com/jobs?q=Junior%20Systems%20Engineer%20%28New%20Graduate%29%20Aviya%20Aerospace%20Systems</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row175" class="row_heading level0 row175" >293</th>
      <td id="T_3f2a9_row175_col0" class="data row175 col0" >Développeur(se) de logiciels junior</td>
      <td id="T_3f2a9_row175_col1" class="data row175 col1" > Maritime International, une division de L3Harris, est un fournisseur mondial de premier plan de contrôles-commandes non ITAR et de solutions de simulation pour… </td>
      <td id="T_3f2a9_row175_col2" class="data row175 col2" >30+ days ago</td>
      <td id="T_3f2a9_row175_col3" class="data row175 col3" >https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%28se%29%20de%20logiciels%20junior%20French%20Canadian%20Instance</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row176" class="row_heading level0 row176" >294</th>
      <td id="T_3f2a9_row176_col0" class="data row176 col0" >Junior Water Resources Engineer or Engineer-in-Training</td>
      <td id="T_3f2a9_row176_col1" class="data row176 col1" > Development of numerical models for multiple hydraulic systems including rivers, stormwater/sanitary systems, dams, wetlands, weirs and channels as well as… </td>
      <td id="T_3f2a9_row176_col2" class="data row176 col2" >30+ days ago</td>
      <td id="T_3f2a9_row176_col3" class="data row176 col3" >https://ca.indeed.com/jobs?q=Junior%20Water%20Resources%20Engineer%20or%20Engineer-in-Training%20CBCL%20Limited</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row177" class="row_heading level0 row177" >295</th>
      <td id="T_3f2a9_row177_col0" class="data row177 col0" >Junior Full Stack Developer - DevOps</td>
      <td id="T_3f2a9_row177_col1" class="data row177 col1" > Support the Canadian Surface Combatant (CSC) Tactical Operating Environment (TOE). Act as the Subject Matter Expert (SME) for relevant system design areas. </td>
      <td id="T_3f2a9_row177_col2" class="data row177 col2" >30+ days ago</td>
      <td id="T_3f2a9_row177_col3" class="data row177 col3" >https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20-%20DevOps%20Lockheed%20Martin%20Corporation</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row178" class="row_heading level0 row178" >296</th>
      <td id="T_3f2a9_row178_col0" class="data row178 col0" >Junior Cybersecurity Analyst</td>
      <td id="T_3f2a9_row178_col1" class="data row178 col1" > They will support the delivery and execution of white-glove cyber security services to an exclusive set of clients. Strong analytical and investigative skills. </td>
      <td id="T_3f2a9_row178_col2" class="data row178 col2" >30+ days ago</td>
      <td id="T_3f2a9_row178_col3" class="data row178 col3" >https://ca.indeed.com/jobs?q=Junior%20Cybersecurity%20Analyst%20Richter</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row179" class="row_heading level0 row179" >297</th>
      <td id="T_3f2a9_row179_col0" class="data row179 col0" >Junior Technical Project Manager</td>
      <td id="T_3f2a9_row179_col1" class="data row179 col1" > You have your finger on the pulse of all activities in your domain, no matter the complexity or the timelines. Our game nights are legendary.*. </td>
      <td id="T_3f2a9_row179_col2" class="data row179 col2" >30+ days ago</td>
      <td id="T_3f2a9_row179_col3" class="data row179 col3" >https://ca.indeed.com/jobs?q=Junior%20Technical%20Project%20Manager%20Leap%20Tools</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row180" class="row_heading level0 row180" >298</th>
      <td id="T_3f2a9_row180_col0" class="data row180 col0" >Software Engineer I - Quartz Core Developer</td>
      <td id="T_3f2a9_row180_col1" class="data row180 col1" > Thousands of developers are using the highly-agile platform to deliver applications to thousands of end users. Linux compute farms on-tap. </td>
      <td id="T_3f2a9_row180_col2" class="data row180 col2" >30+ days ago</td>
      <td id="T_3f2a9_row180_col3" class="data row180 col3" >https://ca.indeed.com/jobs?q=Software%20Engineer%20I%20-%20Quartz%20Core%20Developer%20Bank%20of%20America</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row181" class="row_heading level0 row181" >299</th>
      <td id="T_3f2a9_row181_col0" class="data row181 col0" >Junior DevOps Engineer</td>
      <td id="T_3f2a9_row181_col1" class="data row181 col1" > This job involves development and maintenance of scalable, secure and highly-available services and infrastructure for online gaming such as player progression,… </td>
      <td id="T_3f2a9_row181_col2" class="data row181 col2" >30+ days ago</td>
      <td id="T_3f2a9_row181_col3" class="data row181 col3" >https://ca.indeed.com/jobs?q=Junior%20DevOps%20Engineer%20Hellbent%20Games</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row182" class="row_heading level0 row182" >282</th>
      <td id="T_3f2a9_row182_col0" class="data row182 col0" >Junior Software Developers</td>
      <td id="T_3f2a9_row182_col1" class="data row182 col1" > David Aplin Group, one of Canada's Best Managed Companies, has partnered with our client to recruit Junior Software Developers. </td>
      <td id="T_3f2a9_row182_col2" class="data row182 col2" >30+ days ago</td>
      <td id="T_3f2a9_row182_col3" class="data row182 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developers%20David%20Aplin%20Group</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row183" class="row_heading level0 row183" >281</th>
      <td id="T_3f2a9_row183_col0" class="data row183 col0" >Junior Software Developer</td>
      <td id="T_3f2a9_row183_col1" class="data row183 col1" > We encourage cross functional developers to not only learn programming languages, but also the related tools and supporting systems. </td>
      <td id="T_3f2a9_row183_col2" class="data row183 col2" >30+ days ago</td>
      <td id="T_3f2a9_row183_col3" class="data row183 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20Prolucid%20Technologies</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row184" class="row_heading level0 row184" >280</th>
      <td id="T_3f2a9_row184_col0" class="data row184 col0" >Ingénieur(e) junior en mécanique des roches</td>
      <td id="T_3f2a9_row184_col1" class="data row184 col1" > Réduire les données et analyser des données d’enquête; Préparer et utiliser des modèles 2D et 3D; Participer à la caractérisation géotechnique et aux… </td>
      <td id="T_3f2a9_row184_col2" class="data row184 col2" >30+ days ago</td>
      <td id="T_3f2a9_row184_col3" class="data row184 col3" >https://ca.indeed.com/jobs?q=Ing%C3%A9nieur%28e%29%20junior%20en%20m%C3%A9canique%20des%20roches%20Golder%20Associates</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row185" class="row_heading level0 row185" >279</th>
      <td id="T_3f2a9_row185_col0" class="data row185 col0" >Junior Electrical Engineer</td>
      <td id="T_3f2a9_row185_col1" class="data row185 col1" > Work collaboratively with clients, project managers, engineers, designers and drafters in the preparation of deliverables to BBA and client standards. </td>
      <td id="T_3f2a9_row185_col2" class="data row185 col2" >30+ days ago</td>
      <td id="T_3f2a9_row185_col3" class="data row185 col3" >https://ca.indeed.com/jobs?q=Junior%20Electrical%20Engineer%20BBA</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row186" class="row_heading level0 row186" >263</th>
      <td id="T_3f2a9_row186_col0" class="data row186 col0" >Junior Software Developer</td>
      <td id="T_3f2a9_row186_col1" class="data row186 col1" > Wedge Networks is seeking candidates to fill a junior software development position on our research and development team, developing software for our network… </td>
      <td id="T_3f2a9_row186_col2" class="data row186 col2" >30+ days ago</td>
      <td id="T_3f2a9_row186_col3" class="data row186 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20Wedge%20Networks</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row187" class="row_heading level0 row187" >264</th>
      <td id="T_3f2a9_row187_col0" class="data row187 col0" >Full Stack Engineer (Junior)</td>
      <td id="T_3f2a9_row187_col1" class="data row187 col1" > At least 1 years of experience python TurboGears framework and celery library. As a FullStack Engineer, you will be responsible for implementing real-time and… </td>
      <td id="T_3f2a9_row187_col2" class="data row187 col2" >30+ days ago</td>
      <td id="T_3f2a9_row187_col3" class="data row187 col3" >https://ca.indeed.com/jobs?q=Full%20Stack%20Engineer%20%28Junior%29%20Sangoma</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row188" class="row_heading level0 row188" >265</th>
      <td id="T_3f2a9_row188_col0" class="data row188 col0" >Junior Product Management Specialist</td>
      <td id="T_3f2a9_row188_col1" class="data row188 col1" > The successful candidate will join the Product Management team and specialize in solution documentation. In this position you would be responsible for sourcing,… </td>
      <td id="T_3f2a9_row188_col2" class="data row188 col2" >30+ days ago</td>
      <td id="T_3f2a9_row188_col3" class="data row188 col3" >https://ca.indeed.com/jobs?q=Junior%20Product%20Management%20Specialist%20Fortinet</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row189" class="row_heading level0 row189" >266</th>
      <td id="T_3f2a9_row189_col0" class="data row189 col0" >Jr. / Int. Software Engineering (12mo fixed term)</td>
      <td id="T_3f2a9_row189_col1" class="data row189 col1" > Magellan Aerospace, Winnipeg is looking for a high performing Entry Level (or Intermediate) Software Engineering/Developer to join our development team. </td>
      <td id="T_3f2a9_row189_col2" class="data row189 col2" >30+ days ago</td>
      <td id="T_3f2a9_row189_col3" class="data row189 col3" >https://ca.indeed.com/jobs?q=Jr.%20/%20Int.%20Software%20Engineering%20%2812mo%20fixed%20term%29%20Magellan%20Aerospace</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row190" class="row_heading level0 row190" >63</th>
      <td id="T_3f2a9_row190_col0" class="data row190 col0" >Développeur BI junior | Junior Business Intelligence Develop...</td>
      <td id="T_3f2a9_row190_col1" class="data row190 col1" > Participating to data quality checks. Developing data models, working conjointly with senior developers. 1 to 3 years' experience in data analysis developing… </td>
      <td id="T_3f2a9_row190_col2" class="data row190 col2" >30+ days ago</td>
      <td id="T_3f2a9_row190_col3" class="data row190 col3" >https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20BI%20junior%20%7C%20Junior%20Business%20Intelligence%20Develop...%20Delmar%20International%20Inc.</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row191" class="row_heading level0 row191" >267</th>
      <td id="T_3f2a9_row191_col0" class="data row191 col0" >Junior Firmware Engineer</td>
      <td id="T_3f2a9_row191_col1" class="data row191 col1" > Participate in the development of next-generation smart grid communication devices and equipment. Involve in system design discussions and provide comprehensive… </td>
      <td id="T_3f2a9_row191_col2" class="data row191 col2" >30+ days ago</td>
      <td id="T_3f2a9_row191_col3" class="data row191 col3" >https://ca.indeed.com/jobs?q=Junior%20Firmware%20Engineer%20Corinex%20Communications</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row192" class="row_heading level0 row192" >268</th>
      <td id="T_3f2a9_row192_col0" class="data row192 col0" >Jr. NSP Software Tester</td>
      <td id="T_3f2a9_row192_col1" class="data row192 col1" > Define the test strategy, design test plans, and carry out the validation of various features, emphasizing automated tests. </td>
      <td id="T_3f2a9_row192_col2" class="data row192 col2" >30+ days ago</td>
      <td id="T_3f2a9_row192_col3" class="data row192 col3" >https://ca.indeed.com/jobs?q=Jr.%20NSP%20Software%20Tester%20NOKIA</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row193" class="row_heading level0 row193" >260</th>
      <td id="T_3f2a9_row193_col0" class="data row193 col0" >Pipeline Technical Director, Level I Vancouver, BC</td>
      <td id="T_3f2a9_row193_col1" class="data row193 col1" > The Pipeline TD develops and maintains software tools, providing front-line support to artists, and general troubleshooting of the CG pipeline in a fast-paced,… </td>
      <td id="T_3f2a9_row193_col2" class="data row193 col2" >30+ days ago</td>
      <td id="T_3f2a9_row193_col3" class="data row193 col3" >https://ca.indeed.com/jobs?q=Pipeline%20Technical%20Director%2C%20Level%20I%20Vancouver%2C%20BC%20Industrial%20Light%20%26%20Magic</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row194" class="row_heading level0 row194" >269</th>
      <td id="T_3f2a9_row194_col0" class="data row194 col0" >Applied Scientist I</td>
      <td id="T_3f2a9_row194_col1" class="data row194 col1" > MS in Computer Science, Electrical Engineering, Mathematics or Physics. Our research themes include, but are not limited to: unsupervised, self-supervised and… </td>
      <td id="T_3f2a9_row194_col2" class="data row194 col2" >30+ days ago</td>
      <td id="T_3f2a9_row194_col3" class="data row194 col3" >https://ca.indeed.com/jobs?q=Applied%20Scientist%20I%20Amazon%20Dev%20Centre%20Canada%20ULC</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row195" class="row_heading level0 row195" >271</th>
      <td id="T_3f2a9_row195_col0" class="data row195 col0" >Junior Software Engineer</td>
      <td id="T_3f2a9_row195_col1" class="data row195 col1" > The Junior Software Engineer is responsible for producing and implementing functional software solutions that align with the client needs and business goals. </td>
      <td id="T_3f2a9_row195_col2" class="data row195 col2" >30+ days ago</td>
      <td id="T_3f2a9_row195_col3" class="data row195 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Engineer%20Symend</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row196" class="row_heading level0 row196" >272</th>
      <td id="T_3f2a9_row196_col0" class="data row196 col0" >Junior DevOps Engineer</td>
      <td id="T_3f2a9_row196_col1" class="data row196 col1" > As a Junior DevOps Engineer, your main priorities will be to work with our developers to help us build and maintain our technology stack in support of the… </td>
      <td id="T_3f2a9_row196_col2" class="data row196 col2" >30+ days ago</td>
      <td id="T_3f2a9_row196_col3" class="data row196 col3" >https://ca.indeed.com/jobs?q=Junior%20DevOps%20Engineer%20Navigator%20Games</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row197" class="row_heading level0 row197" >273</th>
      <td id="T_3f2a9_row197_col0" class="data row197 col0" >Junior Pipeline TD -- Développeur du Pipeline Junior</td>
      <td id="T_3f2a9_row197_col1" class="data row197 col1" > Cinesite is recruiting a Junior Pipeline TD who will be responsible to maintain and advance the Cinesite pipeline on our animated movies and VFX shows. </td>
      <td id="T_3f2a9_row197_col2" class="data row197 col2" >30+ days ago</td>
      <td id="T_3f2a9_row197_col3" class="data row197 col3" >https://ca.indeed.com/jobs?q=Junior%20Pipeline%20TD%20--%20D%C3%A9veloppeur%20du%20Pipeline%20Junior%20Cinesite-Montreal</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row198" class="row_heading level0 row198" >274</th>
      <td id="T_3f2a9_row198_col0" class="data row198 col0" >System Integration Engineer, Junior/Intermediate</td>
      <td id="T_3f2a9_row198_col1" class="data row198 col1" > This role will be working on the Land Command Support System (LCSS) which primarily supports the Canadian Army operations by providing the information services… </td>
      <td id="T_3f2a9_row198_col2" class="data row198 col2" >30+ days ago</td>
      <td id="T_3f2a9_row198_col3" class="data row198 col3" >https://ca.indeed.com/jobs?q=System%20Integration%20Engineer%2C%20Junior/Intermediate%20General%20Dynamics%20Missions%20Systems-Canada</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row199" class="row_heading level0 row199" >275</th>
      <td id="T_3f2a9_row199_col0" class="data row199 col0" >Research Associate I/II, Assay Development</td>
      <td id="T_3f2a9_row199_col1" class="data row199 col1" > BlueRock Therapeutics is seeking a Research Associate I/II, Assay Development in Toronto ON. The successful candidate will support the development of cell… </td>
      <td id="T_3f2a9_row199_col2" class="data row199 col2" >30+ days ago</td>
      <td id="T_3f2a9_row199_col3" class="data row199 col3" >https://ca.indeed.com/jobs?q=Research%20Associate%20I/II%2C%20Assay%20Development%20BlueRock%20Therapeutics</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row200" class="row_heading level0 row200" >276</th>
      <td id="T_3f2a9_row200_col0" class="data row200 col0" >Junior Software Control Engineer</td>
      <td id="T_3f2a9_row200_col1" class="data row200 col1" > Candu Energy Inc. is a leading full-service nuclear technology company and committed to design and deliver state-of-the-art CANDU® reactors, carry out life… </td>
      <td id="T_3f2a9_row200_col2" class="data row200 col2" >30+ days ago</td>
      <td id="T_3f2a9_row200_col3" class="data row200 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Control%20Engineer%20SNC-Lavalin</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row201" class="row_heading level0 row201" >277</th>
      <td id="T_3f2a9_row201_col0" class="data row201 col0" >SCIENTIFIQUE JUNIOR – TRAITEMENT AUTOMATIQUE DU LANGAGE NATU...</td>
      <td id="T_3f2a9_row201_col1" class="data row201 col1" > Pour réussir à ce poste, le candidat retenu devra combiner des passions pour la linguistique, l’informatique ainsi que pour l’apprentissage automatique. </td>
      <td id="T_3f2a9_row201_col2" class="data row201 col2" >30+ days ago</td>
      <td id="T_3f2a9_row201_col3" class="data row201 col3" >https://ca.indeed.com/jobs?q=SCIENTIFIQUE%20JUNIOR%20%E2%80%93%20TRAITEMENT%20AUTOMATIQUE%20DU%20LANGAGE%20NATU...%20Centre%20de%20recherche%20informatique%20de%20Montr%C3%A9al...</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row202" class="row_heading level0 row202" >278</th>
      <td id="T_3f2a9_row202_col0" class="data row202 col0" >Junior Python Developer</td>
      <td id="T_3f2a9_row202_col1" class="data row202 col1" > Production Technology is an umbrella term used to describe the group of people supporting, developing and improving the tools and technologies that artists use… </td>
      <td id="T_3f2a9_row202_col2" class="data row202 col2" >30+ days ago</td>
      <td id="T_3f2a9_row202_col3" class="data row202 col3" >https://ca.indeed.com/jobs?q=Junior%20Python%20Developer%20DNEG</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row203" class="row_heading level0 row203" >270</th>
      <td id="T_3f2a9_row203_col0" class="data row203 col0" >Actuarial Trainee</td>
      <td id="T_3f2a9_row203_col1" class="data row203 col1" > If you are currently studying towards the Faculty and Institute of Actuaries (IFoA) examinations and have relevant actuarial work experience in the Life… </td>
      <td id="T_3f2a9_row203_col2" class="data row203 col2" >30+ days ago</td>
      <td id="T_3f2a9_row203_col3" class="data row203 col3" >https://ca.indeed.com/jobs?q=Actuarial%20Trainee%20Aviva</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row204" class="row_heading level0 row204" >64</th>
      <td id="T_3f2a9_row204_col0" class="data row204 col0" >Jr. Email Marketing Implementation Specialist at Digital Age...</td>
      <td id="T_3f2a9_row204_col1" class="data row204 col1" > Measure campaign results and optimize based on data. Analyzing campaign and email performance data to develop insights and make recommendations on areas for… </td>
      <td id="T_3f2a9_row204_col2" class="data row204 col2" >30+ days ago</td>
      <td id="T_3f2a9_row204_col3" class="data row204 col3" >https://ca.indeed.com/jobs?q=Jr.%20Email%20Marketing%20Implementation%20Specialist%20at%20Digital%20Age...%20Arctic%20Leaf%20Inc.</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row205" class="row_heading level0 row205" >210</th>
      <td id="T_3f2a9_row205_col0" class="data row205 col0" >Junior Settlement / Financial / Risk Analyst</td>
      <td id="T_3f2a9_row205_col1" class="data row205 col1" > Dynasty Power is currently looking to hire a Junior Settlement / Financial / Risk Analyst. This position will be accountable for settlements of trading… </td>
      <td id="T_3f2a9_row205_col2" class="data row205 col2" >30+ days ago</td>
      <td id="T_3f2a9_row205_col3" class="data row205 col3" >https://ca.indeed.com/jobs?q=Junior%20Settlement%20/%20Financial%20/%20Risk%20Analyst%20Dynasty%20Power%20Inc.</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row206" class="row_heading level0 row206" >216</th>
      <td id="T_3f2a9_row206_col0" class="data row206 col0" >Junior Software Developer (Open to Remote)</td>
      <td id="T_3f2a9_row206_col1" class="data row206 col1" > We need software developers who can help us develop and maintain systems that are always online and can handle hundreds of thousands of transactions per second. </td>
      <td id="T_3f2a9_row206_col2" class="data row206 col2" >30+ days ago</td>
      <td id="T_3f2a9_row206_col3" class="data row206 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20%28Open%20to%20Remote%29%20S%26P%20Global</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row207" class="row_heading level0 row207" >76</th>
      <td id="T_3f2a9_row207_col0" class="data row207 col0" >Financial Analyst I</td>
      <td id="T_3f2a9_row207_col1" class="data row207 col1" > Skill in performing detailed numerical computations and accurate data entry. Hours: 37.5 hours per week. As an integral member of the Grant Operations team… </td>
      <td id="T_3f2a9_row207_col2" class="data row207 col2" >30+ days ago</td>
      <td id="T_3f2a9_row207_col3" class="data row207 col3" >https://ca.indeed.com/jobs?q=Financial%20Analyst%20I%20University%20Health%20Network</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row208" class="row_heading level0 row208" >75</th>
      <td id="T_3f2a9_row208_col0" class="data row208 col0" >Junior Financial Analyst</td>
      <td id="T_3f2a9_row208_col1" class="data row208 col1" > Liaise with operational departments to gather relevant data and investigate issues that impact business growth. Resilient approach to problem solving. </td>
      <td id="T_3f2a9_row208_col2" class="data row208 col2" >30+ days ago</td>
      <td id="T_3f2a9_row208_col3" class="data row208 col3" >https://ca.indeed.com/jobs?q=Junior%20Financial%20Analyst%20Robert%20Half</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row209" class="row_heading level0 row209" >74</th>
      <td id="T_3f2a9_row209_col0" class="data row209 col0" >Jr. Business Intelligence Developer, Enterprise Analytics</td>
      <td id="T_3f2a9_row209_col1" class="data row209 col1" > Develop ETL procedures, SSIS packages and maintain data flow processes. Advanced understanding of data warehousing concepts and best practices required. </td>
      <td id="T_3f2a9_row209_col2" class="data row209 col2" >30+ days ago</td>
      <td id="T_3f2a9_row209_col3" class="data row209 col3" >https://ca.indeed.com/jobs?q=Jr.%20Business%20Intelligence%20Developer%2C%20Enterprise%20Analytics%20Southlake%20Regional%20Health%20Centre</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row210" class="row_heading level0 row210" >73</th>
      <td id="T_3f2a9_row210_col0" class="data row210 col0" >Junior Pricing Analyst</td>
      <td id="T_3f2a9_row210_col1" class="data row210 col1" > Collects data and maintains the database. Prepares financial and sku analysis reports, analyses margins and competitive market data. </td>
      <td id="T_3f2a9_row210_col2" class="data row210 col2" >30+ days ago</td>
      <td id="T_3f2a9_row210_col3" class="data row210 col3" >https://ca.indeed.com/jobs?q=Junior%20Pricing%20Analyst%20B%C3%A9langer%20UPT</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row211" class="row_heading level0 row211" >72</th>
      <td id="T_3f2a9_row211_col0" class="data row211 col0" >Jr Financial Analyst</td>
      <td id="T_3f2a9_row211_col1" class="data row211 col1" > Focus on detail and accuracy with respect to data integrity while working with large volumes of data. Collect all relevant data to prepare monthly GST/HST/QST… </td>
      <td id="T_3f2a9_row211_col2" class="data row211 col2" >30+ days ago</td>
      <td id="T_3f2a9_row211_col3" class="data row211 col3" >https://ca.indeed.com/jobs?q=Jr%20Financial%20Analyst%20MCAP</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row212" class="row_heading level0 row212" >71</th>
      <td id="T_3f2a9_row212_col0" class="data row212 col0" >Junior Sales Data Coordinator</td>
      <td id="T_3f2a9_row212_col1" class="data row212 col1" > Reporting to the National Sales &amp; Marketing Director, the Junior Sales Data Coordinator will be internal link between the pricing analyst and inside sales. </td>
      <td id="T_3f2a9_row212_col2" class="data row212 col2" >30+ days ago</td>
      <td id="T_3f2a9_row212_col3" class="data row212 col3" >https://ca.indeed.com/jobs?q=Junior%20Sales%20Data%20Coordinator%20B%C3%A9langer%20UPT</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row213" class="row_heading level0 row213" >70</th>
      <td id="T_3f2a9_row213_col0" class="data row213 col0" >Jr. Quality Assurance Analyst (Manufacturing)</td>
      <td id="T_3f2a9_row213_col1" class="data row213 col1" > Implementing approved sampling, reporting and data analysis as required. Assist in developing, maintaining, and evaluating the company Quality system meeting… </td>
      <td id="T_3f2a9_row213_col2" class="data row213 col2" >30+ days ago</td>
      <td id="T_3f2a9_row213_col3" class="data row213 col3" >https://ca.indeed.com/jobs?q=Jr.%20Quality%20Assurance%20Analyst%20%28Manufacturing%29%20MDA</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row214" class="row_heading level0 row214" >69</th>
      <td id="T_3f2a9_row214_col0" class="data row214 col0" >Associate Product Manager, Data</td>
      <td id="T_3f2a9_row214_col1" class="data row214 col1" > Collaborate with stakeholders to define their big data needs for the business. Are you actively looking for a new opportunity? Or just checking the market? </td>
      <td id="T_3f2a9_row214_col2" class="data row214 col2" >30+ days ago</td>
      <td id="T_3f2a9_row214_col3" class="data row214 col3" >https://ca.indeed.com/jobs?q=Associate%20Product%20Manager%2C%20Data%20Lightspeed%20Commerce</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row215" class="row_heading level0 row215" >300</th>
      <td id="T_3f2a9_row215_col0" class="data row215 col0" >HYDROGÉOLOGUE JUNIOR/INTERMÉDIAIRE (INGÉNIEUR OU GÉOLOGUE) M...</td>
      <td id="T_3f2a9_row215_col1" class="data row215 col1" > WSP est l’une des plus importantes firmes de services professionnels à travers le monde. Nous accordons une grande valeur à nos employés et à notre réputation. </td>
      <td id="T_3f2a9_row215_col2" class="data row215 col2" >30+ days ago</td>
      <td id="T_3f2a9_row215_col3" class="data row215 col3" >https://ca.indeed.com/jobs?q=HYDROG%C3%89OLOGUE%20JUNIOR/INTERM%C3%89DIAIRE%20%28ING%C3%89NIEUR%20OU%20G%C3%89OLOGUE%29%20M...%20WSP</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row216" class="row_heading level0 row216" >68</th>
      <td id="T_3f2a9_row216_col0" class="data row216 col0" >Data Processing Analyst I</td>
      <td id="T_3f2a9_row216_col1" class="data row216 col1" > Very good with data, numbers and patterns. Follow set instructions and run different scripts to extract data from images. Perform quality control of results. </td>
      <td id="T_3f2a9_row216_col2" class="data row216 col2" >30+ days ago</td>
      <td id="T_3f2a9_row216_col3" class="data row216 col3" >https://ca.indeed.com/jobs?q=Data%20Processing%20Analyst%20I%20ERIS%20Environmental%20Risk%20Information%20Services</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row217" class="row_heading level0 row217" >67</th>
      <td id="T_3f2a9_row217_col0" class="data row217 col0" >Junior Analyst, Indirect Tax</td>
      <td id="T_3f2a9_row217_col1" class="data row217 col1" > Familiarity with data analytics software such as Power BI and SQL and the ability to transform and visualize data is an asset. You’ve got big plans. </td>
      <td id="T_3f2a9_row217_col2" class="data row217 col2" >30+ days ago</td>
      <td id="T_3f2a9_row217_col3" class="data row217 col3" >https://ca.indeed.com/jobs?q=Junior%20Analyst%2C%20Indirect%20Tax%20KPMG</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row218" class="row_heading level0 row218" >66</th>
      <td id="T_3f2a9_row218_col0" class="data row218 col0" >Junior Data Scientist</td>
      <td id="T_3f2a9_row218_col1" class="data row218 col1" > Reviews clinical data at aggregate levels on a regular basis using analytical reporting tools to support the identification of risks and data patterns or trends… </td>
      <td id="T_3f2a9_row218_col2" class="data row218 col2" >30+ days ago</td>
      <td id="T_3f2a9_row218_col3" class="data row218 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Scientist%20Providence%20Health%20Care</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row219" class="row_heading level0 row219" >169</th>
      <td id="T_3f2a9_row219_col0" class="data row219 col0" >Junior Full Stack Developer</td>
      <td id="T_3f2a9_row219_col1" class="data row219 col1" > Visual Knowledge Share Ltd (VKS, vksapp.com) is looking for a talented, passionate, roll-up-your-sleeves, hands-on Junior Full Stack Developer. </td>
      <td id="T_3f2a9_row219_col2" class="data row219 col2" >30+ days ago</td>
      <td id="T_3f2a9_row219_col3" class="data row219 col3" >https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20Visual%20Knowledge%20Share%20Ltd</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row220" class="row_heading level0 row220" >170</th>
      <td id="T_3f2a9_row220_col0" class="data row220 col0" >Junior Web Developer</td>
      <td id="T_3f2a9_row220_col1" class="data row220 col1" > Provide programming supports to lead developer on an Seed to Sale Cannabis Enterprise Software project. Develop documentation and assistance tools to support… </td>
      <td id="T_3f2a9_row220_col2" class="data row220 col2" >30+ days ago</td>
      <td id="T_3f2a9_row220_col3" class="data row220 col3" >https://ca.indeed.com/jobs?q=Junior%20Web%20Developer%20Trellis</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row221" class="row_heading level0 row221" >171</th>
      <td id="T_3f2a9_row221_col0" class="data row221 col0" >Junior C++ Software Developer</td>
      <td id="T_3f2a9_row221_col1" class="data row221 col1" > We need software engineers who can help us develop and maintain systems that are always online and can handle hundreds of thousands of transactions per second. </td>
      <td id="T_3f2a9_row221_col2" class="data row221 col2" >30+ days ago</td>
      <td id="T_3f2a9_row221_col3" class="data row221 col3" >https://ca.indeed.com/jobs?q=Junior%20C%2B%2B%20Software%20Developer%20S%26P%20Global</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row222" class="row_heading level0 row222" >172</th>
      <td id="T_3f2a9_row222_col0" class="data row222 col0" >Junior Software Developer; Server</td>
      <td id="T_3f2a9_row222_col1" class="data row222 col1" > We offer product record keeping and distribution systems, supporting a full range of investments, accounts and regulatory bodies. </td>
      <td id="T_3f2a9_row222_col2" class="data row222 col2" >30+ days ago</td>
      <td id="T_3f2a9_row222_col3" class="data row222 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%3B%20Server%20RPM%20TECHNOLOGIES%20CORP</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row223" class="row_heading level0 row223" >77</th>
      <td id="T_3f2a9_row223_col0" class="data row223 col0" >Business Intelligence Analyst I</td>
      <td id="T_3f2a9_row223_col1" class="data row223 col1" > Basic ability to mine data, profile data and derive business solutions using data. Critically evaluate information gathered from multiple data sources and… </td>
      <td id="T_3f2a9_row223_col2" class="data row223 col2" >30+ days ago</td>
      <td id="T_3f2a9_row223_col3" class="data row223 col3" >https://ca.indeed.com/jobs?q=Business%20Intelligence%20Analyst%20I%20Finning%20International%20Inc.</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row224" class="row_heading level0 row224" >174</th>
      <td id="T_3f2a9_row224_col0" class="data row224 col0" >Analyste d'affaires, junior</td>
      <td id="T_3f2a9_row224_col1" class="data row224 col1" > / Carry out projects with potential returns and economic benefits for Quebecers. / Collaborate on dynamic teams with high-level professionals committed to… </td>
      <td id="T_3f2a9_row224_col2" class="data row224 col2" >30+ days ago</td>
      <td id="T_3f2a9_row224_col3" class="data row224 col3" >https://ca.indeed.com/jobs?q=Analyste%20d%27affaires%2C%20junior%20Caisse%20de%20d%C3%A9p%C3%B4t%20et%20placement%20du%20Qu%C3%A9bec</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row225" class="row_heading level0 row225" >78</th>
      <td id="T_3f2a9_row225_col0" class="data row225 col0" >Graduate Trainee Assistant Analyst - GTA</td>
      <td id="T_3f2a9_row225_col1" class="data row225 col1" > Ability to utilize computer software programs for data management, such as Microsoft Excel. Work independently and as a part of engineering and technical teams… </td>
      <td id="T_3f2a9_row225_col2" class="data row225 col2" >30+ days ago</td>
      <td id="T_3f2a9_row225_col3" class="data row225 col3" >https://ca.indeed.com/jobs?q=Graduate%20Trainee%20Assistant%20Analyst%20-%20GTA%20Kinectrics</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row226" class="row_heading level0 row226" >80</th>
      <td id="T_3f2a9_row226_col0" class="data row226 col0" >Junior CRM Business Analyst</td>
      <td id="T_3f2a9_row226_col1" class="data row226 col1" > Assists in analytics with need-based support on reports data extraction, compiling and manipulation. CRM Business Analyst with the delivery of CRM initiatives,… </td>
      <td id="T_3f2a9_row226_col2" class="data row226 col2" >30+ days ago</td>
      <td id="T_3f2a9_row226_col3" class="data row226 col3" >https://ca.indeed.com/jobs?q=Junior%20CRM%20Business%20Analyst%20Educators%20Financial%20Group</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row227" class="row_heading level0 row227" >97</th>
      <td id="T_3f2a9_row227_col0" class="data row227 col0" >Commercial Financial Analyst I</td>
      <td id="T_3f2a9_row227_col1" class="data row227 col1" > Data management experience and the ability to manage large sets of data and accurate reports. As part of the commercial finance organization, your position will… </td>
      <td id="T_3f2a9_row227_col2" class="data row227 col2" >30+ days ago</td>
      <td id="T_3f2a9_row227_col3" class="data row227 col3" >https://ca.indeed.com/jobs?q=Commercial%20Financial%20Analyst%20I%20Thermo%20Fisher%20Scientific</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row228" class="row_heading level0 row228" >96</th>
      <td id="T_3f2a9_row228_col0" class="data row228 col0" >Junior Business Analyst (remote)</td>
      <td id="T_3f2a9_row228_col1" class="data row228 col1" > Analyzes and evaluates complex data processing systems both current and proposed, translating business area customer information systems requirements into… </td>
      <td id="T_3f2a9_row228_col2" class="data row228 col2" >30+ days ago</td>
      <td id="T_3f2a9_row228_col3" class="data row228 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20%28remote%29%20Software%20International</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row229" class="row_heading level0 row229" >95</th>
      <td id="T_3f2a9_row229_col0" class="data row229 col0" >Quality Assurance Specialist (Backend/Data) - Junior/Interme...</td>
      <td id="T_3f2a9_row229_col1" class="data row229 col1" > Perform data analysis using SQL to ensure data quality and quality of programs. Practical experience with manipulating test data &amp; its validation techniques. </td>
      <td id="T_3f2a9_row229_col2" class="data row229 col2" >30+ days ago</td>
      <td id="T_3f2a9_row229_col3" class="data row229 col3" >https://ca.indeed.com/jobs?q=Quality%20Assurance%20Specialist%20%28Backend/Data%29%20-%20Junior/Interme...%20Klick%20Health</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row230" class="row_heading level0 row230" >94</th>
      <td id="T_3f2a9_row230_col0" class="data row230 col0" >Junior Asset Management Consultant and Data Analyst</td>
      <td id="T_3f2a9_row230_col1" class="data row230 col1" > Develop and analyze asset data to support asset management planning. Create and manage asset inventories and data structures, including the development of… </td>
      <td id="T_3f2a9_row230_col2" class="data row230 col2" >30+ days ago</td>
      <td id="T_3f2a9_row230_col3" class="data row230 col3" >https://ca.indeed.com/jobs?q=Junior%20Asset%20Management%20Consultant%20and%20Data%20Analyst%20GM%20BluePlan%20Engineering</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row231" class="row_heading level0 row231" >93</th>
      <td id="T_3f2a9_row231_col0" class="data row231 col0" >Junior Power Analyst</td>
      <td id="T_3f2a9_row231_col1" class="data row231 col1" > Analyze data to look for profitable trading strategies. Passion for trading, financial derivatives and financial data analysis considered an asset. </td>
      <td id="T_3f2a9_row231_col2" class="data row231 col2" >30+ days ago</td>
      <td id="T_3f2a9_row231_col3" class="data row231 col3" >https://ca.indeed.com/jobs?q=Junior%20Power%20Analyst%20Dynasty%20Power%20Inc.</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row232" class="row_heading level0 row232" >92</th>
      <td id="T_3f2a9_row232_col0" class="data row232 col0" >Junior Business Analyst</td>
      <td id="T_3f2a9_row232_col1" class="data row232 col1" > Work closely with IT team to satisfy data sampling, project analysis, testing verification, and other user requests from existing client databases. </td>
      <td id="T_3f2a9_row232_col2" class="data row232 col2" >30+ days ago</td>
      <td id="T_3f2a9_row232_col3" class="data row232 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20Dokainish%20%26%20Company</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row233" class="row_heading level0 row233" >91</th>
      <td id="T_3f2a9_row233_col0" class="data row233 col0" >Junior Financial Analyst</td>
      <td id="T_3f2a9_row233_col1" class="data row233 col1" > Support the Finance team in producing meaningful data/analysis. Perform reconciliation processes for various reports and systems to ensure data integrity. </td>
      <td id="T_3f2a9_row233_col2" class="data row233 col2" >30+ days ago</td>
      <td id="T_3f2a9_row233_col3" class="data row233 col3" >https://ca.indeed.com/jobs?q=Junior%20Financial%20Analyst%20Questrade%20Financial%20Group</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row234" class="row_heading level0 row234" >90</th>
      <td id="T_3f2a9_row234_col0" class="data row234 col0" >Junior Business Analyst</td>
      <td id="T_3f2a9_row234_col1" class="data row234 col1" > Management of Excel spreadsheets, including updating and editing data as required. The Business Analysis team is seeking a full-time Junior Business Analyst… </td>
      <td id="T_3f2a9_row234_col2" class="data row234 col2" >30+ days ago</td>
      <td id="T_3f2a9_row234_col3" class="data row234 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20Centrecorp%20Management%20Services%20Limited</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row235" class="row_heading level0 row235" >89</th>
      <td id="T_3f2a9_row235_col0" class="data row235 col0" >Data Architect I - Analytics Solutions</td>
      <td id="T_3f2a9_row235_col1" class="data row235 col1" > Understanding of data modelling, design and architecture principles and techniques across master data, transaction data and derived data. </td>
      <td id="T_3f2a9_row235_col2" class="data row235 col2" >30+ days ago</td>
      <td id="T_3f2a9_row235_col3" class="data row235 col3" >https://ca.indeed.com/jobs?q=Data%20Architect%20I%20-%20Analytics%20Solutions%20Electronic%20Arts</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row236" class="row_heading level0 row236" >88</th>
      <td id="T_3f2a9_row236_col0" class="data row236 col0" >Clinical Data Manager I - REMOTE</td>
      <td id="T_3f2a9_row236_col1" class="data row236 col1" > Actively cleaning data, managing CRF and query trends and data reporting to ensure a clean database lock ready for analysis. </td>
      <td id="T_3f2a9_row236_col2" class="data row236 col2" >30+ days ago</td>
      <td id="T_3f2a9_row236_col3" class="data row236 col3" >https://ca.indeed.com/jobs?q=Clinical%20Data%20Manager%20I%20-%20REMOTE%20Precision%20for%20Medicine</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row237" class="row_heading level0 row237" >87</th>
      <td id="T_3f2a9_row237_col0" class="data row237 col0" >Jr. Data Analyst</td>
      <td id="T_3f2a9_row237_col1" class="data row237 col1" > Familiarity with data mining techniques. Reporting to the Director of Analytics, you will collect, clean, organize and analyze data for the organization. </td>
      <td id="T_3f2a9_row237_col2" class="data row237 col2" >30+ days ago</td>
      <td id="T_3f2a9_row237_col3" class="data row237 col3" >https://ca.indeed.com/jobs?q=Jr.%20Data%20Analyst%20Blackstone%20Energy</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row238" class="row_heading level0 row238" >86</th>
      <td id="T_3f2a9_row238_col0" class="data row238 col0" >Jr. Data Scientist</td>
      <td id="T_3f2a9_row238_col1" class="data row238 col1" > Integration with 3rd party API’s for data collection and analysis, including weather data, time-series data, and event-based data sets. </td>
      <td id="T_3f2a9_row238_col2" class="data row238 col2" >30+ days ago</td>
      <td id="T_3f2a9_row238_col3" class="data row238 col3" >https://ca.indeed.com/jobs?q=Jr.%20Data%20Scientist%20SimpTek%20Technologies</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row239" class="row_heading level0 row239" >85</th>
      <td id="T_3f2a9_row239_col0" class="data row239 col0" >Data Steward I</td>
      <td id="T_3f2a9_row239_col1" class="data row239 col1" > Complete metadata and data quality tasks. Identify and monitor the quality of critical data elements. Manage data work activities requiring coordination across… </td>
      <td id="T_3f2a9_row239_col2" class="data row239 col2" >30+ days ago</td>
      <td id="T_3f2a9_row239_col3" class="data row239 col3" >https://ca.indeed.com/jobs?q=Data%20Steward%20I%20TD%20Bank</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row240" class="row_heading level0 row240" >84</th>
      <td id="T_3f2a9_row240_col0" class="data row240 col0" >Field Data Scientist I / Junior Field Data Scientist</td>
      <td id="T_3f2a9_row240_col1" class="data row240 col1" > Conducting research to identify data sources and data products for specific client requirements. Design and build data products. </td>
      <td id="T_3f2a9_row240_col2" class="data row240 col2" >30+ days ago</td>
      <td id="T_3f2a9_row240_col3" class="data row240 col3" >https://ca.indeed.com/jobs?q=Field%20Data%20Scientist%20I%20/%20Junior%20Field%20Data%20Scientist%20ThinkData%20Works</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row241" class="row_heading level0 row241" >83</th>
      <td id="T_3f2a9_row241_col0" class="data row241 col0" >Junior Developer – Test Data</td>
      <td id="T_3f2a9_row241_col1" class="data row241 col1" > Develop, maintain knowledge of data available from upstream sources and data within various platforms. Support data profiling using TD tooling and ad hoc system… </td>
      <td id="T_3f2a9_row241_col2" class="data row241 col2" >30+ days ago</td>
      <td id="T_3f2a9_row241_col3" class="data row241 col3" >https://ca.indeed.com/jobs?q=Junior%20Developer%20%E2%80%93%20Test%20Data%20CGI%20Inc</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row242" class="row_heading level0 row242" >82</th>
      <td id="T_3f2a9_row242_col0" class="data row242 col0" >Junior Data Analyst</td>
      <td id="T_3f2a9_row242_col1" class="data row242 col1" > Investigate data quality issues identified by data stakeholders as well as those detected by data quality monitoring rules. </td>
      <td id="T_3f2a9_row242_col2" class="data row242 col2" >30+ days ago</td>
      <td id="T_3f2a9_row242_col3" class="data row242 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20Canadian%20Niagara%20Hotels</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row243" class="row_heading level0 row243" >81</th>
      <td id="T_3f2a9_row243_col0" class="data row243 col0" >FL Junior Data Analyst</td>
      <td id="T_3f2a9_row243_col1" class="data row243 col1" > Perform data integrity and quality checks. Experience with data repositories and advance Excel skills. Junior/Intermediate Data Analyst requirement for minimum… </td>
      <td id="T_3f2a9_row243_col2" class="data row243 col2" >30+ days ago</td>
      <td id="T_3f2a9_row243_col3" class="data row243 col3" >https://ca.indeed.com/jobs?q=FL%20Junior%20Data%20Analyst%20Fujitsu</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row244" class="row_heading level0 row244" >79</th>
      <td id="T_3f2a9_row244_col0" class="data row244 col0" >Data Processing Analyst I - 1 year contract (2)</td>
      <td id="T_3f2a9_row244_col1" class="data row244 col1" > Very good with data, numbers and patterns. Follow set instructions and run different scripts to extract data from images. Perform quality control of results. </td>
      <td id="T_3f2a9_row244_col2" class="data row244 col2" >30+ days ago</td>
      <td id="T_3f2a9_row244_col3" class="data row244 col3" >https://ca.indeed.com/jobs?q=Data%20Processing%20Analyst%20I%20-%201%20year%20contract%20%282%29%20ERIS%20Info.</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row245" class="row_heading level0 row245" >65</th>
      <td id="T_3f2a9_row245_col0" class="data row245 col0" >Junior Business Analyst</td>
      <td id="T_3f2a9_row245_col1" class="data row245 col1" > Roles &amp; Responsibilities: • Elicits and documents requirements using a variety of methods, such as interviews, document analysis, requirements workshops,… </td>
      <td id="T_3f2a9_row245_col2" class="data row245 col2" >30+ days ago</td>
      <td id="T_3f2a9_row245_col3" class="data row245 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20Pivotree</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row246" class="row_heading level0 row246" >175</th>
      <td id="T_3f2a9_row246_col0" class="data row246 col0" >Jr .Net</td>
      <td id="T_3f2a9_row246_col1" class="data row246 col1" > Strong on SQL server programming. T4 hire with option to train can be considered. 1 to 2 years of experience. Strong on SQL server programming. </td>
      <td id="T_3f2a9_row246_col2" class="data row246 col2" >30+ days ago</td>
      <td id="T_3f2a9_row246_col3" class="data row246 col3" >https://ca.indeed.com/jobs?q=Jr%20.Net%20Virtusa</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row247" class="row_heading level0 row247" >177</th>
      <td id="T_3f2a9_row247_col0" class="data row247 col0" >Scientifique de données junior</td>
      <td id="T_3f2a9_row247_col1" class="data row247 col1" > Notre client recherche un scientifique de données junior. Fondée en tant qu'entreprise axée sur la création de nouvelles opportunités de vente nettes pour les… </td>
      <td id="T_3f2a9_row247_col2" class="data row247 col2" >30+ days ago</td>
      <td id="T_3f2a9_row247_col3" class="data row247 col3" >https://ca.indeed.com/jobs?q=Scientifique%20de%20donn%C3%A9es%20junior%20Robert%20Half</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row248" class="row_heading level0 row248" >199</th>
      <td id="T_3f2a9_row248_col0" class="data row248 col0" >Junior Software Quality Assurance Specialist</td>
      <td id="T_3f2a9_row248_col1" class="data row248 col1" > Review development specifications, technical documentations, and user stories to build and execute appropriate test plans. Job Type: Full-time, Permanent. </td>
      <td id="T_3f2a9_row248_col2" class="data row248 col2" >30+ days ago</td>
      <td id="T_3f2a9_row248_col3" class="data row248 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Quality%20Assurance%20Specialist%20Piicomm%20Inc.</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row249" class="row_heading level0 row249" >200</th>
      <td id="T_3f2a9_row249_col0" class="data row249 col0" >Junior Software Developer</td>
      <td id="T_3f2a9_row249_col1" class="data row249 col1" > Through your knowledge of industry-proven technologies and methodologies (see below), you will be responsible for delivering high-quality, efficient code as… </td>
      <td id="T_3f2a9_row249_col2" class="data row249 col2" >30+ days ago</td>
      <td id="T_3f2a9_row249_col3" class="data row249 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20COVNEX</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row250" class="row_heading level0 row250" >201</th>
      <td id="T_3f2a9_row250_col0" class="data row250 col0" >Reporting Analyst I (Canada Remote)</td>
      <td id="T_3f2a9_row250_col1" class="data row250 col1" > The Reporting team is a core function of the Fullscript Data team, responsible for helping our team understand performance and drive effective planning and… </td>
      <td id="T_3f2a9_row250_col2" class="data row250 col2" >30+ days ago</td>
      <td id="T_3f2a9_row250_col3" class="data row250 col3" >https://ca.indeed.com/jobs?q=Reporting%20Analyst%20I%20%28Canada%20Remote%29%20Fullscript</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row251" class="row_heading level0 row251" >202</th>
      <td id="T_3f2a9_row251_col0" class="data row251 col0" >Student Internship - Junior Developer</td>
      <td id="T_3f2a9_row251_col1" class="data row251 col1" > They solve complex issues related to scalability, growth, and usability, and are accountable for their own productivity. Work with SQL Server databases. </td>
      <td id="T_3f2a9_row251_col2" class="data row251 col2" >30+ days ago</td>
      <td id="T_3f2a9_row251_col3" class="data row251 col3" >https://ca.indeed.com/jobs?q=Student%20Internship%20-%20Junior%20Developer%20Jovaco</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row252" class="row_heading level0 row252" >203</th>
      <td id="T_3f2a9_row252_col0" class="data row252 col0" >Junior Systems Administrator</td>
      <td id="T_3f2a9_row252_col1" class="data row252 col1" > Our products help legal, finance, and tax teams be transaction and audit-ready by organizing business entity and corporate structure information. </td>
      <td id="T_3f2a9_row252_col2" class="data row252 col2" >30+ days ago</td>
      <td id="T_3f2a9_row252_col3" class="data row252 col3" >https://ca.indeed.com/jobs?q=Junior%20Systems%20Administrator%20Athennian</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row253" class="row_heading level0 row253" >204</th>
      <td id="T_3f2a9_row253_col0" class="data row253 col0" >Junior Water Resources Engineer</td>
      <td id="T_3f2a9_row253_col1" class="data row253 col1" > Design of engineering infrastructure including, but not limited to, dikes, fish habitat enhancement, dams, intakes, and hazard mitigation structures. </td>
      <td id="T_3f2a9_row253_col2" class="data row253 col2" >30+ days ago</td>
      <td id="T_3f2a9_row253_col3" class="data row253 col3" >https://ca.indeed.com/jobs?q=Junior%20Water%20Resources%20Engineer%20Kerr%20Wood%20Leidal</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row254" class="row_heading level0 row254" >206</th>
      <td id="T_3f2a9_row254_col0" class="data row254 col0" >Jr. Developer</td>
      <td id="T_3f2a9_row254_col1" class="data row254 col1" > Tjene specializes in Corporate Real Estate, Business Intelligence, and Data Management. Cross Functional: All consultants are cross trained to serve in a… </td>
      <td id="T_3f2a9_row254_col2" class="data row254 col2" >30+ days ago</td>
      <td id="T_3f2a9_row254_col3" class="data row254 col3" >https://ca.indeed.com/jobs?q=Jr.%20Developer%20Tjene%20Corp</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row255" class="row_heading level0 row255" >207</th>
      <td id="T_3f2a9_row255_col0" class="data row255 col0" >MySQL DBA I</td>
      <td id="T_3f2a9_row255_col1" class="data row255 col1" > Percona is a leader in providing best-of-breed enterprise-class support, consulting, managed services, training and software for MySQL®, MariaDB®, MongoDB®,… </td>
      <td id="T_3f2a9_row255_col2" class="data row255 col2" >30+ days ago</td>
      <td id="T_3f2a9_row255_col3" class="data row255 col3" >https://ca.indeed.com/jobs?q=MySQL%20DBA%20I%20Percona</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row256" class="row_heading level0 row256" >208</th>
      <td id="T_3f2a9_row256_col0" class="data row256 col0" >Jr. Data/Reporting Analyst</td>
      <td id="T_3f2a9_row256_col1" class="data row256 col1" > The Jr Data/Reporting Analyst will be responsible for maintaining our clients Data and Reporting needs on a Weekly/Monthly bases. </td>
      <td id="T_3f2a9_row256_col2" class="data row256 col2" >30+ days ago</td>
      <td id="T_3f2a9_row256_col3" class="data row256 col3" >https://ca.indeed.com/jobs?q=Jr.%20Data/Reporting%20Analyst%20Scarsin</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row257" class="row_heading level0 row257" >209</th>
      <td id="T_3f2a9_row257_col0" class="data row257 col0" >Junior Drupal Developer (Remote Friendly)</td>
      <td id="T_3f2a9_row257_col1" class="data row257 col1" > Acro Media is looking for a Drupal Software Developer to develop Drupal 8 and Commerce builds. If you’re desperate to break free from that office life where you… </td>
      <td id="T_3f2a9_row257_col2" class="data row257 col2" >30+ days ago</td>
      <td id="T_3f2a9_row257_col3" class="data row257 col3" >https://ca.indeed.com/jobs?q=Junior%20Drupal%20Developer%20%28Remote%20Friendly%29%20Acro%20Media</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row258" class="row_heading level0 row258" >99</th>
      <td id="T_3f2a9_row258_col0" class="data row258 col0" >Scientist I/II, Process Development Analytics</td>
      <td id="T_3f2a9_row258_col1" class="data row258 col1" > Strong practical knowledge of experimental design, and statistical analysis of data. Train and supervise junior staff members in supporting analytical… </td>
      <td id="T_3f2a9_row258_col2" class="data row258 col2" >30+ days ago</td>
      <td id="T_3f2a9_row258_col3" class="data row258 col3" >https://ca.indeed.com/jobs?q=Scientist%20I/II%2C%20Process%20Development%20Analytics%20BlueRock%20Therapeutics</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row259" class="row_heading level0 row259" >211</th>
      <td id="T_3f2a9_row259_col0" class="data row259 col0" >Junior Software Engineer</td>
      <td id="T_3f2a9_row259_col1" class="data row259 col1" > Engineering focus areas for this position include wireless gateways, LAN/WAN switches, IoT nodes, interface units and sensors. </td>
      <td id="T_3f2a9_row259_col2" class="data row259 col2" >30+ days ago</td>
      <td id="T_3f2a9_row259_col3" class="data row259 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Engineer%20Optima%20Tele.com%2C%20Inc.</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row260" class="row_heading level0 row260" >212</th>
      <td id="T_3f2a9_row260_col0" class="data row260 col0" >Junior Developer</td>
      <td id="T_3f2a9_row260_col1" class="data row260 col1" > In this role, you will work on a platform that facilitates connections between businesses and their customers, through a combination of appointments, lobby… </td>
      <td id="T_3f2a9_row260_col2" class="data row260 col2" >30+ days ago</td>
      <td id="T_3f2a9_row260_col3" class="data row260 col3" >https://ca.indeed.com/jobs?q=Junior%20Developer%20Coconut%20Software</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row261" class="row_heading level0 row261" >214</th>
      <td id="T_3f2a9_row261_col0" class="data row261 col0" >Junior Software Developer; AUI</td>
      <td id="T_3f2a9_row261_col1" class="data row261 col1" > We offer product record keeping and distribution systems, supporting a full range of investments, accounts and regulatory bodies. </td>
      <td id="T_3f2a9_row261_col2" class="data row261 col2" >30+ days ago</td>
      <td id="T_3f2a9_row261_col3" class="data row261 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%3B%20AUI%20RPM%20TECHNOLOGIES%20CORP</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row262" class="row_heading level0 row262" >198</th>
      <td id="T_3f2a9_row262_col0" class="data row262 col0" >Junior Software Developer</td>
      <td id="T_3f2a9_row262_col1" class="data row262 col1" > You will be required to learn how to leverage HTML5 for use on tablets or developing smartphone apps with any number of development frameworks. </td>
      <td id="T_3f2a9_row262_col2" class="data row262 col2" >30+ days ago</td>
      <td id="T_3f2a9_row262_col3" class="data row262 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20i-Open%20Technologies</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row263" class="row_heading level0 row263" >176</th>
      <td id="T_3f2a9_row263_col0" class="data row263 col0" >Junior Environmental Technical Administrator</td>
      <td id="T_3f2a9_row263_col1" class="data row263 col1" > Contaminated Land Assessments and Management Programs (Phase I and II ESAs, Remediations, Risk Assessments),. Field work may involve travel (sometimes to remote… </td>
      <td id="T_3f2a9_row263_col2" class="data row263 col2" >30+ days ago</td>
      <td id="T_3f2a9_row263_col3" class="data row263 col3" >https://ca.indeed.com/jobs?q=Junior%20Environmental%20Technical%20Administrator%20Parsons</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row264" class="row_heading level0 row264" >197</th>
      <td id="T_3f2a9_row264_col0" class="data row264 col0" >Junior Systems Administrator Fulltime- Permanent</td>
      <td id="T_3f2a9_row264_col1" class="data row264 col1" > Moreover, this Junior Systems Administrator role will have elevated access within client environments, therefore, the added responsibility of ensuring the… </td>
      <td id="T_3f2a9_row264_col2" class="data row264 col2" >30+ days ago</td>
      <td id="T_3f2a9_row264_col3" class="data row264 col3" >https://ca.indeed.com/jobs?q=Junior%20Systems%20Administrator%20Fulltime-%20Permanent%20ProServeIT</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row265" class="row_heading level0 row265" >195</th>
      <td id="T_3f2a9_row265_col0" class="data row265 col0" >Junior Full Stack Developer</td>
      <td id="T_3f2a9_row265_col1" class="data row265 col1" > We deliver solutions to customers in markets ranging from Medical Devices, Aerospace &amp; Defence, Nuclear &amp; Energy, Transportation, and Advanced Manufacturing. </td>
      <td id="T_3f2a9_row265_col2" class="data row265 col2" >30+ days ago</td>
      <td id="T_3f2a9_row265_col3" class="data row265 col3" >https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20Prolucid%20Technologies</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row266" class="row_heading level0 row266" >179</th>
      <td id="T_3f2a9_row266_col0" class="data row266 col0" >Junior/Intermediate Ruby on Rails Developer</td>
      <td id="T_3f2a9_row266_col1" class="data row266 col1" > You will work on customer- and admin-facing products, third party integrations both canned and bespoke, and help architect the system toward greater flexibility… </td>
      <td id="T_3f2a9_row266_col2" class="data row266 col2" >30+ days ago</td>
      <td id="T_3f2a9_row266_col3" class="data row266 col3" >https://ca.indeed.com/jobs?q=Junior/Intermediate%20Ruby%20on%20Rails%20Developer%20ZayZoon</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row267" class="row_heading level0 row267" >180</th>
      <td id="T_3f2a9_row267_col0" class="data row267 col0" >Développeur(se) Junior, Intelligence d'affaires</td>
      <td id="T_3f2a9_row267_col1" class="data row267 col1" > / Carry out projects with potential returns and economic benefits for Quebecers. / Collaborate on dynamic teams with high-level professionals committed to… </td>
      <td id="T_3f2a9_row267_col2" class="data row267 col2" >30+ days ago</td>
      <td id="T_3f2a9_row267_col3" class="data row267 col3" >https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%28se%29%20Junior%2C%20Intelligence%20d%27affaires%20Caisse%20de%20d%C3%A9p%C3%B4t%20et%20placement%20du%20Qu%C3%A9bec</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row268" class="row_heading level0 row268" >181</th>
      <td id="T_3f2a9_row268_col0" class="data row268 col0" >Junior Developer - Quality Assurance</td>
      <td id="T_3f2a9_row268_col1" class="data row268 col1" > With the arrival of transportation technologies such as CAV and Vehicle-to-Everything (V2X). The Junior Developer / QA Engineer will be entrusted to both test… </td>
      <td id="T_3f2a9_row268_col2" class="data row268 col2" >30+ days ago</td>
      <td id="T_3f2a9_row268_col3" class="data row268 col3" >https://ca.indeed.com/jobs?q=Junior%20Developer%20-%20Quality%20Assurance%20Fortran%20Traffic%20Systems</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row269" class="row_heading level0 row269" >182</th>
      <td id="T_3f2a9_row269_col0" class="data row269 col0" >Junior Devops Engineer</td>
      <td id="T_3f2a9_row269_col1" class="data row269 col1" > This role is for a fearless self-starter with good communication skills, a strong work ethic, and the ability to participate in all aspects of the software… </td>
      <td id="T_3f2a9_row269_col2" class="data row269 col2" >30+ days ago</td>
      <td id="T_3f2a9_row269_col3" class="data row269 col3" >https://ca.indeed.com/jobs?q=Junior%20Devops%20Engineer%20Scribendi</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row270" class="row_heading level0 row270" >183</th>
      <td id="T_3f2a9_row270_col0" class="data row270 col0" >Junior Programmer Analyst</td>
      <td id="T_3f2a9_row270_col1" class="data row270 col1" > Successful businesses understand their customers and their competitors. World, as well as to all levels of government (from federal to municipal in Canada). </td>
      <td id="T_3f2a9_row270_col2" class="data row270 col2" >30+ days ago</td>
      <td id="T_3f2a9_row270_col3" class="data row270 col3" >https://ca.indeed.com/jobs?q=Junior%20Programmer%20Analyst%20Advanis</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row271" class="row_heading level0 row271" >184</th>
      <td id="T_3f2a9_row271_col0" class="data row271 col0" >Junior Research Consultant</td>
      <td id="T_3f2a9_row271_col1" class="data row271 col1" > As this role is within the marketing and communications team, the ideal candidate for this position will have excellent writing skills, with a keen interest in… </td>
      <td id="T_3f2a9_row271_col2" class="data row271 col2" >30+ days ago</td>
      <td id="T_3f2a9_row271_col3" class="data row271 col3" >https://ca.indeed.com/jobs?q=Junior%20Research%20Consultant%20Arksum%20Results</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row272" class="row_heading level0 row272" >186</th>
      <td id="T_3f2a9_row272_col0" class="data row272 col0" >Junior Developer</td>
      <td id="T_3f2a9_row272_col1" class="data row272 col1" > As part of an information technology team, the Junior Developer creates efficient and effective technology based solutions to meet the operational needs of… </td>
      <td id="T_3f2a9_row272_col2" class="data row272 col2" >30+ days ago</td>
      <td id="T_3f2a9_row272_col3" class="data row272 col3" >https://ca.indeed.com/jobs?q=Junior%20Developer%20University%20of%20Alberta%20Students%27%20Union</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row273" class="row_heading level0 row273" >187</th>
      <td id="T_3f2a9_row273_col0" class="data row273 col0" >Junior Web Developer</td>
      <td id="T_3f2a9_row273_col1" class="data row273 col1" > You will work closely with our CTO on various projects, ranging from prototyping, developing and testing new product &amp; service ideas to updates and changes to… </td>
      <td id="T_3f2a9_row273_col2" class="data row273 col2" >30+ days ago</td>
      <td id="T_3f2a9_row273_col3" class="data row273 col3" >https://ca.indeed.com/jobs?q=Junior%20Web%20Developer%20Outshinery%20Creative</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row274" class="row_heading level0 row274" >188</th>
      <td id="T_3f2a9_row274_col0" class="data row274 col0" >Junior Developer/Programmer</td>
      <td id="T_3f2a9_row274_col1" class="data row274 col1" > Maintain software design consistency, aesthetics, and functionality of web application pages, communications systems, and data processing. </td>
      <td id="T_3f2a9_row274_col2" class="data row274 col2" >30+ days ago</td>
      <td id="T_3f2a9_row274_col3" class="data row274 col3" >https://ca.indeed.com/jobs?q=Junior%20Developer/Programmer%20SimplyCast</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row275" class="row_heading level0 row275" >189</th>
      <td id="T_3f2a9_row275_col0" class="data row275 col0" >Junior Actuarial Analyst</td>
      <td id="T_3f2a9_row275_col1" class="data row275 col1" > Participate in quarterly valuation processes involving the calculation of technical provisions and the analysis of results. 0 to 3 years of relevant experience. </td>
      <td id="T_3f2a9_row275_col2" class="data row275 col2" >30+ days ago</td>
      <td id="T_3f2a9_row275_col3" class="data row275 col3" >https://ca.indeed.com/jobs?q=Junior%20Actuarial%20Analyst%20SCOR</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row276" class="row_heading level0 row276" >190</th>
      <td id="T_3f2a9_row276_col0" class="data row276 col0" >Jr. Network Administrator</td>
      <td id="T_3f2a9_row276_col1" class="data row276 col1" > Administration of user accounts for various corporate systems (Active Directory, Linux accounts, O365/Azure). Management of server and hardware updates. </td>
      <td id="T_3f2a9_row276_col2" class="data row276 col2" >30+ days ago</td>
      <td id="T_3f2a9_row276_col3" class="data row276 col3" >https://ca.indeed.com/jobs?q=Jr.%20Network%20Administrator%20Evertz%20Microsystems%20Limited</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row277" class="row_heading level0 row277" >191</th>
      <td id="T_3f2a9_row277_col0" class="data row277 col0" >Junior Full Stack Developer</td>
      <td id="T_3f2a9_row277_col1" class="data row277 col1" > Markdale Financial Management is looking for a part-time Junior Full Stack Web Developer to join our team. Currently an undergrad in Computer Science. </td>
      <td id="T_3f2a9_row277_col2" class="data row277 col2" >30+ days ago</td>
      <td id="T_3f2a9_row277_col3" class="data row277 col3" >https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20Markdale%20Financial%20Management</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row278" class="row_heading level0 row278" >192</th>
      <td id="T_3f2a9_row278_col0" class="data row278 col0" >Junior Guidewire Developer</td>
      <td id="T_3f2a9_row278_col1" class="data row278 col1" > As a Business Technology Analyst, in Insurance Core Technology group within our Consulting Practice, you'll work within an engagement team and be responsible… </td>
      <td id="T_3f2a9_row278_col2" class="data row278 col2" >30+ days ago</td>
      <td id="T_3f2a9_row278_col3" class="data row278 col3" >https://ca.indeed.com/jobs?q=Junior%20Guidewire%20Developer%20Ouest</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row279" class="row_heading level0 row279" >193</th>
      <td id="T_3f2a9_row279_col0" class="data row279 col0" >Junior (Jr.) Developer (Canada Summer Jobs 2022)</td>
      <td id="T_3f2a9_row279_col1" class="data row279 col1" > Canada Summer Jobs 2022 - Position is open to all youth aged 15 to 30 years. Position starts on May 2nd, 2022 and ends on June 27th, 2022. </td>
      <td id="T_3f2a9_row279_col2" class="data row279 col2" >30+ days ago</td>
      <td id="T_3f2a9_row279_col3" class="data row279 col3" >https://ca.indeed.com/jobs?q=Junior%20%28Jr.%29%20Developer%20%28Canada%20Summer%20Jobs%202022%29%20SimplyCast</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row280" class="row_heading level0 row280" >194</th>
      <td id="T_3f2a9_row280_col0" class="data row280 col0" >Junior Software Developer - Microsoft Dynamics F&O Consultin...</td>
      <td id="T_3f2a9_row280_col1" class="data row280 col1" > BDO is looking for a full-time permanent Junior Software Developer to join our client-facing Microsoft Dynamics 365 for Finance and Operations Consulting… </td>
      <td id="T_3f2a9_row280_col2" class="data row280 col2" >30+ days ago</td>
      <td id="T_3f2a9_row280_col3" class="data row280 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20-%20Microsoft%20Dynamics%20F%26O%20Consultin...%20BDO</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row281" class="row_heading level0 row281" >196</th>
      <td id="T_3f2a9_row281_col0" class="data row281 col0" >Jr. Software Engineer - Lighthouse</td>
      <td id="T_3f2a9_row281_col1" class="data row281 col1" > Work closely with clients to understand key business issues. Gather and analyze requirements to develop impactful recommendations and solutions. </td>
      <td id="T_3f2a9_row281_col2" class="data row281 col2" >30+ days ago</td>
      <td id="T_3f2a9_row281_col3" class="data row281 col3" >https://ca.indeed.com/jobs?q=Jr.%20Software%20Engineer%20-%20Lighthouse%20KPMG</td>
    </tr>
    <tr>
      <th id="T_3f2a9_level0_row282" class="row_heading level0 row282" >301</th>
      <td id="T_3f2a9_row282_col0" class="data row282 col0" >Junior Python Solution Developer for Jeppesen - a Boeing Com...</td>
      <td id="T_3f2a9_row282_col1" class="data row282 col1" > As a Junior Software Solution Developer, you will work on our various software solutions for commercial airlines. 2+ years of working in software development. </td>
      <td id="T_3f2a9_row282_col2" class="data row282 col2" >30+ days ago</td>
      <td id="T_3f2a9_row282_col3" class="data row282 col3" >https://ca.indeed.com/jobs?q=Junior%20Python%20Solution%20Developer%20for%20Jeppesen%20-%20a%20Boeing%20Com...%20Sigma%20Software</td>
    </tr>
  </tbody>
</table>





```python

```

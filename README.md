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





<table id="T_baf65">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_baf65_level0_col0" class="col_heading level0 col0" >titles</th>
      <th id="T_baf65_level0_col1" class="col_heading level0 col1" >jobSnippets</th>
      <th id="T_baf65_level0_col2" class="col_heading level0 col2" >dates</th>
      <th id="T_baf65_level0_col3" class="col_heading level0 col3" >links</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_baf65_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_baf65_row0_col0" class="data row0 col0" >Data Scientist I</td>
      <td id="T_baf65_row0_col1" class="data row0 col1" > You are familiar with data functions including data modelling, visualization, data profiling, data origin and lineage, report design and more. </td>
      <td id="T_baf65_row0_col2" class="data row0 col2" >Just posted</td>
      <td id="T_baf65_row0_col3" class="data row0 col3" >https://ca.indeed.com/jobs?q=Data%20Scientist%20I%20TD%20Bank</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_baf65_row1_col0" class="data row1 col0" >Cloud Support Engineer I - Analytics, Support Engineering</td>
      <td id="T_baf65_row1_col1" class="data row1 col1" > Familiar with data warehousing and ETL process. Exposure to Database Fundamentals and General Troubleshooting (tuning and optimization, deadlocks, keys,… </td>
      <td id="T_baf65_row1_col2" class="data row1 col2" >Just posted</td>
      <td id="T_baf65_row1_col3" class="data row1 col3" >https://ca.indeed.com/jobs?q=Cloud%20Support%20Engineer%20I%20-%20Analytics%2C%20Support%20Engineering%20Amazon%20Web%20Services%20Canada%2C%20In</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row2" class="row_heading level0 row2" >2</th>
      <td id="T_baf65_row2_col0" class="data row2 col0" >Business Info Mgmt Analyst I</td>
      <td id="T_baf65_row2_col1" class="data row2 col1" > Develop and maintain knowledge of data available from upstream sources and data within relevant platform / applications (e.g. through data profiling, data… </td>
      <td id="T_baf65_row2_col2" class="data row2 col2" >Today</td>
      <td id="T_baf65_row2_col3" class="data row2 col3" >https://ca.indeed.com/jobs?q=Business%20Info%20Mgmt%20Analyst%20I%20TD%20Bank</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row3" class="row_heading level0 row3" >3</th>
      <td id="T_baf65_row3_col0" class="data row3 col0" >Junior Technologist (Monitoring/Data Services)</td>
      <td id="T_baf65_row3_col1" class="data row3 col1" > Aerological Observations – Preparing transmitting equipment as well as inflating and releasing large hydrogen-filled weather balloons for the purposes of… </td>
      <td id="T_baf65_row3_col2" class="data row3 col2" >Today</td>
      <td id="T_baf65_row3_col3" class="data row3 col3" >https://ca.indeed.com/jobs?q=Junior%20Technologist%20%28Monitoring/Data%20Services%29%20Environment%20and%20Climate%20Change%20Canada</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row4" class="row_heading level0 row4" >83</th>
      <td id="T_baf65_row4_col0" class="data row4 col0" >Junior Developer</td>
      <td id="T_baf65_row4_col1" class="data row4 col1" > Under the general supervision of the Manager, Application Development, the incumbent develops tests, implements and documents moderate computer programs and… </td>
      <td id="T_baf65_row4_col2" class="data row4 col2" >Just posted</td>
      <td id="T_baf65_row4_col3" class="data row4 col3" >https://ca.indeed.com/jobs?q=Junior%20Developer%20University%20of%20Manitoba</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row5" class="row_heading level0 row5" >82</th>
      <td id="T_baf65_row5_col0" class="data row5 col0" >Développeur .Net junior</td>
      <td id="T_baf65_row5_col1" class="data row5 col1" > Net pour un poste permanent pour l'un de ses clients. Grâce à vos connaissances, vous participerez au développement de différents produits, tel LogiVet,… </td>
      <td id="T_baf65_row5_col2" class="data row5 col2" >Today</td>
      <td id="T_baf65_row5_col3" class="data row5 col3" >https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20.Net%20junior%20NOVIPRO</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row6" class="row_heading level0 row6" >191</th>
      <td id="T_baf65_row6_col0" class="data row6 col0" >Junior Software Developer</td>
      <td id="T_baf65_row6_col1" class="data row6 col1" > Tasks will include adding new features to existing products, maintaining older products, and exploring the integration of new technologies. </td>
      <td id="T_baf65_row6_col2" class="data row6 col2" >Just posted</td>
      <td id="T_baf65_row6_col3" class="data row6 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20Visionstate%20Inc.</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row7" class="row_heading level0 row7" >89</th>
      <td id="T_baf65_row7_col0" class="data row7 col0" >Jr. CRM Analyst</td>
      <td id="T_baf65_row7_col1" class="data row7 col1" > With a strong, active and familial culture, Pub United is the agency’s social club, hosting events as wide reaching as Curling, Trivia Nights and more. </td>
      <td id="T_baf65_row7_col2" class="data row7 col2" >1 day ago</td>
      <td id="T_baf65_row7_col3" class="data row7 col3" >https://ca.indeed.com/jobs?q=Jr.%20CRM%20Analyst%20Publicis%20Worldwide</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row8" class="row_heading level0 row8" >88</th>
      <td id="T_baf65_row8_col0" class="data row8 col0" >Junior Systems Administrator</td>
      <td id="T_baf65_row8_col1" class="data row8 col1" > This role has customer-facing responsibilities, and our ideal hire needs to be experienced in the support and delivery of technical systems and solutions while… </td>
      <td id="T_baf65_row8_col2" class="data row8 col2" >1 day ago</td>
      <td id="T_baf65_row8_col3" class="data row8 col3" >https://ca.indeed.com/jobs?q=Junior%20Systems%20Administrator%20ProServeIT</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row9" class="row_heading level0 row9" >86</th>
      <td id="T_baf65_row9_col0" class="data row9 col0" >Software Quality Assurance Analyst (Junior to Intermediate)...</td>
      <td id="T_baf65_row9_col1" class="data row9 col1" > As a QA Analyst, you will be responsible for performing Software Applications testing. Perform testing during the test execution phase and report defects when… </td>
      <td id="T_baf65_row9_col2" class="data row9 col2" >1 day ago</td>
      <td id="T_baf65_row9_col3" class="data row9 col3" >https://ca.indeed.com/jobs?q=Software%20Quality%20Assurance%20Analyst%20%28Junior%20to%20Intermediate%29...%20Help%20Desk%20Technology</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row10" class="row_heading level0 row10" >85</th>
      <td id="T_baf65_row10_col0" class="data row10 col0" >Junior or Intermediate Quality Assurance Analyst</td>
      <td id="T_baf65_row10_col1" class="data row10 col1" > We are looking for a Junior or Intermediate Quality Assurance Analyst to work with our QA team, conducting testing of our web and desktop applications. </td>
      <td id="T_baf65_row10_col2" class="data row10 col2" >Active 1 day ago</td>
      <td id="T_baf65_row10_col3" class="data row10 col3" >https://ca.indeed.com/jobs?q=Junior%20or%20Intermediate%20Quality%20Assurance%20Analyst%20LBMX%20Inc</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row11" class="row_heading level0 row11" >192</th>
      <td id="T_baf65_row11_col0" class="data row11 col0" >Junior Support Technician</td>
      <td id="T_baf65_row11_col1" class="data row11 col1" > Remote support of our live systems in the field. Shift work with shifts between 7am and 1am Monday to Sunday. Live fault finding and problem solving. </td>
      <td id="T_baf65_row11_col2" class="data row11 col2" >1 day ago</td>
      <td id="T_baf65_row11_col3" class="data row11 col3" >https://ca.indeed.com/jobs?q=Junior%20Support%20Technician%20Gmax%20Technology%20Ltd.</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row12" class="row_heading level0 row12" >193</th>
      <td id="T_baf65_row12_col0" class="data row12 col0" >Software Engineer</td>
      <td id="T_baf65_row12_col1" class="data row12 col1" > The candidate will work closely with our robotics engineers to productize and maintain Applanix’s software for autonomous vehicle navigation. </td>
      <td id="T_baf65_row12_col2" class="data row12 col2" >1 day ago</td>
      <td id="T_baf65_row12_col3" class="data row12 col3" >https://ca.indeed.com/jobs?q=Software%20Engineer%20Applanix</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row13" class="row_heading level0 row13" >91</th>
      <td id="T_baf65_row13_col0" class="data row13 col0" >Junior Solutions Specialist</td>
      <td id="T_baf65_row13_col1" class="data row13 col1" > This person will also provide paid training sessions and work as a dedicated consultant to our customers. Unlike other CRMs, the combination of Method’s deep… </td>
      <td id="T_baf65_row13_col2" class="data row13 col2" >1 day ago</td>
      <td id="T_baf65_row13_col3" class="data row13 col3" >https://ca.indeed.com/jobs?q=Junior%20Solutions%20Specialist%20Method%3ACRM</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row14" class="row_heading level0 row14" >10</th>
      <td id="T_baf65_row14_col0" class="data row14 col0" >Wealth Ops Analyst I</td>
      <td id="T_baf65_row14_col1" class="data row14 col1" > Strong data analyst skills (1-3 years’ experience in data analyst) can be new grad with some experience and very strong technical skills. </td>
      <td id="T_baf65_row14_col2" class="data row14 col2" >1 day ago</td>
      <td id="T_baf65_row14_col3" class="data row14 col3" >https://ca.indeed.com/jobs?q=Wealth%20Ops%20Analyst%20I%20TD%20Bank</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row15" class="row_heading level0 row15" >9</th>
      <td id="T_baf65_row15_col0" class="data row15 col0" >Jr. DBA Database Administrator</td>
      <td id="T_baf65_row15_col1" class="data row15 col1" > Dawn InfoTek Inc. is a professional IT consulting team that partners with major financial institutions, investment firms and government sectors. </td>
      <td id="T_baf65_row15_col2" class="data row15 col2" >1 day ago</td>
      <td id="T_baf65_row15_col3" class="data row15 col3" >https://ca.indeed.com/jobs?q=Jr.%20DBA%20Database%20Administrator%20Dawn%20InfoTek%20Inc.</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row16" class="row_heading level0 row16" >8</th>
      <td id="T_baf65_row16_col0" class="data row16 col0" >Junior Specialist, Marketing, 12 Month Contract</td>
      <td id="T_baf65_row16_col1" class="data row16 col1" > Support the commercial teams with data analysis, to elevate understanding of brand performance and insights. In this exciting role, you will be responsible for… </td>
      <td id="T_baf65_row16_col2" class="data row16 col2" >1 day ago</td>
      <td id="T_baf65_row16_col3" class="data row16 col3" >https://ca.indeed.com/jobs?q=Junior%20Specialist%2C%20Marketing%2C%2012%20Month%20Contract%20ABBVIE</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row17" class="row_heading level0 row17" >7</th>
      <td id="T_baf65_row17_col0" class="data row17 col0" >junior business and system analyst</td>
      <td id="T_baf65_row17_col1" class="data row17 col1" > Interpret data and analyze results. Develop and implement data collection scenarios. Document data models and use cases. Knowledge of Agile, and Scrum. </td>
      <td id="T_baf65_row17_col2" class="data row17 col2" >Active 1 day ago</td>
      <td id="T_baf65_row17_col3" class="data row17 col3" >https://ca.indeed.com/jobs?q=junior%20business%20and%20system%20analyst%20Zen%20Artech%20Services</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row18" class="row_heading level0 row18" >6</th>
      <td id="T_baf65_row18_col0" class="data row18 col0" >Financial Analyst I</td>
      <td id="T_baf65_row18_col1" class="data row18 col1" > Strategic Projects: Assists the Senior Financial Analysts with data compilation for strategic projects including but not limited to, mergers, enterprise systems… </td>
      <td id="T_baf65_row18_col2" class="data row18 col2" >1 day ago</td>
      <td id="T_baf65_row18_col3" class="data row18 col3" >https://ca.indeed.com/jobs?q=Financial%20Analyst%20I%20First%20West%20Credit%20Union</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row19" class="row_heading level0 row19" >5</th>
      <td id="T_baf65_row19_col0" class="data row19 col0" >Junior Data Analyst</td>
      <td id="T_baf65_row19_col1" class="data row19 col1" > Identifies and addresses data integrity/reliability issues and uses data cleaning processes to achieve required data quality standards. </td>
      <td id="T_baf65_row19_col2" class="data row19 col2" >1 day ago</td>
      <td id="T_baf65_row19_col3" class="data row19 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20University%20of%20Waterloo</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row20" class="row_heading level0 row20" >4</th>
      <td id="T_baf65_row20_col0" class="data row20 col0" >Jr. Business Analyst</td>
      <td id="T_baf65_row20_col1" class="data row20 col1" > Summarize large volumes of data into meaningful insights via process workflow maps and executive presentations. FTE Opportunity: Possibility based on need. </td>
      <td id="T_baf65_row20_col2" class="data row20 col2" >1 day ago</td>
      <td id="T_baf65_row20_col3" class="data row20 col3" >https://ca.indeed.com/jobs?q=Jr.%20Business%20Analyst%20Dawn%20InfoTek%20Inc.</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row21" class="row_heading level0 row21" >196</th>
      <td id="T_baf65_row21_col0" class="data row21 col0" >Systems Development Engineer I, Aurora Control Plane</td>
      <td id="T_baf65_row21_col1" class="data row21 col1" > Bachelor’s Degree in Computer Science or related field, or four years of equivalent professional experience. Guarantees best-in-class availability and failover… </td>
      <td id="T_baf65_row21_col2" class="data row21 col2" >2 days ago</td>
      <td id="T_baf65_row21_col3" class="data row21 col3" >https://ca.indeed.com/jobs?q=Systems%20Development%20Engineer%20I%2C%20Aurora%20Control%20Plane%20AMZN%20CAN%20Fulfillment%20Svcs%2C%20ULC</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row22" class="row_heading level0 row22" >197</th>
      <td id="T_baf65_row22_col0" class="data row22 col0" >Junior Engineering Physicist</td>
      <td id="T_baf65_row22_col1" class="data row22 col1" > The Junior Engineering Physicist is responsible for running simulations in FLUKA/GEANT4 for development of target design for irradiation. </td>
      <td id="T_baf65_row22_col2" class="data row22 col2" >2 days ago</td>
      <td id="T_baf65_row22_col3" class="data row22 col3" >https://ca.indeed.com/jobs?q=Junior%20Engineering%20Physicist%20TRIUMF</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row23" class="row_heading level0 row23" >198</th>
      <td id="T_baf65_row23_col0" class="data row23 col0" >Engineer I-Digital Design</td>
      <td id="T_baf65_row23_col1" class="data row23 col1" > The digital design engineer will be working closely with system architecture, analog, firmware/software, and validation teams to develop next generation, state… </td>
      <td id="T_baf65_row23_col2" class="data row23 col2" >2 days ago</td>
      <td id="T_baf65_row23_col3" class="data row23 col3" >https://ca.indeed.com/jobs?q=Engineer%20I-Digital%20Design%20Microchip%20Technology</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row24" class="row_heading level0 row24" >194</th>
      <td id="T_baf65_row24_col0" class="data row24 col0" >Software Engineer in Algorithms & Optimization - Junior</td>
      <td id="T_baf65_row24_col1" class="data row24 col1" > At RideCo, you will be switching hats between Software Engineer, and Data Scientist depending on the problem at hand. Web Stack: Django, Flask, Gunicorn, Nginx. </td>
      <td id="T_baf65_row24_col2" class="data row24 col2" >2 days ago</td>
      <td id="T_baf65_row24_col3" class="data row24 col3" >https://ca.indeed.com/jobs?q=Software%20Engineer%20in%20Algorithms%20%26%20Optimization%20-%20Junior%20RideCo</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row25" class="row_heading level0 row25" >195</th>
      <td id="T_baf65_row25_col0" class="data row25 col0" >Engineer I-Computer Aided Design</td>
      <td id="T_baf65_row25_col1" class="data row25 col1" > The primary purpose of the methodology team is to enable Microchip’s ability of producing the best quality chips in terms of power, speed, and area with cutting… </td>
      <td id="T_baf65_row25_col2" class="data row25 col2" >2 days ago</td>
      <td id="T_baf65_row25_col3" class="data row25 col3" >https://ca.indeed.com/jobs?q=Engineer%20I-Computer%20Aided%20Design%20Microchip%20Technology</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row26" class="row_heading level0 row26" >94</th>
      <td id="T_baf65_row26_col0" class="data row26 col0" >Quality Engineer I</td>
      <td id="T_baf65_row26_col1" class="data row26 col1" > Seismic integrates with business-critical platforms including Microsoft, Salesforce, Google and Adobe. The Quality Engineer champions the quality of Seismic's… </td>
      <td id="T_baf65_row26_col2" class="data row26 col2" >2 days ago</td>
      <td id="T_baf65_row26_col3" class="data row26 col3" >https://ca.indeed.com/jobs?q=Quality%20Engineer%20I%20Seismic</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row27" class="row_heading level0 row27" >93</th>
      <td id="T_baf65_row27_col0" class="data row27 col0" >Junior Application Programmer Analyst, IMITS</td>
      <td id="T_baf65_row27_col1" class="data row27 col1" > As per the current Public Health Order, full vaccination against COVID-19 is a condition of employment with PHSA as of October 26, 2021. </td>
      <td id="T_baf65_row27_col2" class="data row27 col2" >2 days ago</td>
      <td id="T_baf65_row27_col3" class="data row27 col3" >https://ca.indeed.com/jobs?q=Junior%20Application%20Programmer%20Analyst%2C%20IMITS%20PHSA</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row28" class="row_heading level0 row28" >11</th>
      <td id="T_baf65_row28_col0" class="data row28 col0" >Junior Business Analyst</td>
      <td id="T_baf65_row28_col1" class="data row28 col1" > (i.e. for domains in technology, data science, etc.,…). Collaborating with multiple disciplines (creative, technology delivery, data science) to deliver… </td>
      <td id="T_baf65_row28_col2" class="data row28 col2" >2 days ago</td>
      <td id="T_baf65_row28_col3" class="data row28 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20GALE%20Partners</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row29" class="row_heading level0 row29" >12</th>
      <td id="T_baf65_row29_col0" class="data row29 col0" >Financial Analyst I, North American Customer Fulfillment</td>
      <td id="T_baf65_row29_col1" class="data row29 col1" > Identifies incomplete or inaccurate data, identifies root causes of data issues, escalates discrepancies, fixes data where possible or partners to deliver a… </td>
      <td id="T_baf65_row29_col2" class="data row29 col2" >2 days ago</td>
      <td id="T_baf65_row29_col3" class="data row29 col3" >https://ca.indeed.com/jobs?q=Financial%20Analyst%20I%2C%20North%20American%20Customer%20Fulfillment%20AMZN%20CAN%20Fulfillment%20Svcs%2C%20ULC</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row30" class="row_heading level0 row30" >13</th>
      <td id="T_baf65_row30_col0" class="data row30 col0" >Finance Ops Analyst I</td>
      <td id="T_baf65_row30_col1" class="data row30 col1" > Support the collection of meaningful data and/or research, coordinating efforts with various finance areas. Provide accurate and thorough data analysis for own… </td>
      <td id="T_baf65_row30_col2" class="data row30 col2" >2 days ago</td>
      <td id="T_baf65_row30_col3" class="data row30 col3" >https://ca.indeed.com/jobs?q=Finance%20Ops%20Analyst%20I%20TD%20Bank</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row31" class="row_heading level0 row31" >14</th>
      <td id="T_baf65_row31_col0" class="data row31 col0" >Junior Credit Card Analyst (12 Month Contract)</td>
      <td id="T_baf65_row31_col1" class="data row31 col1" > *experience with data analysis tools including using spreadsheets (MS Excel, Google Docs, Sheets) and SQL/relational databases.*. Bonus points if you have....*. </td>
      <td id="T_baf65_row31_col2" class="data row31 col2" >Active 2 days ago</td>
      <td id="T_baf65_row31_col3" class="data row31 col3" >https://ca.indeed.com/jobs?q=Junior%20Credit%20Card%20Analyst%20%2812%20Month%20Contract%29%20Credit%20Sesame</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row32" class="row_heading level0 row32" >15</th>
      <td id="T_baf65_row32_col0" class="data row32 col0" >OPÉRATRICE OU OPÉRATEUR EN INFORMATIQUE CLASSE I (100%) / DA...</td>
      <td id="T_baf65_row32_col1" class="data row32 col1" > They make backup copies, copy compressor destroy files on various media and transfer data from one workstation or organization to another. </td>
      <td id="T_baf65_row32_col2" class="data row32 col2" >2 days ago</td>
      <td id="T_baf65_row32_col3" class="data row32 col3" >https://ca.indeed.com/jobs?q=OP%C3%89RATRICE%20OU%20OP%C3%89RATEUR%20EN%20INFORMATIQUE%20CLASSE%20I%20%28100%25%29%20/%20DA...%20Riverside%20School%20Board</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row33" class="row_heading level0 row33" >16</th>
      <td id="T_baf65_row33_col0" class="data row33 col0" >Junior Data Scientist</td>
      <td id="T_baf65_row33_col1" class="data row33 col1" > Ability to make data driven decisions for any small thing. Working knowledge of Data pipeline and data-science model deployment. </td>
      <td id="T_baf65_row33_col2" class="data row33 col2" >2 days ago</td>
      <td id="T_baf65_row33_col3" class="data row33 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Scientist%20VassuTech%20Services%20Inc.%2C</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row34" class="row_heading level0 row34" >98</th>
      <td id="T_baf65_row34_col0" class="data row34 col0" >Jr. Software Engineer</td>
      <td id="T_baf65_row34_col1" class="data row34 col1" > This involves deploying local intranet webpages, tools and data integrations with our CRM, ERP and reporting systems. Support IT planning and strategy. </td>
      <td id="T_baf65_row34_col2" class="data row34 col2" >2 days ago</td>
      <td id="T_baf65_row34_col3" class="data row34 col3" >https://ca.indeed.com/jobs?q=Jr.%20Software%20Engineer%20Malpack%20Ltd</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row35" class="row_heading level0 row35" >97</th>
      <td id="T_baf65_row35_col0" class="data row35 col0" >Junior PL/SQL Developer</td>
      <td id="T_baf65_row35_col1" class="data row35 col1" > At HALIGHT, the PL/SQL Database Developer is responsible for creating and maintaining storage frameworks. The Database Developer will elucidate the intended use… </td>
      <td id="T_baf65_row35_col2" class="data row35 col2" >Active 2 days ago</td>
      <td id="T_baf65_row35_col3" class="data row35 col3" >https://ca.indeed.com/jobs?q=Junior%20PL/SQL%20Developer%20HALIGHT%20Inc.</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row36" class="row_heading level0 row36" >96</th>
      <td id="T_baf65_row36_col0" class="data row36 col0" >Junior Training Developer</td>
      <td id="T_baf65_row36_col1" class="data row36 col1" > Our Saskatchewan customer is currently looking for a Junior Training Developer on a contract until March 2023. In depth experience designing training content. </td>
      <td id="T_baf65_row36_col2" class="data row36 col2" >2 days ago</td>
      <td id="T_baf65_row36_col3" class="data row36 col3" >https://ca.indeed.com/jobs?q=Junior%20Training%20Developer%20Paradigm%20Consulting%20Group</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row37" class="row_heading level0 row37" >95</th>
      <td id="T_baf65_row37_col0" class="data row37 col0" >Jr Software Developer (FT)</td>
      <td id="T_baf65_row37_col1" class="data row37 col1" > We are looking for an intermediate full stack developer that wants to get their keyboard working on all aspects of a fully functioning web suite that also… </td>
      <td id="T_baf65_row37_col2" class="data row37 col2" >Active 2 days ago</td>
      <td id="T_baf65_row37_col3" class="data row37 col3" >https://ca.indeed.com/jobs?q=Jr%20Software%20Developer%20%28FT%29%20The%20Artona%20Group</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row38" class="row_heading level0 row38" >101</th>
      <td id="T_baf65_row38_col0" class="data row38 col0" >Conversion Analyst I</td>
      <td id="T_baf65_row38_col1" class="data row38 col1" > Vertafore Canada is looking for a Conversion Analyst who is passionate about meeting customer needs and has Insurance industry experience. </td>
      <td id="T_baf65_row38_col2" class="data row38 col2" >3 days ago</td>
      <td id="T_baf65_row38_col3" class="data row38 col3" >https://ca.indeed.com/jobs?q=Conversion%20Analyst%20I%20Vertafore</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row39" class="row_heading level0 row39" >102</th>
      <td id="T_baf65_row39_col0" class="data row39 col0" >Junior Web Developer</td>
      <td id="T_baf65_row39_col1" class="data row39 col1" > Your primary responsibility will be to take care of our clients’ sites. Delivering new, maintaining and updating existing content. </td>
      <td id="T_baf65_row39_col2" class="data row39 col2" >3 days ago</td>
      <td id="T_baf65_row39_col3" class="data row39 col3" >https://ca.indeed.com/jobs?q=Junior%20Web%20Developer%20Horizon%20Studios%20Inc.</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row40" class="row_heading level0 row40" >99</th>
      <td id="T_baf65_row40_col0" class="data row40 col0" >Junior Web Developer</td>
      <td id="T_baf65_row40_col1" class="data row40 col1" > The Junior Web Developer is responsible for design of e-mail broadcasts, and will assist with the design, redesign, and maintenance of websites for Kenilworth… </td>
      <td id="T_baf65_row40_col2" class="data row40 col2" >Active 3 days ago</td>
      <td id="T_baf65_row40_col3" class="data row40 col3" >https://ca.indeed.com/jobs?q=Junior%20Web%20Developer%20Kenilworth%20Media%20Inc</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row41" class="row_heading level0 row41" >203</th>
      <td id="T_baf65_row41_col0" class="data row41 col0" >Junior Resource Analyst</td>
      <td id="T_baf65_row41_col1" class="data row41 col1" > Data manipulation, forest estate modelling, and resource planning; and. Contribute to projects managed by project teams in areas such as, but not limited to,… </td>
      <td id="T_baf65_row41_col2" class="data row41 col2" >Active 3 days ago</td>
      <td id="T_baf65_row41_col3" class="data row41 col3" >https://ca.indeed.com/jobs?q=Junior%20Resource%20Analyst%20Ecora</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row42" class="row_heading level0 row42" >200</th>
      <td id="T_baf65_row42_col0" class="data row42 col0" >Application Support Specialist I - Information Technology</td>
      <td id="T_baf65_row42_col1" class="data row42 col1" > Are you creative, dynamic and passionate? Do you like to think outside of the box and find new ways to achieve your goals? Work Status: 1-year contract. </td>
      <td id="T_baf65_row42_col2" class="data row42 col2" >3 days ago</td>
      <td id="T_baf65_row42_col3" class="data row42 col3" >https://ca.indeed.com/jobs?q=Application%20Support%20Specialist%20I%20-%20Information%20Technology%20Corus%20Entertainment</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row43" class="row_heading level0 row43" >201</th>
      <td id="T_baf65_row43_col0" class="data row43 col0" >Junior Application Engineer and Project Manager</td>
      <td id="T_baf65_row43_col1" class="data row43 col1" > The Junior Application Engineer and Project Manager role will appeal to engineers or scientists with an interest in materials, additive manufacturing,… </td>
      <td id="T_baf65_row43_col2" class="data row43 col2" >Active 3 days ago</td>
      <td id="T_baf65_row43_col3" class="data row43 col3" >https://ca.indeed.com/jobs?q=Junior%20Application%20Engineer%20and%20Project%20Manager%20Bassetti%20Americas</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row44" class="row_heading level0 row44" >202</th>
      <td id="T_baf65_row44_col0" class="data row44 col0" >Junior Full Stack Developer</td>
      <td id="T_baf65_row44_col1" class="data row44 col1" > You have a passion for solving complex problems and working on products used by millions of people. You like to understand the big picture when it comes to… </td>
      <td id="T_baf65_row44_col2" class="data row44 col2" >Active 3 days ago</td>
      <td id="T_baf65_row44_col3" class="data row44 col3" >https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20Leap%20Tools</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row45" class="row_heading level0 row45" >100</th>
      <td id="T_baf65_row45_col0" class="data row45 col0" >Junior Database Administrator</td>
      <td id="T_baf65_row45_col1" class="data row45 col1" > CSSI currently employs over 125 staff members, consisting of insurance industry professionals, certified computer technologists and programmers, trained support… </td>
      <td id="T_baf65_row45_col2" class="data row45 col2" >Active 3 days ago</td>
      <td id="T_baf65_row45_col3" class="data row45 col3" >https://ca.indeed.com/jobs?q=Junior%20Database%20Administrator%20Custom%20Software%20Solutions%20Inc.</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row46" class="row_heading level0 row46" >204</th>
      <td id="T_baf65_row46_col0" class="data row46 col0" >Junior Embedded Software Engineer</td>
      <td id="T_baf65_row46_col1" class="data row46 col1" > If you're interested in developing the full bare-metal &amp; RTOS embedded stack (from drivers to signal processing and GUI), as well as contributing to signal… </td>
      <td id="T_baf65_row46_col2" class="data row46 col2" >Active 3 days ago</td>
      <td id="T_baf65_row46_col3" class="data row46 col3" >https://ca.indeed.com/jobs?q=Junior%20Embedded%20Software%20Engineer%20General%20Technologies%20Corp.</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row47" class="row_heading level0 row47" >199</th>
      <td id="T_baf65_row47_col0" class="data row47 col0" >Junior Embedded Software Engineer</td>
      <td id="T_baf65_row47_col1" class="data row47 col1" > In this role, you will be a member of the Engineering Design Team and will interact closely with other engineers to design and produce new and innovative… </td>
      <td id="T_baf65_row47_col2" class="data row47 col2" >Active 3 days ago</td>
      <td id="T_baf65_row47_col3" class="data row47 col3" >https://ca.indeed.com/jobs?q=Junior%20Embedded%20Software%20Engineer%20ChemChamp%20North%20America</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row48" class="row_heading level0 row48" >17</th>
      <td id="T_baf65_row48_col0" class="data row48 col0" >Jr. DB2 Database Administrator</td>
      <td id="T_baf65_row48_col1" class="data row48 col1" > Provide DB2 Administrative services to application development team. Design/develop/test/support DB2 LUW database. Performance tuning and trouble shooting. </td>
      <td id="T_baf65_row48_col2" class="data row48 col2" >Active 3 days ago</td>
      <td id="T_baf65_row48_col3" class="data row48 col3" >https://ca.indeed.com/jobs?q=Jr.%20DB2%20Database%20Administrator%20Dawn%20InfoTek%20Inc.</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row49" class="row_heading level0 row49" >18</th>
      <td id="T_baf65_row49_col0" class="data row49 col0" >Junior Customer Service/Data entry</td>
      <td id="T_baf65_row49_col1" class="data row49 col1" > Personne très organisée avec une grande attention aux détails. Compétences analytiques; capacite à identifier et résoudre les problèmes. </td>
      <td id="T_baf65_row49_col2" class="data row49 col2" >3 days ago</td>
      <td id="T_baf65_row49_col3" class="data row49 col3" >https://ca.indeed.com/jobs?q=Junior%20Customer%20Service/Data%20entry%20Corporation%20Dynamo%20Logistik</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row50" class="row_heading level0 row50" >103</th>
      <td id="T_baf65_row50_col0" class="data row50 col0" >Jr. Developer</td>
      <td id="T_baf65_row50_col1" class="data row50 col1" > The Jr. Developer will participate in all phases of the software development life cycle including design, development, enhancement, and maintenance. </td>
      <td id="T_baf65_row50_col2" class="data row50 col2" >4 days ago</td>
      <td id="T_baf65_row50_col3" class="data row50 col3" >https://ca.indeed.com/jobs?q=Jr.%20Developer%20taq</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row51" class="row_heading level0 row51" >105</th>
      <td id="T_baf65_row51_col0" class="data row51 col0" >Développeur QA Junior</td>
      <td id="T_baf65_row51_col1" class="data row51 col1" > Un leader mondial dans les logiciels spécialisés en Revenue Management (RM) pour le transport de passagers, recherche actuellement un Développeur QA pour… </td>
      <td id="T_baf65_row51_col2" class="data row51 col2" >Active 4 days ago</td>
      <td id="T_baf65_row51_col3" class="data row51 col3" >https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20QA%20Junior%20Tannous%20HR%20Solutions</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row52" class="row_heading level0 row52" >106</th>
      <td id="T_baf65_row52_col0" class="data row52 col0" >Junior Full Stack Software Developer - New Grad Opportunity</td>
      <td id="T_baf65_row52_col1" class="data row52 col1" > We’re looking for a full stack engineer with progressive technical experience, sharp coding skills, and a passion for building innovative products in a high… </td>
      <td id="T_baf65_row52_col2" class="data row52 col2" >4 days ago</td>
      <td id="T_baf65_row52_col3" class="data row52 col3" >https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Software%20Developer%20-%20New%20Grad%20Opportunity%20Aislelabs</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row53" class="row_heading level0 row53" >107</th>
      <td id="T_baf65_row53_col0" class="data row53 col0" >JUNIOR CASE COSTING ANALYST, FT</td>
      <td id="T_baf65_row53_col1" class="data row53 col1" > Reporting to the Supervisor Funding Performance, the successful applicant will be an integral part of the case costing team providing support for the… </td>
      <td id="T_baf65_row53_col2" class="data row53 col2" >4 days ago</td>
      <td id="T_baf65_row53_col3" class="data row53 col3" >https://ca.indeed.com/jobs?q=JUNIOR%20CASE%20COSTING%20ANALYST%2C%20FT%20Niagara%20Health%20System</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row54" class="row_heading level0 row54" >108</th>
      <td id="T_baf65_row54_col0" class="data row54 col0" >Junior Analyst</td>
      <td id="T_baf65_row54_col1" class="data row54 col1" > Reporting to the Business Analyst, the Junior Analyst collects data, models scenarios and provides insights to support business decision making across all… </td>
      <td id="T_baf65_row54_col2" class="data row54 col2" >Active 4 days ago</td>
      <td id="T_baf65_row54_col3" class="data row54 col3" >https://ca.indeed.com/jobs?q=Junior%20Analyst%20Freeman%20Herbs</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row55" class="row_heading level0 row55" >206</th>
      <td id="T_baf65_row55_col0" class="data row55 col0" >Engineer I ( Cyber System Engineer )</td>
      <td id="T_baf65_row55_col1" class="data row55 col1" > Explain why you're a winning candidate. Think "TD" if you crave meaningful work and embrace change like we do. Carve out a career for yourself. </td>
      <td id="T_baf65_row55_col2" class="data row55 col2" >4 days ago</td>
      <td id="T_baf65_row55_col3" class="data row55 col3" >https://ca.indeed.com/jobs?q=Engineer%20I%20%28%20Cyber%20System%20Engineer%20%29%20TD%20Bank</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row56" class="row_heading level0 row56" >205</th>
      <td id="T_baf65_row56_col0" class="data row56 col0" >Actuarial Analyst I</td>
      <td id="T_baf65_row56_col1" class="data row56 col1" > The Insurance Analytics and Modelling team specializing in property and casualty insurance. The team analyzes and transforms data into high-quality predictive… </td>
      <td id="T_baf65_row56_col2" class="data row56 col2" >4 days ago</td>
      <td id="T_baf65_row56_col3" class="data row56 col3" >https://ca.indeed.com/jobs?q=Actuarial%20Analyst%20I%20TD%20Bank</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row57" class="row_heading level0 row57" >109</th>
      <td id="T_baf65_row57_col0" class="data row57 col0" >Application and Infrastructure Analyst I</td>
      <td id="T_baf65_row57_col1" class="data row57 col1" > The Financial &amp; Corporate Services department is in need of an Application and Infrastructure Analyst I to provide high quality maintenance and service level… </td>
      <td id="T_baf65_row57_col2" class="data row57 col2" >4 days ago</td>
      <td id="T_baf65_row57_col3" class="data row57 col3" >https://ca.indeed.com/jobs?q=Application%20and%20Infrastructure%20Analyst%20I%20City%20of%20Edmonton</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row58" class="row_heading level0 row58" >104</th>
      <td id="T_baf65_row58_col0" class="data row58 col0" >Junior Forecast Analyst-Shared Services</td>
      <td id="T_baf65_row58_col1" class="data row58 col1" > Junior Forecast Analyst – Shared Services*. Reporting to the Director of Operations Support, the Junior Forecast Analyst contributes to Arctic Glacier’s success… </td>
      <td id="T_baf65_row58_col2" class="data row58 col2" >Active 4 days ago</td>
      <td id="T_baf65_row58_col3" class="data row58 col3" >https://ca.indeed.com/jobs?q=Junior%20Forecast%20Analyst-Shared%20Services%20Arctic%20Glacier</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row59" class="row_heading level0 row59" >20</th>
      <td id="T_baf65_row59_col0" class="data row59 col0" >Data (Game) Analyst - fit for experienced or junior</td>
      <td id="T_baf65_row59_col1" class="data row59 col1" > Experience analyzing data using statistics. Analyzing user's collected data. Validating the quality of the data. \*\*In-Office (Non-remote) position\*\*. </td>
      <td id="T_baf65_row59_col2" class="data row59 col2" >Active 4 days ago</td>
      <td id="T_baf65_row59_col3" class="data row59 col3" >https://ca.indeed.com/jobs?q=Data%20%28Game%29%20Analyst%20-%20fit%20for%20experienced%20or%20junior%20Blazesoft</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row60" class="row_heading level0 row60" >19</th>
      <td id="T_baf65_row60_col0" class="data row60 col0" >Financial Analyst I</td>
      <td id="T_baf65_row60_col1" class="data row60 col1" > Proven ability to analysis data into meaningful information. Our well established oil and gas client is seeking a Financial Analyst I in Edmonton, AB.*. </td>
      <td id="T_baf65_row60_col2" class="data row60 col2" >Active 4 days ago</td>
      <td id="T_baf65_row60_col3" class="data row60 col3" >https://ca.indeed.com/jobs?q=Financial%20Analyst%20I%20Fast%20Labour%20Solutions%20-%20Canada</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row61" class="row_heading level0 row61" >110</th>
      <td id="T_baf65_row61_col0" class="data row61 col0" >Junior Solution Integrator</td>
      <td id="T_baf65_row61_col1" class="data row61 col1" > Solution Integrators are responsible for the deployment and integration of Infrastructure Solutions in enterprise environments. Fundamental knowledge of TCP/IP. </td>
      <td id="T_baf65_row61_col2" class="data row61 col2" >Active 5 days ago</td>
      <td id="T_baf65_row61_col3" class="data row61 col3" >https://ca.indeed.com/jobs?q=Junior%20Solution%20Integrator%20FlexITy%20Solutions</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row62" class="row_heading level0 row62" >111</th>
      <td id="T_baf65_row62_col0" class="data row62 col0" >Junior Buissness Analyst</td>
      <td id="T_baf65_row62_col1" class="data row62 col1" > The Junior Business Analyst will act as an extension of the Business Analyst and will be involved in the maintenance of programs used for client relations and… </td>
      <td id="T_baf65_row62_col2" class="data row62 col2" >Active 5 days ago</td>
      <td id="T_baf65_row62_col3" class="data row62 col3" >https://ca.indeed.com/jobs?q=Junior%20Buissness%20Analyst%20The%20Central%20Group%20Ltd.</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row63" class="row_heading level0 row63" >114</th>
      <td id="T_baf65_row63_col0" class="data row63 col0" >Software Developer I</td>
      <td id="T_baf65_row63_col1" class="data row63 col1" > Using leading-edge technology, you’ll help connect British Columbians to healthy and safe workplaces – providing support for injury prevention programs,… </td>
      <td id="T_baf65_row63_col2" class="data row63 col2" >7 days ago</td>
      <td id="T_baf65_row63_col3" class="data row63 col3" >https://ca.indeed.com/jobs?q=Software%20Developer%20I%20WorkSafeBC</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row64" class="row_heading level0 row64" >112</th>
      <td id="T_baf65_row64_col0" class="data row64 col0" >Systems Analyst I</td>
      <td id="T_baf65_row64_col1" class="data row64 col1" > The Systems Analyst I maintains operational excellence of Seaspan’s live business systems. Working closely with team members and directly supporting end users,… </td>
      <td id="T_baf65_row64_col2" class="data row64 col2" >7 days ago</td>
      <td id="T_baf65_row64_col3" class="data row64 col3" >https://ca.indeed.com/jobs?q=Systems%20Analyst%20I%20Seaspan%20ULC</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row65" class="row_heading level0 row65" >115</th>
      <td id="T_baf65_row65_col0" class="data row65 col0" >GIS Analyst - Junior</td>
      <td id="T_baf65_row65_col1" class="data row65 col1" > The successful candidate must hold a valid Reliability Security Clearance or be eligible for one. Runs geotargeting analysis leveraging GIS tools; </td>
      <td id="T_baf65_row65_col2" class="data row65 col2" >7 days ago</td>
      <td id="T_baf65_row65_col3" class="data row65 col3" >https://ca.indeed.com/jobs?q=GIS%20Analyst%20-%20Junior%20Adecco%20Canada</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row66" class="row_heading level0 row66" >113</th>
      <td id="T_baf65_row66_col0" class="data row66 col0" >Jr. Site Reliability Engineer</td>
      <td id="T_baf65_row66_col1" class="data row66 col1" > Reporting to senior technical staff, the role contributes to several facets of the product and services delivery lifecycles of the Univeris EWMS SaaS platform… </td>
      <td id="T_baf65_row66_col2" class="data row66 col2" >7 days ago</td>
      <td id="T_baf65_row66_col3" class="data row66 col3" >https://ca.indeed.com/jobs?q=Jr.%20Site%20Reliability%20Engineer%20Univeris%20Corp</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row67" class="row_heading level0 row67" >21</th>
      <td id="T_baf65_row67_col0" class="data row67 col0" >Junior Market Analyst - Intern</td>
      <td id="T_baf65_row67_col1" class="data row67 col1" > Strong analytical and critical thinking skills; ability to quickly interpret large amounts of data. Insights &amp; Reporting: Routine presentations of data… </td>
      <td id="T_baf65_row67_col2" class="data row67 col2" >7 days ago</td>
      <td id="T_baf65_row67_col3" class="data row67 col3" >https://ca.indeed.com/jobs?q=Junior%20Market%20Analyst%20-%20Intern%20Husky%20Injection%20Molding</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row68" class="row_heading level0 row68" >208</th>
      <td id="T_baf65_row68_col0" class="data row68 col0" >Jr. Software Designer</td>
      <td id="T_baf65_row68_col1" class="data row68 col1" > Come create the technology that helps the world act together. Nokia is committed to innovation and technology leadership across mobile, fixed and cloud networks… </td>
      <td id="T_baf65_row68_col2" class="data row68 col2" >7 days ago</td>
      <td id="T_baf65_row68_col3" class="data row68 col3" >https://ca.indeed.com/jobs?q=Jr.%20Software%20Designer%20NOKIA</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row69" class="row_heading level0 row69" >116</th>
      <td id="T_baf65_row69_col0" class="data row69 col0" >Air Quality Specialist</td>
      <td id="T_baf65_row69_col1" class="data row69 col1" > You will work within a group of professionals with varying levels of experience; You will assist with conducting air quality assessments and air dispersion… </td>
      <td id="T_baf65_row69_col2" class="data row69 col2" >7 days ago</td>
      <td id="T_baf65_row69_col3" class="data row69 col3" >https://ca.indeed.com/jobs?q=Air%20Quality%20Specialist%20WSP</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row70" class="row_heading level0 row70" >119</th>
      <td id="T_baf65_row70_col0" class="data row70 col0" >JUNIOR PL1 MAINFRAME DEVELOPER (remote work)</td>
      <td id="T_baf65_row70_col1" class="data row70 col1" > If you have applied for an IBM role previously, you will be able to log into the candidate zone using your previous IBM log in details. </td>
      <td id="T_baf65_row70_col2" class="data row70 col2" >8 days ago</td>
      <td id="T_baf65_row70_col3" class="data row70 col3" >https://ca.indeed.com/jobs?q=JUNIOR%20PL1%20MAINFRAME%20DEVELOPER%20%28remote%20work%29%20Kyndryl</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row71" class="row_heading level0 row71" >22</th>
      <td id="T_baf65_row71_col0" class="data row71 col0" >Research Analyst I</td>
      <td id="T_baf65_row71_col1" class="data row71 col1" > This position has a high degree of administrative responsibilities, data entry and data management. This may include: collect participant data using established… </td>
      <td id="T_baf65_row71_col2" class="data row71 col2" >8 days ago</td>
      <td id="T_baf65_row71_col3" class="data row71 col3" >https://ca.indeed.com/jobs?q=Research%20Analyst%20I%20University%20Health%20Network</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row72" class="row_heading level0 row72" >23</th>
      <td id="T_baf65_row72_col0" class="data row72 col0" >Junior Financial Planning Analyst - Temporary Part Time (Jun...</td>
      <td id="T_baf65_row72_col1" class="data row72 col1" > Advanced Microsoft Office skills (with a focus on data manipulation tools – Excel &amp; Access). The Junior Financial Planning Analyst plays a supporting role in… </td>
      <td id="T_baf65_row72_col2" class="data row72 col2" >Active 8 days ago</td>
      <td id="T_baf65_row72_col3" class="data row72 col3" >https://ca.indeed.com/jobs?q=Junior%20Financial%20Planning%20Analyst%20-%20Temporary%20Part%20Time%20%28Jun...%20Mohawk%20College</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row73" class="row_heading level0 row73" >24</th>
      <td id="T_baf65_row73_col0" class="data row73 col0" >JR Data Processor</td>
      <td id="T_baf65_row73_col1" class="data row73 col1" > Perform a variety of data quality tasks in support of live sports data production. A love and passion for North American professional sports data. </td>
      <td id="T_baf65_row73_col2" class="data row73 col2" >8 days ago</td>
      <td id="T_baf65_row73_col3" class="data row73 col3" >https://ca.indeed.com/jobs?q=JR%20Data%20Processor%20Nielsen</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row74" class="row_heading level0 row74" >209</th>
      <td id="T_baf65_row74_col0" class="data row74 col0" >Applied Scientist I</td>
      <td id="T_baf65_row74_col1" class="data row74 col1" > Master's degree or foreign equivalent in Computer Science, Electrical Engineering, Mathematics or Physics. 1 year of experience conducting independent research… </td>
      <td id="T_baf65_row74_col2" class="data row74 col2" >8 days ago</td>
      <td id="T_baf65_row74_col3" class="data row74 col3" >https://ca.indeed.com/jobs?q=Applied%20Scientist%20I%20Amazon%20Dev%20Centre%20Canada%20ULC</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row75" class="row_heading level0 row75" >118</th>
      <td id="T_baf65_row75_col0" class="data row75 col0" >Junior IT Systems Administrator</td>
      <td id="T_baf65_row75_col1" class="data row75 col1" > Recommend, implement, and maintain secure environments running in Azure using industry-accepted standards (MFA, Azure Firewall, Intune, etc.). </td>
      <td id="T_baf65_row75_col2" class="data row75 col2" >Active 8 days ago</td>
      <td id="T_baf65_row75_col3" class="data row75 col3" >https://ca.indeed.com/jobs?q=Junior%20IT%20Systems%20Administrator%20Matrix%20Solutions%20Inc.</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row76" class="row_heading level0 row76" >25</th>
      <td id="T_baf65_row76_col0" class="data row76 col0" >Data Entry Clerk/Junior Bookkeeper</td>
      <td id="T_baf65_row76_col1" class="data row76 col1" > Payroll data entry (Cross training). Daily data entry to keep company’s bookkeeping up to date. The role provides a wide variety of data entry and… </td>
      <td id="T_baf65_row76_col2" class="data row76 col2" >Active 9 days ago</td>
      <td id="T_baf65_row76_col3" class="data row76 col3" >https://ca.indeed.com/jobs?q=Data%20Entry%20Clerk/Junior%20Bookkeeper%20Seltrek%20Electric%20Ltd</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row77" class="row_heading level0 row77" >26</th>
      <td id="T_baf65_row77_col0" class="data row77 col0" >Business Analyst I</td>
      <td id="T_baf65_row77_col1" class="data row77 col1" > Design/implement data-driven workflows in ZEMA. Design data reports/models optimized for usability, and support analytics and integration. </td>
      <td id="T_baf65_row77_col2" class="data row77 col2" >9 days ago</td>
      <td id="T_baf65_row77_col3" class="data row77 col3" >https://ca.indeed.com/jobs?q=Business%20Analyst%20I%20ZE%20Power%20Group</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row78" class="row_heading level0 row78" >120</th>
      <td id="T_baf65_row78_col0" class="data row78 col0" >Junior Systems Developer</td>
      <td id="T_baf65_row78_col1" class="data row78 col1" > Offering a natural, deep harbour and big ship infrastructure, Halifax can accommodate large volumes of containerized cargo, breakbulk cargo, and project cargo… </td>
      <td id="T_baf65_row78_col2" class="data row78 col2" >9 days ago</td>
      <td id="T_baf65_row78_col3" class="data row78 col3" >https://ca.indeed.com/jobs?q=Junior%20Systems%20Developer%20Halifax%20Port%20Authority</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row79" class="row_heading level0 row79" >121</th>
      <td id="T_baf65_row79_col0" class="data row79 col0" >Junior Full Stack Developer</td>
      <td id="T_baf65_row79_col1" class="data row79 col1" > Helcim is searching for an Junior Full Stack Developer to be responsible for helping develop a wide variety of features including both frontend and backend… </td>
      <td id="T_baf65_row79_col2" class="data row79 col2" >9 days ago</td>
      <td id="T_baf65_row79_col3" class="data row79 col3" >https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20Helcim</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row80" class="row_heading level0 row80" >122</th>
      <td id="T_baf65_row80_col0" class="data row80 col0" >Analista tecnico junior pl/sql</td>
      <td id="T_baf65_row80_col1" class="data row80 col1" > Gruppo Sincrono, Holding Company ICT di Consulenza e Formazione che opera sul mercato dal 1993, sta selezionando per un’importante opportunità professionale per… </td>
      <td id="T_baf65_row80_col2" class="data row80 col2" >9 days ago</td>
      <td id="T_baf65_row80_col3" class="data row80 col3" >https://ca.indeed.com/jobs?q=Analista%20tecnico%20junior%20pl/sql%20Gruppo%20Sincrono</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row81" class="row_heading level0 row81" >210</th>
      <td id="T_baf65_row81_col0" class="data row81 col0" >Junior Systems Administrator</td>
      <td id="T_baf65_row81_col1" class="data row81 col1" > Maintenance of the Ubuntu Linux server infrastructure. Ensures security and configuration compliance of hardware and software to comply with best practices. </td>
      <td id="T_baf65_row81_col2" class="data row81 col2" >9 days ago</td>
      <td id="T_baf65_row81_col3" class="data row81 col3" >https://ca.indeed.com/jobs?q=Junior%20Systems%20Administrator%20PSD</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row82" class="row_heading level0 row82" >27</th>
      <td id="T_baf65_row82_col0" class="data row82 col0" >Business Analyst I, Virtual Care - TELUS Health</td>
      <td id="T_baf65_row82_col1" class="data row82 col1" > Apply strategic, business and financial acumen to create sound business cases and support data-driven decision-making. </td>
      <td id="T_baf65_row82_col2" class="data row82 col2" >9 days ago</td>
      <td id="T_baf65_row82_col3" class="data row82 col3" >https://ca.indeed.com/jobs?q=Business%20Analyst%20I%2C%20Virtual%20Care%20-%20TELUS%20Health%20TELUS</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row83" class="row_heading level0 row83" >123</th>
      <td id="T_baf65_row83_col0" class="data row83 col0" >Junior Developer</td>
      <td id="T_baf65_row83_col1" class="data row83 col1" > If you are a talented and experienced Developer, David Aplin Group has partnered with our client to recruit a Junior Developer who will be responsible for… </td>
      <td id="T_baf65_row83_col2" class="data row83 col2" >10 days ago</td>
      <td id="T_baf65_row83_col3" class="data row83 col3" >https://ca.indeed.com/jobs?q=Junior%20Developer%20David%20Aplin%20Group</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row84" class="row_heading level0 row84" >124</th>
      <td id="T_baf65_row84_col0" class="data row84 col0" >Junior Software Engineer- Web</td>
      <td id="T_baf65_row84_col1" class="data row84 col1" > Backend engineer must be comfortable designing, implementing, deploying and maintaining server-side components. </td>
      <td id="T_baf65_row84_col2" class="data row84 col2" >10 days ago</td>
      <td id="T_baf65_row84_col3" class="data row84 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Engineer-%20Web%20Procom</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row85" class="row_heading level0 row85" >125</th>
      <td id="T_baf65_row85_col0" class="data row85 col0" >Junior Automation Programming Specialist</td>
      <td id="T_baf65_row85_col1" class="data row85 col1" > The Junior Automation Programming Specialist supports our team of Senior Programmers and Automation Specialists. </td>
      <td id="T_baf65_row85_col2" class="data row85 col2" >10 days ago</td>
      <td id="T_baf65_row85_col3" class="data row85 col3" >https://ca.indeed.com/jobs?q=Junior%20Automation%20Programming%20Specialist%20CDN%20Controls%20Ltd.</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row86" class="row_heading level0 row86" >126</th>
      <td id="T_baf65_row86_col0" class="data row86 col0" >Jr. Developer</td>
      <td id="T_baf65_row86_col1" class="data row86 col1" > As a new Jr. Developer, you will be responsible for customizing, developing, and supporting solutions on our internal platform. </td>
      <td id="T_baf65_row86_col2" class="data row86 col2" >10 days ago</td>
      <td id="T_baf65_row86_col3" class="data row86 col3" >https://ca.indeed.com/jobs?q=Jr.%20Developer%20OSG</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row87" class="row_heading level0 row87" >211</th>
      <td id="T_baf65_row87_col0" class="data row87 col0" >Junior SoC Design Engineer</td>
      <td id="T_baf65_row87_col1" class="data row87 col1" > Reasonable accommodations may be made to enable qualified individuals with disabilities to perform essential job functions. Job Types: Full-time, Permanent. </td>
      <td id="T_baf65_row87_col2" class="data row87 col2" >Active 10 days ago</td>
      <td id="T_baf65_row87_col3" class="data row87 col3" >https://ca.indeed.com/jobs?q=Junior%20SoC%20Design%20Engineer%20Solidigm</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row88" class="row_heading level0 row88" >29</th>
      <td id="T_baf65_row88_col0" class="data row88 col0" >Jr. Digital Business Analyst</td>
      <td id="T_baf65_row88_col1" class="data row88 col1" > Analyze data to identify trends, interdependencies among variables and be able to support defining project scope,. Reporting to: Director, Digital Solutions. </td>
      <td id="T_baf65_row88_col2" class="data row88 col2" >10 days ago</td>
      <td id="T_baf65_row88_col3" class="data row88 col3" >https://ca.indeed.com/jobs?q=Jr.%20Digital%20Business%20Analyst%20FirstOntario%20Credit%20Union</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row89" class="row_heading level0 row89" >212</th>
      <td id="T_baf65_row89_col0" class="data row89 col0" >BIOINFORMATICS SCIENTIST I - CA</td>
      <td id="T_baf65_row89_col1" class="data row89 col1" > This position is responsible for in-depth in-silico bioinformatics analysis required for development of sequencing and other molecular methods, bio surveillance… </td>
      <td id="T_baf65_row89_col2" class="data row89 col2" >10 days ago</td>
      <td id="T_baf65_row89_col3" class="data row89 col3" >https://ca.indeed.com/jobs?q=BIOINFORMATICS%20SCIENTIST%20I%20-%20CA%20Luminex</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row90" class="row_heading level0 row90" >213</th>
      <td id="T_baf65_row90_col0" class="data row90 col0" >DevOps Junior / Junior DevOps</td>
      <td id="T_baf65_row90_col1" class="data row90 col1" > À propos d’OPAL-RT Technologies. OPAL-RT s’est donné comme ambitieux défi de démocratiser la simulation temps réel afin de la rendre accessible à chaque… </td>
      <td id="T_baf65_row90_col2" class="data row90 col2" >10 days ago</td>
      <td id="T_baf65_row90_col3" class="data row90 col3" >https://ca.indeed.com/jobs?q=DevOps%20Junior%20/%20Junior%20DevOps%20Opal-RT</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row91" class="row_heading level0 row91" >214</th>
      <td id="T_baf65_row91_col0" class="data row91 col0" >Mixed Signal Test Engineer - JR MTS</td>
      <td id="T_baf65_row91_col1" class="data row91 col1" > The Mixed-signal test professional will be responsible for the design of complex electronics systems and Electronic Ground Support Equipement (EGSE) for testing… </td>
      <td id="T_baf65_row91_col2" class="data row91 col2" >10 days ago</td>
      <td id="T_baf65_row91_col3" class="data row91 col3" >https://ca.indeed.com/jobs?q=Mixed%20Signal%20Test%20Engineer%20-%20JR%20MTS%20MDA</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row92" class="row_heading level0 row92" >28</th>
      <td id="T_baf65_row92_col0" class="data row92 col0" >Jr. Business Analyst - Carriers</td>
      <td id="T_baf65_row92_col1" class="data row92 col1" > Analyze data to identify trends and challenges, and use the data to provide insights to drive improvements through operational initiatives while collaborating… </td>
      <td id="T_baf65_row92_col2" class="data row92 col2" >10 days ago</td>
      <td id="T_baf65_row92_col3" class="data row92 col3" >https://ca.indeed.com/jobs?q=Jr.%20Business%20Analyst%20-%20Carriers%20Shipfusion</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row93" class="row_heading level0 row93" >30</th>
      <td id="T_baf65_row93_col0" class="data row93 col0" >Junior Operations Analyst</td>
      <td id="T_baf65_row93_col1" class="data row93 col1" > Assign and dispatch equipment based on needs identified in data analysis and as requested by customers, create work orders for dispatches. </td>
      <td id="T_baf65_row93_col2" class="data row93 col2" >Active 11 days ago</td>
      <td id="T_baf65_row93_col3" class="data row93 col3" >https://ca.indeed.com/jobs?q=Junior%20Operations%20Analyst%20Hunt%20Personnel%20Temporarily%20Yours</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row94" class="row_heading level0 row94" >127</th>
      <td id="T_baf65_row94_col0" class="data row94 col0" >Développeur Junior .Net</td>
      <td id="T_baf65_row94_col1" class="data row94 col1" > Analyser, diagnostiquer et résoudre les problèmes techniques des utilisateurs. Participer à l'implantation, à l'installation, à la mise à jour et à la… </td>
      <td id="T_baf65_row94_col2" class="data row94 col2" >11 days ago</td>
      <td id="T_baf65_row94_col3" class="data row94 col3" >https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20Junior%20.Net%20Hydro%20Qu%C3%A9bec</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row95" class="row_heading level0 row95" >215</th>
      <td id="T_baf65_row95_col0" class="data row95 col0" >Conseiller(ère) Cybersécurité I | Surveillance et détection...</td>
      <td id="T_baf65_row95_col1" class="data row95 col1" > Démontrer un rôle-conseil et une autonomie dans la réalisation d’activités qui consistent à analyser et résoudre des situations et problématiques variées… </td>
      <td id="T_baf65_row95_col2" class="data row95 col2" >11 days ago</td>
      <td id="T_baf65_row95_col3" class="data row95 col3" >https://ca.indeed.com/jobs?q=Conseiller%28%C3%A8re%29%20Cybers%C3%A9curit%C3%A9%20I%20%7C%20Surveillance%20et%20d%C3%A9tection...%20Hydro%20Qu%C3%A9bec</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row96" class="row_heading level0 row96" >216</th>
      <td id="T_baf65_row96_col0" class="data row96 col0" >Développeur PHP junior - Junior PHP Developper</td>
      <td id="T_baf65_row96_col1" class="data row96 col1" > Leader dans la création et l’édition de jeux, Gameloft® s’est positionné depuis 2000 comme l’une des entreprises les plus innovantes dans son domaine. </td>
      <td id="T_baf65_row96_col2" class="data row96 col2" >11 days ago</td>
      <td id="T_baf65_row96_col3" class="data row96 col3" >https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20PHP%20junior%20-%20Junior%20PHP%20Developper%20Gameloft</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row97" class="row_heading level0 row97" >217</th>
      <td id="T_baf65_row97_col0" class="data row97 col0" >Embedded Low Level Software Developer - Junior</td>
      <td id="T_baf65_row97_col1" class="data row97 col1" > MANNARINO Systems &amp; Software Inc. holds over 20 years of experience in designing, developing, verifying and certifying real-time embedded software for safety… </td>
      <td id="T_baf65_row97_col2" class="data row97 col2" >12 days ago</td>
      <td id="T_baf65_row97_col3" class="data row97 col3" >https://ca.indeed.com/jobs?q=Embedded%20Low%20Level%20Software%20Developer%20-%20Junior%20Mannarino%20Systems%20%26%20Software%20Inc</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row98" class="row_heading level0 row98" >128</th>
      <td id="T_baf65_row98_col0" class="data row98 col0" >Junior Global Business Systems Developer</td>
      <td id="T_baf65_row98_col1" class="data row98 col1" > Responsible for designing and implementing creative database queries and workflows to automate reporting data and provide optimal solutions for database… </td>
      <td id="T_baf65_row98_col2" class="data row98 col2" >12 days ago</td>
      <td id="T_baf65_row98_col3" class="data row98 col3" >https://ca.indeed.com/jobs?q=Junior%20Global%20Business%20Systems%20Developer%20ZOOK%20Canada%20Inc</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row99" class="row_heading level0 row99" >218</th>
      <td id="T_baf65_row99_col0" class="data row99 col0" >Junior Solutions Architect</td>
      <td id="T_baf65_row99_col1" class="data row99 col1" > Provide technical leadership throughout the development life cycle and focus on delivery of quality solutions. Define standards to guide architectural designs. </td>
      <td id="T_baf65_row99_col2" class="data row99 col2" >13 days ago</td>
      <td id="T_baf65_row99_col3" class="data row99 col3" >https://ca.indeed.com/jobs?q=Junior%20Solutions%20Architect%20BIMM</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row100" class="row_heading level0 row100" >129</th>
      <td id="T_baf65_row100_col0" class="data row100 col0" >Junior Salesforce Developer</td>
      <td id="T_baf65_row100_col1" class="data row100 col1" > You will be helping our Salesforce development teams to ensure we continuously deliver exceptional tools for the business to service our customers accurately… </td>
      <td id="T_baf65_row100_col2" class="data row100 col2" >13 days ago</td>
      <td id="T_baf65_row100_col3" class="data row100 col3" >https://ca.indeed.com/jobs?q=Junior%20Salesforce%20Developer%20Just%20Energy</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row101" class="row_heading level0 row101" >130</th>
      <td id="T_baf65_row101_col0" class="data row101 col0" >Junior Software Developer-AQE</td>
      <td id="T_baf65_row101_col1" class="data row101 col1" > In this role you will be able to provide technical insights and expertise to support comprehensive automated verification. Previous experience in software QA. </td>
      <td id="T_baf65_row101_col2" class="data row101 col2" >Active 13 days ago</td>
      <td id="T_baf65_row101_col3" class="data row101 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer-AQE%20Keywords%20Studios</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row102" class="row_heading level0 row102" >31</th>
      <td id="T_baf65_row102_col0" class="data row102 col0" >Analyst, Cost of Goods Sold Finance</td>
      <td id="T_baf65_row102_col1" class="data row102 col1" > 2 years of Operations and Supply Chain Finance experience however not mandatory as this is a junior position. We believe that cannabis can be a force for good. </td>
      <td id="T_baf65_row102_col2" class="data row102 col2" >14 days ago</td>
      <td id="T_baf65_row102_col3" class="data row102 col3" >https://ca.indeed.com/jobs?q=Analyst%2C%20Cost%20of%20Goods%20Sold%20Finance%20Canopy%20Growth%20Corporation</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row103" class="row_heading level0 row103" >32</th>
      <td id="T_baf65_row103_col0" class="data row103 col0" >Jr. Financial Analyst</td>
      <td id="T_baf65_row103_col1" class="data row103 col1" > Strong analytical and data gathering skills. Familiarity with data query/management tools considered an asset (Access, SQL, Business Objects). </td>
      <td id="T_baf65_row103_col2" class="data row103 col2" >14 days ago</td>
      <td id="T_baf65_row103_col3" class="data row103 col3" >https://ca.indeed.com/jobs?q=Jr.%20Financial%20Analyst%20Aviva</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row104" class="row_heading level0 row104" >131</th>
      <td id="T_baf65_row104_col0" class="data row104 col0" >Junior Full Stack Software Developer</td>
      <td id="T_baf65_row104_col1" class="data row104 col1" > DataDrill is currently seeking a Junior Full Stack Software Developer within the R&amp;D department. You have excellent verbal and written communication skills. </td>
      <td id="T_baf65_row104_col2" class="data row104 col2" >14 days ago</td>
      <td id="T_baf65_row104_col3" class="data row104 col3" >https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Software%20Developer%20DataDrill%20Communications%20Inc.</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row105" class="row_heading level0 row105" >219</th>
      <td id="T_baf65_row105_col0" class="data row105 col0" >Jr. Project Coordinator - EHS Co-op</td>
      <td id="T_baf65_row105_col1" class="data row105 col1" > This project is part of Bruce Power’s Life Extension Program, which will allow Bruce Power’s CANDU units to continue to operate safely through to 2064, the… </td>
      <td id="T_baf65_row105_col2" class="data row105 col2" >14 days ago</td>
      <td id="T_baf65_row105_col3" class="data row105 col3" >https://ca.indeed.com/jobs?q=Jr.%20Project%20Coordinator%20-%20EHS%20Co-op%20United%20E%26C</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row106" class="row_heading level0 row106" >220</th>
      <td id="T_baf65_row106_col0" class="data row106 col0" >Junior Python Developer</td>
      <td id="T_baf65_row106_col1" class="data row106 col1" > 2-3 years relevant experience or equivalent - with the majority of experience with Python. Design, develop, test, deploy, maintain and improve software… </td>
      <td id="T_baf65_row106_col2" class="data row106 col2" >15 days ago</td>
      <td id="T_baf65_row106_col3" class="data row106 col3" >https://ca.indeed.com/jobs?q=Junior%20Python%20Developer%20Macadamian</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row107" class="row_heading level0 row107" >33</th>
      <td id="T_baf65_row107_col0" class="data row107 col0" >Analyst, Business I</td>
      <td id="T_baf65_row107_col1" class="data row107 col1" > Evaluate the data collected through task analysis, business process, surveys and workshops. The Business Analyst Role is responsible for ensuring the… </td>
      <td id="T_baf65_row107_col2" class="data row107 col2" >15 days ago</td>
      <td id="T_baf65_row107_col3" class="data row107 col3" >https://ca.indeed.com/jobs?q=Analyst%2C%20Business%20I%20Mosaic%20North%20America</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row108" class="row_heading level0 row108" >34</th>
      <td id="T_baf65_row108_col0" class="data row108 col0" >Junior Business Analyst, Inventory Control</td>
      <td id="T_baf65_row108_col1" class="data row108 col1" > 1-2 years experience in data analysis. Analyze data for inventory and other functions of the company on a needs basis. Monday to Friday working hours. </td>
      <td id="T_baf65_row108_col2" class="data row108 col2" >15 days ago</td>
      <td id="T_baf65_row108_col3" class="data row108 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%2C%20Inventory%20Control%20LGC%20Limited</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row109" class="row_heading level0 row109" >221</th>
      <td id="T_baf65_row109_col0" class="data row109 col0" >Junior Software Developer - 5G RAN OAM</td>
      <td id="T_baf65_row109_col1" class="data row109 col1" > Experience using scripting languages (python, shell (bash), etc). Motivated designers with broad backgrounds and service mindset to be a consultant. </td>
      <td id="T_baf65_row109_col2" class="data row109 col2" >16 days ago</td>
      <td id="T_baf65_row109_col3" class="data row109 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20-%205G%20RAN%20OAM%20Syntronic</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row110" class="row_heading level0 row110" >222</th>
      <td id="T_baf65_row110_col0" class="data row110 col0" >Jr. Application Engineering Specialist- Autonomy Software</td>
      <td id="T_baf65_row110_col1" class="data row110 col1" > Headquartered in Kitchener, ON, Canada, Avidbots offers comprehensive service and support to customers in 5 continents. </td>
      <td id="T_baf65_row110_col2" class="data row110 col2" >16 days ago</td>
      <td id="T_baf65_row110_col3" class="data row110 col3" >https://ca.indeed.com/jobs?q=Jr.%20Application%20Engineering%20Specialist-%20Autonomy%20Software%20Avidbots</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row111" class="row_heading level0 row111" >223</th>
      <td id="T_baf65_row111_col0" class="data row111 col0" >Jr. Project Coordinator</td>
      <td id="T_baf65_row111_col1" class="data row111 col1" > The Shoreline Power Group is a Joint Venture of Aecon, United and SNC-Lavalin. Shoreline Power Group will be completing the Fuel Channel and Feeder Replacement … </td>
      <td id="T_baf65_row111_col2" class="data row111 col2" >17 days ago</td>
      <td id="T_baf65_row111_col3" class="data row111 col3" >https://ca.indeed.com/jobs?q=Jr.%20Project%20Coordinator%20Aecon%20Group</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row112" class="row_heading level0 row112" >135</th>
      <td id="T_baf65_row112_col0" class="data row112 col0" >Junior Systems Analyst, Clinical Solutions, IMITS</td>
      <td id="T_baf65_row112_col1" class="data row112 col1" > As per the current Public Health Order, full vaccination against COVID-19 is a condition of employment with PHSA as of October 26, 2021. </td>
      <td id="T_baf65_row112_col2" class="data row112 col2" >17 days ago</td>
      <td id="T_baf65_row112_col3" class="data row112 col3" >https://ca.indeed.com/jobs?q=Junior%20Systems%20Analyst%2C%20Clinical%20Solutions%2C%20IMITS%20PHSA</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row113" class="row_heading level0 row113" >134</th>
      <td id="T_baf65_row113_col0" class="data row113 col0" >Junior Data Engineer</td>
      <td id="T_baf65_row113_col1" class="data row113 col1" > We’re looking for a Junior Data Engineer to join our Revenue Management Team to support the design, development and maintenance of our data warehouse and ETL… </td>
      <td id="T_baf65_row113_col2" class="data row113 col2" >17 days ago</td>
      <td id="T_baf65_row113_col3" class="data row113 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Engineer%20Canadian%20Niagara%20Hotels</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row114" class="row_heading level0 row114" >35</th>
      <td id="T_baf65_row114_col0" class="data row114 col0" >Junior Business Analyst</td>
      <td id="T_baf65_row114_col1" class="data row114 col1" > Develop and monitor data quality metrics and ensure business data and reporting needs are met. You are responsible for developing and monitoring data quality… </td>
      <td id="T_baf65_row114_col2" class="data row114 col2" >20 days ago</td>
      <td id="T_baf65_row114_col3" class="data row114 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20Norsat%20International%20Inc.</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row115" class="row_heading level0 row115" >136</th>
      <td id="T_baf65_row115_col0" class="data row115 col0" >Junior Marketing Analyst (temp. up to 6 months)</td>
      <td id="T_baf65_row115_col1" class="data row115 col1" > In this role you will be responsible for providing support to the Marketing Analyst in analyzing and reporting on both marketing initiatives and general… </td>
      <td id="T_baf65_row115_col2" class="data row115 col2" >20 days ago</td>
      <td id="T_baf65_row115_col3" class="data row115 col3" >https://ca.indeed.com/jobs?q=Junior%20Marketing%20Analyst%20%28temp.%20up%20to%206%20months%29%20Boston%20Pizza%20International</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row116" class="row_heading level0 row116" >224</th>
      <td id="T_baf65_row116_col0" class="data row116 col0" >Junior Silicon Validation Engineer - (20241)</td>
      <td id="T_baf65_row116_col1" class="data row116 col1" > You will be responsible for testing of our SerDes devices, developing Python automation scripts to characterize the devices, and performing device result… </td>
      <td id="T_baf65_row116_col2" class="data row116 col2" >21 days ago</td>
      <td id="T_baf65_row116_col3" class="data row116 col3" >https://ca.indeed.com/jobs?q=Junior%20Silicon%20Validation%20Engineer%20-%20%2820241%29%20Alphawave%20IP</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row117" class="row_heading level0 row117" >37</th>
      <td id="T_baf65_row117_col0" class="data row117 col0" >Junior Data Analyst</td>
      <td id="T_baf65_row117_col1" class="data row117 col1" > Acquire data from primary or secondary data sources and maintain databases/data systems. Experience analyzing and trending data from multiple sources. </td>
      <td id="T_baf65_row117_col2" class="data row117 col2" >21 days ago</td>
      <td id="T_baf65_row117_col3" class="data row117 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20Match%20Retail</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row118" class="row_heading level0 row118" >36</th>
      <td id="T_baf65_row118_col0" class="data row118 col0" >Junior Database Administrator - Co-Op Student</td>
      <td id="T_baf65_row118_col1" class="data row118 col1" > Access professional development workshops hosted by domain experts on topics ranging from how to be a top consultant, how to apply the agile methodology, data &amp;… </td>
      <td id="T_baf65_row118_col2" class="data row118 col2" >21 days ago</td>
      <td id="T_baf65_row118_col3" class="data row118 col3" >https://ca.indeed.com/jobs?q=Junior%20Database%20Administrator%20-%20Co-Op%20Student%20CGI%20Inc</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row119" class="row_heading level0 row119" >225</th>
      <td id="T_baf65_row119_col0" class="data row119 col0" >Junior Environmental Engineer</td>
      <td id="T_baf65_row119_col1" class="data row119 col1" > Review and analyze water quality and monitoring data. Program and write scripts and tools for visualizing data and conducting statistical analysis. </td>
      <td id="T_baf65_row119_col2" class="data row119 col2" >22 days ago</td>
      <td id="T_baf65_row119_col3" class="data row119 col3" >https://ca.indeed.com/jobs?q=Junior%20Environmental%20Engineer%20Kerr%20Wood%20Leidal</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row120" class="row_heading level0 row120" >138</th>
      <td id="T_baf65_row120_col0" class="data row120 col0" >Junior Software Development Engineer in Test</td>
      <td id="T_baf65_row120_col1" class="data row120 col1" > As a Junior Software Development Engineer in Test (Jr. SDET), you will be part of a small, highly focused team responsible for delivery of highly scalable and… </td>
      <td id="T_baf65_row120_col2" class="data row120 col2" >22 days ago</td>
      <td id="T_baf65_row120_col3" class="data row120 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Development%20Engineer%20in%20Test%20Global%20Relay</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row121" class="row_heading level0 row121" >139</th>
      <td id="T_baf65_row121_col0" class="data row121 col0" >FL Junior .Net Developer</td>
      <td id="T_baf65_row121_col1" class="data row121 col1" > Coding, unit testing and creating supporting documentation. Gaining understanding of customer’s needs and collaborates with other consultants and support teams… </td>
      <td id="T_baf65_row121_col2" class="data row121 col2" >22 days ago</td>
      <td id="T_baf65_row121_col3" class="data row121 col3" >https://ca.indeed.com/jobs?q=FL%20Junior%20.Net%20Developer%20Fujitsu</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row122" class="row_heading level0 row122" >39</th>
      <td id="T_baf65_row122_col0" class="data row122 col0" >Junior Cloud Data Developer</td>
      <td id="T_baf65_row122_col1" class="data row122 col1" > Learn to support, navigate and manage a large enterprise data environment. Also, a passion to understand business opportunities that will allow the candidate to… </td>
      <td id="T_baf65_row122_col2" class="data row122 col2" >22 days ago</td>
      <td id="T_baf65_row122_col3" class="data row122 col3" >https://ca.indeed.com/jobs?q=Junior%20Cloud%20Data%20Developer%20ARC%20Resources%20Ltd</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row123" class="row_heading level0 row123" >38</th>
      <td id="T_baf65_row123_col0" class="data row123 col0" >Junior Cloud Data Developer</td>
      <td id="T_baf65_row123_col1" class="data row123 col1" > Learn to support, navigate and manage a large enterprise data environment. Also, a passion to understand business opportunities that will allow the candidate to… </td>
      <td id="T_baf65_row123_col2" class="data row123 col2" >22 days ago</td>
      <td id="T_baf65_row123_col3" class="data row123 col3" >https://ca.indeed.com/jobs?q=Junior%20Cloud%20Data%20Developer%20ARC%20Resources%20Ltd.</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row124" class="row_heading level0 row124" >41</th>
      <td id="T_baf65_row124_col0" class="data row124 col0" >Montreal - Analyste Technique Junior ou chef de Projet Techn...</td>
      <td id="T_baf65_row124_col1" class="data row124 col1" > En tant qu'analyste technique junior ou chef de projet technique junior chez FDM, vous suivrez une formation spécifique à l'industrie et poursuivrez votre… </td>
      <td id="T_baf65_row124_col2" class="data row124 col2" >23 days ago</td>
      <td id="T_baf65_row124_col3" class="data row124 col3" >https://ca.indeed.com/jobs?q=Montreal%20-%20Analyste%20Technique%20Junior%20ou%20chef%20de%20Projet%20Techn...%20FDM%20Group</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row125" class="row_heading level0 row125" >40</th>
      <td id="T_baf65_row125_col0" class="data row125 col0" >Toronto - Junior Technical Business Analyst/ Junior Technica...</td>
      <td id="T_baf65_row125_col1" class="data row125 col1" > These roles are crucial in helping organizations with the accuracy and timely presentation of data, in line with internal process, governance, and regulatory… </td>
      <td id="T_baf65_row125_col2" class="data row125 col2" >23 days ago</td>
      <td id="T_baf65_row125_col3" class="data row125 col3" >https://ca.indeed.com/jobs?q=Toronto%20-%20Junior%20Technical%20Business%20Analyst/%20Junior%20Technica...%20FDM%20Group</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row126" class="row_heading level0 row126" >42</th>
      <td id="T_baf65_row126_col0" class="data row126 col0" >Montreal - Junior Finance/Compliance Analyst</td>
      <td id="T_baf65_row126_col1" class="data row126 col1" > FDM Junior Finance/Compliance Analysts take on responsibilities such as conducting client due diligence, monitoring and reporting transactions to regulators,… </td>
      <td id="T_baf65_row126_col2" class="data row126 col2" >23 days ago</td>
      <td id="T_baf65_row126_col3" class="data row126 col3" >https://ca.indeed.com/jobs?q=Montreal%20-%20Junior%20Finance/Compliance%20Analyst%20FDM%20Group</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row127" class="row_heading level0 row127" >43</th>
      <td id="T_baf65_row127_col0" class="data row127 col0" >Junior Business Analyst - Co-Op Student</td>
      <td id="T_baf65_row127_col1" class="data row127 col1" > Developing understanding of Accounts payable and accounts receivable. Takes accountability for results and exhibits a “can do” demeanor. </td>
      <td id="T_baf65_row127_col2" class="data row127 col2" >23 days ago</td>
      <td id="T_baf65_row127_col3" class="data row127 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20-%20Co-Op%20Student%20CGI</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row128" class="row_heading level0 row128" >146</th>
      <td id="T_baf65_row128_col0" class="data row128 col0" >Montreal - Développeur de Logiciels Junior</td>
      <td id="T_baf65_row128_col1" class="data row128 col1" > Renseignez-vous sur les préparatifs de FDM pour le coronavirus (COVID-19) ici. Certains postes courants que vous pourriez occuper incluent Développeur Front-end… </td>
      <td id="T_baf65_row128_col2" class="data row128 col2" >23 days ago</td>
      <td id="T_baf65_row128_col3" class="data row128 col3" >https://ca.indeed.com/jobs?q=Montreal%20-%20D%C3%A9veloppeur%20de%20Logiciels%20Junior%20FDM%20Group</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row129" class="row_heading level0 row129" >145</th>
      <td id="T_baf65_row129_col0" class="data row129 col0" >Montreal - Junior Software Developer</td>
      <td id="T_baf65_row129_col1" class="data row129 col1" > As a Software Developer your main role will be to solve problems, upgrade existing systems and improve efficiency for the overall success of large software… </td>
      <td id="T_baf65_row129_col2" class="data row129 col2" >23 days ago</td>
      <td id="T_baf65_row129_col3" class="data row129 col3" >https://ca.indeed.com/jobs?q=Montreal%20-%20Junior%20Software%20Developer%20FDM%20Group</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row130" class="row_heading level0 row130" >144</th>
      <td id="T_baf65_row130_col0" class="data row130 col0" >Montreal - Spécialiste Junior TechOps</td>
      <td id="T_baf65_row130_col1" class="data row130 col1" > Renseignez-vous sur les préparatifs de FDM pour le coronavirus (COVID-19) ici. Certains postes courants dans lesquels vous pourriez travailler incluent l… </td>
      <td id="T_baf65_row130_col2" class="data row130 col2" >23 days ago</td>
      <td id="T_baf65_row130_col3" class="data row130 col3" >https://ca.indeed.com/jobs?q=Montreal%20-%20Sp%C3%A9cialiste%20Junior%20TechOps%20FDM%20Group</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row131" class="row_heading level0 row131" >142</th>
      <td id="T_baf65_row131_col0" class="data row131 col0" >Toronto - Junior Tech-Ops Specialist</td>
      <td id="T_baf65_row131_col1" class="data row131 col1" > A Technical Operations role lands well into the space supporting IT Applications and Services for the business through monitoring, maintenance, and incident… </td>
      <td id="T_baf65_row131_col2" class="data row131 col2" >23 days ago</td>
      <td id="T_baf65_row131_col3" class="data row131 col3" >https://ca.indeed.com/jobs?q=Toronto%20-%20Junior%20Tech-Ops%20Specialist%20FDM%20Group</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row132" class="row_heading level0 row132" >143</th>
      <td id="T_baf65_row132_col0" class="data row132 col0" >Toronto - Junior Software Developer</td>
      <td id="T_baf65_row132_col1" class="data row132 col1" > As a Software Developer your main role will be to solve problems, upgrade existing systems and improve efficiency for the overall success of large software… </td>
      <td id="T_baf65_row132_col2" class="data row132 col2" >23 days ago</td>
      <td id="T_baf65_row132_col3" class="data row132 col3" >https://ca.indeed.com/jobs?q=Toronto%20-%20Junior%20Software%20Developer%20FDM%20Group</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row133" class="row_heading level0 row133" >140</th>
      <td id="T_baf65_row133_col0" class="data row133 col0" >Remote Training - Canada - Junior Software Developer</td>
      <td id="T_baf65_row133_col1" class="data row133 col1" > As a Software Developer your main role will be to solve problems, upgrade existing systems and improve efficiency for the overall success of large software… </td>
      <td id="T_baf65_row133_col2" class="data row133 col2" >23 days ago</td>
      <td id="T_baf65_row133_col3" class="data row133 col3" >https://ca.indeed.com/jobs?q=Remote%20Training%20-%20Canada%20-%20Junior%20Software%20Developer%20FDM%20Group</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row134" class="row_heading level0 row134" >141</th>
      <td id="T_baf65_row134_col0" class="data row134 col0" >Montreal - Junior Software Tester - Bilingual</td>
      <td id="T_baf65_row134_col1" class="data row134 col1" > As a Junior Software Tester, you will learn the role of a technical tester in order to assure the quality of systems and applications through the full… </td>
      <td id="T_baf65_row134_col2" class="data row134 col2" >23 days ago</td>
      <td id="T_baf65_row134_col3" class="data row134 col3" >https://ca.indeed.com/jobs?q=Montreal%20-%20Junior%20Software%20Tester%20-%20Bilingual%20FDM%20Group</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row135" class="row_heading level0 row135" >226</th>
      <td id="T_baf65_row135_col0" class="data row135 col0" >Toronto - Junior Data Engineer</td>
      <td id="T_baf65_row135_col1" class="data row135 col1" > Find out about FDM’s Coronavirus (COVID-19) preparations here. Note: Please only submit one application, even if you are interested in more than one opportunity… </td>
      <td id="T_baf65_row135_col2" class="data row135 col2" >23 days ago</td>
      <td id="T_baf65_row135_col3" class="data row135 col3" >https://ca.indeed.com/jobs?q=Toronto%20-%20Junior%20Data%20Engineer%20FDM%20Group</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row136" class="row_heading level0 row136" >228</th>
      <td id="T_baf65_row136_col0" class="data row136 col0" >Junior Cloud Engineer</td>
      <td id="T_baf65_row136_col1" class="data row136 col1" > Assist with the mentorship of junior engineers through pair programming exercises. An automation engineer, you will be a member of the cloud and transformation… </td>
      <td id="T_baf65_row136_col2" class="data row136 col2" >24 days ago</td>
      <td id="T_baf65_row136_col3" class="data row136 col3" >https://ca.indeed.com/jobs?q=Junior%20Cloud%20Engineer%20Royal%20Bank%20of%20Canada</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row137" class="row_heading level0 row137" >227</th>
      <td id="T_baf65_row137_col0" class="data row137 col0" >Dev Full Stack Junior</td>
      <td id="T_baf65_row137_col1" class="data row137 col1" > Thales est une entreprise où les personnes les plus brillantes du monde entier se regroupent pour mettre en commun leurs idées et ainsi s'inspirer mutuellement. </td>
      <td id="T_baf65_row137_col2" class="data row137 col2" >24 days ago</td>
      <td id="T_baf65_row137_col3" class="data row137 col3" >https://ca.indeed.com/jobs?q=Dev%20Full%20Stack%20Junior%20Thales</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row138" class="row_heading level0 row138" >229</th>
      <td id="T_baf65_row138_col0" class="data row138 col0" >Junior DevOps Engineer</td>
      <td id="T_baf65_row138_col1" class="data row138 col1" > Improving healthcare through innovative technology is at the core of Intelerad’s work. Our scalable medical imaging platform connects clinicians to a powerful… </td>
      <td id="T_baf65_row138_col2" class="data row138 col2" >27 days ago</td>
      <td id="T_baf65_row138_col3" class="data row138 col3" >https://ca.indeed.com/jobs?q=Junior%20DevOps%20Engineer%20Intelerad</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row139" class="row_heading level0 row139" >44</th>
      <td id="T_baf65_row139_col0" class="data row139 col0" >Junior Digital Marketing Specialist</td>
      <td id="T_baf65_row139_col1" class="data row139 col1" > Widespread media monitoring to collect data about PAL Airlines brand mentions and news articles. Media monitoring to collect data about the aviation industry… </td>
      <td id="T_baf65_row139_col2" class="data row139 col2" >27 days ago</td>
      <td id="T_baf65_row139_col3" class="data row139 col3" >https://ca.indeed.com/jobs?q=Junior%20Digital%20Marketing%20Specialist%20PAL%20Airlines</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row140" class="row_heading level0 row140" >45</th>
      <td id="T_baf65_row140_col0" class="data row140 col0" >Data Quality Coordinator I, Policy Reporter (Remote U.S.)</td>
      <td id="T_baf65_row140_col1" class="data row140 col1" >Overview: Company Overview: This is a dynamic opportunity to join a rapidly growing company, with industry leading software and services in the healthcare…</td>
      <td id="T_baf65_row140_col2" class="data row140 col2" >28 days ago</td>
      <td id="T_baf65_row140_col3" class="data row140 col3" >https://ca.indeed.com/jobs?q=Data%20Quality%20Coordinator%20I%2C%20Policy%20Reporter%20%28Remote%20U.S.%29%20TrialCard</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row141" class="row_heading level0 row141" >46</th>
      <td id="T_baf65_row141_col0" class="data row141 col0" >Data Quality Coordinator I, Policy Reporter (Remote Canada)</td>
      <td id="T_baf65_row141_col1" class="data row141 col1" > Enhance data quality work process with SQL, BI tools or data profiler. Performing data cleansing activities independently and as directed by the Data Quality… </td>
      <td id="T_baf65_row141_col2" class="data row141 col2" >28 days ago</td>
      <td id="T_baf65_row141_col3" class="data row141 col3" >https://ca.indeed.com/jobs?q=Data%20Quality%20Coordinator%20I%2C%20Policy%20Reporter%20%28Remote%20Canada%29%20TrialCard</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row142" class="row_heading level0 row142" >234</th>
      <td id="T_baf65_row142_col0" class="data row142 col0" >Dev Full Stack Junior</td>
      <td id="T_baf65_row142_col1" class="data row142 col1" > Thales est une entreprise où les personnes les plus brillantes du monde entier se regroupent pour mettre en commun leurs idées et ainsi s'inspirer mutuellement. </td>
      <td id="T_baf65_row142_col2" class="data row142 col2" >28 days ago</td>
      <td id="T_baf65_row142_col3" class="data row142 col3" >https://ca.indeed.com/jobs?q=Dev%20Full%20Stack%20Junior%20Thales%20Digital%20Solutions%20Inc.%2C%20Research%20%26...</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row143" class="row_heading level0 row143" >230</th>
      <td id="T_baf65_row143_col0" class="data row143 col0" >Junior Technical Artist</td>
      <td id="T_baf65_row143_col1" class="data row143 col1" > Work across departments to support the development of software tools and scripts which improve the development of visual targets. </td>
      <td id="T_baf65_row143_col2" class="data row143 col2" >28 days ago</td>
      <td id="T_baf65_row143_col3" class="data row143 col3" >https://ca.indeed.com/jobs?q=Junior%20Technical%20Artist%202K</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row144" class="row_heading level0 row144" >231</th>
      <td id="T_baf65_row144_col0" class="data row144 col0" >Embedded Low Level Software Developer - Junior</td>
      <td id="T_baf65_row144_col1" class="data row144 col1" > MANNARINO Systems &amp; Software Inc. holds over 20 years experience in designing, developing, verifying and certifying real-time embedded software for safety… </td>
      <td id="T_baf65_row144_col2" class="data row144 col2" >28 days ago</td>
      <td id="T_baf65_row144_col3" class="data row144 col3" >https://ca.indeed.com/jobs?q=Embedded%20Low%20Level%20Software%20Developer%20-%20Junior%20MANNARINO</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row145" class="row_heading level0 row145" >232</th>
      <td id="T_baf65_row145_col0" class="data row145 col0" >Développeur de Logiciels Embarqués de Bas Niveau - Junior</td>
      <td id="T_baf65_row145_col1" class="data row145 col1" > D’une gamme complète d’assurance collective et un plan RÉER collectif; D’une politique d’horaire flexible; Développer la documentation du logiciel conformément… </td>
      <td id="T_baf65_row145_col2" class="data row145 col2" >28 days ago</td>
      <td id="T_baf65_row145_col3" class="data row145 col3" >https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20de%20Logiciels%20Embarqu%C3%A9s%20de%20Bas%20Niveau%20-%20Junior%20MANNARINO</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row146" class="row_heading level0 row146" >233</th>
      <td id="T_baf65_row146_col0" class="data row146 col0" >Junior Technical Artist</td>
      <td id="T_baf65_row146_col1" class="data row146 col1" > Work across departments to support the development of software tools and scripts which improve the development of visual targets. </td>
      <td id="T_baf65_row146_col2" class="data row146 col2" >28 days ago</td>
      <td id="T_baf65_row146_col3" class="data row146 col3" >https://ca.indeed.com/jobs?q=Junior%20Technical%20Artist%20HB%20Studios</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row147" class="row_heading level0 row147" >147</th>
      <td id="T_baf65_row147_col0" class="data row147 col0" >Quality Assurance Analyst I</td>
      <td id="T_baf65_row147_col1" class="data row147 col1" > AAPS Salaried - Information Systems and Technology, Level B. Systems &amp; Development | Arts Instructional Support and Information Technology. </td>
      <td id="T_baf65_row147_col2" class="data row147 col2" >29 days ago</td>
      <td id="T_baf65_row147_col3" class="data row147 col3" >https://ca.indeed.com/jobs?q=Quality%20Assurance%20Analyst%20I%20University%20of%20British%20Columbia</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row148" class="row_heading level0 row148" >47</th>
      <td id="T_baf65_row148_col0" class="data row148 col0" >Junior Business Analyst</td>
      <td id="T_baf65_row148_col1" class="data row148 col1" > Ensuring and maintaining data accuracy. Liaison with operations and developers to raise and understand any data discrepancies. </td>
      <td id="T_baf65_row148_col2" class="data row148 col2" >29 days ago</td>
      <td id="T_baf65_row148_col3" class="data row148 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20Motoinsight</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row149" class="row_heading level0 row149" >237</th>
      <td id="T_baf65_row149_col0" class="data row149 col0" >JR Software Engineer</td>
      <td id="T_baf65_row149_col1" class="data row149 col1" > Knowledge and use of several Integrated software development environment SDE tools and scripting languages (python, etc). Knowledge and use of databases. </td>
      <td id="T_baf65_row149_col2" class="data row149 col2" >29 days ago</td>
      <td id="T_baf65_row149_col3" class="data row149 col3" >https://ca.indeed.com/jobs?q=JR%20Software%20Engineer%20Safran</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row150" class="row_heading level0 row150" >236</th>
      <td id="T_baf65_row150_col0" class="data row150 col0" >Spécialiste en design I - Normes et meilleures pratiques lié...</td>
      <td id="T_baf65_row150_col1" class="data row150 col1" > Ottawa, ON, CA Calgary, AB, CA Edmonton, AB, CA Montreal, Quebec, CA Toronto, ON, CA Vancouver, British Columbia, CA. </td>
      <td id="T_baf65_row150_col2" class="data row150 col2" >29 days ago</td>
      <td id="T_baf65_row150_col3" class="data row150 col3" >https://ca.indeed.com/jobs?q=Sp%C3%A9cialiste%20en%20design%20I%20-%20Normes%20et%20meilleures%20pratiques%20li%C3%A9...%20TELUS</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row151" class="row_heading level0 row151" >235</th>
      <td id="T_baf65_row151_col0" class="data row151 col0" >Design Specialist I - RAN Standards and Best Practices</td>
      <td id="T_baf65_row151_col1" class="data row151 col1" > The national RAN Standards and Best Practices team sits at the intersection of the planning, engineering, implementation, and operations teams. </td>
      <td id="T_baf65_row151_col2" class="data row151 col2" >29 days ago</td>
      <td id="T_baf65_row151_col3" class="data row151 col3" >https://ca.indeed.com/jobs?q=Design%20Specialist%20I%20-%20RAN%20Standards%20and%20Best%20Practices%20TELUS</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row152" class="row_heading level0 row152" >238</th>
      <td id="T_baf65_row152_col0" class="data row152 col0" >Junior Software Engineer</td>
      <td id="T_baf65_row152_col1" class="data row152 col1" > Aviya provides expertise in program management, systems, software, mechanical, and hardware engineering to many of the top-tier Aerospace and Defense… </td>
      <td id="T_baf65_row152_col2" class="data row152 col2" >30+ days ago</td>
      <td id="T_baf65_row152_col3" class="data row152 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Engineer%20Aviya%20Aerospace%20Systems</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row153" class="row_heading level0 row153" >239</th>
      <td id="T_baf65_row153_col0" class="data row153 col0" >Python Developer (Consultant I)</td>
      <td id="T_baf65_row153_col1" class="data row153 col1" > We provide guidance/ coaching to every employee through our mentoring program wherein every junior level employee is assigned a senior level professional as… </td>
      <td id="T_baf65_row153_col2" class="data row153 col2" >30+ days ago</td>
      <td id="T_baf65_row153_col3" class="data row153 col3" >https://ca.indeed.com/jobs?q=Python%20Developer%20%28Consultant%20I%29%20EXL%20Services</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row154" class="row_heading level0 row154" >241</th>
      <td id="T_baf65_row154_col0" class="data row154 col0" >Co-op Junior ASIC Verification Engineer</td>
      <td id="T_baf65_row154_col1" class="data row154 col1" > This is a 4-12 months' Full-time (8 months or more preferred), Co-op employment opportunity starting September 2022. Hands on experience in Perl and Python. </td>
      <td id="T_baf65_row154_col2" class="data row154 col2" >30+ days ago</td>
      <td id="T_baf65_row154_col3" class="data row154 col3" >https://ca.indeed.com/jobs?q=Co-op%20Junior%20ASIC%20Verification%20Engineer%20NETINT%20Technologies%20Inc.</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row155" class="row_heading level0 row155" >80</th>
      <td id="T_baf65_row155_col0" class="data row155 col0" >UM - Junior Analyst, Decision Sciences</td>
      <td id="T_baf65_row155_col1" class="data row155 col1" > Support development of custom data models and algorithms to apply to data sets. Assess the effectiveness and accuracy of new data sources with a understanding… </td>
      <td id="T_baf65_row155_col2" class="data row155 col2" >30+ days ago</td>
      <td id="T_baf65_row155_col3" class="data row155 col3" >https://ca.indeed.com/jobs?q=UM%20-%20Junior%20Analyst%2C%20Decision%20Sciences%20IPG%20Mediabrands</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row156" class="row_heading level0 row156" >48</th>
      <td id="T_baf65_row156_col0" class="data row156 col0" >Oracle Database Administrator Jr</td>
      <td id="T_baf65_row156_col1" class="data row156 col1" > Understanding of relational and dimensional data modeling. By submitting your application, you consent to Equisoft collecting, using &amp; storing your personal… </td>
      <td id="T_baf65_row156_col2" class="data row156 col2" >30+ days ago</td>
      <td id="T_baf65_row156_col3" class="data row156 col3" >https://ca.indeed.com/jobs?q=Oracle%20Database%20Administrator%20Jr%20Equisoft</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row157" class="row_heading level0 row157" >49</th>
      <td id="T_baf65_row157_col0" class="data row157 col0" >Remote, Ontario – Junior Data Analytics Engineer</td>
      <td id="T_baf65_row157_col1" class="data row157 col1" > Use large data sets to address business issues. Understanding of data warehousing concepts and NoSQL Databases. BS or MS in Computer Science or related fields. </td>
      <td id="T_baf65_row157_col2" class="data row157 col2" >30+ days ago</td>
      <td id="T_baf65_row157_col3" class="data row157 col3" >https://ca.indeed.com/jobs?q=Remote%2C%20Ontario%20%E2%80%93%20Junior%20Data%20Analytics%20Engineer%20CaseWare%20RCM</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row158" class="row_heading level0 row158" >50</th>
      <td id="T_baf65_row158_col0" class="data row158 col0" >Junior Business Analyst</td>
      <td id="T_baf65_row158_col1" class="data row158 col1" > Documenting and analyzing the required information and data to determine potential solutions from a technical and business perspective. </td>
      <td id="T_baf65_row158_col2" class="data row158 col2" >30+ days ago</td>
      <td id="T_baf65_row158_col3" class="data row158 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20RPM%20TECHNOLOGIES%20CORP</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row159" class="row_heading level0 row159" >51</th>
      <td id="T_baf65_row159_col0" class="data row159 col0" >Junior Clinical Trials Data Analyst (Hybrid)</td>
      <td id="T_baf65_row159_col1" class="data row159 col1" > Process clients’ clinical trials data set. Using our tools you will analyze and mitigate the risk of re-identification for trial participants whose data appears… </td>
      <td id="T_baf65_row159_col2" class="data row159 col2" >30+ days ago</td>
      <td id="T_baf65_row159_col3" class="data row159 col3" >https://ca.indeed.com/jobs?q=Junior%20Clinical%20Trials%20Data%20Analyst%20%28Hybrid%29%20IQVIA</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row160" class="row_heading level0 row160" >52</th>
      <td id="T_baf65_row160_col0" class="data row160 col0" >Junior Data Automation Engineer</td>
      <td id="T_baf65_row160_col1" class="data row160 col1" > Experience with query optimization, performance tuning, data quality and data processing. Strong data processing skills and experience in the creation of data… </td>
      <td id="T_baf65_row160_col2" class="data row160 col2" >30+ days ago</td>
      <td id="T_baf65_row160_col3" class="data row160 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Automation%20Engineer%20Kalibrate</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row161" class="row_heading level0 row161" >242</th>
      <td id="T_baf65_row161_col0" class="data row161 col0" >Junior Pipeline TD -- Développeur du Pipeline Junior</td>
      <td id="T_baf65_row161_col1" class="data row161 col1" > Cinesite is recruiting a Junior Pipeline TD who will be responsible to maintain and advance the Cinesite pipeline on our animated movies and VFX shows. </td>
      <td id="T_baf65_row161_col2" class="data row161 col2" >30+ days ago</td>
      <td id="T_baf65_row161_col3" class="data row161 col3" >https://ca.indeed.com/jobs?q=Junior%20Pipeline%20TD%20--%20D%C3%A9veloppeur%20du%20Pipeline%20Junior%20Cinesite-Montreal</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row162" class="row_heading level0 row162" >243</th>
      <td id="T_baf65_row162_col0" class="data row162 col0" >Junior DevOps Engineer</td>
      <td id="T_baf65_row162_col1" class="data row162 col1" > As a development team member, you will be responsible for ensuring the smooth operation of production systems and development/test environments. </td>
      <td id="T_baf65_row162_col2" class="data row162 col2" >30+ days ago</td>
      <td id="T_baf65_row162_col3" class="data row162 col3" >https://ca.indeed.com/jobs?q=Junior%20DevOps%20Engineer%20Global%20Relay</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row163" class="row_heading level0 row163" >264</th>
      <td id="T_baf65_row163_col0" class="data row163 col0" >Junior DevOps Engineer</td>
      <td id="T_baf65_row163_col1" class="data row163 col1" > Proficiency with a scripting language (python/ruby). Generous vacation allotments and flexible working hours. Extended health and wellness spending accounts. </td>
      <td id="T_baf65_row163_col2" class="data row163 col2" >30+ days ago</td>
      <td id="T_baf65_row163_col3" class="data row163 col3" >https://ca.indeed.com/jobs?q=Junior%20DevOps%20Engineer%20Thrive%20Health</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row164" class="row_heading level0 row164" >265</th>
      <td id="T_baf65_row164_col0" class="data row164 col0" >Junior Python Developer</td>
      <td id="T_baf65_row164_col1" class="data row164 col1" > As an Juniour Python Developer (internally called ATD) you will perform a variety of tasks to assist the Pipeline Technical Directors (Pipeline TDs) to ensure… </td>
      <td id="T_baf65_row164_col2" class="data row164 col2" >30+ days ago</td>
      <td id="T_baf65_row164_col3" class="data row164 col3" >https://ca.indeed.com/jobs?q=Junior%20Python%20Developer%20ReDefine</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row165" class="row_heading level0 row165" >266</th>
      <td id="T_baf65_row165_col0" class="data row165 col0" >Junior Python Developer</td>
      <td id="T_baf65_row165_col1" class="data row165 col1" > Production Technology is an umbrella term used to describe the group of people supporting, developing and improving the tools and technologies that artists use… </td>
      <td id="T_baf65_row165_col2" class="data row165 col2" >30+ days ago</td>
      <td id="T_baf65_row165_col3" class="data row165 col3" >https://ca.indeed.com/jobs?q=Junior%20Python%20Developer%20DNEG</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row166" class="row_heading level0 row166" >267</th>
      <td id="T_baf65_row166_col0" class="data row166 col0" >Junior Hydrogeologist/ Groundwater Modeller</td>
      <td id="T_baf65_row166_col1" class="data row166 col1" > + Work within a team of hydrogeologists, geologists, geochemists, and groundwater modellers on a wide variety of projects. </td>
      <td id="T_baf65_row166_col2" class="data row166 col2" >30+ days ago</td>
      <td id="T_baf65_row166_col3" class="data row166 col3" >https://ca.indeed.com/jobs?q=Junior%20Hydrogeologist/%20Groundwater%20Modeller%20AECOM</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row167" class="row_heading level0 row167" >268</th>
      <td id="T_baf65_row167_col0" class="data row167 col0" >Bioinformatics Scientist I</td>
      <td id="T_baf65_row167_col1" class="data row167 col1" > We are seeking a highly motivated and experienced Bioinformatics Scientist in the Department of Research and Development. </td>
      <td id="T_baf65_row167_col2" class="data row167 col2" >30+ days ago</td>
      <td id="T_baf65_row167_col3" class="data row167 col3" >https://ca.indeed.com/jobs?q=Bioinformatics%20Scientist%20I%20Geneseeq%20Technology</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row168" class="row_heading level0 row168" >269</th>
      <td id="T_baf65_row168_col0" class="data row168 col0" >Junior Site Reliability Engineer Developer</td>
      <td id="T_baf65_row168_col1" class="data row168 col1" > This role reports to our Shared Capabilities organization, and you’ll have the opportunity to learn and grow, expanding your knowledge base and getting hands-on… </td>
      <td id="T_baf65_row168_col2" class="data row168 col2" >30+ days ago</td>
      <td id="T_baf65_row168_col3" class="data row168 col3" >https://ca.indeed.com/jobs?q=Junior%20Site%20Reliability%20Engineer%20Developer%20Royal%20Bank%20of%20Canada</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row169" class="row_heading level0 row169" >263</th>
      <td id="T_baf65_row169_col0" class="data row169 col0" >Analyst, Development Infrastructure - Junior</td>
      <td id="T_baf65_row169_col1" class="data row169 col1" > The prospective employee will report to the Development Services manager and will be supporting the engineering community in a wide variety of work. </td>
      <td id="T_baf65_row169_col2" class="data row169 col2" >30+ days ago</td>
      <td id="T_baf65_row169_col3" class="data row169 col3" >https://ca.indeed.com/jobs?q=Analyst%2C%20Development%20Infrastructure%20-%20Junior%20General%20Dynamics%20Missions%20Systems-Canada</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row170" class="row_heading level0 row170" >270</th>
      <td id="T_baf65_row170_col0" class="data row170 col0" >Junior DevOps Engineer</td>
      <td id="T_baf65_row170_col1" class="data row170 col1" > This job involves development and maintenance of scalable, secure and highly-available services and infrastructure for online gaming such as player progression,… </td>
      <td id="T_baf65_row170_col2" class="data row170 col2" >30+ days ago</td>
      <td id="T_baf65_row170_col3" class="data row170 col3" >https://ca.indeed.com/jobs?q=Junior%20DevOps%20Engineer%20Hellbent%20Games</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row171" class="row_heading level0 row171" >272</th>
      <td id="T_baf65_row171_col0" class="data row171 col0" >DevOps SRE - Junior</td>
      <td id="T_baf65_row171_col1" class="data row171 col1" > The SRE will modernize, transform, and maintain legacy and micro-segment capabilities to continuously improve quality, performance, availability, reliability,… </td>
      <td id="T_baf65_row171_col2" class="data row171 col2" >30+ days ago</td>
      <td id="T_baf65_row171_col3" class="data row171 col3" >https://ca.indeed.com/jobs?q=DevOps%20SRE%20-%20Junior%20NTT%20DATA</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row172" class="row_heading level0 row172" >273</th>
      <td id="T_baf65_row172_col0" class="data row172 col0" >Software Engineer I/II</td>
      <td id="T_baf65_row172_col1" class="data row172 col1" > You will have opportunities to work on multiple layers of the technology stack, ranging from customer-focused user experience work, building scalable… </td>
      <td id="T_baf65_row172_col2" class="data row172 col2" >30+ days ago</td>
      <td id="T_baf65_row172_col3" class="data row172 col3" >https://ca.indeed.com/jobs?q=Software%20Engineer%20I/II%20Microsoft</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row173" class="row_heading level0 row173" >274</th>
      <td id="T_baf65_row173_col0" class="data row173 col0" >MRI Physicist, Junior</td>
      <td id="T_baf65_row173_col1" class="data row173 col1" > The MRI Physicist position is an opportunity to develop applications on this novel system that leverage unique aspects of Synaptive MRI systems to address… </td>
      <td id="T_baf65_row173_col2" class="data row173 col2" >30+ days ago</td>
      <td id="T_baf65_row173_col3" class="data row173 col3" >https://ca.indeed.com/jobs?q=MRI%20Physicist%2C%20Junior%20Synaptive%20Medical%20Inc.</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row174" class="row_heading level0 row174" >275</th>
      <td id="T_baf65_row174_col0" class="data row174 col0" >Développeur(se) de logiciels junior</td>
      <td id="T_baf65_row174_col1" class="data row174 col1" > Maritime International, une division de L3Harris, est un fournisseur mondial de premier plan de contrôles-commandes non ITAR et de solutions de simulation pour… </td>
      <td id="T_baf65_row174_col2" class="data row174 col2" >30+ days ago</td>
      <td id="T_baf65_row174_col3" class="data row174 col3" >https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%28se%29%20de%20logiciels%20junior%20French%20Canadian%20Instance</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row175" class="row_heading level0 row175" >276</th>
      <td id="T_baf65_row175_col0" class="data row175 col0" >Junior Product Management Specialist</td>
      <td id="T_baf65_row175_col1" class="data row175 col1" > The successful candidate will join the Product Management team and specialize in solution documentation. In this position you would be responsible for sourcing,… </td>
      <td id="T_baf65_row175_col2" class="data row175 col2" >30+ days ago</td>
      <td id="T_baf65_row175_col3" class="data row175 col3" >https://ca.indeed.com/jobs?q=Junior%20Product%20Management%20Specialist%20Fortinet</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row176" class="row_heading level0 row176" >277</th>
      <td id="T_baf65_row176_col0" class="data row176 col0" >Junior C/C++ & Fortran Compiler Developer</td>
      <td id="T_baf65_row176_col1" class="data row176 col1" > Software Developers at IBM are the backbone of our strategic initiatives to design, code, test, and provide industry-leading solutions that make the world run… </td>
      <td id="T_baf65_row176_col2" class="data row176 col2" >30+ days ago</td>
      <td id="T_baf65_row176_col3" class="data row176 col3" >https://ca.indeed.com/jobs?q=Junior%20C/C%2B%2B%20%26%20Fortran%20Compiler%20Developer%20IBM</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row177" class="row_heading level0 row177" >271</th>
      <td id="T_baf65_row177_col0" class="data row177 col0" >Vancouver | Matchmove Artist | Junior</td>
      <td id="T_baf65_row177_col1" class="data row177 col1" > You will be working with artists with a wealth of experience on various productions. It is important to have basic knowledge of Syntheyes and matchmove. </td>
      <td id="T_baf65_row177_col2" class="data row177 col2" >30+ days ago</td>
      <td id="T_baf65_row177_col3" class="data row177 col3" >https://ca.indeed.com/jobs?q=Vancouver%20%7C%20Matchmove%20Artist%20%7C%20Junior%20Track%20Visual%20Effects</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row178" class="row_heading level0 row178" >244</th>
      <td id="T_baf65_row178_col0" class="data row178 col0" >Junior ASIC Verification Engineer</td>
      <td id="T_baf65_row178_col1" class="data row178 col1" > You will work closely with ASIC design and verification engineers to verify SOC function features, close function &amp; code coverage holes. </td>
      <td id="T_baf65_row178_col2" class="data row178 col2" >30+ days ago</td>
      <td id="T_baf65_row178_col3" class="data row178 col3" >https://ca.indeed.com/jobs?q=Junior%20ASIC%20Verification%20Engineer%20NETINT%20Technologies%20Inc.</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row179" class="row_heading level0 row179" >246</th>
      <td id="T_baf65_row179_col0" class="data row179 col0" >Junior Software Engineer</td>
      <td id="T_baf65_row179_col1" class="data row179 col1" > Participate in daily standup and other team meetings. Identify, prioritize and execute tasks in the software development life cycle. </td>
      <td id="T_baf65_row179_col2" class="data row179 col2" >30+ days ago</td>
      <td id="T_baf65_row179_col3" class="data row179 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Engineer%20PointClickCare</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row180" class="row_heading level0 row180" >247</th>
      <td id="T_baf65_row180_col0" class="data row180 col0" >Solutions Architect I - AWS-T3210</td>
      <td id="T_baf65_row180_col1" class="data row180 col1" > Bachelor’s degree or foreign equivalent in Computer Science, Engineering, Mathematics, or a related field. 1 year of experience in the job offered or related… </td>
      <td id="T_baf65_row180_col2" class="data row180 col2" >30+ days ago</td>
      <td id="T_baf65_row180_col3" class="data row180 col3" >https://ca.indeed.com/jobs?q=Solutions%20Architect%20I%20-%20AWS-T3210%20Amazon%20Web%20Services%20Canada%2C%20In</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row181" class="row_heading level0 row181" >53</th>
      <td id="T_baf65_row181_col0" class="data row181 col0" >Jr. Power BI Developer</td>
      <td id="T_baf65_row181_col1" class="data row181 col1" > Leading the design and development of consumer-facing reporting and analytics solutions, including data modeling and data visualization. </td>
      <td id="T_baf65_row181_col2" class="data row181 col2" >30+ days ago</td>
      <td id="T_baf65_row181_col3" class="data row181 col3" >https://ca.indeed.com/jobs?q=Jr.%20Power%20BI%20Developer%20Bond%20Brand%20Loyalty%20Inc</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row182" class="row_heading level0 row182" >249</th>
      <td id="T_baf65_row182_col0" class="data row182 col0" >Junior Electrical Engineer</td>
      <td id="T_baf65_row182_col1" class="data row182 col1" > Work collaboratively with clients, project managers, engineers, designers and drafters in the preparation of deliverables to BBA and client standards. </td>
      <td id="T_baf65_row182_col2" class="data row182 col2" >30+ days ago</td>
      <td id="T_baf65_row182_col3" class="data row182 col3" >https://ca.indeed.com/jobs?q=Junior%20Electrical%20Engineer%20BBA</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row183" class="row_heading level0 row183" >250</th>
      <td id="T_baf65_row183_col0" class="data row183 col0" >Junior Mechanical Engineer</td>
      <td id="T_baf65_row183_col1" class="data row183 col1" > We are seeking a Junior Mechanical Engineer to join our Process and Mine Infrastructure Design team on a full-time basis based in our Sudbury or Mississauga… </td>
      <td id="T_baf65_row183_col2" class="data row183 col2" >30+ days ago</td>
      <td id="T_baf65_row183_col3" class="data row183 col3" >https://ca.indeed.com/jobs?q=Junior%20Mechanical%20Engineer%20WSP</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row184" class="row_heading level0 row184" >251</th>
      <td id="T_baf65_row184_col0" class="data row184 col0" >Junior/Intermediate Wind Engineer Project Coordinator - Buil...</td>
      <td id="T_baf65_row184_col1" class="data row184 col1" > Solving challenging problems related to wind engineering of high-rise buildings, long-span roofs, stadia, and other special structures in the built environment. </td>
      <td id="T_baf65_row184_col2" class="data row184 col2" >30+ days ago</td>
      <td id="T_baf65_row184_col3" class="data row184 col3" >https://ca.indeed.com/jobs?q=Junior/Intermediate%20Wind%20Engineer%20Project%20Coordinator%20-%20Buil...%20RWDI</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row185" class="row_heading level0 row185" >261</th>
      <td id="T_baf65_row185_col0" class="data row185 col0" >Junior Actuarial Associate - Corporate Actuarial</td>
      <td id="T_baf65_row185_col1" class="data row185 col1" > This position is part of the Canadian Corporate Actuarial Team, which is responsible for actuarial activities associated with SCORâ€™s Canada Life &amp; Health… </td>
      <td id="T_baf65_row185_col2" class="data row185 col2" >30+ days ago</td>
      <td id="T_baf65_row185_col3" class="data row185 col3" >https://ca.indeed.com/jobs?q=Junior%20Actuarial%20Associate%20-%20Corporate%20Actuarial%20SCOR</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row186" class="row_heading level0 row186" >252</th>
      <td id="T_baf65_row186_col0" class="data row186 col0" >Junior Embedded Software Designer</td>
      <td id="T_baf65_row186_col1" class="data row186 col1" > Currently, our engineering team is seeking a full-time Junior Embedded Software Developer, to work in a hybrid environment based in our Ottawa ON office. </td>
      <td id="T_baf65_row186_col2" class="data row186 col2" >30+ days ago</td>
      <td id="T_baf65_row186_col3" class="data row186 col3" >https://ca.indeed.com/jobs?q=Junior%20Embedded%20Software%20Designer%20Allen%20Vanguard</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row187" class="row_heading level0 row187" >254</th>
      <td id="T_baf65_row187_col0" class="data row187 col0" >Jr/Intermediate Software Engineer, ProAV Embedded</td>
      <td id="T_baf65_row187_col1" class="data row187 col1" > Design, develop, test, deploy, maintain and improve software. Manage individual project priorities, deadlines and deliverables. Social events and sports teams. </td>
      <td id="T_baf65_row187_col2" class="data row187 col2" >30+ days ago</td>
      <td id="T_baf65_row187_col3" class="data row187 col3" >https://ca.indeed.com/jobs?q=Jr/Intermediate%20Software%20Engineer%2C%20ProAV%20Embedded%20Evertz%20Microsystems%20Limited</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row188" class="row_heading level0 row188" >256</th>
      <td id="T_baf65_row188_col0" class="data row188 col0" >Junior Software Developer</td>
      <td id="T_baf65_row188_col1" class="data row188 col1" > Financial Risk Analytics is part of the IHS Markit group and provides industry leading risk analytics solutions to sell side institutions within the financial… </td>
      <td id="T_baf65_row188_col2" class="data row188 col2" >30+ days ago</td>
      <td id="T_baf65_row188_col3" class="data row188 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20S%26P%20Global</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row189" class="row_heading level0 row189" >257</th>
      <td id="T_baf65_row189_col0" class="data row189 col0" >Pipeline Technical Director, Level I Vancouver, BC</td>
      <td id="T_baf65_row189_col1" class="data row189 col1" > Position at Industrial Light &amp; Magic. The Pipeline TD develops and maintains software tools, providing front-line support to artists, and general… </td>
      <td id="T_baf65_row189_col2" class="data row189 col2" >30+ days ago</td>
      <td id="T_baf65_row189_col3" class="data row189 col3" >https://ca.indeed.com/jobs?q=Pipeline%20Technical%20Director%2C%20Level%20I%20Vancouver%2C%20BC%20Industrial%20Light%20%26%20Magic</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row190" class="row_heading level0 row190" >258</th>
      <td id="T_baf65_row190_col0" class="data row190 col0" >Spécialiste d'opérations T.I</td>
      <td id="T_baf65_row190_col1" class="data row190 col1" > En tant que Spécialiste des opérations TI, vous aurez l’opportunité d’améliorer la productivité de tous les employés de l'entreprise. </td>
      <td id="T_baf65_row190_col2" class="data row190 col2" >30+ days ago</td>
      <td id="T_baf65_row190_col3" class="data row190 col3" >https://ca.indeed.com/jobs?q=Sp%C3%A9cialiste%20d%27op%C3%A9rations%20T.I%20Robert%20Half</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row191" class="row_heading level0 row191" >259</th>
      <td id="T_baf65_row191_col0" class="data row191 col0" >Jr. Nuage/Cloud 2LS CS Engineer</td>
      <td id="T_baf65_row191_col1" class="data row191 col1" > Ability to write scripts at a Unix/Linux level (bash, python). Come create the technology that helps the world act together. The team you’ll part of. </td>
      <td id="T_baf65_row191_col2" class="data row191 col2" >30+ days ago</td>
      <td id="T_baf65_row191_col3" class="data row191 col3" >https://ca.indeed.com/jobs?q=Jr.%20Nuage/Cloud%202LS%20CS%20Engineer%20NOKIA</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row192" class="row_heading level0 row192" >253</th>
      <td id="T_baf65_row192_col0" class="data row192 col0" >Cyber Security Engineer I - Threat Protect</td>
      <td id="T_baf65_row192_col1" class="data row192 col1" > TD Engineering covers a broad range of exercises and initiatives including requirements gathering, design specification, industry analysis, vendor engagement… </td>
      <td id="T_baf65_row192_col2" class="data row192 col2" >30+ days ago</td>
      <td id="T_baf65_row192_col3" class="data row192 col3" >https://ca.indeed.com/jobs?q=Cyber%20Security%20Engineer%20I%20-%20Threat%20Protect%20TD%20Bank</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row193" class="row_heading level0 row193" >54</th>
      <td id="T_baf65_row193_col0" class="data row193 col0" >Junior Data Scientist</td>
      <td id="T_baf65_row193_col1" class="data row193 col1" > Reviews clinical data at aggregate levels on a regular basis using analytical reporting tools to support the identification of risks and data patterns or trends… </td>
      <td id="T_baf65_row193_col2" class="data row193 col2" >30+ days ago</td>
      <td id="T_baf65_row193_col3" class="data row193 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Scientist%20Providence%20Health%20Care</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row194" class="row_heading level0 row194" >58</th>
      <td id="T_baf65_row194_col0" class="data row194 col0" >Junior Pricing Analyst</td>
      <td id="T_baf65_row194_col1" class="data row194 col1" > Collects data and maintains the database. Prepares financial and sku analysis reports, analyses margins and competitive market data. </td>
      <td id="T_baf65_row194_col2" class="data row194 col2" >30+ days ago</td>
      <td id="T_baf65_row194_col3" class="data row194 col3" >https://ca.indeed.com/jobs?q=Junior%20Pricing%20Analyst%20B%C3%A9langer%20UPT</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row195" class="row_heading level0 row195" >56</th>
      <td id="T_baf65_row195_col0" class="data row195 col0" >IT Support – Junior Data Coordinator</td>
      <td id="T_baf65_row195_col1" class="data row195 col1" > Coordinate and manipulate all data that is derived from WM Systems. Create reports in Microsoft Excel, Word and PowerPoint as required. </td>
      <td id="T_baf65_row195_col2" class="data row195 col2" >30+ days ago</td>
      <td id="T_baf65_row195_col3" class="data row195 col3" >https://ca.indeed.com/jobs?q=IT%20Support%20%E2%80%93%20Junior%20Data%20Coordinator%20Wellsite%20Masters</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row196" class="row_heading level0 row196" >170</th>
      <td id="T_baf65_row196_col0" class="data row196 col0" >Junior DevOps Engineer</td>
      <td id="T_baf65_row196_col1" class="data row196 col1" > As a Junior DevOps Engineer, your main priorities will be to work with our developers to help us build and maintain our technology stack in support of the… </td>
      <td id="T_baf65_row196_col2" class="data row196 col2" >30+ days ago</td>
      <td id="T_baf65_row196_col3" class="data row196 col3" >https://ca.indeed.com/jobs?q=Junior%20DevOps%20Engineer%20Navigator%20Games</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row197" class="row_heading level0 row197" >169</th>
      <td id="T_baf65_row197_col0" class="data row197 col0" >Jr. Software Engineer - Lighthouse</td>
      <td id="T_baf65_row197_col1" class="data row197 col1" > Work closely with clients to understand key business issues. Gather and analyze requirements to develop impactful recommendations and solutions. </td>
      <td id="T_baf65_row197_col2" class="data row197 col2" >30+ days ago</td>
      <td id="T_baf65_row197_col3" class="data row197 col3" >https://ca.indeed.com/jobs?q=Jr.%20Software%20Engineer%20-%20Lighthouse%20KPMG</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row198" class="row_heading level0 row198" >168</th>
      <td id="T_baf65_row198_col0" class="data row198 col0" >Junior Developer/Programmer</td>
      <td id="T_baf65_row198_col1" class="data row198 col1" > Maintain software design consistency, aesthetics, and functionality of web application pages, communications systems, and data processing. </td>
      <td id="T_baf65_row198_col2" class="data row198 col2" >30+ days ago</td>
      <td id="T_baf65_row198_col3" class="data row198 col3" >https://ca.indeed.com/jobs?q=Junior%20Developer/Programmer%20SimplyCast</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row199" class="row_heading level0 row199" >167</th>
      <td id="T_baf65_row199_col0" class="data row199 col0" >Technical Support Specialist I</td>
      <td id="T_baf65_row199_col1" class="data row199 col1" > Our Technical Support Specialists manage and develop key relationships with our enterprise and small business customers as the first key point of contact for… </td>
      <td id="T_baf65_row199_col2" class="data row199 col2" >30+ days ago</td>
      <td id="T_baf65_row199_col3" class="data row199 col3" >https://ca.indeed.com/jobs?q=Technical%20Support%20Specialist%20I%20Coconut%20Software</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row200" class="row_heading level0 row200" >166</th>
      <td id="T_baf65_row200_col0" class="data row200 col0" >Conseiller(ère) Junior en plateformes de données et intellig...</td>
      <td id="T_baf65_row200_col1" class="data row200 col1" > / Carry out projects with potential returns and economic benefits for Quebecers. / Collaborate on dynamic teams with high-level professionals committed to… </td>
      <td id="T_baf65_row200_col2" class="data row200 col2" >30+ days ago</td>
      <td id="T_baf65_row200_col3" class="data row200 col3" >https://ca.indeed.com/jobs?q=Conseiller%28%C3%A8re%29%20Junior%20en%20plateformes%20de%20donn%C3%A9es%20et%20intellig...%20Caisse%20de%20d%C3%A9p%C3%B4t%20et%20placement%20du%20Qu%C3%A9bec</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row201" class="row_heading level0 row201" >165</th>
      <td id="T_baf65_row201_col0" class="data row201 col0" >Jr. Software Engineer</td>
      <td id="T_baf65_row201_col1" class="data row201 col1" > With a strong, active and familial culture, Pub United is the agency’s social club, hosting events as wide reaching as Curling, Trivia Nights and more. </td>
      <td id="T_baf65_row201_col2" class="data row201 col2" >30+ days ago</td>
      <td id="T_baf65_row201_col3" class="data row201 col3" >https://ca.indeed.com/jobs?q=Jr.%20Software%20Engineer%20Publicis%20Worldwide</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row202" class="row_heading level0 row202" >164</th>
      <td id="T_baf65_row202_col0" class="data row202 col0" >Junior Web Developer</td>
      <td id="T_baf65_row202_col1" class="data row202 col1" > Provide programming supports to lead developer on an Seed to Sale Cannabis Enterprise Software project. Develop documentation and assistance tools to support… </td>
      <td id="T_baf65_row202_col2" class="data row202 col2" >30+ days ago</td>
      <td id="T_baf65_row202_col3" class="data row202 col3" >https://ca.indeed.com/jobs?q=Junior%20Web%20Developer%20Trellis</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row203" class="row_heading level0 row203" >163</th>
      <td id="T_baf65_row203_col0" class="data row203 col0" >Junior Full Stack Developer</td>
      <td id="T_baf65_row203_col1" class="data row203 col1" > We are seeking for a Junior Full Stack Developer to join our team who will be responsible for participating in all phases of the development life-cycle,… </td>
      <td id="T_baf65_row203_col2" class="data row203 col2" >30+ days ago</td>
      <td id="T_baf65_row203_col3" class="data row203 col3" >https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20Steelhaus%20Technologies</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row204" class="row_heading level0 row204" >162</th>
      <td id="T_baf65_row204_col0" class="data row204 col0" >Junior Database Administrator</td>
      <td id="T_baf65_row204_col1" class="data row204 col1" > They act as strategic partners with each business unit to help Questrade leverage technology to gain competitive advantage. You have experience with GIT/GitLab. </td>
      <td id="T_baf65_row204_col2" class="data row204 col2" >30+ days ago</td>
      <td id="T_baf65_row204_col3" class="data row204 col3" >https://ca.indeed.com/jobs?q=Junior%20Database%20Administrator%20Questrade%20Financial%20Group</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row205" class="row_heading level0 row205" >161</th>
      <td id="T_baf65_row205_col0" class="data row205 col0" >Jr. Product Owner</td>
      <td id="T_baf65_row205_col1" class="data row205 col1" > The Jr. Product Owner at Labatt requires a technical expertise to create, deliver and support a product roadmap for our custom internal Ordering tool built on… </td>
      <td id="T_baf65_row205_col2" class="data row205 col2" >30+ days ago</td>
      <td id="T_baf65_row205_col3" class="data row205 col3" >https://ca.indeed.com/jobs?q=Jr.%20Product%20Owner%20Labatt%20Breweries%20Canada</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row206" class="row_heading level0 row206" >160</th>
      <td id="T_baf65_row206_col0" class="data row206 col0" >Junior Integration Analyst</td>
      <td id="T_baf65_row206_col1" class="data row206 col1" > Your role will be to help develop applications, technological options and proposed solutions, from project design to implementation, mainly in production data… </td>
      <td id="T_baf65_row206_col2" class="data row206 col2" >30+ days ago</td>
      <td id="T_baf65_row206_col3" class="data row206 col3" >https://ca.indeed.com/jobs?q=Junior%20Integration%20Analyst%20BBA</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row207" class="row_heading level0 row207" >159</th>
      <td id="T_baf65_row207_col0" class="data row207 col0" >Part-time Low Code Junior Developer Experience@siemens</td>
      <td id="T_baf65_row207_col1" class="data row207 col1" > Recent graduates enrolled in this program will be partnered with a mentor and receive one on one coaching and guidance in support of their development and to… </td>
      <td id="T_baf65_row207_col2" class="data row207 col2" >30+ days ago</td>
      <td id="T_baf65_row207_col3" class="data row207 col3" >https://ca.indeed.com/jobs?q=Part-time%20Low%20Code%20Junior%20Developer%20Experience%40siemens%20Siemens</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row208" class="row_heading level0 row208" >158</th>
      <td id="T_baf65_row208_col0" class="data row208 col0" >Junior Systems Analyst (New Grads )</td>
      <td id="T_baf65_row208_col1" class="data row208 col1" > Developing for MS Power Platform concepts (PowerApp, PowerBI, PowerAutomate). Provide Technical Consulting and Training for Citizen developers. </td>
      <td id="T_baf65_row208_col2" class="data row208 col2" >30+ days ago</td>
      <td id="T_baf65_row208_col3" class="data row208 col3" >https://ca.indeed.com/jobs?q=Junior%20Systems%20Analyst%20%28New%20Grads%20%29%20BASF</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row209" class="row_heading level0 row209" >157</th>
      <td id="T_baf65_row209_col0" class="data row209 col0" >Développeur(se) Junior, Intelligence d'affaires</td>
      <td id="T_baf65_row209_col1" class="data row209 col1" > / Carry out projects with potential returns and economic benefits for Quebecers. / Collaborate on dynamic teams with high-level professionals committed to… </td>
      <td id="T_baf65_row209_col2" class="data row209 col2" >30+ days ago</td>
      <td id="T_baf65_row209_col3" class="data row209 col3" >https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%28se%29%20Junior%2C%20Intelligence%20d%27affaires%20Caisse%20de%20d%C3%A9p%C3%B4t%20et%20placement%20du%20Qu%C3%A9bec</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row210" class="row_heading level0 row210" >156</th>
      <td id="T_baf65_row210_col0" class="data row210 col0" >Junior Developer Analyst</td>
      <td id="T_baf65_row210_col1" class="data row210 col1" > Looking for junior/intermediate candidates getting started in their career and have room to grow - Specifically (2 – 5 years of experience). </td>
      <td id="T_baf65_row210_col2" class="data row210 col2" >30+ days ago</td>
      <td id="T_baf65_row210_col3" class="data row210 col3" >https://ca.indeed.com/jobs?q=Junior%20Developer%20Analyst%20Fujitsu</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row211" class="row_heading level0 row211" >154</th>
      <td id="T_baf65_row211_col0" class="data row211 col0" >Junior Associate Director, Middle Office Operations, MOV</td>
      <td id="T_baf65_row211_col1" class="data row211 col1" > Reporting to the Director, Middle Office and Valuation, you will have an important role in ensuring we provide quality fund administration services to our… </td>
      <td id="T_baf65_row211_col2" class="data row211 col2" >30+ days ago</td>
      <td id="T_baf65_row211_col3" class="data row211 col3" >https://ca.indeed.com/jobs?q=Junior%20Associate%20Director%2C%20Middle%20Office%20Operations%2C%20MOV%20Mitsubishi%20UFJ%20Fund%20Services</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row212" class="row_heading level0 row212" >79</th>
      <td id="T_baf65_row212_col0" class="data row212 col0" >Analyste adjoint(e) bilingue en gestion de données / Junior...</td>
      <td id="T_baf65_row212_col1" class="data row212 col1" > Handling the data enrichment of the small to medium data customers by vertically coordinating with customers, Data Quality and IT for new data or current data… </td>
      <td id="T_baf65_row212_col2" class="data row212 col2" >30+ days ago</td>
      <td id="T_baf65_row212_col3" class="data row212 col3" >https://ca.indeed.com/jobs?q=Analyste%20adjoint%28e%29%20bilingue%20en%20gestion%20de%20donn%C3%A9es%20/%20Junior...%20Equifax</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row213" class="row_heading level0 row213" >78</th>
      <td id="T_baf65_row213_col0" class="data row213 col0" >Junior Digital Marketing Specialist</td>
      <td id="T_baf65_row213_col1" class="data row213 col1" > Widespread media monitoring to collect data about Air Borealis brand mentions and news articles. Media monitoring to collect data about the aviation industry… </td>
      <td id="T_baf65_row213_col2" class="data row213 col2" >30 days ago</td>
      <td id="T_baf65_row213_col3" class="data row213 col3" >https://ca.indeed.com/jobs?q=Junior%20Digital%20Marketing%20Specialist%20PAL</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row214" class="row_heading level0 row214" >77</th>
      <td id="T_baf65_row214_col0" class="data row214 col0" >Jr. Business Intelligence Developer, Enterprise Analytics</td>
      <td id="T_baf65_row214_col1" class="data row214 col1" > Develop ETL procedures, SSIS packages and maintain data flow processes. Advanced understanding of data warehousing concepts and best practices required. </td>
      <td id="T_baf65_row214_col2" class="data row214 col2" >30+ days ago</td>
      <td id="T_baf65_row214_col3" class="data row214 col3" >https://ca.indeed.com/jobs?q=Jr.%20Business%20Intelligence%20Developer%2C%20Enterprise%20Analytics%20Southlake%20Regional%20Health%20Centre</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row215" class="row_heading level0 row215" >76</th>
      <td id="T_baf65_row215_col0" class="data row215 col0" >Mechanical EIT, Data Centres</td>
      <td id="T_baf65_row215_col1" class="data row215 col1" > Basic knowledge of building mechanical systems to support data centres (DCs); This position is focused on data centres, telecom COs and other mission-critical… </td>
      <td id="T_baf65_row215_col2" class="data row215 col2" >30+ days ago</td>
      <td id="T_baf65_row215_col3" class="data row215 col3" >https://ca.indeed.com/jobs?q=Mechanical%20EIT%2C%20Data%20Centres%20WSP</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row216" class="row_heading level0 row216" >75</th>
      <td id="T_baf65_row216_col0" class="data row216 col0" >Financial Analyst I</td>
      <td id="T_baf65_row216_col1" class="data row216 col1" >Job Field: Finance/Accounting Job Type: Full-time Building Location: Length of Assignment: Who We Are BGIS is a leading provider of customized facility…</td>
      <td id="T_baf65_row216_col2" class="data row216 col2" >30+ days ago</td>
      <td id="T_baf65_row216_col3" class="data row216 col3" >https://ca.indeed.com/jobs?q=Financial%20Analyst%20I%20BGIS</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row217" class="row_heading level0 row217" >74</th>
      <td id="T_baf65_row217_col0" class="data row217 col0" >Commercial Financial Analyst I</td>
      <td id="T_baf65_row217_col1" class="data row217 col1" > Data management experience and the ability to manage large sets of data and accurate reports. As part of the commercial finance organization, your position will… </td>
      <td id="T_baf65_row217_col2" class="data row217 col2" >30+ days ago</td>
      <td id="T_baf65_row217_col3" class="data row217 col3" >https://ca.indeed.com/jobs?q=Commercial%20Financial%20Analyst%20I%20Thermo%20Fisher%20Scientific</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row218" class="row_heading level0 row218" >171</th>
      <td id="T_baf65_row218_col0" class="data row218 col0" >Jr .Net</td>
      <td id="T_baf65_row218_col1" class="data row218 col1" > Strong on SQL server programming. T4 hire with option to train can be considered. 1 to 2 years of experience. Strong on SQL server programming. </td>
      <td id="T_baf65_row218_col2" class="data row218 col2" >30+ days ago</td>
      <td id="T_baf65_row218_col3" class="data row218 col3" >https://ca.indeed.com/jobs?q=Jr%20.Net%20Virtusa</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row219" class="row_heading level0 row219" >73</th>
      <td id="T_baf65_row219_col0" class="data row219 col0" >Développeur BI junior</td>
      <td id="T_baf65_row219_col1" class="data row219 col1" > Alors que la technologie s’inscrit au cœur de la transformation numérique de nos clients, nous savons que les individus sont au cœur du succès en affaires. </td>
      <td id="T_baf65_row219_col2" class="data row219 col2" >30+ days ago</td>
      <td id="T_baf65_row219_col3" class="data row219 col3" >https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20BI%20junior%20CGI</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row220" class="row_heading level0 row220" >148</th>
      <td id="T_baf65_row220_col0" class="data row220 col0" >Full Stack Engineer (Junior)</td>
      <td id="T_baf65_row220_col1" class="data row220 col1" > As a FullStack Engineer, you will be responsible for implementing real-time and highly scalable and distributed software for our Call Center As A Service (CCAAS… </td>
      <td id="T_baf65_row220_col2" class="data row220 col2" >30+ days ago</td>
      <td id="T_baf65_row220_col3" class="data row220 col3" >https://ca.indeed.com/jobs?q=Full%20Stack%20Engineer%20%28Junior%29%20Sangoma</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row221" class="row_heading level0 row221" >149</th>
      <td id="T_baf65_row221_col0" class="data row221 col0" >Junior Software Developer</td>
      <td id="T_baf65_row221_col1" class="data row221 col1" > Work closely with other developers in an agile and collaborative environment to foster continuous improvement at the team and company level. </td>
      <td id="T_baf65_row221_col2" class="data row221 col2" >30+ days ago</td>
      <td id="T_baf65_row221_col3" class="data row221 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20Bioinformatics%20Solutions</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row222" class="row_heading level0 row222" >150</th>
      <td id="T_baf65_row222_col0" class="data row222 col0" >Jr. Network Administrator</td>
      <td id="T_baf65_row222_col1" class="data row222 col1" > Able to provide tech support in/out office. Might occasionally have to give technical support to clients. Should be able to work after work hours (Saturdays… </td>
      <td id="T_baf65_row222_col2" class="data row222 col2" >30+ days ago</td>
      <td id="T_baf65_row222_col3" class="data row222 col3" >https://ca.indeed.com/jobs?q=Jr.%20Network%20Administrator%20BreezeMaxWeb</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row223" class="row_heading level0 row223" >152</th>
      <td id="T_baf65_row223_col0" class="data row223 col0" >Junior Web Developer</td>
      <td id="T_baf65_row223_col1" class="data row223 col1" > You will work with cutting-edge technologies, learn how they are applied in the ecommerce sector, and collaborate extensively with stakeholders and the… </td>
      <td id="T_baf65_row223_col2" class="data row223 col2" >30+ days ago</td>
      <td id="T_baf65_row223_col3" class="data row223 col3" >https://ca.indeed.com/jobs?q=Junior%20Web%20Developer%20Scribendi</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row224" class="row_heading level0 row224" >153</th>
      <td id="T_baf65_row224_col0" class="data row224 col0" >Programmeur ou Programmeuse Analyste Junior - Télétravail</td>
      <td id="T_baf65_row224_col1" class="data row224 col1" > Vous y aurez d’innombrables occasions d'apprendre et de développer des compétences variées en travaillant sur des projets mobilisateurs. </td>
      <td id="T_baf65_row224_col2" class="data row224 col2" >30+ days ago</td>
      <td id="T_baf65_row224_col3" class="data row224 col3" >https://ca.indeed.com/jobs?q=Programmeur%20ou%20Programmeuse%20Analyste%20Junior%20-%20T%C3%A9l%C3%A9travail%20CIMA%2B</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row225" class="row_heading level0 row225" >278</th>
      <td id="T_baf65_row225_col0" class="data row225 col0" >Junior Software Developer</td>
      <td id="T_baf65_row225_col1" class="data row225 col1" > Wedge Networks is seeking candidates to fill a junior software development position on our research and development team, developing software for our network… </td>
      <td id="T_baf65_row225_col2" class="data row225 col2" >30+ days ago</td>
      <td id="T_baf65_row225_col3" class="data row225 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20Wedge%20Networks</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row226" class="row_heading level0 row226" >172</th>
      <td id="T_baf65_row226_col0" class="data row226 col0" >Junior Software Engineer</td>
      <td id="T_baf65_row226_col1" class="data row226 col1" > We pack medications by dose and time into “PocketPacks” and deliver them to your doorstep for free. Our platform is hosted on AWS, uses Angular for web, Flutter… </td>
      <td id="T_baf65_row226_col2" class="data row226 col2" >30+ days ago</td>
      <td id="T_baf65_row226_col3" class="data row226 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Engineer%20PocketPills</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row227" class="row_heading level0 row227" >173</th>
      <td id="T_baf65_row227_col0" class="data row227 col0" >Junior Developer</td>
      <td id="T_baf65_row227_col1" class="data row227 col1" > Reporting to the Architecture and Development Manager, the incumbent is working as a member of the Red-D-Arc Information Technology team, responsible for… </td>
      <td id="T_baf65_row227_col2" class="data row227 col2" >30+ days ago</td>
      <td id="T_baf65_row227_col3" class="data row227 col3" >https://ca.indeed.com/jobs?q=Junior%20Developer%20Airgas%20Inc.</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row228" class="row_heading level0 row228" >174</th>
      <td id="T_baf65_row228_col0" class="data row228 col0" >Junior C++ Software Developer</td>
      <td id="T_baf65_row228_col1" class="data row228 col1" > We need software engineers who can help us develop and maintain systems that are always online and can handle hundreds of thousands of transactions per second. </td>
      <td id="T_baf65_row228_col2" class="data row228 col2" >30+ days ago</td>
      <td id="T_baf65_row228_col3" class="data row228 col3" >https://ca.indeed.com/jobs?q=Junior%20C%2B%2B%20Software%20Developer%20S%26P%20Global</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row229" class="row_heading level0 row229" >70</th>
      <td id="T_baf65_row229_col0" class="data row229 col0" >Junior Data Engineer</td>
      <td id="T_baf65_row229_col1" class="data row229 col1" > Work with data engineers, analysts, data scientists, and game developers to determine the data needs of our games. Experience with SQL and database management. </td>
      <td id="T_baf65_row229_col2" class="data row229 col2" >30+ days ago</td>
      <td id="T_baf65_row229_col3" class="data row229 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Engineer%20Hothead%20Games</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row230" class="row_heading level0 row230" >69</th>
      <td id="T_baf65_row230_col0" class="data row230 col0" >Junior Data Engineer</td>
      <td id="T_baf65_row230_col1" class="data row230 col1" > Build and maintain data collection pipelines. Experience using Python to transform data. Manage data refresh intervals and resolve errors. </td>
      <td id="T_baf65_row230_col2" class="data row230 col2" >30+ days ago</td>
      <td id="T_baf65_row230_col3" class="data row230 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Engineer%20Valsoft</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row231" class="row_heading level0 row231" >68</th>
      <td id="T_baf65_row231_col0" class="data row231 col0" >Junior Business Analyst</td>
      <td id="T_baf65_row231_col1" class="data row231 col1" > Work closely with IT team to satisfy data sampling, project analysis, testing verification, and other user requests from existing client databases. </td>
      <td id="T_baf65_row231_col2" class="data row231 col2" >30+ days ago</td>
      <td id="T_baf65_row231_col3" class="data row231 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20Dokainish%20%26%20Company</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row232" class="row_heading level0 row232" >67</th>
      <td id="T_baf65_row232_col0" class="data row232 col0" >Junior Sales Data Coordinator</td>
      <td id="T_baf65_row232_col1" class="data row232 col1" > Reporting to the National Sales &amp; Marketing Director, the Junior Sales Data Coordinator will be internal link between the pricing analyst and inside sales. </td>
      <td id="T_baf65_row232_col2" class="data row232 col2" >30+ days ago</td>
      <td id="T_baf65_row232_col3" class="data row232 col3" >https://ca.indeed.com/jobs?q=Junior%20Sales%20Data%20Coordinator%20B%C3%A9langer%20UPT</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row233" class="row_heading level0 row233" >66</th>
      <td id="T_baf65_row233_col0" class="data row233 col0" >Junior Quantitative Hydrogeologist</td>
      <td id="T_baf65_row233_col1" class="data row233 col1" > Data compilation, reduction, and preliminary interpretation, including water quality results, hydraulic response testing data analysis, water balance model,… </td>
      <td id="T_baf65_row233_col2" class="data row233 col2" >30+ days ago</td>
      <td id="T_baf65_row233_col3" class="data row233 col3" >https://ca.indeed.com/jobs?q=Junior%20Quantitative%20Hydrogeologist%20GHD</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row234" class="row_heading level0 row234" >65</th>
      <td id="T_baf65_row234_col0" class="data row234 col0" >Junior Financial Planning Analyst</td>
      <td id="T_baf65_row234_col1" class="data row234 col1" > Performs trend and variance analyses; incorporates data from different areas and synthesizes. At United Natural Foods Inc. (UNFI) Canada, our mission is simple:… </td>
      <td id="T_baf65_row234_col2" class="data row234 col2" >30+ days ago</td>
      <td id="T_baf65_row234_col3" class="data row234 col3" >https://ca.indeed.com/jobs?q=Junior%20Financial%20Planning%20Analyst%20UNFI</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row235" class="row_heading level0 row235" >71</th>
      <td id="T_baf65_row235_col0" class="data row235 col0" >Junior Project Finance Analyst (Montreal or Laval)</td>
      <td id="T_baf65_row235_col1" class="data row235 col1" > 0 - 5 years of financial/data analysis experience. The primary focuses of this position include: evaluating construction job cost, data reporting/analysis for… </td>
      <td id="T_baf65_row235_col2" class="data row235 col2" >30+ days ago</td>
      <td id="T_baf65_row235_col3" class="data row235 col3" >https://ca.indeed.com/jobs?q=Junior%20Project%20Finance%20Analyst%20%28Montreal%20or%20Laval%29%20Kiewit%20Corporation</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row236" class="row_heading level0 row236" >64</th>
      <td id="T_baf65_row236_col0" class="data row236 col0" >Junior Analyst, Sales Operations & Planning</td>
      <td id="T_baf65_row236_col1" class="data row236 col1" > Support sales data and information tracking related to new vendor onboarding. Strong knowledge of Qlikview or similar data analysis / reporting tools. </td>
      <td id="T_baf65_row236_col2" class="data row236 col2" >30+ days ago</td>
      <td id="T_baf65_row236_col3" class="data row236 col3" >https://ca.indeed.com/jobs?q=Junior%20Analyst%2C%20Sales%20Operations%20%26%20Planning%20UNFI</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row237" class="row_heading level0 row237" >62</th>
      <td id="T_baf65_row237_col0" class="data row237 col0" >Junior Database Analyst</td>
      <td id="T_baf65_row237_col1" class="data row237 col1" > Maintain reliability, stability and data integrity of the databases. 1-2 years of experience as a data administrator in SQL server environment. </td>
      <td id="T_baf65_row237_col2" class="data row237 col2" >30+ days ago</td>
      <td id="T_baf65_row237_col3" class="data row237 col3" >https://ca.indeed.com/jobs?q=Junior%20Database%20Analyst%20HealthHub%20Solutions</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row238" class="row_heading level0 row238" >61</th>
      <td id="T_baf65_row238_col0" class="data row238 col0" >Programmeur(euse) débutant en SQL / SQL Junior Programmer</td>
      <td id="T_baf65_row238_col1" class="data row238 col1" > Experience working with enterprise data. Knowledge of ETL and BI data warehouse architecture is an asset. Solid computer science fundamentals such as algorithms… </td>
      <td id="T_baf65_row238_col2" class="data row238 col2" >30+ days ago</td>
      <td id="T_baf65_row238_col3" class="data row238 col3" >https://ca.indeed.com/jobs?q=Programmeur%28euse%29%20d%C3%A9butant%20en%20SQL%20/%20SQL%20Junior%20Programmer%20Ove%20d%C3%A9cors%20ULC</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row239" class="row_heading level0 row239" >60</th>
      <td id="T_baf65_row239_col0" class="data row239 col0" >Analyst, Client Business I</td>
      <td id="T_baf65_row239_col1" class="data row239 col1" > Works with media partners to distill and analyze their data. Experience using sales data (Nielsen, IRi) required. Manages and tracks all media campaigns. </td>
      <td id="T_baf65_row239_col2" class="data row239 col2" >30+ days ago</td>
      <td id="T_baf65_row239_col3" class="data row239 col3" >https://ca.indeed.com/jobs?q=Analyst%2C%20Client%20Business%20I%20Mosaic%20North%20America</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row240" class="row_heading level0 row240" >59</th>
      <td id="T_baf65_row240_col0" class="data row240 col0" >Business Operations Analyst I, AWS Commerce Platform Busines...</td>
      <td id="T_baf65_row240_col1" class="data row240 col1" > At least 1+ years of experience with data warehousing and reporting. AWS has the most services and more features within those services, than any other cloud… </td>
      <td id="T_baf65_row240_col2" class="data row240 col2" >30+ days ago</td>
      <td id="T_baf65_row240_col3" class="data row240 col3" >https://ca.indeed.com/jobs?q=Business%20Operations%20Analyst%20I%2C%20AWS%20Commerce%20Platform%20Busines...%20Amazon%20Dev%20Centre%20Canada%20ULC</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row241" class="row_heading level0 row241" >81</th>
      <td id="T_baf65_row241_col0" class="data row241 col0" >Junior Asset Management Consultant and Data Analyst</td>
      <td id="T_baf65_row241_col1" class="data row241 col1" > Develop and analyze asset data to support asset management planning. Create and manage asset inventories and data structures, including the development of… </td>
      <td id="T_baf65_row241_col2" class="data row241 col2" >30+ days ago</td>
      <td id="T_baf65_row241_col3" class="data row241 col3" >https://ca.indeed.com/jobs?q=Junior%20Asset%20Management%20Consultant%20and%20Data%20Analyst%20GM%20BluePlan%20Engineering</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row242" class="row_heading level0 row242" >57</th>
      <td id="T_baf65_row242_col0" class="data row242 col0" >Business Analyst I, AWS Commerce Platform Business Operation...</td>
      <td id="T_baf65_row242_col1" class="data row242 col1" > At least 1+ years of experience with data warehousing and reporting. At least 1+ years of professional working experience in related occupations of Business… </td>
      <td id="T_baf65_row242_col2" class="data row242 col2" >30+ days ago</td>
      <td id="T_baf65_row242_col3" class="data row242 col3" >https://ca.indeed.com/jobs?q=Business%20Analyst%20I%2C%20AWS%20Commerce%20Platform%20Business%20Operation...%20Amazon%20Dev%20Centre%20Canada%20ULC</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row243" class="row_heading level0 row243" >63</th>
      <td id="T_baf65_row243_col0" class="data row243 col0" >Junior Financial Data Analyst</td>
      <td id="T_baf65_row243_col1" class="data row243 col1" > Reporting to the Senior Paralegal, and Partner responsible for project completions, this role will assist our high performing Real Estate legal group with… </td>
      <td id="T_baf65_row243_col2" class="data row243 col2" >30+ days ago</td>
      <td id="T_baf65_row243_col3" class="data row243 col3" >https://ca.indeed.com/jobs?q=Junior%20Financial%20Data%20Analyst%20Lawson%20Lundell%20LLP</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row244" class="row_heading level0 row244" >55</th>
      <td id="T_baf65_row244_col0" class="data row244 col0" >Jr. Data Scientist</td>
      <td id="T_baf65_row244_col1" class="data row244 col1" > Integration with 3rd party API’s for data collection and analysis, including weather data, time-series data, and event-based data sets. </td>
      <td id="T_baf65_row244_col2" class="data row244 col2" >30+ days ago</td>
      <td id="T_baf65_row244_col3" class="data row244 col3" >https://ca.indeed.com/jobs?q=Jr.%20Data%20Scientist%20SimpTek%20Technologies</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row245" class="row_heading level0 row245" >72</th>
      <td id="T_baf65_row245_col0" class="data row245 col0" >Junior AI/Database Administrator</td>
      <td id="T_baf65_row245_col1" class="data row245 col1" > Databases – design and implement a database to track and monitor a predetermined set of data points. Excel – track and monitor predetermined set of data points… </td>
      <td id="T_baf65_row245_col2" class="data row245 col2" >30+ days ago</td>
      <td id="T_baf65_row245_col3" class="data row245 col3" >https://ca.indeed.com/jobs?q=Junior%20AI/Database%20Administrator%20Tetra%20Tech</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row246" class="row_heading level0 row246" >176</th>
      <td id="T_baf65_row246_col0" class="data row246 col0" >Junior Capital Accountant</td>
      <td id="T_baf65_row246_col1" class="data row246 col1" > The role will focus on capital projects and all associated financials, including variance analysis, reporting and all financial entries. </td>
      <td id="T_baf65_row246_col2" class="data row246 col2" >30+ days ago</td>
      <td id="T_baf65_row246_col3" class="data row246 col3" >https://ca.indeed.com/jobs?q=Junior%20Capital%20Accountant%20SECURE%20Energy%20Services%20Inc.</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row247" class="row_heading level0 row247" >177</th>
      <td id="T_baf65_row247_col0" class="data row247 col0" >Junior Oracle DBA</td>
      <td id="T_baf65_row247_col1" class="data row247 col1" > Defines and administers data base organization, standards, controls, procedures, and documentation. Provides experienced technical consulting in the definition,… </td>
      <td id="T_baf65_row247_col2" class="data row247 col2" >30+ days ago</td>
      <td id="T_baf65_row247_col3" class="data row247 col3" >https://ca.indeed.com/jobs?q=Junior%20Oracle%20DBA%20AstraNorth</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row248" class="row_heading level0 row248" >178</th>
      <td id="T_baf65_row248_col0" class="data row248 col0" >Junior QA Developer [#3998]</td>
      <td id="T_baf65_row248_col1" class="data row248 col1" > Within an Agile development team (Scrum), the QA Developer is responsible for the development of test cases, the implementation and maintenance of automated and… </td>
      <td id="T_baf65_row248_col2" class="data row248 col2" >30+ days ago</td>
      <td id="T_baf65_row248_col3" class="data row248 col3" >https://ca.indeed.com/jobs?q=Junior%20QA%20Developer%20%5B%233998%5D%20Alteo</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row249" class="row_heading level0 row249" >179</th>
      <td id="T_baf65_row249_col0" class="data row249 col0" >Junior Software Developer; AUI</td>
      <td id="T_baf65_row249_col1" class="data row249 col1" > We offer product record keeping and distribution systems, supporting a full range of investments, accounts and regulatory bodies. </td>
      <td id="T_baf65_row249_col2" class="data row249 col2" >30+ days ago</td>
      <td id="T_baf65_row249_col3" class="data row249 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%3B%20AUI%20RPM%20TECHNOLOGIES%20CORP</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row250" class="row_heading level0 row250" >180</th>
      <td id="T_baf65_row250_col0" class="data row250 col0" >Junior Software Developer</td>
      <td id="T_baf65_row250_col1" class="data row250 col1" > You will support with architecting, developing, and maintaining internal and external facing solutions used for field data collection, document and data… </td>
      <td id="T_baf65_row250_col2" class="data row250 col2" >30+ days ago</td>
      <td id="T_baf65_row250_col3" class="data row250 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20WSP</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row251" class="row_heading level0 row251" >190</th>
      <td id="T_baf65_row251_col0" class="data row251 col0" >Actuarial Analyst</td>
      <td id="T_baf65_row251_col1" class="data row251 col1" > This team is responsible for the valuation of liabilities, calculation of the industry premium rate and other premium related support for the Underwriting area,… </td>
      <td id="T_baf65_row251_col2" class="data row251 col2" >30+ days ago</td>
      <td id="T_baf65_row251_col3" class="data row251 col3" >https://ca.indeed.com/jobs?q=Actuarial%20Analyst%20The%20Workers%27%20Compensation%20Board</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row252" class="row_heading level0 row252" >181</th>
      <td id="T_baf65_row252_col0" class="data row252 col0" >Junior Full Stack Developer</td>
      <td id="T_baf65_row252_col1" class="data row252 col1" > Markdale Financial Management is looking for a part-time Junior Full Stack Web Developer to join our team. Currently an undergrad in Computer Science. </td>
      <td id="T_baf65_row252_col2" class="data row252 col2" >30+ days ago</td>
      <td id="T_baf65_row252_col3" class="data row252 col3" >https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20Markdale%20Financial%20Management</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row253" class="row_heading level0 row253" >183</th>
      <td id="T_baf65_row253_col0" class="data row253 col0" >Junior Software Engineer</td>
      <td id="T_baf65_row253_col1" class="data row253 col1" > Engineering focus areas for this position include wireless gateways, LAN/WAN switches, IoT nodes, interface units and sensors. </td>
      <td id="T_baf65_row253_col2" class="data row253 col2" >30+ days ago</td>
      <td id="T_baf65_row253_col3" class="data row253 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Engineer%20Optima%20Tele.com%2C%20Inc.</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row254" class="row_heading level0 row254" >185</th>
      <td id="T_baf65_row254_col0" class="data row254 col0" >Junior Front-End Web Developer</td>
      <td id="T_baf65_row254_col1" class="data row254 col1" > Entry to Intermediate (1-3 years working experience). Main responsibilities will include interpretation of UI/UX wireframes, creating an inventory of required… </td>
      <td id="T_baf65_row254_col2" class="data row254 col2" >30+ days ago</td>
      <td id="T_baf65_row254_col3" class="data row254 col3" >https://ca.indeed.com/jobs?q=Junior%20Front-End%20Web%20Developer%20ONR</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row255" class="row_heading level0 row255" >186</th>
      <td id="T_baf65_row255_col0" class="data row255 col0" >Junior Power Analyst</td>
      <td id="T_baf65_row255_col1" class="data row255 col1" > Analyzing large amounts of data and keeping a pulse on the 24hr power markets are some key roles of the position. </td>
      <td id="T_baf65_row255_col2" class="data row255 col2" >30+ days ago</td>
      <td id="T_baf65_row255_col3" class="data row255 col3" >https://ca.indeed.com/jobs?q=Junior%20Power%20Analyst%20Dynasty%20Power%20Inc.</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row256" class="row_heading level0 row256" >187</th>
      <td id="T_baf65_row256_col0" class="data row256 col0" >Junior Software Developer; Server</td>
      <td id="T_baf65_row256_col1" class="data row256 col1" > We offer product record keeping and distribution systems, supporting a full range of investments, accounts and regulatory bodies. </td>
      <td id="T_baf65_row256_col2" class="data row256 col2" >30+ days ago</td>
      <td id="T_baf65_row256_col3" class="data row256 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%3B%20Server%20RPM%20TECHNOLOGIES%20CORP</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row257" class="row_heading level0 row257" >182</th>
      <td id="T_baf65_row257_col0" class="data row257 col0" >Junior/Intermediate Hydrogeologist</td>
      <td id="T_baf65_row257_col1" class="data row257 col1" > As a Junior/Intermediate Hydrogeologist, you would be involved in a variety of projects related to hydrogeologic assessment, groundwater supply development, and… </td>
      <td id="T_baf65_row257_col2" class="data row257 col2" >30+ days ago</td>
      <td id="T_baf65_row257_col3" class="data row257 col3" >https://ca.indeed.com/jobs?q=Junior/Intermediate%20Hydrogeologist%20Stantec</td>
    </tr>
    <tr>
      <th id="T_baf65_level0_row258" class="row_heading level0 row258" >279</th>
      <td id="T_baf65_row258_col0" class="data row258 col0" >Junior Analyst, CRM & Business Intelligence</td>
      <td id="T_baf65_row258_col1" class="data row258 col1" > The Junior Analyst, CRM &amp; Business Intelligence is an entry level role that is responsible for the day-to-day CRM management and supporting the Business… </td>
      <td id="T_baf65_row258_col2" class="data row258 col2" >30+ days ago</td>
      <td id="T_baf65_row258_col3" class="data row258 col3" >https://ca.indeed.com/jobs?q=Junior%20Analyst%2C%20CRM%20%26%20Business%20Intelligence%20Vancouver%20Whitecaps%20FC</td>
    </tr>
  </tbody>
</table>





```python

```

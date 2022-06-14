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





<table id="T_c6c4b">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_c6c4b_level0_col0" class="col_heading level0 col0" >titles</th>
      <th id="T_c6c4b_level0_col1" class="col_heading level0 col1" >jobSnippets</th>
      <th id="T_c6c4b_level0_col2" class="col_heading level0 col2" >dates</th>
      <th id="T_c6c4b_level0_col3" class="col_heading level0 col3" >links</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_c6c4b_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_c6c4b_row0_col0" class="data row0 col0" >Junior Business Analyst</td>
      <td id="T_c6c4b_row0_col1" class="data row0 col1" > Management of Excel spreadsheets, including updating and editing data as required. The Business Analysis team is seeking a full-time Junior Business Analyst… </td>
      <td id="T_c6c4b_row0_col2" class="data row0 col2" >Just posted</td>
      <td id="T_c6c4b_row0_col3" class="data row0 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20Centrecorp%20Management%20Services%20Limited</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row1" class="row_heading level0 row1" >81</th>
      <td id="T_c6c4b_row1_col0" class="data row1 col0" >JUNIOR CASE COSTING ANALYST, FT</td>
      <td id="T_c6c4b_row1_col1" class="data row1 col1" > Reporting to the Supervisor Funding Performance, the successful applicant will be an integral part of the case costing team providing support for the… </td>
      <td id="T_c6c4b_row1_col2" class="data row1 col2" >Today</td>
      <td id="T_c6c4b_row1_col3" class="data row1 col3" >https://ca.indeed.com/jobs?q=JUNIOR%20CASE%20COSTING%20ANALYST%2C%20FT%20Niagara%20Health%20System</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row2" class="row_heading level0 row2" >82</th>
      <td id="T_c6c4b_row2_col0" class="data row2 col0" >Junior Full Stack Software Developer - New Grad Opportunity</td>
      <td id="T_c6c4b_row2_col1" class="data row2 col1" > We’re looking for a full stack engineer with progressive technical experience, sharp coding skills, and a passion for building innovative products in a high… </td>
      <td id="T_c6c4b_row2_col2" class="data row2 col2" >Just posted</td>
      <td id="T_c6c4b_row2_col3" class="data row2 col3" >https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Software%20Developer%20-%20New%20Grad%20Opportunity%20Aislelabs</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row3" class="row_heading level0 row3" >83</th>
      <td id="T_c6c4b_row3_col0" class="data row3 col0" >Junior Systems Developer</td>
      <td id="T_c6c4b_row3_col1" class="data row3 col1" > Offering a natural, deep harbour and big ship infrastructure, Halifax can accommodate large volumes of containerized cargo, breakbulk cargo, and project cargo… </td>
      <td id="T_c6c4b_row3_col2" class="data row3 col2" >Just posted</td>
      <td id="T_c6c4b_row3_col3" class="data row3 col3" >https://ca.indeed.com/jobs?q=Junior%20Systems%20Developer%20Halifax%20Port%20Authority</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row4" class="row_heading level0 row4" >84</th>
      <td id="T_c6c4b_row4_col0" class="data row4 col0" >Channel Application Specialist – Junior Developer (Investor'...</td>
      <td id="T_c6c4b_row4_col1" class="data row4 col1" > As Channel Application Specialist – Junior Developer, you will be responsible for assisting the DI&amp;A team including Investor Services, and Global Operations in… </td>
      <td id="T_c6c4b_row4_col2" class="data row4 col2" >Today</td>
      <td id="T_c6c4b_row4_col3" class="data row4 col3" >https://ca.indeed.com/jobs?q=Channel%20Application%20Specialist%20%E2%80%93%20Junior%20Developer%20%28Investor%27...%20CIBC</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row5" class="row_heading level0 row5" >80</th>
      <td id="T_c6c4b_row5_col0" class="data row5 col0" >Junior Underwriter</td>
      <td id="T_c6c4b_row5_col1" class="data row5 col1" > We enable employers to provide their employees with the health care they need and want more comprehensively and cost-effectively than traditional health… </td>
      <td id="T_c6c4b_row5_col2" class="data row5 col2" >Today</td>
      <td id="T_c6c4b_row5_col3" class="data row5 col3" >https://ca.indeed.com/jobs?q=Junior%20Underwriter%20Benecaid</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row6" class="row_heading level0 row6" >188</th>
      <td id="T_c6c4b_row6_col0" class="data row6 col0" >Engineer I ( Cyber System Engineer )</td>
      <td id="T_c6c4b_row6_col1" class="data row6 col1" > PTS designs, delivers and maintains available, adaptable, secure, and cost-effective infrastructure-based technology services to TD and supports the bank’s… </td>
      <td id="T_c6c4b_row6_col2" class="data row6 col2" >Just posted</td>
      <td id="T_c6c4b_row6_col3" class="data row6 col3" >https://ca.indeed.com/jobs?q=Engineer%20I%20%28%20Cyber%20System%20Engineer%20%29%20TD%20Bank</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row7" class="row_heading level0 row7" >189</th>
      <td id="T_c6c4b_row7_col0" class="data row7 col0" >QA Analyst</td>
      <td id="T_c6c4b_row7_col1" class="data row7 col1" > Analyze, document, and prioritize bug reports. Define, implement, and maintain a testing suite. Create and document test scenarios. </td>
      <td id="T_c6c4b_row7_col2" class="data row7 col2" >Just posted</td>
      <td id="T_c6c4b_row7_col3" class="data row7 col3" >https://ca.indeed.com/jobs?q=QA%20Analyst%20SHIPTRACK%20INC.</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row8" class="row_heading level0 row8" >190</th>
      <td id="T_c6c4b_row8_col0" class="data row8 col0" >Junior Embedded Software Engineer</td>
      <td id="T_c6c4b_row8_col1" class="data row8 col1" >*Company Description* ChemChamp is North America’s leading developer of on-site chemical recycling solutions. We are looking for a Junior Embedded Software…</td>
      <td id="T_c6c4b_row8_col2" class="data row8 col2" >Today</td>
      <td id="T_c6c4b_row8_col3" class="data row8 col3" >https://ca.indeed.com/jobs?q=Junior%20Embedded%20Software%20Engineer%20ChemChamp%20North%20America</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row9" class="row_heading level0 row9" >79</th>
      <td id="T_c6c4b_row9_col0" class="data row9 col0" >Jr. Developer</td>
      <td id="T_c6c4b_row9_col1" class="data row9 col1" > The Jr. Developer will participate in all phases of the software development life cycle including design, development, enhancement, and maintenance. </td>
      <td id="T_c6c4b_row9_col2" class="data row9 col2" >Just posted</td>
      <td id="T_c6c4b_row9_col3" class="data row9 col3" >https://ca.indeed.com/jobs?q=Jr.%20Developer%20taq</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row10" class="row_heading level0 row10" >1</th>
      <td id="T_c6c4b_row10_col0" class="data row10 col0" >Junior Pricing Analyst</td>
      <td id="T_c6c4b_row10_col1" class="data row10 col1" > Plays an active role in data governance. Serves as a reference resource for the user community, especially as it relates to pricing and master data maintenance. </td>
      <td id="T_c6c4b_row10_col2" class="data row10 col2" >Just posted</td>
      <td id="T_c6c4b_row10_col3" class="data row10 col3" >https://ca.indeed.com/jobs?q=Junior%20Pricing%20Analyst%20UNFI%20Canada</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row11" class="row_heading level0 row11" >2</th>
      <td id="T_c6c4b_row11_col0" class="data row11 col0" >Junior Business Analyst</td>
      <td id="T_c6c4b_row11_col1" class="data row11 col1" > Documenting and analyzing the required information and data to determine potential solutions from a technical and business perspective. </td>
      <td id="T_c6c4b_row11_col2" class="data row11 col2" >Just posted</td>
      <td id="T_c6c4b_row11_col3" class="data row11 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20RPM%20TECHNOLOGIES%20CORP</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row12" class="row_heading level0 row12" >3</th>
      <td id="T_c6c4b_row12_col0" class="data row12 col0" >Jr. Inventory Analyst</td>
      <td id="T_c6c4b_row12_col1" class="data row12 col1" > Report on inventory which is on hand, on order, and usage data. Our client is leading the industry in snack foods, and they are seeking a Jr Inventory Analyst/… </td>
      <td id="T_c6c4b_row12_col2" class="data row12 col2" >Just posted</td>
      <td id="T_c6c4b_row12_col3" class="data row12 col3" >https://ca.indeed.com/jobs?q=Jr.%20Inventory%20Analyst%20Equation%20Staffing%20Solutions.</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row13" class="row_heading level0 row13" >4</th>
      <td id="T_c6c4b_row13_col0" class="data row13 col0" >Data (Game) Analyst - fit for experienced or junior</td>
      <td id="T_c6c4b_row13_col1" class="data row13 col1" > Experience analyzing data using statistics. Analyzing user's collected data. Validating the quality of the data. Proficiency in Power BI or similar BI products. </td>
      <td id="T_c6c4b_row13_col2" class="data row13 col2" >1 day ago</td>
      <td id="T_c6c4b_row13_col3" class="data row13 col3" >https://ca.indeed.com/jobs?q=Data%20%28Game%29%20Analyst%20-%20fit%20for%20experienced%20or%20junior%20Blazesoft</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row14" class="row_heading level0 row14" >86</th>
      <td id="T_c6c4b_row14_col0" class="data row14 col0" >Junior Forecast Analyst-Shared Services</td>
      <td id="T_c6c4b_row14_col1" class="data row14 col1" > Junior Forecast Analyst – Shared Services*. Reporting to the Director of Operations Support, the Junior Forecast Analyst contributes to Arctic Glacier’s success… </td>
      <td id="T_c6c4b_row14_col2" class="data row14 col2" >Active 1 day ago</td>
      <td id="T_c6c4b_row14_col3" class="data row14 col3" >https://ca.indeed.com/jobs?q=Junior%20Forecast%20Analyst-Shared%20Services%20Arctic%20Glacier</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row15" class="row_heading level0 row15" >87</th>
      <td id="T_c6c4b_row15_col0" class="data row15 col0" >Jr Software Developer (FT)</td>
      <td id="T_c6c4b_row15_col1" class="data row15 col1" > We are looking for an intermediate full stack developer that wants to get their keyboard working on all aspects of a fully functioning web-suite that also… </td>
      <td id="T_c6c4b_row15_col2" class="data row15 col2" >1 day ago</td>
      <td id="T_c6c4b_row15_col3" class="data row15 col3" >https://ca.indeed.com/jobs?q=Jr%20Software%20Developer%20%28FT%29%20The%20Artona%20Group</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row16" class="row_heading level0 row16" >88</th>
      <td id="T_c6c4b_row16_col0" class="data row16 col0" >Software Engineer Trainee (Fresh Graduates)</td>
      <td id="T_c6c4b_row16_col1" class="data row16 col1" > DLT Labs is a global leader in delivery of enterprise blockchain solutions and technologies, as well as a pioneer in the implementation of standards. </td>
      <td id="T_c6c4b_row16_col2" class="data row16 col2" >Active 1 day ago</td>
      <td id="T_c6c4b_row16_col3" class="data row16 col3" >https://ca.indeed.com/jobs?q=Software%20Engineer%20Trainee%20%28Fresh%20Graduates%29%20DLT%20Labs</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row17" class="row_heading level0 row17" >89</th>
      <td id="T_c6c4b_row17_col0" class="data row17 col0" >Junior or Intermediate Quality Assurance Analyst</td>
      <td id="T_c6c4b_row17_col1" class="data row17 col1" > We are looking for a Junior or Intermediate Quality Assurance Analyst to work with our QA team, conducting testing of our web and desktop applications. </td>
      <td id="T_c6c4b_row17_col2" class="data row17 col2" >Active 1 day ago</td>
      <td id="T_c6c4b_row17_col3" class="data row17 col3" >https://ca.indeed.com/jobs?q=Junior%20or%20Intermediate%20Quality%20Assurance%20Analyst%20LBMX%20Inc</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row18" class="row_heading level0 row18" >91</th>
      <td id="T_c6c4b_row18_col0" class="data row18 col0" >Jr Software Developer (Remote/Hybrid)</td>
      <td id="T_c6c4b_row18_col1" class="data row18 col1" > Assisting the development manager with all aspects of software design and coding. Attending and contributing to company development meetings. </td>
      <td id="T_c6c4b_row18_col2" class="data row18 col2" >Active 2 days ago</td>
      <td id="T_c6c4b_row18_col3" class="data row18 col3" >https://ca.indeed.com/jobs?q=Jr%20Software%20Developer%20%28Remote/Hybrid%29%20CADdetails%20Ltd.</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row19" class="row_heading level0 row19" >92</th>
      <td id="T_c6c4b_row19_col0" class="data row19 col0" >Jr. React Web Developer</td>
      <td id="T_c6c4b_row19_col1" class="data row19 col1" > You’re passionate about programming, web development, and learning &amp; problem solving. Your analytical and problem-solving skills allow you to find creative… </td>
      <td id="T_c6c4b_row19_col2" class="data row19 col2" >Active 2 days ago</td>
      <td id="T_c6c4b_row19_col3" class="data row19 col3" >https://ca.indeed.com/jobs?q=Jr.%20React%20Web%20Developer%20Creator.co</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row20" class="row_heading level0 row20" >193</th>
      <td id="T_c6c4b_row20_col0" class="data row20 col0" >Junior / Intermediate Electrical / Electronic Hardware Desig...</td>
      <td id="T_c6c4b_row20_col1" class="data row20 col1" > Junior / Intermediate Electrical / Electronic Hardware Design Engineer*. Imagine being part of a team that creates cutting edge cleantech solutions that improve… </td>
      <td id="T_c6c4b_row20_col2" class="data row20 col2" >Active 3 days ago</td>
      <td id="T_c6c4b_row20_col3" class="data row20 col3" >https://ca.indeed.com/jobs?q=Junior%20/%20Intermediate%20Electrical%20/%20Electronic%20Hardware%20Desig...%20Poseidon%20Ocean%20Systems</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row21" class="row_heading level0 row21" >5</th>
      <td id="T_c6c4b_row21_col0" class="data row21 col0" >Data Annotation Specialist I</td>
      <td id="T_c6c4b_row21_col1" class="data row21 col1" > O Passion for data efficiency and accuracy. A Data Annotation Specialist I annotates surgical videos using specialized software to identify key events in the… </td>
      <td id="T_c6c4b_row21_col2" class="data row21 col2" >Active 3 days ago</td>
      <td id="T_c6c4b_row21_col3" class="data row21 col3" >https://ca.indeed.com/jobs?q=Data%20Annotation%20Specialist%20I%20Surgical%20Safety%20Technologies</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row22" class="row_heading level0 row22" >93</th>
      <td id="T_c6c4b_row22_col0" class="data row22 col0" >Software Developer (Junior)</td>
      <td id="T_c6c4b_row22_col1" class="data row22 col1" > $55-65k/year (depending on experience). Full benefits including dental, health and medical. Design, develop, upgrade, and implement Microsoft D365 modules. </td>
      <td id="T_c6c4b_row22_col2" class="data row22 col2" >3 days ago</td>
      <td id="T_c6c4b_row22_col3" class="data row22 col3" >https://ca.indeed.com/jobs?q=Software%20Developer%20%28Junior%29%20AppleOne</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row23" class="row_heading level0 row23" >94</th>
      <td id="T_c6c4b_row23_col0" class="data row23 col0" >Junior Purchasing Data Analyst</td>
      <td id="T_c6c4b_row23_col1" class="data row23 col1" > Max Advanced Brakes* is a leading supplier of automotive brake parts in North America, headquartered in Markham, Ontario. Perform other duties as assigned. </td>
      <td id="T_c6c4b_row23_col2" class="data row23 col2" >Active 3 days ago</td>
      <td id="T_c6c4b_row23_col3" class="data row23 col3" >https://ca.indeed.com/jobs?q=Junior%20Purchasing%20Data%20Analyst%20Max%20Advanced%20Brakes</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row24" class="row_heading level0 row24" >95</th>
      <td id="T_c6c4b_row24_col0" class="data row24 col0" >Jr. Site Reliability Engineer</td>
      <td id="T_c6c4b_row24_col1" class="data row24 col1" > Reporting to senior technical staff, the role contributes to several facets of the product and services delivery lifecycles of the Univeris EWMS SaaS platform… </td>
      <td id="T_c6c4b_row24_col2" class="data row24 col2" >3 days ago</td>
      <td id="T_c6c4b_row24_col3" class="data row24 col3" >https://ca.indeed.com/jobs?q=Jr.%20Site%20Reliability%20Engineer%20Univeris%20Corp</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row25" class="row_heading level0 row25" >96</th>
      <td id="T_c6c4b_row25_col0" class="data row25 col0" >Junior Software Developer</td>
      <td id="T_c6c4b_row25_col1" class="data row25 col1" > Fieldshare is a SaaS project management software for environmental, energy and property management sectors. We are currently building the next generation of our… </td>
      <td id="T_c6c4b_row25_col2" class="data row25 col2" >Active 3 days ago</td>
      <td id="T_c6c4b_row25_col3" class="data row25 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20Fieldshare</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row26" class="row_heading level0 row26" >98</th>
      <td id="T_c6c4b_row26_col0" class="data row26 col0" >Admin Technician/ Jr IT Technician/ Sr IT Technician</td>
      <td id="T_c6c4b_row26_col1" class="data row26 col1" > We are looking for skilled Admin Technician, Junior and Senior IT Technicians to fill current and future contract engagements. </td>
      <td id="T_c6c4b_row26_col2" class="data row26 col2" >3 days ago</td>
      <td id="T_c6c4b_row26_col3" class="data row26 col3" >https://ca.indeed.com/jobs?q=Admin%20Technician/%20Jr%20IT%20Technician/%20Sr%20IT%20Technician%20KPMG</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row27" class="row_heading level0 row27" >192</th>
      <td id="T_c6c4b_row27_col0" class="data row27 col0" >Junior Software Engineer</td>
      <td id="T_c6c4b_row27_col1" class="data row27 col1" >Junior Software Engineer As a Junior Software Engineer, you have an interest in game development and are open to working in any technical area as determined…</td>
      <td id="T_c6c4b_row27_col2" class="data row27 col2" >3 days ago</td>
      <td id="T_c6c4b_row27_col3" class="data row27 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Engineer%20Gasket%20Games</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row28" class="row_heading level0 row28" >191</th>
      <td id="T_c6c4b_row28_col0" class="data row28 col0" >Jr. Software Designer</td>
      <td id="T_c6c4b_row28_col1" class="data row28 col1" > The NSP portfolio provides a comprehensive management solution that allows our customers to monitor, provision, and troubleshoot IP, Wireless, and Optical… </td>
      <td id="T_c6c4b_row28_col2" class="data row28 col2" >3 days ago</td>
      <td id="T_c6c4b_row28_col3" class="data row28 col3" >https://ca.indeed.com/jobs?q=Jr.%20Software%20Designer%20NOKIA</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row29" class="row_heading level0 row29" >6</th>
      <td id="T_c6c4b_row29_col0" class="data row29 col0" >Junior Pricing Coordinator / Pricing Analyst</td>
      <td id="T_c6c4b_row29_col1" class="data row29 col1" > Manage data collection of internal systems utilized by Max Advanced Brakes. Manages key pricing programs and provides comprehensive reporting, tracking and… </td>
      <td id="T_c6c4b_row29_col2" class="data row29 col2" >Active 3 days ago</td>
      <td id="T_c6c4b_row29_col3" class="data row29 col3" >https://ca.indeed.com/jobs?q=Junior%20Pricing%20Coordinator%20/%20Pricing%20Analyst%20Max%20Advanced%20Brakes</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row30" class="row_heading level0 row30" >195</th>
      <td id="T_c6c4b_row30_col0" class="data row30 col0" >AIR QUALITY SPECIALIST</td>
      <td id="T_c6c4b_row30_col1" class="data row30 col1" > You will work within a group of professionals with varying levels of experience; You will assist with conducting air quality assessments and air dispersion… </td>
      <td id="T_c6c4b_row30_col2" class="data row30 col2" >3 days ago</td>
      <td id="T_c6c4b_row30_col3" class="data row30 col3" >https://ca.indeed.com/jobs?q=AIR%20QUALITY%20SPECIALIST%20WSP</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row31" class="row_heading level0 row31" >7</th>
      <td id="T_c6c4b_row31_col0" class="data row31 col0" >Junior Market Analyst - Intern</td>
      <td id="T_c6c4b_row31_col1" class="data row31 col1" > Strong analytical and critical thinking skills; ability to quickly interpret large amounts of data. Insights &amp; Reporting: Routine presentations of data… </td>
      <td id="T_c6c4b_row31_col2" class="data row31 col2" >3 days ago</td>
      <td id="T_c6c4b_row31_col3" class="data row31 col3" >https://ca.indeed.com/jobs?q=Junior%20Market%20Analyst%20-%20Intern%20Husky%20Injection%20Molding</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row32" class="row_heading level0 row32" >194</th>
      <td id="T_c6c4b_row32_col0" class="data row32 col0" >Junior Embedded Software Engineer</td>
      <td id="T_c6c4b_row32_col1" class="data row32 col1" > If you're interested in developing the full bare-metal &amp; RTOS embedded stack (from drivers to signal processing and GUI), as well as contributing to signal… </td>
      <td id="T_c6c4b_row32_col2" class="data row32 col2" >Active 3 days ago</td>
      <td id="T_c6c4b_row32_col3" class="data row32 col3" >https://ca.indeed.com/jobs?q=Junior%20Embedded%20Software%20Engineer%20General%20Technologies%20Corp.</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row33" class="row_heading level0 row33" >196</th>
      <td id="T_c6c4b_row33_col0" class="data row33 col0" >Applied Scientist I</td>
      <td id="T_c6c4b_row33_col1" class="data row33 col1" > Master's degree or foreign equivalent in Computer Science, Electrical Engineering, Mathematics or Physics. 1 year of experience conducting independent research… </td>
      <td id="T_c6c4b_row33_col2" class="data row33 col2" >4 days ago</td>
      <td id="T_c6c4b_row33_col3" class="data row33 col3" >https://ca.indeed.com/jobs?q=Applied%20Scientist%20I%20Amazon%20Dev%20Centre%20Canada%20ULC</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row34" class="row_heading level0 row34" >106</th>
      <td id="T_c6c4b_row34_col0" class="data row34 col0" >Junior Digital Performance Analyst - Mobility</td>
      <td id="T_c6c4b_row34_col1" class="data row34 col1" > We're a customer-driven and product-minded team within TELUS, responsible for our company's digital evolution. </td>
      <td id="T_c6c4b_row34_col2" class="data row34 col2" >Active 4 days ago</td>
      <td id="T_c6c4b_row34_col3" class="data row34 col3" >https://ca.indeed.com/jobs?q=Junior%20Digital%20Performance%20Analyst%20-%20Mobility%20TELUS%20Digital</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row35" class="row_heading level0 row35" >105</th>
      <td id="T_c6c4b_row35_col0" class="data row35 col0" >Junior Programmer</td>
      <td id="T_c6c4b_row35_col1" class="data row35 col1" > The Junior Programmer is responsible for designing, building and maintaining reliant software for operational use. </td>
      <td id="T_c6c4b_row35_col2" class="data row35 col2" >Active 4 days ago</td>
      <td id="T_c6c4b_row35_col3" class="data row35 col3" >https://ca.indeed.com/jobs?q=Junior%20Programmer%20Extend%20Communications</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row36" class="row_heading level0 row36" >103</th>
      <td id="T_c6c4b_row36_col0" class="data row36 col0" >Junior Applications Developer – Summer Student</td>
      <td id="T_c6c4b_row36_col1" class="data row36 col1" > Everyone is encouraged to take ownership of his/her ideas and to see them through to completion, collaborating with key influencers as required. </td>
      <td id="T_c6c4b_row36_col2" class="data row36 col2" >4 days ago</td>
      <td id="T_c6c4b_row36_col3" class="data row36 col3" >https://ca.indeed.com/jobs?q=Junior%20Applications%20Developer%20%E2%80%93%20Summer%20Student%20Careers%20at%20ECO%20Canada</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row37" class="row_heading level0 row37" >101</th>
      <td id="T_c6c4b_row37_col0" class="data row37 col0" >Junior PL/SQL Developer</td>
      <td id="T_c6c4b_row37_col1" class="data row37 col1" > At HALIGHT, the PL/SQL Database Developer is responsible for creating and maintaining storage frameworks. The Database Developer will elucidate the intended use… </td>
      <td id="T_c6c4b_row37_col2" class="data row37 col2" >4 days ago</td>
      <td id="T_c6c4b_row37_col3" class="data row37 col3" >https://ca.indeed.com/jobs?q=Junior%20PL/SQL%20Developer%20HALIGHT%20Inc.</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row38" class="row_heading level0 row38" >107</th>
      <td id="T_c6c4b_row38_col0" class="data row38 col0" >Junior Buissness Analyst</td>
      <td id="T_c6c4b_row38_col1" class="data row38 col1" > The Junior Business Analyst will act as an extension of the Business Analyst and will be involved in the maintenance of programs used for client relations and… </td>
      <td id="T_c6c4b_row38_col2" class="data row38 col2" >Active 4 days ago</td>
      <td id="T_c6c4b_row38_col3" class="data row38 col3" >https://ca.indeed.com/jobs?q=Junior%20Buissness%20Analyst%20The%20Central%20Group%20Ltd.</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row39" class="row_heading level0 row39" >102</th>
      <td id="T_c6c4b_row39_col0" class="data row39 col0" >Junior IT Systems Administrator</td>
      <td id="T_c6c4b_row39_col1" class="data row39 col1" > Recommend, implement, and maintain secure environments running in Azure using industry-accepted standards (MFA, Azure Firewall, Intune, etc.). </td>
      <td id="T_c6c4b_row39_col2" class="data row39 col2" >Active 4 days ago</td>
      <td id="T_c6c4b_row39_col3" class="data row39 col3" >https://ca.indeed.com/jobs?q=Junior%20IT%20Systems%20Administrator%20Matrix%20Solutions%20Inc.</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row40" class="row_heading level0 row40" >99</th>
      <td id="T_c6c4b_row40_col0" class="data row40 col0" >JUNIOR PL1 MAINFRAME DEVELOPER (remote work)</td>
      <td id="T_c6c4b_row40_col1" class="data row40 col1" > Our world has never been more alive with opportunities and, at Kyndryl, we’re ready to seize them. We design, build, manage and modernize the mission-critical… </td>
      <td id="T_c6c4b_row40_col2" class="data row40 col2" >4 days ago</td>
      <td id="T_c6c4b_row40_col3" class="data row40 col3" >https://ca.indeed.com/jobs?q=JUNIOR%20PL1%20MAINFRAME%20DEVELOPER%20%28remote%20work%29%20Kyndryl</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row41" class="row_heading level0 row41" >8</th>
      <td id="T_c6c4b_row41_col0" class="data row41 col0" >Junior Database Administrator</td>
      <td id="T_c6c4b_row41_col1" class="data row41 col1" > Participate in bulk data conversion tasks. CSSI currently employs over 125 staff members, consisting of insurance industry professionals, certified computer… </td>
      <td id="T_c6c4b_row41_col2" class="data row41 col2" >Active 4 days ago</td>
      <td id="T_c6c4b_row41_col3" class="data row41 col3" >https://ca.indeed.com/jobs?q=Junior%20Database%20Administrator%20Custom%20Software%20Solutions%20Inc.</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row42" class="row_heading level0 row42" >9</th>
      <td id="T_c6c4b_row42_col0" class="data row42 col0" >Jr. DB2 Database Administrator</td>
      <td id="T_c6c4b_row42_col1" class="data row42 col1" > Provide DB2 Administrative services to application development team. Design/develop/test/support DB2 LUW database. Performance tuning and trouble shooting. </td>
      <td id="T_c6c4b_row42_col2" class="data row42 col2" >Active 4 days ago</td>
      <td id="T_c6c4b_row42_col3" class="data row42 col3" >https://ca.indeed.com/jobs?q=Jr.%20DB2%20Database%20Administrator%20Dawn%20InfoTek%20Inc.</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row43" class="row_heading level0 row43" >10</th>
      <td id="T_c6c4b_row43_col0" class="data row43 col0" >Junior Financial Planning Analyst - Temporary Part Time (Jun...</td>
      <td id="T_c6c4b_row43_col1" class="data row43 col1" > Advanced Microsoft Office skills (with a focus on data manipulation tools – Excel &amp; Access). The Junior Financial Planning Analyst plays a supporting role in… </td>
      <td id="T_c6c4b_row43_col2" class="data row43 col2" >Active 4 days ago</td>
      <td id="T_c6c4b_row43_col3" class="data row43 col3" >https://ca.indeed.com/jobs?q=Junior%20Financial%20Planning%20Analyst%20-%20Temporary%20Part%20Time%20%28Jun...%20Mohawk%20College</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row44" class="row_heading level0 row44" >11</th>
      <td id="T_c6c4b_row44_col0" class="data row44 col0" >Junior Data Entry Operator</td>
      <td id="T_c6c4b_row44_col1" class="data row44 col1" > Ensuring data is backed up. Storing hard copies of data in an organized manner to optimize retrieval. Handling and helping staff with Microsoft Dynamics 365. </td>
      <td id="T_c6c4b_row44_col2" class="data row44 col2" >4 days ago</td>
      <td id="T_c6c4b_row44_col3" class="data row44 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Entry%20Operator%20Maplesoft%20Group</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row45" class="row_heading level0 row45" >12</th>
      <td id="T_c6c4b_row45_col0" class="data row45 col0" >Neuroimaging Data Scientist/Programmer Junior</td>
      <td id="T_c6c4b_row45_col1" class="data row45 col1" > We conduct projects associating MRI imaging data (structural, functional, diffusion) with behavioral data in patients with Parkinson’s disease and evaluate how… </td>
      <td id="T_c6c4b_row45_col2" class="data row45 col2" >4 days ago</td>
      <td id="T_c6c4b_row45_col3" class="data row45 col3" >https://ca.indeed.com/jobs?q=Neuroimaging%20Data%20Scientist/Programmer%20Junior%20University%20of%20British%20Columbia</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row46" class="row_heading level0 row46" >13</th>
      <td id="T_c6c4b_row46_col0" class="data row46 col0" >JR Data Processor</td>
      <td id="T_c6c4b_row46_col1" class="data row46 col1" > Perform a variety of data quality tasks in support of live sports data production. A love and passion for North American professional sports data. </td>
      <td id="T_c6c4b_row46_col2" class="data row46 col2" >4 days ago</td>
      <td id="T_c6c4b_row46_col3" class="data row46 col3" >https://ca.indeed.com/jobs?q=JR%20Data%20Processor%20Nielsen</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row47" class="row_heading level0 row47" >199</th>
      <td id="T_c6c4b_row47_col0" class="data row47 col0" >Junior Application Engineer and Project Manager</td>
      <td id="T_c6c4b_row47_col1" class="data row47 col1" > The Junior Application Engineer and Project Manager role will appeal to engineers or scientists with an interest in materials, additive manufacturing,… </td>
      <td id="T_c6c4b_row47_col2" class="data row47 col2" >Active 5 days ago</td>
      <td id="T_c6c4b_row47_col3" class="data row47 col3" >https://ca.indeed.com/jobs?q=Junior%20Application%20Engineer%20and%20Project%20Manager%20Bassetti%20Americas</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row48" class="row_heading level0 row48" >198</th>
      <td id="T_c6c4b_row48_col0" class="data row48 col0" >Junior Full Stack Developer New Graduate Opportunities</td>
      <td id="T_c6c4b_row48_col1" class="data row48 col1" > Building smart and efficient code that works well within a service-based system architecture. Developing new features and systems, as well as maintaining… </td>
      <td id="T_c6c4b_row48_col2" class="data row48 col2" >5 days ago</td>
      <td id="T_c6c4b_row48_col3" class="data row48 col3" >https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20New%20Graduate%20Opportunities%20Helcim</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row49" class="row_heading level0 row49" >108</th>
      <td id="T_c6c4b_row49_col0" class="data row49 col0" >Jr. Network Administrator</td>
      <td id="T_c6c4b_row49_col1" class="data row49 col1" > Administration of user accounts for various corporate systems (Active Directory, Linux accounts, O365/Azure). Management of server and hardware updates. </td>
      <td id="T_c6c4b_row49_col2" class="data row49 col2" >5 days ago</td>
      <td id="T_c6c4b_row49_col3" class="data row49 col3" >https://ca.indeed.com/jobs?q=Jr.%20Network%20Administrator%20Evertz%20Microsystems%20Limited</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row50" class="row_heading level0 row50" >109</th>
      <td id="T_c6c4b_row50_col0" class="data row50 col0" >Développeur QA Junior</td>
      <td id="T_c6c4b_row50_col1" class="data row50 col1" > Un leader mondial dans les logiciels spécialisés en Revenue Management (RM) pour le transport de passagers, recherche actuellement un Développeur QA pour… </td>
      <td id="T_c6c4b_row50_col2" class="data row50 col2" >Active 5 days ago</td>
      <td id="T_c6c4b_row50_col3" class="data row50 col3" >https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20QA%20Junior%20Tannous%20HR%20Solutions</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row51" class="row_heading level0 row51" >110</th>
      <td id="T_c6c4b_row51_col0" class="data row51 col0" >Analista tecnico junior pl/sql</td>
      <td id="T_c6c4b_row51_col1" class="data row51 col1" > Gruppo Sincrono, Holding Company ICT di Consulenza e Formazione che opera sul mercato dal 1993, sta selezionando per un’importante opportunità professionale per… </td>
      <td id="T_c6c4b_row51_col2" class="data row51 col2" >5 days ago</td>
      <td id="T_c6c4b_row51_col3" class="data row51 col3" >https://ca.indeed.com/jobs?q=Analista%20tecnico%20junior%20pl/sql%20Gruppo%20Sincrono</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row52" class="row_heading level0 row52" >202</th>
      <td id="T_c6c4b_row52_col0" class="data row52 col0" >Junior Test Automation Specialist / Spécialiste en automatis...</td>
      <td id="T_c6c4b_row52_col1" class="data row52 col1" > This role has been designated as ‘Edge’, which means you will primarily work outside of an HPE office. Develop Python automation scripts to optimize manual… </td>
      <td id="T_c6c4b_row52_col2" class="data row52 col2" >5 days ago</td>
      <td id="T_c6c4b_row52_col3" class="data row52 col3" >https://ca.indeed.com/jobs?q=Junior%20Test%20Automation%20Specialist%20/%20Sp%C3%A9cialiste%20en%20automatis...%20HPE1US</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row53" class="row_heading level0 row53" >16</th>
      <td id="T_c6c4b_row53_col0" class="data row53 col0" >Business Analyst I</td>
      <td id="T_c6c4b_row53_col1" class="data row53 col1" > Design/implement data-driven workflows in ZEMA. Design data reports/models optimized for usability, and support analytics and integration. </td>
      <td id="T_c6c4b_row53_col2" class="data row53 col2" >5 days ago</td>
      <td id="T_c6c4b_row53_col3" class="data row53 col3" >https://ca.indeed.com/jobs?q=Business%20Analyst%20I%20ZE%20Power%20Group</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row54" class="row_heading level0 row54" >200</th>
      <td id="T_c6c4b_row54_col0" class="data row54 col0" >Junior Full Stack Developer</td>
      <td id="T_c6c4b_row54_col1" class="data row54 col1" > Helcim is searching for an Junior Full Stack Developer to be responsible for helping develop a wide variety of features including both frontend and backend… </td>
      <td id="T_c6c4b_row54_col2" class="data row54 col2" >5 days ago</td>
      <td id="T_c6c4b_row54_col3" class="data row54 col3" >https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20Helcim</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row55" class="row_heading level0 row55" >15</th>
      <td id="T_c6c4b_row55_col0" class="data row55 col0" >Junior Business Intelligence Developer</td>
      <td id="T_c6c4b_row55_col1" class="data row55 col1" > Good understanding of concepts and some experience with SQL, data modeling, ETL development, and data warehousing. </td>
      <td id="T_c6c4b_row55_col2" class="data row55 col2" >5 days ago</td>
      <td id="T_c6c4b_row55_col3" class="data row55 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Intelligence%20Developer%20IPG%20Mediabrands</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row56" class="row_heading level0 row56" >14</th>
      <td id="T_c6c4b_row56_col0" class="data row56 col0" >Data Entry Clerk/Junior Bookkeeper</td>
      <td id="T_c6c4b_row56_col1" class="data row56 col1" > Payroll data entry (Cross training). Daily data entry to keep company’s bookkeeping up to date. The role provides a wide variety of data entry and… </td>
      <td id="T_c6c4b_row56_col2" class="data row56 col2" >Active 5 days ago</td>
      <td id="T_c6c4b_row56_col3" class="data row56 col3" >https://ca.indeed.com/jobs?q=Data%20Entry%20Clerk/Junior%20Bookkeeper%20Seltrek%20Electric%20Ltd</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row57" class="row_heading level0 row57" >197</th>
      <td id="T_c6c4b_row57_col0" class="data row57 col0" >Junior Systems Administrator</td>
      <td id="T_c6c4b_row57_col1" class="data row57 col1" > Maintenance of the Ubuntu Linux server infrastructure. Ensures security and configuration compliance of hardware and software to comply with best practices. </td>
      <td id="T_c6c4b_row57_col2" class="data row57 col2" >5 days ago</td>
      <td id="T_c6c4b_row57_col3" class="data row57 col3" >https://ca.indeed.com/jobs?q=Junior%20Systems%20Administrator%20PSD</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row58" class="row_heading level0 row58" >201</th>
      <td id="T_c6c4b_row58_col0" class="data row58 col0" >Jr. / Int. Software Engineering (12mo fixed term)</td>
      <td id="T_c6c4b_row58_col1" class="data row58 col1" > Magellan Aerospace, Winnipeg is looking for a high performing Entry Level (or Intermediate) Software Engineering/Developer to join our development team. </td>
      <td id="T_c6c4b_row58_col2" class="data row58 col2" >5 days ago</td>
      <td id="T_c6c4b_row58_col3" class="data row58 col3" >https://ca.indeed.com/jobs?q=Jr.%20/%20Int.%20Software%20Engineering%20%2812mo%20fixed%20term%29%20Magellan%20Aerospace</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row59" class="row_heading level0 row59" >112</th>
      <td id="T_c6c4b_row59_col0" class="data row59 col0" >Jr. Developer</td>
      <td id="T_c6c4b_row59_col1" class="data row59 col1" > As a new Jr. Developer, you will be responsible for customizing, developing, and supporting solutions on our internal platform. </td>
      <td id="T_c6c4b_row59_col2" class="data row59 col2" >6 days ago</td>
      <td id="T_c6c4b_row59_col3" class="data row59 col3" >https://ca.indeed.com/jobs?q=Jr.%20Developer%20OSG</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row60" class="row_heading level0 row60" >111</th>
      <td id="T_c6c4b_row60_col0" class="data row60 col0" >Junior Python Developer</td>
      <td id="T_c6c4b_row60_col1" class="data row60 col1" > Participate in team discussions to fully understand the business and technical requirements. Write high quality, efficient, testable, and maintainable code. </td>
      <td id="T_c6c4b_row60_col2" class="data row60 col2" >6 days ago</td>
      <td id="T_c6c4b_row60_col3" class="data row60 col3" >https://ca.indeed.com/jobs?q=Junior%20Python%20Developer%20Infinite%20Investment%20Systems</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row61" class="row_heading level0 row61" >17</th>
      <td id="T_c6c4b_row61_col0" class="data row61 col0" >Jr. Digital Business Analyst</td>
      <td id="T_c6c4b_row61_col1" class="data row61 col1" > Analyze data to identify trends, interdependencies among variables and be able to support defining project scope,. Product needs and alternative solutions. </td>
      <td id="T_c6c4b_row61_col2" class="data row61 col2" >6 days ago</td>
      <td id="T_c6c4b_row61_col3" class="data row61 col3" >https://ca.indeed.com/jobs?q=Jr.%20Digital%20Business%20Analyst%20FirstOntario%20Credit%20Union</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row62" class="row_heading level0 row62" >18</th>
      <td id="T_c6c4b_row62_col0" class="data row62 col0" >Jr. Business Analyst - Carriers</td>
      <td id="T_c6c4b_row62_col1" class="data row62 col1" > Analyze data to identify trends and challenges, and use the data to provide insights to drive improvements through operational initiatives while collaborating… </td>
      <td id="T_c6c4b_row62_col2" class="data row62 col2" >6 days ago</td>
      <td id="T_c6c4b_row62_col3" class="data row62 col3" >https://ca.indeed.com/jobs?q=Jr.%20Business%20Analyst%20-%20Carriers%20Shipfusion</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row63" class="row_heading level0 row63" >207</th>
      <td id="T_c6c4b_row63_col0" class="data row63 col0" >DevOps Junior / Junior DevOps</td>
      <td id="T_c6c4b_row63_col1" class="data row63 col1" > À propos d’OPAL-RT Technologies. OPAL-RT s’est donné comme ambitieux défi de démocratiser la simulation temps réel afin de la rendre accessible à chaque… </td>
      <td id="T_c6c4b_row63_col2" class="data row63 col2" >6 days ago</td>
      <td id="T_c6c4b_row63_col3" class="data row63 col3" >https://ca.indeed.com/jobs?q=DevOps%20Junior%20/%20Junior%20DevOps%20Opal-RT</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row64" class="row_heading level0 row64" >208</th>
      <td id="T_c6c4b_row64_col0" class="data row64 col0" >Junior Mechanical Engineer</td>
      <td id="T_c6c4b_row64_col1" class="data row64 col1" > P.Eng. exercising initiative and independent judgment in performing assigned tasks. You will report to the V.P. of Operations and assist and advise the sales… </td>
      <td id="T_c6c4b_row64_col2" class="data row64 col2" >Active 6 days ago</td>
      <td id="T_c6c4b_row64_col3" class="data row64 col3" >https://ca.indeed.com/jobs?q=Junior%20Mechanical%20Engineer%20Green%20Matters%20Technologies</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row65" class="row_heading level0 row65" >114</th>
      <td id="T_c6c4b_row65_col0" class="data row65 col0" >Junior Software Engineer- Web</td>
      <td id="T_c6c4b_row65_col1" class="data row65 col1" > Backend engineer must be comfortable designing, implementing, deploying and maintaining server-side components. </td>
      <td id="T_c6c4b_row65_col2" class="data row65 col2" >6 days ago</td>
      <td id="T_c6c4b_row65_col3" class="data row65 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Engineer-%20Web%20Procom</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row66" class="row_heading level0 row66" >206</th>
      <td id="T_c6c4b_row66_col0" class="data row66 col0" >Mixed Signal Test Engineer - JR MTS</td>
      <td id="T_c6c4b_row66_col1" class="data row66 col1" > The Mixed-signal test professional will be responsible for the design of complex electronics systems and Electronic Ground Support Equipement (EGSE) for testing… </td>
      <td id="T_c6c4b_row66_col2" class="data row66 col2" >6 days ago</td>
      <td id="T_c6c4b_row66_col3" class="data row66 col3" >https://ca.indeed.com/jobs?q=Mixed%20Signal%20Test%20Engineer%20-%20JR%20MTS%20MDA</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row67" class="row_heading level0 row67" >205</th>
      <td id="T_c6c4b_row67_col0" class="data row67 col0" >Junior Software Developer (DataHub Team)</td>
      <td id="T_c6c4b_row67_col1" class="data row67 col1" > You love solving problems and enjoy getting to the root cause of issues. You enjoy exploring new technologies to deliver a reliable, secure, and highly… </td>
      <td id="T_c6c4b_row67_col2" class="data row67 col2" >6 days ago</td>
      <td id="T_c6c4b_row67_col3" class="data row67 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20%28DataHub%20Team%29%20Pason%20Systems%20Corp</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row68" class="row_heading level0 row68" >204</th>
      <td id="T_c6c4b_row68_col0" class="data row68 col0" >Junior Pipeline TD</td>
      <td id="T_c6c4b_row68_col1" class="data row68 col1" >- ICON Creative Studio is Canada’s largest independently owned animation entertainment company located in the historic Gastown district of Vancouver, BC…</td>
      <td id="T_c6c4b_row68_col2" class="data row68 col2" >6 days ago</td>
      <td id="T_c6c4b_row68_col3" class="data row68 col3" >https://ca.indeed.com/jobs?q=Junior%20Pipeline%20TD%20ICON%20Creative%20Studio</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row69" class="row_heading level0 row69" >203</th>
      <td id="T_c6c4b_row69_col0" class="data row69 col0" >BIOINFORMATICS SCIENTIST I - CA</td>
      <td id="T_c6c4b_row69_col1" class="data row69 col1" > This position is responsible for in-depth in-silico bioinformatics analysis required for development of sequencing and other molecular methods, bio surveillance… </td>
      <td id="T_c6c4b_row69_col2" class="data row69 col2" >6 days ago</td>
      <td id="T_c6c4b_row69_col3" class="data row69 col3" >https://ca.indeed.com/jobs?q=BIOINFORMATICS%20SCIENTIST%20I%20-%20CA%20Luminex</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row70" class="row_heading level0 row70" >113</th>
      <td id="T_c6c4b_row70_col0" class="data row70 col0" >Junior Automation Programming Specialist</td>
      <td id="T_c6c4b_row70_col1" class="data row70 col1" > Exile Automation is a dynamic leading-edge company where everyone understands their contributions are integral to the success of the team and that we win as a… </td>
      <td id="T_c6c4b_row70_col2" class="data row70 col2" >6 days ago</td>
      <td id="T_c6c4b_row70_col3" class="data row70 col3" >https://ca.indeed.com/jobs?q=Junior%20Automation%20Programming%20Specialist%20CDN%20Controls%20Ltd.</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row71" class="row_heading level0 row71" >118</th>
      <td id="T_c6c4b_row71_col0" class="data row71 col0" >Développeur Junior .Net</td>
      <td id="T_c6c4b_row71_col1" class="data row71 col1" > Analyser, diagnostiquer et résoudre les problèmes techniques des utilisateurs. Participer à l'implantation, à l'installation, à la mise à jour et à la… </td>
      <td id="T_c6c4b_row71_col2" class="data row71 col2" >7 days ago</td>
      <td id="T_c6c4b_row71_col3" class="data row71 col3" >https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20Junior%20.Net%20Hydro%20Qu%C3%A9bec</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row72" class="row_heading level0 row72" >117</th>
      <td id="T_c6c4b_row72_col0" class="data row72 col0" >Développeur PHP junior - Junior PHP Developper</td>
      <td id="T_c6c4b_row72_col1" class="data row72 col1" > Leader dans la création et l’édition de jeux, Gameloft® s’est positionné depuis 2000 comme l’une des entreprises les plus innovantes dans son domaine. </td>
      <td id="T_c6c4b_row72_col2" class="data row72 col2" >7 days ago</td>
      <td id="T_c6c4b_row72_col3" class="data row72 col3" >https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20PHP%20junior%20-%20Junior%20PHP%20Developper%20Gameloft</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row73" class="row_heading level0 row73" >116</th>
      <td id="T_c6c4b_row73_col0" class="data row73 col0" >Junior Resource Analyst</td>
      <td id="T_c6c4b_row73_col1" class="data row73 col1" > Data manipulation, forest estate modelling, and resource planning; and. Contribute to projects managed by project teams in areas such as, but not limited to,… </td>
      <td id="T_c6c4b_row73_col2" class="data row73 col2" >Active 7 days ago</td>
      <td id="T_c6c4b_row73_col3" class="data row73 col3" >https://ca.indeed.com/jobs?q=Junior%20Resource%20Analyst%20Ecora</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row74" class="row_heading level0 row74" >115</th>
      <td id="T_c6c4b_row74_col0" class="data row74 col0" >Junior Software Developer</td>
      <td id="T_c6c4b_row74_col1" class="data row74 col1" > In this role you will be able to provide technical insights and expertise to support comprehensive automated verification. Fix bugs on existing scripts. </td>
      <td id="T_c6c4b_row74_col2" class="data row74 col2" >Active 7 days ago</td>
      <td id="T_c6c4b_row74_col3" class="data row74 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20Keywords%20Studios</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row75" class="row_heading level0 row75" >210</th>
      <td id="T_c6c4b_row75_col0" class="data row75 col0" >Embedded Low Level Software Developer - Junior</td>
      <td id="T_c6c4b_row75_col1" class="data row75 col1" > MANNARINO Systems &amp; Software Inc. holds over 20 years of experience in designing, developing, verifying and certifying real-time embedded software for safety… </td>
      <td id="T_c6c4b_row75_col2" class="data row75 col2" >8 days ago</td>
      <td id="T_c6c4b_row75_col3" class="data row75 col3" >https://ca.indeed.com/jobs?q=Embedded%20Low%20Level%20Software%20Developer%20-%20Junior%20Mannarino%20Systems%20%26%20Software%20Inc</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row76" class="row_heading level0 row76" >209</th>
      <td id="T_c6c4b_row76_col0" class="data row76 col0" >Développeur(se) Logiciel Junior|Junior Software Developer</td>
      <td id="T_c6c4b_row76_col1" class="data row76 col1" > ALTEN Canada is currently looking for freshly graduated junior consultants to participate in the digital transformation of its renowned clients in the greater… </td>
      <td id="T_c6c4b_row76_col2" class="data row76 col2" >Active 8 days ago</td>
      <td id="T_c6c4b_row76_col3" class="data row76 col3" >https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%28se%29%20Logiciel%20Junior%7CJunior%20Software%20Developer%20ALTEN%20CANADA%20INC.</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row77" class="row_heading level0 row77" >19</th>
      <td id="T_c6c4b_row77_col0" class="data row77 col0" >Junior Data Engineer</td>
      <td id="T_c6c4b_row77_col1" class="data row77 col1" > Build and maintain data pipeline architecture required for optimal extraction, transformation, and loading of data from a wide variety of data sources. </td>
      <td id="T_c6c4b_row77_col2" class="data row77 col2" >Active 8 days ago</td>
      <td id="T_c6c4b_row77_col3" class="data row77 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Engineer%20Canadian%20Niagara%20Hotels</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row78" class="row_heading level0 row78" >212</th>
      <td id="T_c6c4b_row78_col0" class="data row78 col0" >Développeur junior, DevOps</td>
      <td id="T_c6c4b_row78_col1" class="data row78 col1" >Description de l'entreprise Notre spécialité, c'est d'optimiser! Et nous sommes fiers de notre expertise. Nous mettons à profit notre intelligence collective…</td>
      <td id="T_c6c4b_row78_col2" class="data row78 col2" >9 days ago</td>
      <td id="T_c6c4b_row78_col3" class="data row78 col3" >https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20junior%2C%20DevOps%20GIRO</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row79" class="row_heading level0 row79" >120</th>
      <td id="T_c6c4b_row79_col0" class="data row79 col0" >Junior Software Developer-AQE</td>
      <td id="T_c6c4b_row79_col1" class="data row79 col1" > In this role you will be able to provide technical insights and expertise to support comprehensive automated verification. Previous experience in software QA. </td>
      <td id="T_c6c4b_row79_col2" class="data row79 col2" >Active 9 days ago</td>
      <td id="T_c6c4b_row79_col3" class="data row79 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer-AQE%20Keywords%20Studios</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row80" class="row_heading level0 row80" >20</th>
      <td id="T_c6c4b_row80_col0" class="data row80 col0" >Junior Data Engineer - OpenRoad Auto Group</td>
      <td id="T_c6c4b_row80_col1" class="data row80 col1" > Ensure high data integrity and quality from various data sources that are aligned to industry best practices. Graduates of Computer Science, Electrical/Computer… </td>
      <td id="T_c6c4b_row80_col2" class="data row80 col2" >9 days ago</td>
      <td id="T_c6c4b_row80_col3" class="data row80 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Engineer%20-%20OpenRoad%20Auto%20Group%20OpenRoad%20Auto%20Group</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row81" class="row_heading level0 row81" >211</th>
      <td id="T_c6c4b_row81_col0" class="data row81 col0" >Junior Solutions Architect</td>
      <td id="T_c6c4b_row81_col1" class="data row81 col1" > Provide technical leadership throughout the development life cycle and focus on delivery of quality solutions. Define standards to guide architectural designs. </td>
      <td id="T_c6c4b_row81_col2" class="data row81 col2" >9 days ago</td>
      <td id="T_c6c4b_row81_col3" class="data row81 col3" >https://ca.indeed.com/jobs?q=Junior%20Solutions%20Architect%20BIMM</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row82" class="row_heading level0 row82" >119</th>
      <td id="T_c6c4b_row82_col0" class="data row82 col0" >Junior Salesforce Developer</td>
      <td id="T_c6c4b_row82_col1" class="data row82 col1" > Location: 80 Courtneypark Dr. West, Mississauga, Ontario. Just Energy is a consumer company focused on essential needs, including electricity and natural gas;… </td>
      <td id="T_c6c4b_row82_col2" class="data row82 col2" >9 days ago</td>
      <td id="T_c6c4b_row82_col3" class="data row82 col3" >https://ca.indeed.com/jobs?q=Junior%20Salesforce%20Developer%20Just%20Energy</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row83" class="row_heading level0 row83" >121</th>
      <td id="T_c6c4b_row83_col0" class="data row83 col0" >Junior Full Stack Software Developer</td>
      <td id="T_c6c4b_row83_col1" class="data row83 col1" > DataDrill is currently seeking a Junior Full Stack Software Developer within the R&amp;D department. You have excellent verbal and written communication skills. </td>
      <td id="T_c6c4b_row83_col2" class="data row83 col2" >10 days ago</td>
      <td id="T_c6c4b_row83_col3" class="data row83 col3" >https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Software%20Developer%20DataDrill%20Communications%20Inc.</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row84" class="row_heading level0 row84" >22</th>
      <td id="T_c6c4b_row84_col0" class="data row84 col0" >Analyst, Cost of Goods Sold Finance</td>
      <td id="T_c6c4b_row84_col1" class="data row84 col1" > 2 years of Operations and Supply Chain Finance experience however not mandatory as this is a junior position. As the Senior Analyst, Cost of Goods Sold Finance,… </td>
      <td id="T_c6c4b_row84_col2" class="data row84 col2" >10 days ago</td>
      <td id="T_c6c4b_row84_col3" class="data row84 col3" >https://ca.indeed.com/jobs?q=Analyst%2C%20Cost%20of%20Goods%20Sold%20Finance%20Canopy%20Growth%20Corporation</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row85" class="row_heading level0 row85" >23</th>
      <td id="T_c6c4b_row85_col0" class="data row85 col0" >Junior Business Analyst, Inventory Control (42449)</td>
      <td id="T_c6c4b_row85_col1" class="data row85 col1" > 1-2 years experience in data analysis. Analyze data for inventory and other functions of the company on a needs basis. Monday to Friday working hours. </td>
      <td id="T_c6c4b_row85_col2" class="data row85 col2" >10 days ago</td>
      <td id="T_c6c4b_row85_col3" class="data row85 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%2C%20Inventory%20Control%20%2842449%29%20Toronto%20Research%20Chemicals</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row86" class="row_heading level0 row86" >21</th>
      <td id="T_c6c4b_row86_col0" class="data row86 col0" >Jr. Financial Analyst</td>
      <td id="T_c6c4b_row86_col1" class="data row86 col1" > Ability to extract, manipulate and analyze data from multiple systems/sources and databases. Serving as the go-to person in the Ontario Region (20+ sites) for… </td>
      <td id="T_c6c4b_row86_col2" class="data row86 col2" >10 days ago</td>
      <td id="T_c6c4b_row86_col3" class="data row86 col3" >https://ca.indeed.com/jobs?q=Jr.%20Financial%20Analyst%20American%20Iron%20and%20Metal</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row87" class="row_heading level0 row87" >24</th>
      <td id="T_c6c4b_row87_col0" class="data row87 col0" >Analyst, Business I</td>
      <td id="T_c6c4b_row87_col1" class="data row87 col1" > Evaluate the data collected through task analysis, business process, surveys and workshops. The Business Analyst Role is responsible for ensuring the… </td>
      <td id="T_c6c4b_row87_col2" class="data row87 col2" >11 days ago</td>
      <td id="T_c6c4b_row87_col3" class="data row87 col3" >https://ca.indeed.com/jobs?q=Analyst%2C%20Business%20I%20Mosaic%20North%20America</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row88" class="row_heading level0 row88" >214</th>
      <td id="T_c6c4b_row88_col0" class="data row88 col0" >Junior Python Developer</td>
      <td id="T_c6c4b_row88_col1" class="data row88 col1" > 2-3 years relevant experience or equivalent - with the majority of experience with Python. Design, develop, test, deploy, maintain and improve software… </td>
      <td id="T_c6c4b_row88_col2" class="data row88 col2" >11 days ago</td>
      <td id="T_c6c4b_row88_col3" class="data row88 col3" >https://ca.indeed.com/jobs?q=Junior%20Python%20Developer%20Macadamian</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row89" class="row_heading level0 row89" >123</th>
      <td id="T_c6c4b_row89_col0" class="data row89 col0" >Jr. Applications Analyst</td>
      <td id="T_c6c4b_row89_col1" class="data row89 col1" > Temporary, Full-Time – 35 hours per week. Six-month term, with the possibility of extension. We are currently recruiting for a Temporary, full-time Junior… </td>
      <td id="T_c6c4b_row89_col2" class="data row89 col2" >11 days ago</td>
      <td id="T_c6c4b_row89_col3" class="data row89 col3" >https://ca.indeed.com/jobs?q=Jr.%20Applications%20Analyst%20City%20of%20Leduc</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row90" class="row_heading level0 row90" >25</th>
      <td id="T_c6c4b_row90_col0" class="data row90 col0" >Junior ESG Research Analyst - Bahasa</td>
      <td id="T_c6c4b_row90_col1" class="data row90 col1" > As a Junior ESG Research Analyst, you will play a crucial role in supporting RepRisk's growth and global reach by analyzing and entering risk incidents from… </td>
      <td id="T_c6c4b_row90_col2" class="data row90 col2" >Active 11 days ago</td>
      <td id="T_c6c4b_row90_col3" class="data row90 col3" >https://ca.indeed.com/jobs?q=Junior%20ESG%20Research%20Analyst%20-%20Bahasa%20RepRisk%20AG</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row91" class="row_heading level0 row91" >122</th>
      <td id="T_c6c4b_row91_col0" class="data row91 col0" >IT Support Specialist (Junior - Intermediate)</td>
      <td id="T_c6c4b_row91_col1" class="data row91 col1" > \* Day to day responsibilities include corresponding with staff via telephone, email and chat, creating and closing trouble tickets, resolving technical issues,… </td>
      <td id="T_c6c4b_row91_col2" class="data row91 col2" >Active 11 days ago</td>
      <td id="T_c6c4b_row91_col3" class="data row91 col3" >https://ca.indeed.com/jobs?q=IT%20Support%20Specialist%20%28Junior%20-%20Intermediate%29%20Websdepot%20Technology%20Partners%20Inc.</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row92" class="row_heading level0 row92" >26</th>
      <td id="T_c6c4b_row92_col0" class="data row92 col0" >Junior Business Analyst, Inventory Control</td>
      <td id="T_c6c4b_row92_col1" class="data row92 col1" > 1-2 years experience in data analysis. Analyze data for inventory and other functions of the company on a needs basis. Monday to Friday working hours. </td>
      <td id="T_c6c4b_row92_col2" class="data row92 col2" >11 days ago</td>
      <td id="T_c6c4b_row92_col3" class="data row92 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%2C%20Inventory%20Control%20LGC%20Limited</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row93" class="row_heading level0 row93" >125</th>
      <td id="T_c6c4b_row93_col0" class="data row93 col0" >Junior Front End Developer</td>
      <td id="T_c6c4b_row93_col1" class="data row93 col1" > MyMarketing is a unique digital marketing agency that provides businesses with a comprehensive, no-commitment digital marketing monthly subscription. </td>
      <td id="T_c6c4b_row93_col2" class="data row93 col2" >Active 12 days ago</td>
      <td id="T_c6c4b_row93_col3" class="data row93 col3" >https://ca.indeed.com/jobs?q=Junior%20Front%20End%20Developer%20myMarketing.io</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row94" class="row_heading level0 row94" >218</th>
      <td id="T_c6c4b_row94_col0" class="data row94 col0" >Junior Lighting Technical Director (Feature Animation) Vanco...</td>
      <td id="T_c6c4b_row94_col1" class="data row94 col1" > The Junior Lighting TDs work under a sequence lighting lead to make basic lighting and shader tweaks. They may also manage renders and provide them to comp. </td>
      <td id="T_c6c4b_row94_col2" class="data row94 col2" >12 days ago</td>
      <td id="T_c6c4b_row94_col3" class="data row94 col3" >https://ca.indeed.com/jobs?q=Junior%20Lighting%20Technical%20Director%20%28Feature%20Animation%29%20Vanco...%20Industrial%20Light%20%26%20Magic</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row95" class="row_heading level0 row95" >217</th>
      <td id="T_c6c4b_row95_col0" class="data row95 col0" >Jr. Application Engineering Specialist- Autonomy Software</td>
      <td id="T_c6c4b_row95_col1" class="data row95 col1" > Headquartered in Kitchener, ON, Canada, Avidbots offers comprehensive service and support to customers in 5 continents. </td>
      <td id="T_c6c4b_row95_col2" class="data row95 col2" >12 days ago</td>
      <td id="T_c6c4b_row95_col3" class="data row95 col3" >https://ca.indeed.com/jobs?q=Jr.%20Application%20Engineering%20Specialist-%20Autonomy%20Software%20Avidbots</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row96" class="row_heading level0 row96" >216</th>
      <td id="T_c6c4b_row96_col0" class="data row96 col0" >Junior Software Developer - 5G RAN OAM</td>
      <td id="T_c6c4b_row96_col1" class="data row96 col1" > Experience using scripting languages (python, shell (bash), etc). Motivated designers with broad backgrounds and service mindset to be a consultant. </td>
      <td id="T_c6c4b_row96_col2" class="data row96 col2" >12 days ago</td>
      <td id="T_c6c4b_row96_col3" class="data row96 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20-%205G%20RAN%20OAM%20Syntronic</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row97" class="row_heading level0 row97" >127</th>
      <td id="T_c6c4b_row97_col0" class="data row97 col0" >Junior Systems Analyst, Clinical Solutions, IMITS</td>
      <td id="T_c6c4b_row97_col1" class="data row97 col1" > As per the current Public Health Order, full vaccination against COVID-19 is a condition of employment with PHSA as of October 26, 2021. </td>
      <td id="T_c6c4b_row97_col2" class="data row97 col2" >13 days ago</td>
      <td id="T_c6c4b_row97_col3" class="data row97 col3" >https://ca.indeed.com/jobs?q=Junior%20Systems%20Analyst%2C%20Clinical%20Solutions%2C%20IMITS%20PHSA</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row98" class="row_heading level0 row98" >126</th>
      <td id="T_c6c4b_row98_col0" class="data row98 col0" >Junior Systems Administrator</td>
      <td id="T_c6c4b_row98_col1" class="data row98 col1" > Do you want to make a big impact on a fast-growing IT organization? Do you want to be part of a team that truly supports employee growth and development? </td>
      <td id="T_c6c4b_row98_col2" class="data row98 col2" >13 days ago</td>
      <td id="T_c6c4b_row98_col3" class="data row98 col3" >https://ca.indeed.com/jobs?q=Junior%20Systems%20Administrator%20ProServeIT</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row99" class="row_heading level0 row99" >219</th>
      <td id="T_c6c4b_row99_col0" class="data row99 col0" >Jr. Project Coordinator</td>
      <td id="T_c6c4b_row99_col1" class="data row99 col1" > This project is part of Bruce Power’s Life Extension Program, which will allow Bruce Power’s CANDU units to continue to operate safely through to 2064, the… </td>
      <td id="T_c6c4b_row99_col2" class="data row99 col2" >13 days ago</td>
      <td id="T_c6c4b_row99_col3" class="data row99 col3" >https://ca.indeed.com/jobs?q=Jr.%20Project%20Coordinator%20Aecon%20Group</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row100" class="row_heading level0 row100" >27</th>
      <td id="T_c6c4b_row100_col0" class="data row100 col0" >Financial Analyst I</td>
      <td id="T_c6c4b_row100_col1" class="data row100 col1" > Financial reporting, data analysis, financial systems, attention to detail. Strong Problem Solving Skills Proficient in Excel and Analytical Tools Proven… </td>
      <td id="T_c6c4b_row100_col2" class="data row100 col2" >13 days ago</td>
      <td id="T_c6c4b_row100_col3" class="data row100 col3" >https://ca.indeed.com/jobs?q=Financial%20Analyst%20I%20Agilus%20Work%20Solutions</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row101" class="row_heading level0 row101" >28</th>
      <td id="T_c6c4b_row101_col0" class="data row101 col0" >Junior Credit Card Analyst (12 Month Contract)</td>
      <td id="T_c6c4b_row101_col1" class="data row101 col1" > Experience with data analysis tools including using spreadsheets (MS Excel, Google Docs, Sheets) and SQL/relational databases. Bonus points if you have.... </td>
      <td id="T_c6c4b_row101_col2" class="data row101 col2" >13 days ago</td>
      <td id="T_c6c4b_row101_col3" class="data row101 col3" >https://ca.indeed.com/jobs?q=Junior%20Credit%20Card%20Analyst%20%2812%20Month%20Contract%29%20Credit%20Sesame</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row102" class="row_heading level0 row102" >29</th>
      <td id="T_c6c4b_row102_col0" class="data row102 col0" >Junior DBA (Database Administrator)</td>
      <td id="T_c6c4b_row102_col1" class="data row102 col1" > Provide DB2 Administrative services to application development team. Design/develop/test/support DB2 LUW database. Performance tuning and trouble shooting. </td>
      <td id="T_c6c4b_row102_col2" class="data row102 col2" >Active 15 days ago</td>
      <td id="T_c6c4b_row102_col3" class="data row102 col3" >https://ca.indeed.com/jobs?q=Junior%20DBA%20%28Database%20Administrator%29%20Dawn%20InfoTek%20Inc.</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row103" class="row_heading level0 row103" >128</th>
      <td id="T_c6c4b_row103_col0" class="data row103 col0" >Junior Database Administrator - Co-Op Student</td>
      <td id="T_c6c4b_row103_col1" class="data row103 col1" > Gaining experience with database platforms: Oracle, MSSQL, PostgreSQL, AWS Aurora, etc. Performing daily maintenance including monitoring backups, managing disk… </td>
      <td id="T_c6c4b_row103_col2" class="data row103 col2" >16 days ago</td>
      <td id="T_c6c4b_row103_col3" class="data row103 col3" >https://ca.indeed.com/jobs?q=Junior%20Database%20Administrator%20-%20Co-Op%20Student%20CGI</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row104" class="row_heading level0 row104" >31</th>
      <td id="T_c6c4b_row104_col0" class="data row104 col0" >Junior Marketing Analyst (temp. up to 6 months)</td>
      <td id="T_c6c4b_row104_col1" class="data row104 col1" > You may have experience data visualization tools such as Power BI; You have the ability to apply critical thinking and problem-solving skills to organize and… </td>
      <td id="T_c6c4b_row104_col2" class="data row104 col2" >16 days ago</td>
      <td id="T_c6c4b_row104_col3" class="data row104 col3" >https://ca.indeed.com/jobs?q=Junior%20Marketing%20Analyst%20%28temp.%20up%20to%206%20months%29%20Boston%20Pizza%20International</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row105" class="row_heading level0 row105" >30</th>
      <td id="T_c6c4b_row105_col0" class="data row105 col0" >Junior Business Analyst</td>
      <td id="T_c6c4b_row105_col1" class="data row105 col1" > Develop and monitor data quality metrics and ensure business data and reporting needs are met. You are responsible for developing and monitoring data quality… </td>
      <td id="T_c6c4b_row105_col2" class="data row105 col2" >16 days ago</td>
      <td id="T_c6c4b_row105_col3" class="data row105 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20Norsat%20International%20Inc.</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row106" class="row_heading level0 row106" >220</th>
      <td id="T_c6c4b_row106_col0" class="data row106 col0" >Junior Silicon Validation Engineer - (20241)</td>
      <td id="T_c6c4b_row106_col1" class="data row106 col1" > You will be responsible for testing of our SerDes devices, developing Python automation scripts to characterize the devices, and performing device result… </td>
      <td id="T_c6c4b_row106_col2" class="data row106 col2" >17 days ago</td>
      <td id="T_c6c4b_row106_col3" class="data row106 col3" >https://ca.indeed.com/jobs?q=Junior%20Silicon%20Validation%20Engineer%20-%20%2820241%29%20Alphawave%20IP</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row107" class="row_heading level0 row107" >32</th>
      <td id="T_c6c4b_row107_col0" class="data row107 col0" >Junior Data Analyst</td>
      <td id="T_c6c4b_row107_col1" class="data row107 col1" > Acquire data from primary or secondary data sources and maintain databases/data systems. Experience analyzing and trending data from multiple sources. </td>
      <td id="T_c6c4b_row107_col2" class="data row107 col2" >17 days ago</td>
      <td id="T_c6c4b_row107_col3" class="data row107 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20Match%20Retail</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row108" class="row_heading level0 row108" >33</th>
      <td id="T_c6c4b_row108_col0" class="data row108 col0" >Junior Database Administrator - Co-Op Student</td>
      <td id="T_c6c4b_row108_col1" class="data row108 col1" > Gaining experience with database platforms: Oracle, MSSQL, PostgreSQL, AWS Aurora, etc. Performing daily maintenance including monitoring backups, managing disk… </td>
      <td id="T_c6c4b_row108_col2" class="data row108 col2" >17 days ago</td>
      <td id="T_c6c4b_row108_col3" class="data row108 col3" >https://ca.indeed.com/jobs?q=Junior%20Database%20Administrator%20-%20Co-Op%20Student%20CGI%20Inc</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row109" class="row_heading level0 row109" >221</th>
      <td id="T_c6c4b_row109_col0" class="data row109 col0" >Junior Software Development Engineer in Test</td>
      <td id="T_c6c4b_row109_col1" class="data row109 col1" > As a Junior Software Development Engineer in Test (Jr. SDET), you will be part of a small, highly focused team responsible for delivery of highly scalable and… </td>
      <td id="T_c6c4b_row109_col2" class="data row109 col2" >18 days ago</td>
      <td id="T_c6c4b_row109_col3" class="data row109 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Development%20Engineer%20in%20Test%20Global%20Relay</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row110" class="row_heading level0 row110" >131</th>
      <td id="T_c6c4b_row110_col0" class="data row110 col0" >FL Junior .Net Developer</td>
      <td id="T_c6c4b_row110_col1" class="data row110 col1" > This resource will be responsible for the following: Coding, unit testing and creating supporting documentation. Participating in system and acceptance testing. </td>
      <td id="T_c6c4b_row110_col2" class="data row110 col2" >18 days ago</td>
      <td id="T_c6c4b_row110_col3" class="data row110 col3" >https://ca.indeed.com/jobs?q=FL%20Junior%20.Net%20Developer%20Fujitsu</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row111" class="row_heading level0 row111" >132</th>
      <td id="T_c6c4b_row111_col0" class="data row111 col0" >Toronto - Junior Software Developer</td>
      <td id="T_c6c4b_row111_col1" class="data row111 col1" > Since 2014, we have launched the careers of over 1,000 junior software developers in Canada. Find out about FDM’s Coronavirus (COVID-19) preparations here. </td>
      <td id="T_c6c4b_row111_col2" class="data row111 col2" >19 days ago</td>
      <td id="T_c6c4b_row111_col3" class="data row111 col3" >https://ca.indeed.com/jobs?q=Toronto%20-%20Junior%20Software%20Developer%20FDM%20Group</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row112" class="row_heading level0 row112" >133</th>
      <td id="T_c6c4b_row112_col0" class="data row112 col0" >Junior System Network Administrator</td>
      <td id="T_c6c4b_row112_col1" class="data row112 col1" > Receive and resolve all types of technology-related service calls. Local and remote End-user support. Install, configure, and upgrade computer software. </td>
      <td id="T_c6c4b_row112_col2" class="data row112 col2" >19 days ago</td>
      <td id="T_c6c4b_row112_col3" class="data row112 col3" >https://ca.indeed.com/jobs?q=Junior%20System%20Network%20Administrator%20The%20Career%20Foundation</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row113" class="row_heading level0 row113" >134</th>
      <td id="T_c6c4b_row113_col0" class="data row113 col0" >Montreal - Junior Software Tester - Bilingual</td>
      <td id="T_c6c4b_row113_col1" class="data row113 col1" > As a Junior Software Tester, you will learn the role of a technical tester in order to assure the quality of systems and applications through the full… </td>
      <td id="T_c6c4b_row113_col2" class="data row113 col2" >19 days ago</td>
      <td id="T_c6c4b_row113_col3" class="data row113 col3" >https://ca.indeed.com/jobs?q=Montreal%20-%20Junior%20Software%20Tester%20-%20Bilingual%20FDM%20Group</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row114" class="row_heading level0 row114" >135</th>
      <td id="T_c6c4b_row114_col0" class="data row114 col0" >Toronto - Junior Quality Automation Engineer</td>
      <td id="T_c6c4b_row114_col1" class="data row114 col1" > As a Junior Quality Automation Engineer, you will learn the role of a technical tester in order to assure the quality of systems and applications through the… </td>
      <td id="T_c6c4b_row114_col2" class="data row114 col2" >19 days ago</td>
      <td id="T_c6c4b_row114_col3" class="data row114 col3" >https://ca.indeed.com/jobs?q=Toronto%20-%20Junior%20Quality%20Automation%20Engineer%20FDM%20Group</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row115" class="row_heading level0 row115" >136</th>
      <td id="T_c6c4b_row115_col0" class="data row115 col0" >Montreal - Junior Software Developer</td>
      <td id="T_c6c4b_row115_col1" class="data row115 col1" > Since 2014, we have launched the careers of over 1,000 junior software developers in Canada. Find out about FDM’s Coronavirus (COVID-19) preparations here. </td>
      <td id="T_c6c4b_row115_col2" class="data row115 col2" >19 days ago</td>
      <td id="T_c6c4b_row115_col3" class="data row115 col3" >https://ca.indeed.com/jobs?q=Montreal%20-%20Junior%20Software%20Developer%20FDM%20Group</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row116" class="row_heading level0 row116" >223</th>
      <td id="T_c6c4b_row116_col0" class="data row116 col0" >Montreal - Développeur de Logiciels Junior</td>
      <td id="T_c6c4b_row116_col1" class="data row116 col1" > Renseignez-vous sur les préparatifs de FDM pour le coronavirus (COVID-19) ici. Certains postes courants que vous pourriez occuper incluent Développeur Front-end… </td>
      <td id="T_c6c4b_row116_col2" class="data row116 col2" >19 days ago</td>
      <td id="T_c6c4b_row116_col3" class="data row116 col3" >https://ca.indeed.com/jobs?q=Montreal%20-%20D%C3%A9veloppeur%20de%20Logiciels%20Junior%20FDM%20Group</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row117" class="row_heading level0 row117" >36</th>
      <td id="T_c6c4b_row117_col0" class="data row117 col0" >Montreal - Junior Finance/Compliance Analyst</td>
      <td id="T_c6c4b_row117_col1" class="data row117 col1" > FDM Junior Finance/Compliance Analysts take on responsibilities such as conducting client due diligence, monitoring and reporting transactions to regulators,… </td>
      <td id="T_c6c4b_row117_col2" class="data row117 col2" >19 days ago</td>
      <td id="T_c6c4b_row117_col3" class="data row117 col3" >https://ca.indeed.com/jobs?q=Montreal%20-%20Junior%20Finance/Compliance%20Analyst%20FDM%20Group</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row118" class="row_heading level0 row118" >37</th>
      <td id="T_c6c4b_row118_col0" class="data row118 col0" >Montreal - Analyste Technique Junior ou chef de Projet Techn...</td>
      <td id="T_c6c4b_row118_col1" class="data row118 col1" > Certains postes courants dans lesquels vous pourriez travailler incluent chef de projet junior, coordinateur de projet, analyste commercial et plus encore. </td>
      <td id="T_c6c4b_row118_col2" class="data row118 col2" >19 days ago</td>
      <td id="T_c6c4b_row118_col3" class="data row118 col3" >https://ca.indeed.com/jobs?q=Montreal%20-%20Analyste%20Technique%20Junior%20ou%20chef%20de%20Projet%20Techn...%20FDM%20Group</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row119" class="row_heading level0 row119" >222</th>
      <td id="T_c6c4b_row119_col0" class="data row119 col0" >Remote Training - Canada - Junior Software Developer</td>
      <td id="T_c6c4b_row119_col1" class="data row119 col1" > As a Software Developer your main role will be to solve problems, upgrade existing systems and improve efficiency for the overall success of large software… </td>
      <td id="T_c6c4b_row119_col2" class="data row119 col2" >19 days ago</td>
      <td id="T_c6c4b_row119_col3" class="data row119 col3" >https://ca.indeed.com/jobs?q=Remote%20Training%20-%20Canada%20-%20Junior%20Software%20Developer%20FDM%20Group</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row120" class="row_heading level0 row120" >34</th>
      <td id="T_c6c4b_row120_col0" class="data row120 col0" >Toronto - Junior Technical Business Analyst/ Junior Technica...</td>
      <td id="T_c6c4b_row120_col1" class="data row120 col1" > These roles are crucial in helping organizations with the accuracy and timely presentation of data, in line with internal process, governance, and regulatory… </td>
      <td id="T_c6c4b_row120_col2" class="data row120 col2" >19 days ago</td>
      <td id="T_c6c4b_row120_col3" class="data row120 col3" >https://ca.indeed.com/jobs?q=Toronto%20-%20Junior%20Technical%20Business%20Analyst/%20Junior%20Technica...%20FDM%20Group</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row121" class="row_heading level0 row121" >35</th>
      <td id="T_c6c4b_row121_col0" class="data row121 col0" >Toronto - Junior Data Engineer</td>
      <td id="T_c6c4b_row121_col1" class="data row121 col1" > Understanding of data constructs, data modelling and data management tools. As a Junior Data Engineer, you will design, develop and test a large-scale, custom… </td>
      <td id="T_c6c4b_row121_col2" class="data row121 col2" >19 days ago</td>
      <td id="T_c6c4b_row121_col3" class="data row121 col3" >https://ca.indeed.com/jobs?q=Toronto%20-%20Junior%20Data%20Engineer%20FDM%20Group</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row122" class="row_heading level0 row122" >38</th>
      <td id="T_c6c4b_row122_col0" class="data row122 col0" >Junior Business Analyst - Co-Op Student</td>
      <td id="T_c6c4b_row122_col1" class="data row122 col1" > Developing understanding of Accounts payable and accounts receivable. Takes accountability for results and exhibits a “can do” demeanor. </td>
      <td id="T_c6c4b_row122_col2" class="data row122 col2" >19 days ago</td>
      <td id="T_c6c4b_row122_col3" class="data row122 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20-%20Co-Op%20Student%20CGI</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row123" class="row_heading level0 row123" >224</th>
      <td id="T_c6c4b_row123_col0" class="data row123 col0" >Junior Cloud Engineer</td>
      <td id="T_c6c4b_row123_col1" class="data row123 col1" > Assist with the mentorship of junior engineers through pair programming exercises. An automation engineer, you will be a member of the cloud and transformation… </td>
      <td id="T_c6c4b_row123_col2" class="data row123 col2" >20 days ago</td>
      <td id="T_c6c4b_row123_col3" class="data row123 col3" >https://ca.indeed.com/jobs?q=Junior%20Cloud%20Engineer%20Royal%20Bank%20of%20Canada</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row124" class="row_heading level0 row124" >39</th>
      <td id="T_c6c4b_row124_col0" class="data row124 col0" >Junior Digital Marketing Specialist</td>
      <td id="T_c6c4b_row124_col1" class="data row124 col1" > Widespread media monitoring to collect data about PAL Airlines brand mentions and news articles. Community management for all PAL Airlines social media outlets. </td>
      <td id="T_c6c4b_row124_col2" class="data row124 col2" >23 days ago</td>
      <td id="T_c6c4b_row124_col3" class="data row124 col3" >https://ca.indeed.com/jobs?q=Junior%20Digital%20Marketing%20Specialist%20PAL%20Airlines</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row125" class="row_heading level0 row125" >225</th>
      <td id="T_c6c4b_row125_col0" class="data row125 col0" >Junior DevOps Engineer</td>
      <td id="T_c6c4b_row125_col1" class="data row125 col1" > The Jr. DevOps Platform Engineer position is responsible for developing, designing, automating and maintaining our complex datacenter, on-premise, and cloud… </td>
      <td id="T_c6c4b_row125_col2" class="data row125 col2" >23 days ago</td>
      <td id="T_c6c4b_row125_col3" class="data row125 col3" >https://ca.indeed.com/jobs?q=Junior%20DevOps%20Engineer%20Intelerad</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row126" class="row_heading level0 row126" >231</th>
      <td id="T_c6c4b_row126_col0" class="data row126 col0" >Junior Technical Artist</td>
      <td id="T_c6c4b_row126_col1" class="data row126 col1" > Work across departments to support the development of software tools and scripts which improve the development of visual targets. </td>
      <td id="T_c6c4b_row126_col2" class="data row126 col2" >24 days ago</td>
      <td id="T_c6c4b_row126_col3" class="data row126 col3" >https://ca.indeed.com/jobs?q=Junior%20Technical%20Artist%20HB%20Studios</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row127" class="row_heading level0 row127" >230</th>
      <td id="T_c6c4b_row127_col0" class="data row127 col0" >Junior Software Engineer/Designer – Peterborough, ON</td>
      <td id="T_c6c4b_row127_col1" class="data row127 col1" > Knowledge and use of several Integrated software development environment SDE tools and scripting languages (python, etc). Knowledge and use of databases. </td>
      <td id="T_c6c4b_row127_col2" class="data row127 col2" >24 days ago</td>
      <td id="T_c6c4b_row127_col3" class="data row127 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Engineer/Designer%20%E2%80%93%20Peterborough%2C%20ON%20Can-Tech%20Services</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row128" class="row_heading level0 row128" >229</th>
      <td id="T_c6c4b_row128_col0" class="data row128 col0" >Développeur de Logiciels Embarqués de Bas Niveau - Junior</td>
      <td id="T_c6c4b_row128_col1" class="data row128 col1" > D’une gamme complète d’assurance collective et un plan RÉER collectif; D’une politique d’horaire flexible; Développer la documentation du logiciel conformément… </td>
      <td id="T_c6c4b_row128_col2" class="data row128 col2" >24 days ago</td>
      <td id="T_c6c4b_row128_col3" class="data row128 col3" >https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20de%20Logiciels%20Embarqu%C3%A9s%20de%20Bas%20Niveau%20-%20Junior%20MANNARINO</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row129" class="row_heading level0 row129" >228</th>
      <td id="T_c6c4b_row129_col0" class="data row129 col0" >Embedded Low Level Software Developer - Junior</td>
      <td id="T_c6c4b_row129_col1" class="data row129 col1" > MANNARINO Systems &amp; Software Inc. holds over 20 years experience in designing, developing, verifying and certifying real-time embedded software for safety… </td>
      <td id="T_c6c4b_row129_col2" class="data row129 col2" >24 days ago</td>
      <td id="T_c6c4b_row129_col3" class="data row129 col3" >https://ca.indeed.com/jobs?q=Embedded%20Low%20Level%20Software%20Developer%20-%20Junior%20MANNARINO</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row130" class="row_heading level0 row130" >227</th>
      <td id="T_c6c4b_row130_col0" class="data row130 col0" >Junior Technical Artist</td>
      <td id="T_c6c4b_row130_col1" class="data row130 col1" > Work across departments to support the development of software tools and scripts which improve the development of visual targets. </td>
      <td id="T_c6c4b_row130_col2" class="data row130 col2" >24 days ago</td>
      <td id="T_c6c4b_row130_col3" class="data row130 col3" >https://ca.indeed.com/jobs?q=Junior%20Technical%20Artist%202K</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row131" class="row_heading level0 row131" >226</th>
      <td id="T_c6c4b_row131_col0" class="data row131 col0" >Dev Full Stack Junior</td>
      <td id="T_c6c4b_row131_col1" class="data row131 col1" > Thales est une entreprise où les personnes les plus brillantes du monde entier se regroupent pour mettre en commun leurs idées et ainsi s'inspirer mutuellement. </td>
      <td id="T_c6c4b_row131_col2" class="data row131 col2" >24 days ago</td>
      <td id="T_c6c4b_row131_col3" class="data row131 col3" >https://ca.indeed.com/jobs?q=Dev%20Full%20Stack%20Junior%20Thales%20Digital%20Solutions%20Inc.%2C%20Research%20%26...</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row132" class="row_heading level0 row132" >40</th>
      <td id="T_c6c4b_row132_col0" class="data row132 col0" >Data Quality Coordinator I, Policy Reporter (Remote Canada)</td>
      <td id="T_c6c4b_row132_col1" class="data row132 col1" > Enhance data quality work process with SQL, BI tools or data profiler. Performing data cleansing activities independently and as directed by the Data Quality… </td>
      <td id="T_c6c4b_row132_col2" class="data row132 col2" >24 days ago</td>
      <td id="T_c6c4b_row132_col3" class="data row132 col3" >https://ca.indeed.com/jobs?q=Data%20Quality%20Coordinator%20I%2C%20Policy%20Reporter%20%28Remote%20Canada%29%20TrialCard</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row133" class="row_heading level0 row133" >41</th>
      <td id="T_c6c4b_row133_col0" class="data row133 col0" >Data Quality Coordinator I, Policy Reporter (Remote U.S.)</td>
      <td id="T_c6c4b_row133_col1" class="data row133 col1" > Enhance data quality work process with SQL, BI tools or data profiler. Performing data cleansing activities independently and as directed by the Data Quality… </td>
      <td id="T_c6c4b_row133_col2" class="data row133 col2" >24 days ago</td>
      <td id="T_c6c4b_row133_col3" class="data row133 col3" >https://ca.indeed.com/jobs?q=Data%20Quality%20Coordinator%20I%2C%20Policy%20Reporter%20%28Remote%20U.S.%29%20TrialCard</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row134" class="row_heading level0 row134" >42</th>
      <td id="T_c6c4b_row134_col0" class="data row134 col0" >Junior Business Analyst</td>
      <td id="T_c6c4b_row134_col1" class="data row134 col1" > Ensuring and maintaining data accuracy. Liaison with operations and developers to raise and understand any data discrepancies. </td>
      <td id="T_c6c4b_row134_col2" class="data row134 col2" >25 days ago</td>
      <td id="T_c6c4b_row134_col3" class="data row134 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20Motoinsight</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row135" class="row_heading level0 row135" >232</th>
      <td id="T_c6c4b_row135_col0" class="data row135 col0" >Software Engineer I - PitCrew</td>
      <td id="T_c6c4b_row135_col1" class="data row135 col1" > Design, develop, and maintain code for our web-based applications. Collaborate with software and production engineers to design scalable services, plan feature… </td>
      <td id="T_c6c4b_row135_col2" class="data row135 col2" >25 days ago</td>
      <td id="T_c6c4b_row135_col3" class="data row135 col3" >https://ca.indeed.com/jobs?q=Software%20Engineer%20I%20-%20PitCrew%20ACV%20Auctions</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row136" class="row_heading level0 row136" >233</th>
      <td id="T_c6c4b_row136_col0" class="data row136 col0" >JR Software Engineer</td>
      <td id="T_c6c4b_row136_col1" class="data row136 col1" > Knowledge and use of several Integrated software development environment SDE tools and scripting languages (python, etc). Knowledge and use of databases. </td>
      <td id="T_c6c4b_row136_col2" class="data row136 col2" >25 days ago</td>
      <td id="T_c6c4b_row136_col3" class="data row136 col3" >https://ca.indeed.com/jobs?q=JR%20Software%20Engineer%20Safran</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row137" class="row_heading level0 row137" >43</th>
      <td id="T_c6c4b_row137_col0" class="data row137 col0" >Junior Data Engineer</td>
      <td id="T_c6c4b_row137_col1" class="data row137 col1" > A passion for data quality. Strong data analysis skills (SQL). Learn new skills &amp; advance your data development practice. </td>
      <td id="T_c6c4b_row137_col2" class="data row137 col2" >26 days ago</td>
      <td id="T_c6c4b_row137_col3" class="data row137 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Engineer%20TELUS</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row138" class="row_heading level0 row138" >234</th>
      <td id="T_c6c4b_row138_col0" class="data row138 col0" >Junior Electronics Engineer - Integration and Testing</td>
      <td id="T_c6c4b_row138_col1" class="data row138 col1" > Basic programming skills in C, Labview or python. Salary starting at $55,000 depending on experience. Training and development opportunities in a growing… </td>
      <td id="T_c6c4b_row138_col2" class="data row138 col2" >26 days ago</td>
      <td id="T_c6c4b_row138_col3" class="data row138 col3" >https://ca.indeed.com/jobs?q=Junior%20Electronics%20Engineer%20-%20Integration%20and%20Testing%20Preciseley%20Microtechnology</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row139" class="row_heading level0 row139" >235</th>
      <td id="T_c6c4b_row139_col0" class="data row139 col0" >Jr Network Strategy Planning and Optimization Analyst-Supply...</td>
      <td id="T_c6c4b_row139_col1" class="data row139 col1" > We also conduct and simulate the future performance, tradeoffs, and customer service impacts of our models making certain that our design is aligned to business… </td>
      <td id="T_c6c4b_row139_col2" class="data row139 col2" >26 days ago</td>
      <td id="T_c6c4b_row139_col3" class="data row139 col3" >https://ca.indeed.com/jobs?q=Jr%20Network%20Strategy%20Planning%20and%20Optimization%20Analyst-Supply...%20SimWell</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row140" class="row_heading level0 row140" >44</th>
      <td id="T_c6c4b_row140_col0" class="data row140 col0" >Junior Data Automation Engineer</td>
      <td id="T_c6c4b_row140_col1" class="data row140 col1" > Experience with query optimization, performance tuning, data quality and data processing. Strong data processing skills and experience in the creation of data… </td>
      <td id="T_c6c4b_row140_col2" class="data row140 col2" >27 days ago</td>
      <td id="T_c6c4b_row140_col3" class="data row140 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Automation%20Engineer%20Kalibrate</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row141" class="row_heading level0 row141" >236</th>
      <td id="T_c6c4b_row141_col0" class="data row141 col0" >Technicien(nne) informatique junior / Junior IT Technician</td>
      <td id="T_c6c4b_row141_col1" class="data row141 col1" > Fondé en 1981, Goldwater Dubé est un cabinet de litige exerçant principalement en droit de la famille et responsable de certains des cas les plus novateurs dans… </td>
      <td id="T_c6c4b_row141_col2" class="data row141 col2" >27 days ago</td>
      <td id="T_c6c4b_row141_col3" class="data row141 col3" >https://ca.indeed.com/jobs?q=Technicien%28nne%29%20informatique%20junior%20/%20Junior%20IT%20Technician%20Goldwater%2C%20Dub%C3%A9%20Inc.</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row142" class="row_heading level0 row142" >137</th>
      <td id="T_c6c4b_row142_col0" class="data row142 col0" >Junior Developer</td>
      <td id="T_c6c4b_row142_col1" class="data row142 col1" > Reporting to the Architecture and Development Manager, the incumbent is working as a member of the Red-D-Arc Information Technology team, responsible for… </td>
      <td id="T_c6c4b_row142_col2" class="data row142 col2" >28 days ago</td>
      <td id="T_c6c4b_row142_col3" class="data row142 col3" >https://ca.indeed.com/jobs?q=Junior%20Developer%20Airgas%20Inc.</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row143" class="row_heading level0 row143" >138</th>
      <td id="T_c6c4b_row143_col0" class="data row143 col0" >Part-time Low Code Junior Developer Experience@siemens</td>
      <td id="T_c6c4b_row143_col1" class="data row143 col1" > Recent graduates enrolled in this program will be partnered with a mentor and receive one on one coaching and guidance in support of their development and to… </td>
      <td id="T_c6c4b_row143_col2" class="data row143 col2" >28 days ago</td>
      <td id="T_c6c4b_row143_col3" class="data row143 col3" >https://ca.indeed.com/jobs?q=Part-time%20Low%20Code%20Junior%20Developer%20Experience%40siemens%20Siemens</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row144" class="row_heading level0 row144" >237</th>
      <td id="T_c6c4b_row144_col0" class="data row144 col0" >Junior Full-Stack Developer/软件工程师 (Mandarin Required)</td>
      <td id="T_c6c4b_row144_col1" class="data row144 col1" > Maintain clean and functional codebase for both frontend and backend services. Work closely with operation team members to understand moderately complex product… </td>
      <td id="T_c6c4b_row144_col2" class="data row144 col2" >Active 28 days ago</td>
      <td id="T_c6c4b_row144_col3" class="data row144 col3" >https://ca.indeed.com/jobs?q=Junior%20Full-Stack%20Developer/%E8%BD%AF%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%B8%88%20%28Mandarin%20Required%29%20Savvypro%20Education</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row145" class="row_heading level0 row145" >264</th>
      <td id="T_c6c4b_row145_col0" class="data row145 col0" >Junior Electrical Engineer</td>
      <td id="T_c6c4b_row145_col1" class="data row145 col1" > Work collaboratively with clients, project managers, engineers, designers and drafters in the preparation of deliverables to BBA and client standards. </td>
      <td id="T_c6c4b_row145_col2" class="data row145 col2" >30+ days ago</td>
      <td id="T_c6c4b_row145_col3" class="data row145 col3" >https://ca.indeed.com/jobs?q=Junior%20Electrical%20Engineer%20BBA</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row146" class="row_heading level0 row146" >262</th>
      <td id="T_c6c4b_row146_col0" class="data row146 col0" >Développeur(se) de logiciels junior</td>
      <td id="T_c6c4b_row146_col1" class="data row146 col1" > Maritime International, une division de L3Harris, est un fournisseur mondial de premier plan de contrôles-commandes non ITAR et de solutions de simulation pour… </td>
      <td id="T_c6c4b_row146_col2" class="data row146 col2" >30+ days ago</td>
      <td id="T_c6c4b_row146_col3" class="data row146 col3" >https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%28se%29%20de%20logiciels%20junior%20French%20Canadian%20Instance</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row147" class="row_heading level0 row147" >263</th>
      <td id="T_c6c4b_row147_col0" class="data row147 col0" >Remote, Ontario – Junior Data Analytics Engineer</td>
      <td id="T_c6c4b_row147_col1" class="data row147 col1" > Operating under the Alessa brand, the compliance division is focused on creating comprehensive solutions to help financial institutions and many other… </td>
      <td id="T_c6c4b_row147_col2" class="data row147 col2" >30+ days ago</td>
      <td id="T_c6c4b_row147_col3" class="data row147 col3" >https://ca.indeed.com/jobs?q=Remote%2C%20Ontario%20%E2%80%93%20Junior%20Data%20Analytics%20Engineer%20CaseWare%20RCM</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row148" class="row_heading level0 row148" >280</th>
      <td id="T_c6c4b_row148_col0" class="data row148 col0" >Junior Site Reliability Engineer Developer</td>
      <td id="T_c6c4b_row148_col1" class="data row148 col1" > This role reports to our Shared Capabilities organization, and you’ll have the opportunity to learn and grow, expanding your knowledge base and getting hands-on… </td>
      <td id="T_c6c4b_row148_col2" class="data row148 col2" >30+ days ago</td>
      <td id="T_c6c4b_row148_col3" class="data row148 col3" >https://ca.indeed.com/jobs?q=Junior%20Site%20Reliability%20Engineer%20Developer%20Royal%20Bank%20of%20Canada</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row149" class="row_heading level0 row149" >278</th>
      <td id="T_c6c4b_row149_col0" class="data row149 col0" >Python Developer (Consultant I)</td>
      <td id="T_c6c4b_row149_col1" class="data row149 col1" > Our delivery model provides market-leading business outcomes using EXL’s proprietary Business EXLerator Framework™, cutting-edge analytics, digital… </td>
      <td id="T_c6c4b_row149_col2" class="data row149 col2" >30+ days ago</td>
      <td id="T_c6c4b_row149_col3" class="data row149 col3" >https://ca.indeed.com/jobs?q=Python%20Developer%20%28Consultant%20I%29%20EXL%20Services</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row150" class="row_heading level0 row150" >277</th>
      <td id="T_c6c4b_row150_col0" class="data row150 col0" >Junior DevOps Engineer</td>
      <td id="T_c6c4b_row150_col1" class="data row150 col1" > This job involves development and maintenance of scalable, secure and highly-available services and infrastructure for online gaming such as player progression,… </td>
      <td id="T_c6c4b_row150_col2" class="data row150 col2" >30+ days ago</td>
      <td id="T_c6c4b_row150_col3" class="data row150 col3" >https://ca.indeed.com/jobs?q=Junior%20DevOps%20Engineer%20Hellbent%20Games</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row151" class="row_heading level0 row151" >276</th>
      <td id="T_c6c4b_row151_col0" class="data row151 col0" >SOC Analyst I</td>
      <td id="T_c6c4b_row151_col1" class="data row151 col1" > Analyze incoming security signals in real time with a balance of accuracy and speed using a variety of forensic tools. </td>
      <td id="T_c6c4b_row151_col2" class="data row151 col2" >30+ days ago</td>
      <td id="T_c6c4b_row151_col3" class="data row151 col3" >https://ca.indeed.com/jobs?q=SOC%20Analyst%20I%20eSentire</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row152" class="row_heading level0 row152" >275</th>
      <td id="T_c6c4b_row152_col0" class="data row152 col0" >Junior Software Developer</td>
      <td id="T_c6c4b_row152_col1" class="data row152 col1" > Financial Risk Analytics is part of the IHS Markit group and provides industry leading risk analytics solutions to sell side institutions within the financial… </td>
      <td id="T_c6c4b_row152_col2" class="data row152 col2" >30+ days ago</td>
      <td id="T_c6c4b_row152_col3" class="data row152 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20S%26P%20Global</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row153" class="row_heading level0 row153" >274</th>
      <td id="T_c6c4b_row153_col0" class="data row153 col0" >Software Engineer I/II</td>
      <td id="T_c6c4b_row153_col1" class="data row153 col1" > You will have opportunities to work on multiple layers of the technology stack, ranging from customer-focused user experience work, building scalable… </td>
      <td id="T_c6c4b_row153_col2" class="data row153 col2" >30+ days ago</td>
      <td id="T_c6c4b_row153_col3" class="data row153 col3" >https://ca.indeed.com/jobs?q=Software%20Engineer%20I/II%20Microsoft</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row154" class="row_heading level0 row154" >261</th>
      <td id="T_c6c4b_row154_col0" class="data row154 col0" >MRI Physicist, Junior</td>
      <td id="T_c6c4b_row154_col1" class="data row154 col1" > The MRI Physicist position is an opportunity to develop applications on this novel system that leverage unique aspects of Synaptive MRI systems to address… </td>
      <td id="T_c6c4b_row154_col2" class="data row154 col2" >30+ days ago</td>
      <td id="T_c6c4b_row154_col3" class="data row154 col3" >https://ca.indeed.com/jobs?q=MRI%20Physicist%2C%20Junior%20Synaptive%20Medical%20Inc.</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row155" class="row_heading level0 row155" >272</th>
      <td id="T_c6c4b_row155_col0" class="data row155 col0" >Junior Hydrogeologist/ Groundwater Modeller</td>
      <td id="T_c6c4b_row155_col1" class="data row155 col1" > + Work within a team of hydrogeologists, geologists, geochemists, and groundwater modellers on a wide variety of projects. </td>
      <td id="T_c6c4b_row155_col2" class="data row155 col2" >30+ days ago</td>
      <td id="T_c6c4b_row155_col3" class="data row155 col3" >https://ca.indeed.com/jobs?q=Junior%20Hydrogeologist/%20Groundwater%20Modeller%20AECOM</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row156" class="row_heading level0 row156" >271</th>
      <td id="T_c6c4b_row156_col0" class="data row156 col0" >JUNIOR MECHANICAL ENGINEER</td>
      <td id="T_c6c4b_row156_col1" class="data row156 col1" > We are seeking a Junior Mechanical Engineer to join our Process and Mine Infrastructure Design team on a full-time basis based in our Sudbury or Mississauga… </td>
      <td id="T_c6c4b_row156_col2" class="data row156 col2" >30+ days ago</td>
      <td id="T_c6c4b_row156_col3" class="data row156 col3" >https://ca.indeed.com/jobs?q=JUNIOR%20MECHANICAL%20ENGINEER%20WSP</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row157" class="row_heading level0 row157" >270</th>
      <td id="T_c6c4b_row157_col0" class="data row157 col0" >Junior Software Developer</td>
      <td id="T_c6c4b_row157_col1" class="data row157 col1" > A subsidiary of LMG Finance, LMG LoanLink is a Canadian owned and operated software company supporting the needs of the finance and insurance (F&amp;I) industry. </td>
      <td id="T_c6c4b_row157_col2" class="data row157 col2" >30+ days ago</td>
      <td id="T_c6c4b_row157_col3" class="data row157 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20LMG%20Finance</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row158" class="row_heading level0 row158" >269</th>
      <td id="T_c6c4b_row158_col0" class="data row158 col0" >Junior Python Developer</td>
      <td id="T_c6c4b_row158_col1" class="data row158 col1" > Production Technology is an umbrella term used to describe the group of people supporting, developing and improving the tools and technologies that artists use… </td>
      <td id="T_c6c4b_row158_col2" class="data row158 col2" >30+ days ago</td>
      <td id="T_c6c4b_row158_col3" class="data row158 col3" >https://ca.indeed.com/jobs?q=Junior%20Python%20Developer%20DNEG</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row159" class="row_heading level0 row159" >268</th>
      <td id="T_c6c4b_row159_col0" class="data row159 col0" >Junior Python Developer</td>
      <td id="T_c6c4b_row159_col1" class="data row159 col1" > As an Juniour Python Developer (internally called ATD) you will perform a variety of tasks to assist the Pipeline Technical Directors (Pipeline TDs) to ensure… </td>
      <td id="T_c6c4b_row159_col2" class="data row159 col2" >30+ days ago</td>
      <td id="T_c6c4b_row159_col3" class="data row159 col3" >https://ca.indeed.com/jobs?q=Junior%20Python%20Developer%20ReDefine</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row160" class="row_heading level0 row160" >266</th>
      <td id="T_c6c4b_row160_col0" class="data row160 col0" >Junior Python Solution Developer for Jeppesen - a Boeing Com...</td>
      <td id="T_c6c4b_row160_col1" class="data row160 col1" >Company Description On behalf of Jeppesen – a Boeing company, we seek a Junior Software Solution Developer to be a part of our experienced team in Montreal,…</td>
      <td id="T_c6c4b_row160_col2" class="data row160 col2" >30+ days ago</td>
      <td id="T_c6c4b_row160_col3" class="data row160 col3" >https://ca.indeed.com/jobs?q=Junior%20Python%20Solution%20Developer%20for%20Jeppesen%20-%20a%20Boeing%20Com...%20Sigma%20Software</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row161" class="row_heading level0 row161" >273</th>
      <td id="T_c6c4b_row161_col0" class="data row161 col0" >Support Center Analyst I</td>
      <td id="T_c6c4b_row161_col1" class="data row161 col1" > Scripting experience in one or more languages (bash, python). The Support Centre is responsible for providing 24x7x365 monitoring and operational support of our… </td>
      <td id="T_c6c4b_row161_col2" class="data row161 col2" >30+ days ago</td>
      <td id="T_c6c4b_row161_col3" class="data row161 col3" >https://ca.indeed.com/jobs?q=Support%20Center%20Analyst%20I%20eSentire</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row162" class="row_heading level0 row162" >260</th>
      <td id="T_c6c4b_row162_col0" class="data row162 col0" >Junior Web Developer</td>
      <td id="T_c6c4b_row162_col1" class="data row162 col1" > You will work with cutting-edge technologies, learn how they are applied in the ecommerce sector, and collaborate extensively with stakeholders and the… </td>
      <td id="T_c6c4b_row162_col2" class="data row162 col2" >30+ days ago</td>
      <td id="T_c6c4b_row162_col3" class="data row162 col3" >https://ca.indeed.com/jobs?q=Junior%20Web%20Developer%20Scribendi</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row163" class="row_heading level0 row163" >238</th>
      <td id="T_c6c4b_row163_col0" class="data row163 col0" >Co-op Junior ASIC Verification Engineer</td>
      <td id="T_c6c4b_row163_col1" class="data row163 col1" > This is a 4-12 months' Full-time (8 months or more preferred), Co-op employment opportunity starting September 2022. Hands on experience in Perl and Python. </td>
      <td id="T_c6c4b_row163_col2" class="data row163 col2" >30+ days ago</td>
      <td id="T_c6c4b_row163_col3" class="data row163 col3" >https://ca.indeed.com/jobs?q=Co-op%20Junior%20ASIC%20Verification%20Engineer%20NETINT%20Technologies%20Inc.</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row164" class="row_heading level0 row164" >258</th>
      <td id="T_c6c4b_row164_col0" class="data row164 col0" >Junior Systems Engineer (New Graduate)</td>
      <td id="T_c6c4b_row164_col1" class="data row164 col1" > Aviya provides expertise in program management, systems, software, mechanical, and hardware engineering to many of the top-tier Aerospace and Defense… </td>
      <td id="T_c6c4b_row164_col2" class="data row164 col2" >30+ days ago</td>
      <td id="T_c6c4b_row164_col3" class="data row164 col3" >https://ca.indeed.com/jobs?q=Junior%20Systems%20Engineer%20%28New%20Graduate%29%20Aviya%20Aerospace%20Systems</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row165" class="row_heading level0 row165" >249</th>
      <td id="T_c6c4b_row165_col0" class="data row165 col0" >Junior DevOps Engineer</td>
      <td id="T_c6c4b_row165_col1" class="data row165 col1" > As a development team member, you will be responsible for ensuring the smooth operation of production systems and development/test environments. </td>
      <td id="T_c6c4b_row165_col2" class="data row165 col2" >30+ days ago</td>
      <td id="T_c6c4b_row165_col3" class="data row165 col3" >https://ca.indeed.com/jobs?q=Junior%20DevOps%20Engineer%20Global%20Relay</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row166" class="row_heading level0 row166" >250</th>
      <td id="T_c6c4b_row166_col0" class="data row166 col0" >Junior Embedded Software Designer</td>
      <td id="T_c6c4b_row166_col1" class="data row166 col1" > Currently, our engineering team is seeking a full-time Junior Embedded Software Developer, to work in a hybrid environment based in our Ottawa ON office. </td>
      <td id="T_c6c4b_row166_col2" class="data row166 col2" >30+ days ago</td>
      <td id="T_c6c4b_row166_col3" class="data row166 col3" >https://ca.indeed.com/jobs?q=Junior%20Embedded%20Software%20Designer%20Allen%20Vanguard</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row167" class="row_heading level0 row167" >251</th>
      <td id="T_c6c4b_row167_col0" class="data row167 col0" >Cloud Engineer, I</td>
      <td id="T_c6c4b_row167_col1" class="data row167 col1" > The perfect candidate will have excellent analysis and troubleshooting skills with attention to detail. Experience with cloud monitoring tools, observing, and… </td>
      <td id="T_c6c4b_row167_col2" class="data row167 col2" >30 days ago</td>
      <td id="T_c6c4b_row167_col3" class="data row167 col3" >https://ca.indeed.com/jobs?q=Cloud%20Engineer%2C%20I%20Zebra%20Technologies</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row168" class="row_heading level0 row168" >252</th>
      <td id="T_c6c4b_row168_col0" class="data row168 col0" >Solutions Architect I - AWS-T3210</td>
      <td id="T_c6c4b_row168_col1" class="data row168 col1" > Bachelor’s degree or foreign equivalent in Computer Science, Engineering, Mathematics, or a related field. 1 year of experience in the job offered or related… </td>
      <td id="T_c6c4b_row168_col2" class="data row168 col2" >30+ days ago</td>
      <td id="T_c6c4b_row168_col3" class="data row168 col3" >https://ca.indeed.com/jobs?q=Solutions%20Architect%20I%20-%20AWS-T3210%20Amazon%20Web%20Services%20Canada%2C%20In</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row169" class="row_heading level0 row169" >253</th>
      <td id="T_c6c4b_row169_col0" class="data row169 col0" >Support Engineer External I (L4)</td>
      <td id="T_c6c4b_row169_col1" class="data row169 col1" > College or university degree, or equivalent industry experience. Three years IT or engineering experience. IT background with a focus on software deployment,… </td>
      <td id="T_c6c4b_row169_col2" class="data row169 col2" >30+ days ago</td>
      <td id="T_c6c4b_row169_col3" class="data row169 col3" >https://ca.indeed.com/jobs?q=Support%20Engineer%20External%20I%20%28L4%29%20Thinkbox%20Software%20Inc.</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row170" class="row_heading level0 row170" >282</th>
      <td id="T_c6c4b_row170_col0" class="data row170 col0" >Junior Software Developer</td>
      <td id="T_c6c4b_row170_col1" class="data row170 col1" > Wedge Networks is seeking candidates to fill a junior software development position on our research and development team, developing software for our network… </td>
      <td id="T_c6c4b_row170_col2" class="data row170 col2" >30+ days ago</td>
      <td id="T_c6c4b_row170_col3" class="data row170 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20Wedge%20Networks</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row171" class="row_heading level0 row171" >254</th>
      <td id="T_c6c4b_row171_col0" class="data row171 col0" >Junior Software Engineer</td>
      <td id="T_c6c4b_row171_col1" class="data row171 col1" > Knowledge and use of several Integrated software development environment SDE tools and scripting languages (python, etc). Knowledge and use of databases. </td>
      <td id="T_c6c4b_row171_col2" class="data row171 col2" >30+ days ago</td>
      <td id="T_c6c4b_row171_col3" class="data row171 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Engineer%20Safran%20Electronics%20%26%20Defense%20Canada</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row172" class="row_heading level0 row172" >248</th>
      <td id="T_c6c4b_row172_col0" class="data row172 col0" >Analyst, Development Infrastructure - Junior</td>
      <td id="T_c6c4b_row172_col1" class="data row172 col1" > The prospective employee will report to the Development Services manager and will be supporting the engineering community in a wide variety of work. </td>
      <td id="T_c6c4b_row172_col2" class="data row172 col2" >30+ days ago</td>
      <td id="T_c6c4b_row172_col3" class="data row172 col3" >https://ca.indeed.com/jobs?q=Analyst%2C%20Development%20Infrastructure%20-%20Junior%20General%20Dynamics%20Missions%20Systems-Canada</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row173" class="row_heading level0 row173" >247</th>
      <td id="T_c6c4b_row173_col0" class="data row173 col0" >Bioinformatics Scientist I</td>
      <td id="T_c6c4b_row173_col1" class="data row173 col1" > We are seeking a highly motivated and experienced Bioinformatics Scientist in the Department of Research and Development. </td>
      <td id="T_c6c4b_row173_col2" class="data row173 col2" >30+ days ago</td>
      <td id="T_c6c4b_row173_col3" class="data row173 col3" >https://ca.indeed.com/jobs?q=Bioinformatics%20Scientist%20I%20Geneseeq%20Technology</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row174" class="row_heading level0 row174" >259</th>
      <td id="T_c6c4b_row174_col0" class="data row174 col0" >Junior Software Engineer</td>
      <td id="T_c6c4b_row174_col1" class="data row174 col1" > Aviya provides expertise in program management, systems, software, mechanical, and hardware engineering to many of the top-tier Aerospace and Defense… </td>
      <td id="T_c6c4b_row174_col2" class="data row174 col2" >30+ days ago</td>
      <td id="T_c6c4b_row174_col3" class="data row174 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Engineer%20Aviya%20Aerospace%20Systems</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row175" class="row_heading level0 row175" >246</th>
      <td id="T_c6c4b_row175_col0" class="data row175 col0" >Jr. Nuage/Cloud 2LS CS Engineer</td>
      <td id="T_c6c4b_row175_col1" class="data row175 col1" > Ability to write scripts at a Unix/Linux level (bash, python). Provide Remote Technical Support (RTS) for the Nuage SDN solutions and associated network… </td>
      <td id="T_c6c4b_row175_col2" class="data row175 col2" >30+ days ago</td>
      <td id="T_c6c4b_row175_col3" class="data row175 col3" >https://ca.indeed.com/jobs?q=Jr.%20Nuage/Cloud%202LS%20CS%20Engineer%20NOKIA</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row176" class="row_heading level0 row176" >244</th>
      <td id="T_c6c4b_row176_col0" class="data row176 col0" >Vancouver | Matchmove Artist | Junior</td>
      <td id="T_c6c4b_row176_col1" class="data row176 col1" > You will be working with artists with a wealth of experience on various productions. It is important to have basic knowledge of Syntheyes and matchmove. </td>
      <td id="T_c6c4b_row176_col2" class="data row176 col2" >30+ days ago</td>
      <td id="T_c6c4b_row176_col3" class="data row176 col3" >https://ca.indeed.com/jobs?q=Vancouver%20%7C%20Matchmove%20Artist%20%7C%20Junior%20Track%20Visual%20Effects</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row177" class="row_heading level0 row177" >243</th>
      <td id="T_c6c4b_row177_col0" class="data row177 col0" >Junior Associate Director, Middle Office Operations, MOV</td>
      <td id="T_c6c4b_row177_col1" class="data row177 col1" > Reporting to the Director, Middle Office and Valuation, you will have an important role in ensuring we provide quality fund administration services to our… </td>
      <td id="T_c6c4b_row177_col2" class="data row177 col2" >30+ days ago</td>
      <td id="T_c6c4b_row177_col3" class="data row177 col3" >https://ca.indeed.com/jobs?q=Junior%20Associate%20Director%2C%20Middle%20Office%20Operations%2C%20MOV%20Mitsubishi%20UFJ%20Fund%20Services</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row178" class="row_heading level0 row178" >242</th>
      <td id="T_c6c4b_row178_col0" class="data row178 col0" >Software Engineer</td>
      <td id="T_c6c4b_row178_col1" class="data row178 col1" > The candidate will work closely with our robotics engineers to productize and maintain Applanix’s software for autonomous vehicle navigation. </td>
      <td id="T_c6c4b_row178_col2" class="data row178 col2" >30+ days ago</td>
      <td id="T_c6c4b_row178_col3" class="data row178 col3" >https://ca.indeed.com/jobs?q=Software%20Engineer%20Applanix</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row179" class="row_heading level0 row179" >240</th>
      <td id="T_c6c4b_row179_col0" class="data row179 col0" >Jr. Product Owner</td>
      <td id="T_c6c4b_row179_col1" class="data row179 col1" > The Jr. Product Owner at Labatt requires a technical expertise to create, deliver and support a product roadmap for our custom internal Ordering tool built on… </td>
      <td id="T_c6c4b_row179_col2" class="data row179 col2" >30+ days ago</td>
      <td id="T_c6c4b_row179_col3" class="data row179 col3" >https://ca.indeed.com/jobs?q=Jr.%20Product%20Owner%20Labatt%20Breweries%20Canada</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row180" class="row_heading level0 row180" >239</th>
      <td id="T_c6c4b_row180_col0" class="data row180 col0" >Software Engineer I - Quartz Core Developer</td>
      <td id="T_c6c4b_row180_col1" class="data row180 col1" > Thousands of developers are using the highly-agile platform to deliver applications to thousands of end users. Linux compute farms on-tap. </td>
      <td id="T_c6c4b_row180_col2" class="data row180 col2" >30+ days ago</td>
      <td id="T_c6c4b_row180_col3" class="data row180 col3" >https://ca.indeed.com/jobs?q=Software%20Engineer%20I%20-%20Quartz%20Core%20Developer%20Bank%20of%20America</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row181" class="row_heading level0 row181" >255</th>
      <td id="T_c6c4b_row181_col0" class="data row181 col0" >Jr. Software Engineer</td>
      <td id="T_c6c4b_row181_col1" class="data row181 col1" > With a strong, active and familial culture, Pub United is the agency’s social club, hosting events as wide reaching as Curling, Trivia Nights and more. </td>
      <td id="T_c6c4b_row181_col2" class="data row181 col2" >30+ days ago</td>
      <td id="T_c6c4b_row181_col3" class="data row181 col3" >https://ca.indeed.com/jobs?q=Jr.%20Software%20Engineer%20Publicis%20Worldwide</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row182" class="row_heading level0 row182" >256</th>
      <td id="T_c6c4b_row182_col0" class="data row182 col0" >Junior Software Engineer</td>
      <td id="T_c6c4b_row182_col1" class="data row182 col1" > Participate in daily standup and other team meetings. Identify, prioritize and execute tasks in the software development life cycle. </td>
      <td id="T_c6c4b_row182_col2" class="data row182 col2" >30+ days ago</td>
      <td id="T_c6c4b_row182_col3" class="data row182 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Engineer%20PointClickCare</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row183" class="row_heading level0 row183" >257</th>
      <td id="T_c6c4b_row183_col0" class="data row183 col0" >Junior Software Developer</td>
      <td id="T_c6c4b_row183_col1" class="data row183 col1" > We encourage cross functional developers to not only learn programming languages, but also the related tools and supporting systems. </td>
      <td id="T_c6c4b_row183_col2" class="data row183 col2" >30+ days ago</td>
      <td id="T_c6c4b_row183_col3" class="data row183 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20Prolucid%20Technologies</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row184" class="row_heading level0 row184" >245</th>
      <td id="T_c6c4b_row184_col0" class="data row184 col0" >Software Engineer In Test I</td>
      <td id="T_c6c4b_row184_col1" class="data row184 col1" > Netomi's Relationship Operating System automatically resolves up to 80% of routine customer service inquiries, decreasing resolution time, and increasing… </td>
      <td id="T_c6c4b_row184_col2" class="data row184 col2" >30+ days ago</td>
      <td id="T_c6c4b_row184_col3" class="data row184 col3" >https://ca.indeed.com/jobs?q=Software%20Engineer%20In%20Test%20I%20Netomi</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row185" class="row_heading level0 row185" >281</th>
      <td id="T_c6c4b_row185_col0" class="data row185 col0" >Jr/Intermediate Software Engineer, ProAV Embedded</td>
      <td id="T_c6c4b_row185_col1" class="data row185 col1" > Design, develop, test, deploy, maintain and improve software. Manage individual project priorities, deadlines and deliverables. Social events and sports teams. </td>
      <td id="T_c6c4b_row185_col2" class="data row185 col2" >30+ days ago</td>
      <td id="T_c6c4b_row185_col3" class="data row185 col3" >https://ca.indeed.com/jobs?q=Jr/Intermediate%20Software%20Engineer%2C%20ProAV%20Embedded%20Evertz%20Microsystems%20Limited</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row186" class="row_heading level0 row186" >142</th>
      <td id="T_c6c4b_row186_col0" class="data row186 col0" >Junior Software Developer</td>
      <td id="T_c6c4b_row186_col1" class="data row186 col1" > You will be required to learn how to leverage HTML5 for use on tablets or developing smartphone apps with any number of development frameworks. </td>
      <td id="T_c6c4b_row186_col2" class="data row186 col2" >30+ days ago</td>
      <td id="T_c6c4b_row186_col3" class="data row186 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20i-Open%20Technologies</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row187" class="row_heading level0 row187" >186</th>
      <td id="T_c6c4b_row187_col0" class="data row187 col0" >Junior Full Stack Developer</td>
      <td id="T_c6c4b_row187_col1" class="data row187 col1" > We are seeking for a Junior Full Stack Developer to join our team who will be responsible for participating in all phases of the development life-cycle,… </td>
      <td id="T_c6c4b_row187_col2" class="data row187 col2" >30+ days ago</td>
      <td id="T_c6c4b_row187_col3" class="data row187 col3" >https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20Steelhaus%20Technologies</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row188" class="row_heading level0 row188" >66</th>
      <td id="T_c6c4b_row188_col0" class="data row188 col0" >Junior Analyst, CRM & Business Intelligence</td>
      <td id="T_c6c4b_row188_col1" class="data row188 col1" > Proficient with data visualization tools such as Tableau or Power BI. Primary point of contact for internal CRM related support tasks (e.g. assisting with data… </td>
      <td id="T_c6c4b_row188_col2" class="data row188 col2" >30+ days ago</td>
      <td id="T_c6c4b_row188_col3" class="data row188 col3" >https://ca.indeed.com/jobs?q=Junior%20Analyst%2C%20CRM%20%26%20Business%20Intelligence%20Vancouver%20Whitecaps%20FC</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row189" class="row_heading level0 row189" >67</th>
      <td id="T_c6c4b_row189_col0" class="data row189 col0" >Junior Quantitative Hydrogeologist</td>
      <td id="T_c6c4b_row189_col1" class="data row189 col1" > Data compilation, reduction, and preliminary interpretation, including water quality results, hydraulic response testing data analysis, water balance model,… </td>
      <td id="T_c6c4b_row189_col2" class="data row189 col2" >30+ days ago</td>
      <td id="T_c6c4b_row189_col3" class="data row189 col3" >https://ca.indeed.com/jobs?q=Junior%20Quantitative%20Hydrogeologist%20GHD</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row190" class="row_heading level0 row190" >68</th>
      <td id="T_c6c4b_row190_col0" class="data row190 col0" >Analyste adjoint(e) bilingue en gestion de données / Junior...</td>
      <td id="T_c6c4b_row190_col1" class="data row190 col1" > Handling the data enrichment of the small to medium data customers by vertically coordinating with customers, Data Quality and IT for new data or current data… </td>
      <td id="T_c6c4b_row190_col2" class="data row190 col2" >30+ days ago</td>
      <td id="T_c6c4b_row190_col3" class="data row190 col3" >https://ca.indeed.com/jobs?q=Analyste%20adjoint%28e%29%20bilingue%20en%20gestion%20de%20donn%C3%A9es%20/%20Junior...%20Equifax</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row191" class="row_heading level0 row191" >69</th>
      <td id="T_c6c4b_row191_col0" class="data row191 col0" >Développeur BI junior</td>
      <td id="T_c6c4b_row191_col1" class="data row191 col1" > Alors que la technologie s’inscrit au cœur de la transformation numérique de nos clients, nous savons que les individus sont au cœur du succès en affaires. </td>
      <td id="T_c6c4b_row191_col2" class="data row191 col2" >30+ days ago</td>
      <td id="T_c6c4b_row191_col3" class="data row191 col3" >https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20BI%20junior%20CGI</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row192" class="row_heading level0 row192" >70</th>
      <td id="T_c6c4b_row192_col0" class="data row192 col0" >Junior AI/Database Administrator</td>
      <td id="T_c6c4b_row192_col1" class="data row192 col1" > Databases – design and implement a database to track and monitor a predetermined set of data points. Excel – track and monitor predetermined set of data points… </td>
      <td id="T_c6c4b_row192_col2" class="data row192 col2" >30+ days ago</td>
      <td id="T_c6c4b_row192_col3" class="data row192 col3" >https://ca.indeed.com/jobs?q=Junior%20AI/Database%20Administrator%20Tetra%20Tech</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row193" class="row_heading level0 row193" >71</th>
      <td id="T_c6c4b_row193_col0" class="data row193 col0" >Oracle Database Administrator Jr</td>
      <td id="T_c6c4b_row193_col1" class="data row193 col1" >Oracle Database Administrator Jr Equisoft, a leading global provider of digital business solutions for the insurance and wealth industries, is actively…</td>
      <td id="T_c6c4b_row193_col2" class="data row193 col2" >30+ days ago</td>
      <td id="T_c6c4b_row193_col3" class="data row193 col3" >https://ca.indeed.com/jobs?q=Oracle%20Database%20Administrator%20Jr%20Equisoft</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row194" class="row_heading level0 row194" >72</th>
      <td id="T_c6c4b_row194_col0" class="data row194 col0" >Junior Pricing Analyst</td>
      <td id="T_c6c4b_row194_col1" class="data row194 col1" > Collects data and maintains the database. Prepares financial and sku analysis reports, analyses margins and competitive market data. </td>
      <td id="T_c6c4b_row194_col2" class="data row194 col2" >30+ days ago</td>
      <td id="T_c6c4b_row194_col3" class="data row194 col3" >https://ca.indeed.com/jobs?q=Junior%20Pricing%20Analyst%20B%C3%A9langer%20UPT</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row195" class="row_heading level0 row195" >73</th>
      <td id="T_c6c4b_row195_col0" class="data row195 col0" >Associate Product Manager, Data</td>
      <td id="T_c6c4b_row195_col1" class="data row195 col1" > Collaborate with stakeholders to define their big data needs for the business. You will help define and execute the vision for Big Data at Lightspeed. </td>
      <td id="T_c6c4b_row195_col2" class="data row195 col2" >30+ days ago</td>
      <td id="T_c6c4b_row195_col3" class="data row195 col3" >https://ca.indeed.com/jobs?q=Associate%20Product%20Manager%2C%20Data%20Lightspeed%20Commerce</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row196" class="row_heading level0 row196" >74</th>
      <td id="T_c6c4b_row196_col0" class="data row196 col0" >Junior Database Analyst</td>
      <td id="T_c6c4b_row196_col1" class="data row196 col1" > Maintain reliability, stability and data integrity of the databases. 1-2 years of experience as a data administrator in SQL server environment. </td>
      <td id="T_c6c4b_row196_col2" class="data row196 col2" >30+ days ago</td>
      <td id="T_c6c4b_row196_col3" class="data row196 col3" >https://ca.indeed.com/jobs?q=Junior%20Database%20Analyst%20HealthHub%20Solutions</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row197" class="row_heading level0 row197" >75</th>
      <td id="T_c6c4b_row197_col0" class="data row197 col0" >Junior Online Marketing Analyst</td>
      <td id="T_c6c4b_row197_col1" class="data row197 col1" > Analytical Skills to interpret data and present recommendations. Ensure data from all sources is accurate and being captured appropriately. </td>
      <td id="T_c6c4b_row197_col2" class="data row197 col2" >30+ days ago</td>
      <td id="T_c6c4b_row197_col3" class="data row197 col3" >https://ca.indeed.com/jobs?q=Junior%20Online%20Marketing%20Analyst%20Core%20Online%20Marketing</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row198" class="row_heading level0 row198" >76</th>
      <td id="T_c6c4b_row198_col0" class="data row198 col0" >Junior Clinical Trials Data Analyst (Hybrid)</td>
      <td id="T_c6c4b_row198_col1" class="data row198 col1" > Process clients’ clinical trials data set. Using our tools you will analyze and mitigate the risk of re-identification for trial participants whose data appears… </td>
      <td id="T_c6c4b_row198_col2" class="data row198 col2" >30+ days ago</td>
      <td id="T_c6c4b_row198_col3" class="data row198 col3" >https://ca.indeed.com/jobs?q=Junior%20Clinical%20Trials%20Data%20Analyst%20%28Hybrid%29%20IQVIA</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row199" class="row_heading level0 row199" >77</th>
      <td id="T_c6c4b_row199_col0" class="data row199 col0" >Jr. Data Scientist</td>
      <td id="T_c6c4b_row199_col1" class="data row199 col1" > Integration with 3rd party API’s for data collection and analysis, including weather data, time-series data, and event-based data sets. </td>
      <td id="T_c6c4b_row199_col2" class="data row199 col2" >30+ days ago</td>
      <td id="T_c6c4b_row199_col3" class="data row199 col3" >https://ca.indeed.com/jobs?q=Jr.%20Data%20Scientist%20SimpTek%20Technologies</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row200" class="row_heading level0 row200" >78</th>
      <td id="T_c6c4b_row200_col0" class="data row200 col0" >Jr. Business Intelligence Developer, Enterprise Analytics</td>
      <td id="T_c6c4b_row200_col1" class="data row200 col1" > Develop ETL procedures, SSIS packages and maintain data flow processes. Advanced understanding of data warehousing concepts and best practices required. </td>
      <td id="T_c6c4b_row200_col2" class="data row200 col2" >30+ days ago</td>
      <td id="T_c6c4b_row200_col3" class="data row200 col3" >https://ca.indeed.com/jobs?q=Jr.%20Business%20Intelligence%20Developer%2C%20Enterprise%20Analytics%20Southlake%20Regional%20Health%20Centre</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row201" class="row_heading level0 row201" >139</th>
      <td id="T_c6c4b_row201_col0" class="data row201 col0" >Conseiller(ère) Junior en plateformes de données et intellig...</td>
      <td id="T_c6c4b_row201_col1" class="data row201 col1" > / Carry out projects with potential returns and economic benefits for Quebecers. / Collaborate on dynamic teams with high-level professionals committed to… </td>
      <td id="T_c6c4b_row201_col2" class="data row201 col2" >30+ days ago</td>
      <td id="T_c6c4b_row201_col3" class="data row201 col3" >https://ca.indeed.com/jobs?q=Conseiller%28%C3%A8re%29%20Junior%20en%20plateformes%20de%20donn%C3%A9es%20et%20intellig...%20Caisse%20de%20d%C3%A9p%C3%B4t%20et%20placement%20du%20Qu%C3%A9bec</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row202" class="row_heading level0 row202" >140</th>
      <td id="T_c6c4b_row202_col0" class="data row202 col0" >Jr. Software Engineer - Lighthouse</td>
      <td id="T_c6c4b_row202_col1" class="data row202 col1" > Work closely with clients to understand key business issues. Gather and analyze requirements to develop impactful recommendations and solutions. </td>
      <td id="T_c6c4b_row202_col2" class="data row202 col2" >30+ days ago</td>
      <td id="T_c6c4b_row202_col3" class="data row202 col3" >https://ca.indeed.com/jobs?q=Jr.%20Software%20Engineer%20-%20Lighthouse%20KPMG</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row203" class="row_heading level0 row203" >141</th>
      <td id="T_c6c4b_row203_col0" class="data row203 col0" >Junior C++ Software Developer</td>
      <td id="T_c6c4b_row203_col1" class="data row203 col1" > We need software engineers who can help us develop and maintain systems that are always online and can handle hundreds of thousands of transactions per second. </td>
      <td id="T_c6c4b_row203_col2" class="data row203 col2" >30+ days ago</td>
      <td id="T_c6c4b_row203_col3" class="data row203 col3" >https://ca.indeed.com/jobs?q=Junior%20C%2B%2B%20Software%20Developer%20S%26P%20Global</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row204" class="row_heading level0 row204" >283</th>
      <td id="T_c6c4b_row204_col0" class="data row204 col0" >Junior DevOps Engineer</td>
      <td id="T_c6c4b_row204_col1" class="data row204 col1" > Proficiency with a scripting language (python/ruby). Generous vacation allotments and flexible working hours. Extended health and wellness spending accounts. </td>
      <td id="T_c6c4b_row204_col2" class="data row204 col2" >30+ days ago</td>
      <td id="T_c6c4b_row204_col3" class="data row204 col3" >https://ca.indeed.com/jobs?q=Junior%20DevOps%20Engineer%20Thrive%20Health</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row205" class="row_heading level0 row205" >65</th>
      <td id="T_c6c4b_row205_col0" class="data row205 col0" >Junior Financial Planning Analyst</td>
      <td id="T_c6c4b_row205_col1" class="data row205 col1" > Performs trend and variance analyses; incorporates data from different areas and synthesizes. This position is responsible for providing updates to daily,… </td>
      <td id="T_c6c4b_row205_col2" class="data row205 col2" >30+ days ago</td>
      <td id="T_c6c4b_row205_col3" class="data row205 col3" >https://ca.indeed.com/jobs?q=Junior%20Financial%20Planning%20Analyst%20UNFI</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row206" class="row_heading level0 row206" >143</th>
      <td id="T_c6c4b_row206_col0" class="data row206 col0" >Programmeur ou Programmeuse Analyste Junior - Télétravail</td>
      <td id="T_c6c4b_row206_col1" class="data row206 col1" > Vous y aurez d’innombrables occasions d'apprendre et de développer des compétences variées en travaillant sur des projets mobilisateurs. </td>
      <td id="T_c6c4b_row206_col2" class="data row206 col2" >30+ days ago</td>
      <td id="T_c6c4b_row206_col3" class="data row206 col3" >https://ca.indeed.com/jobs?q=Programmeur%20ou%20Programmeuse%20Analyste%20Junior%20-%20T%C3%A9l%C3%A9travail%20CIMA%2B</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row207" class="row_heading level0 row207" >64</th>
      <td id="T_c6c4b_row207_col0" class="data row207 col0" >Junior Analyst, Sales Operations & Planning</td>
      <td id="T_c6c4b_row207_col1" class="data row207 col1" > Support sales data and information tracking related to new vendor onboarding. Strong knowledge of Qlikview or similar data analysis / reporting tools. </td>
      <td id="T_c6c4b_row207_col2" class="data row207 col2" >30+ days ago</td>
      <td id="T_c6c4b_row207_col3" class="data row207 col3" >https://ca.indeed.com/jobs?q=Junior%20Analyst%2C%20Sales%20Operations%20%26%20Planning%20UNFI</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row208" class="row_heading level0 row208" >62</th>
      <td id="T_c6c4b_row208_col0" class="data row208 col0" >Junior Sales Data Coordinator</td>
      <td id="T_c6c4b_row208_col1" class="data row208 col1" > Reporting to the National Sales &amp; Marketing Director, the Junior Sales Data Coordinator will be internal link between the pricing analyst and inside sales. </td>
      <td id="T_c6c4b_row208_col2" class="data row208 col2" >30+ days ago</td>
      <td id="T_c6c4b_row208_col3" class="data row208 col3" >https://ca.indeed.com/jobs?q=Junior%20Sales%20Data%20Coordinator%20B%C3%A9langer%20UPT</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row209" class="row_heading level0 row209" >45</th>
      <td id="T_c6c4b_row209_col0" class="data row209 col0" >Program Analyst I – Ajax, ON</td>
      <td id="T_c6c4b_row209_col1" class="data row209 col1" > Support NRC Cost Recovery initiatives by ensuring outstanding claims are tracked, and that the Commercial Manager has all required data to compile claims. </td>
      <td id="T_c6c4b_row209_col2" class="data row209 col2" >30+ days ago</td>
      <td id="T_c6c4b_row209_col3" class="data row209 col3" >https://ca.indeed.com/jobs?q=Program%20Analyst%20I%20%E2%80%93%20Ajax%2C%20ON%20Can-Tech%20Services</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row210" class="row_heading level0 row210" >46</th>
      <td id="T_c6c4b_row210_col0" class="data row210 col0" >Electrical EIT, Data Centres</td>
      <td id="T_c6c4b_row210_col1" class="data row210 col1" > Basic knowledge of power distribution topologies for data centres and familiarity with redundancy concepts; Provide support in preparation of engineering design… </td>
      <td id="T_c6c4b_row210_col2" class="data row210 col2" >30+ days ago</td>
      <td id="T_c6c4b_row210_col3" class="data row210 col3" >https://ca.indeed.com/jobs?q=Electrical%20EIT%2C%20Data%20Centres%20WSP</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row211" class="row_heading level0 row211" >47</th>
      <td id="T_c6c4b_row211_col0" class="data row211 col0" >Business Analyst I, AWS Commerce Platform Business Operation...</td>
      <td id="T_c6c4b_row211_col1" class="data row211 col1" > At least 1+ years of experience with data warehousing and reporting. At least 1+ years of professional working experience in related occupations of Business… </td>
      <td id="T_c6c4b_row211_col2" class="data row211 col2" >30+ days ago</td>
      <td id="T_c6c4b_row211_col3" class="data row211 col3" >https://ca.indeed.com/jobs?q=Business%20Analyst%20I%2C%20AWS%20Commerce%20Platform%20Business%20Operation...%20Amazon%20Dev%20Centre%20Canada%20ULC</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row212" class="row_heading level0 row212" >48</th>
      <td id="T_c6c4b_row212_col0" class="data row212 col0" >Analyst, Client Business I</td>
      <td id="T_c6c4b_row212_col1" class="data row212 col1" > Works with media partners to distill and analyze their data. Experience using sales data (Nielsen, IRi) required. Manages and tracks all media campaigns. </td>
      <td id="T_c6c4b_row212_col2" class="data row212 col2" >30+ days ago</td>
      <td id="T_c6c4b_row212_col3" class="data row212 col3" >https://ca.indeed.com/jobs?q=Analyst%2C%20Client%20Business%20I%20Mosaic%20North%20America</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row213" class="row_heading level0 row213" >49</th>
      <td id="T_c6c4b_row213_col0" class="data row213 col0" >Commercial Financial Analyst I</td>
      <td id="T_c6c4b_row213_col1" class="data row213 col1" > Data management experience and the ability to manage large sets of data and accurate reports. As part of the commercial finance organization, your position will… </td>
      <td id="T_c6c4b_row213_col2" class="data row213 col2" >30+ days ago</td>
      <td id="T_c6c4b_row213_col3" class="data row213 col3" >https://ca.indeed.com/jobs?q=Commercial%20Financial%20Analyst%20I%20Thermo%20Fisher%20Scientific</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row214" class="row_heading level0 row214" >50</th>
      <td id="T_c6c4b_row214_col0" class="data row214 col0" >Junior Data Engineer</td>
      <td id="T_c6c4b_row214_col1" class="data row214 col1" > Build and maintain data collection pipelines. Experience using Python to transform data. Manage data refresh intervals and resolve errors. </td>
      <td id="T_c6c4b_row214_col2" class="data row214 col2" >30+ days ago</td>
      <td id="T_c6c4b_row214_col3" class="data row214 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Engineer%20Valsoft</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row215" class="row_heading level0 row215" >51</th>
      <td id="T_c6c4b_row215_col0" class="data row215 col0" >Junior Business Analyst (remote)</td>
      <td id="T_c6c4b_row215_col1" class="data row215 col1" > Analyzes and evaluates complex data processing systems both current and proposed, translating business area customer information systems requirements into… </td>
      <td id="T_c6c4b_row215_col2" class="data row215 col2" >30+ days ago</td>
      <td id="T_c6c4b_row215_col3" class="data row215 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20%28remote%29%20Software%20International</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row216" class="row_heading level0 row216" >52</th>
      <td id="T_c6c4b_row216_col0" class="data row216 col0" >Junior Data Engineer</td>
      <td id="T_c6c4b_row216_col1" class="data row216 col1" > A foundation in data quality and data governance related activities. In this exciting role, you will help design and build the data platforms needed for optimal… </td>
      <td id="T_c6c4b_row216_col2" class="data row216 col2" >30+ days ago</td>
      <td id="T_c6c4b_row216_col3" class="data row216 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Engineer%20Sobeys</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row217" class="row_heading level0 row217" >53</th>
      <td id="T_c6c4b_row217_col0" class="data row217 col0" >Junior Financial Analyst (8 MONTH CONTRACT)</td>
      <td id="T_c6c4b_row217_col1" class="data row217 col1" > Key contact for Ad-hoc business unit and functional are support (modeling, reporting, analysis, data gathering). Bachelor’s degree or equivalent. </td>
      <td id="T_c6c4b_row217_col2" class="data row217 col2" >30+ days ago</td>
      <td id="T_c6c4b_row217_col3" class="data row217 col3" >https://ca.indeed.com/jobs?q=Junior%20Financial%20Analyst%20%288%20MONTH%20CONTRACT%29%20Cineplex</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row218" class="row_heading level0 row218" >54</th>
      <td id="T_c6c4b_row218_col0" class="data row218 col0" >Junior/Intermediate Advanced Analytics Professional</td>
      <td id="T_c6c4b_row218_col1" class="data row218 col1" > Apply professional experience with data science software to prepare, analyze, and model data. 1+ years of professional work experience in a data analysis… </td>
      <td id="T_c6c4b_row218_col2" class="data row218 col2" >30+ days ago</td>
      <td id="T_c6c4b_row218_col3" class="data row218 col3" >https://ca.indeed.com/jobs?q=Junior/Intermediate%20Advanced%20Analytics%20Professional%20Definity</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row219" class="row_heading level0 row219" >55</th>
      <td id="T_c6c4b_row219_col0" class="data row219 col0" >Junior Data Engineer</td>
      <td id="T_c6c4b_row219_col1" class="data row219 col1" > Work with data engineers, analysts, data scientists, and game developers to determine the data needs of our games. Experience with SQL and database management. </td>
      <td id="T_c6c4b_row219_col2" class="data row219 col2" >30+ days ago</td>
      <td id="T_c6c4b_row219_col3" class="data row219 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Engineer%20Hothead%20Games</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row220" class="row_heading level0 row220" >56</th>
      <td id="T_c6c4b_row220_col0" class="data row220 col0" >Junior Business Analyst</td>
      <td id="T_c6c4b_row220_col1" class="data row220 col1" > Roles &amp; Responsibilities: • Elicits and documents requirements using a variety of methods, such as interviews, document analysis, requirements workshops,… </td>
      <td id="T_c6c4b_row220_col2" class="data row220 col2" >30+ days ago</td>
      <td id="T_c6c4b_row220_col3" class="data row220 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20Pivotree</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row221" class="row_heading level0 row221" >57</th>
      <td id="T_c6c4b_row221_col0" class="data row221 col0" >Business Operations Analyst I, AWS Commerce Platform Busines...</td>
      <td id="T_c6c4b_row221_col1" class="data row221 col1" > At least 1+ years of experience with data warehousing and reporting. At least 1+ years of professional working experience in related occupations of Business… </td>
      <td id="T_c6c4b_row221_col2" class="data row221 col2" >30 days ago</td>
      <td id="T_c6c4b_row221_col3" class="data row221 col3" >https://ca.indeed.com/jobs?q=Business%20Operations%20Analyst%20I%2C%20AWS%20Commerce%20Platform%20Busines...%20Amazon%20Dev%20Centre%20Canada%20ULC</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row222" class="row_heading level0 row222" >58</th>
      <td id="T_c6c4b_row222_col0" class="data row222 col0" >Junior Database Administrator</td>
      <td id="T_c6c4b_row222_col1" class="data row222 col1" > They act as strategic partners with each business unit to help Questrade leverage technology to gain competitive advantage. You have experience with GIT/GitLab. </td>
      <td id="T_c6c4b_row222_col2" class="data row222 col2" >30+ days ago</td>
      <td id="T_c6c4b_row222_col3" class="data row222 col3" >https://ca.indeed.com/jobs?q=Junior%20Database%20Administrator%20Questrade%20Financial%20Group</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row223" class="row_heading level0 row223" >59</th>
      <td id="T_c6c4b_row223_col0" class="data row223 col0" >Mechanical EIT, Data Centres</td>
      <td id="T_c6c4b_row223_col1" class="data row223 col1" > Basic knowledge of building mechanical systems to support data centres (DCs); Reporting directly to the Mechanical Engineering Team Lead or Manager, works under… </td>
      <td id="T_c6c4b_row223_col2" class="data row223 col2" >30+ days ago</td>
      <td id="T_c6c4b_row223_col3" class="data row223 col3" >https://ca.indeed.com/jobs?q=Mechanical%20EIT%2C%20Data%20Centres%20WSP</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row224" class="row_heading level0 row224" >60</th>
      <td id="T_c6c4b_row224_col0" class="data row224 col0" >Financial Analyst I</td>
      <td id="T_c6c4b_row224_col1" class="data row224 col1" > Enters data to sub ledger systems. Gathers audit support data upon request. Prepares and gathers data to support proper transaction reporting. </td>
      <td id="T_c6c4b_row224_col2" class="data row224 col2" >30+ days ago</td>
      <td id="T_c6c4b_row224_col3" class="data row224 col3" >https://ca.indeed.com/jobs?q=Financial%20Analyst%20I%20BGIS</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row225" class="row_heading level0 row225" >61</th>
      <td id="T_c6c4b_row225_col0" class="data row225 col0" >UM - Junior Analyst, Decision Sciences</td>
      <td id="T_c6c4b_row225_col1" class="data row225 col1" > Support development of custom data models and algorithms to apply to data sets. Assess the effectiveness and accuracy of new data sources with a understanding… </td>
      <td id="T_c6c4b_row225_col2" class="data row225 col2" >30+ days ago</td>
      <td id="T_c6c4b_row225_col3" class="data row225 col3" >https://ca.indeed.com/jobs?q=UM%20-%20Junior%20Analyst%2C%20Decision%20Sciences%20IPG%20Mediabrands</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row226" class="row_heading level0 row226" >63</th>
      <td id="T_c6c4b_row226_col0" class="data row226 col0" >Junior Project Finance Analyst (Montreal or Laval)</td>
      <td id="T_c6c4b_row226_col1" class="data row226 col1" > 0 - 5 years of financial/data analysis experience. The primary focuses of this position include: evaluating construction job cost, data reporting/analysis for… </td>
      <td id="T_c6c4b_row226_col2" class="data row226 col2" >30+ days ago</td>
      <td id="T_c6c4b_row226_col3" class="data row226 col3" >https://ca.indeed.com/jobs?q=Junior%20Project%20Finance%20Analyst%20%28Montreal%20or%20Laval%29%20Kiewit%20Corporation</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row227" class="row_heading level0 row227" >144</th>
      <td id="T_c6c4b_row227_col0" class="data row227 col0" >Junior Technical Analyst (4 Month Summer Contracts)</td>
      <td id="T_c6c4b_row227_col1" class="data row227 col1" > The successful candidate will provide maintenance and support for various aspects for the Tolling process covering roadside equipment, Intelligent Transport… </td>
      <td id="T_c6c4b_row227_col2" class="data row227 col2" >30+ days ago</td>
      <td id="T_c6c4b_row227_col3" class="data row227 col3" >https://ca.indeed.com/jobs?q=Junior%20Technical%20Analyst%20%284%20Month%20Summer%20Contracts%29%20407%20ETR</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row228" class="row_heading level0 row228" >145</th>
      <td id="T_c6c4b_row228_col0" class="data row228 col0" >Junior Integration Analyst</td>
      <td id="T_c6c4b_row228_col1" class="data row228 col1" > Your role will be to help develop applications, technological options and proposed solutions, from project design to implementation, mainly in production data… </td>
      <td id="T_c6c4b_row228_col2" class="data row228 col2" >30+ days ago</td>
      <td id="T_c6c4b_row228_col3" class="data row228 col3" >https://ca.indeed.com/jobs?q=Junior%20Integration%20Analyst%20BBA</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row229" class="row_heading level0 row229" >146</th>
      <td id="T_c6c4b_row229_col0" class="data row229 col0" >Junior Developer Analyst</td>
      <td id="T_c6c4b_row229_col1" class="data row229 col1" > Looking for junior/intermediate candidates getting started in their career and have room to grow - Specifically (2 – 5 years of experience). </td>
      <td id="T_c6c4b_row229_col2" class="data row229 col2" >30+ days ago</td>
      <td id="T_c6c4b_row229_col3" class="data row229 col3" >https://ca.indeed.com/jobs?q=Junior%20Developer%20Analyst%20Fujitsu</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row230" class="row_heading level0 row230" >169</th>
      <td id="T_c6c4b_row230_col0" class="data row230 col0" >Junior Software Engineer</td>
      <td id="T_c6c4b_row230_col1" class="data row230 col1" > We are currently looking for a Junior Software Engineer (JSE) to join our team at our Markham, Ontario, CANADA location. Familiarity with test automation tools. </td>
      <td id="T_c6c4b_row230_col2" class="data row230 col2" >30+ days ago</td>
      <td id="T_c6c4b_row230_col3" class="data row230 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Engineer%20Optima%20Tele.com%2C%20Inc.</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row231" class="row_heading level0 row231" >170</th>
      <td id="T_c6c4b_row231_col0" class="data row231 col0" >Junior Power Analyst</td>
      <td id="T_c6c4b_row231_col1" class="data row231 col1" > Dynasty Power is looking for a highly motivated, self-sufficient and enthusiastic individual who has a strong desire to grow within the company to fill a new… </td>
      <td id="T_c6c4b_row231_col2" class="data row231 col2" >30+ days ago</td>
      <td id="T_c6c4b_row231_col3" class="data row231 col3" >https://ca.indeed.com/jobs?q=Junior%20Power%20Analyst%20Dynasty%20Power%20Inc.</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row232" class="row_heading level0 row232" >171</th>
      <td id="T_c6c4b_row232_col0" class="data row232 col0" >Junior Software Developer</td>
      <td id="T_c6c4b_row232_col1" class="data row232 col1" > WSP is one of the world's leading professional services firms. Our purpose is to future proof our cities and environments. A day in the life: </td>
      <td id="T_c6c4b_row232_col2" class="data row232 col2" >30+ days ago</td>
      <td id="T_c6c4b_row232_col3" class="data row232 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20WSP</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row233" class="row_heading level0 row233" >172</th>
      <td id="T_c6c4b_row233_col0" class="data row233 col0" >Junior Oracle DBA</td>
      <td id="T_c6c4b_row233_col1" class="data row233 col1" > Defines and administers data base organization, standards, controls, procedures, and documentation. Provides experienced technical consulting in the definition,… </td>
      <td id="T_c6c4b_row233_col2" class="data row233 col2" >30+ days ago</td>
      <td id="T_c6c4b_row233_col3" class="data row233 col3" >https://ca.indeed.com/jobs?q=Junior%20Oracle%20DBA%20AstraNorth</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row234" class="row_heading level0 row234" >173</th>
      <td id="T_c6c4b_row234_col0" class="data row234 col0" >Salesforce Technologist - Junior</td>
      <td id="T_c6c4b_row234_col1" class="data row234 col1" > You will be supporting our customers through a wide range of scenarios including defining business process, analyzing requirements, implementing in the… </td>
      <td id="T_c6c4b_row234_col2" class="data row234 col2" >30+ days ago</td>
      <td id="T_c6c4b_row234_col3" class="data row234 col3" >https://ca.indeed.com/jobs?q=Salesforce%20Technologist%20-%20Junior%20Procom</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row235" class="row_heading level0 row235" >174</th>
      <td id="T_c6c4b_row235_col0" class="data row235 col0" >Junior Programmer Analyst</td>
      <td id="T_c6c4b_row235_col1" class="data row235 col1" > Successful businesses understand their customers and their competitors. World, as well as to all levels of government (from federal to municipal in Canada). </td>
      <td id="T_c6c4b_row235_col2" class="data row235 col2" >30+ days ago</td>
      <td id="T_c6c4b_row235_col3" class="data row235 col3" >https://ca.indeed.com/jobs?q=Junior%20Programmer%20Analyst%20Advanis</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row236" class="row_heading level0 row236" >175</th>
      <td id="T_c6c4b_row236_col0" class="data row236 col0" >Junior Web Developer</td>
      <td id="T_c6c4b_row236_col1" class="data row236 col1" > You will work closely with our CTO on various projects, ranging from prototyping, developing and testing new product &amp; service ideas to updates and changes to… </td>
      <td id="T_c6c4b_row236_col2" class="data row236 col2" >30+ days ago</td>
      <td id="T_c6c4b_row236_col3" class="data row236 col3" >https://ca.indeed.com/jobs?q=Junior%20Web%20Developer%20Outshinery%20Creative</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row237" class="row_heading level0 row237" >176</th>
      <td id="T_c6c4b_row237_col0" class="data row237 col0" >Junior Web Developer</td>
      <td id="T_c6c4b_row237_col1" class="data row237 col1" > Provide programming supports to lead developer on an Seed to Sale Cannabis Enterprise Software project. Develop documentation and assistance tools to support… </td>
      <td id="T_c6c4b_row237_col2" class="data row237 col2" >30+ days ago</td>
      <td id="T_c6c4b_row237_col3" class="data row237 col3" >https://ca.indeed.com/jobs?q=Junior%20Web%20Developer%20Trellis</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row238" class="row_heading level0 row238" >177</th>
      <td id="T_c6c4b_row238_col0" class="data row238 col0" >Junior Software Developer</td>
      <td id="T_c6c4b_row238_col1" class="data row238 col1" > Through your knowledge of industry-proven technologies and methodologies (see below), you will be responsible for delivering high-quality, efficient code as… </td>
      <td id="T_c6c4b_row238_col2" class="data row238 col2" >30+ days ago</td>
      <td id="T_c6c4b_row238_col3" class="data row238 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20COVNEX</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row239" class="row_heading level0 row239" >178</th>
      <td id="T_c6c4b_row239_col0" class="data row239 col0" >Junior Developer/Programmer</td>
      <td id="T_c6c4b_row239_col1" class="data row239 col1" > Maintain software design consistency, aesthetics, and functionality of web application pages, communications systems, and data processing. </td>
      <td id="T_c6c4b_row239_col2" class="data row239 col2" >30+ days ago</td>
      <td id="T_c6c4b_row239_col3" class="data row239 col3" >https://ca.indeed.com/jobs?q=Junior%20Developer/Programmer%20SimplyCast</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row240" class="row_heading level0 row240" >179</th>
      <td id="T_c6c4b_row240_col0" class="data row240 col0" >Junior/Intermediate Hydrogeologist</td>
      <td id="T_c6c4b_row240_col1" class="data row240 col1" > As a Junior/Intermediate Hydrogeologist, you would be involved in a variety of projects related to hydrogeologic assessment, groundwater supply development, and… </td>
      <td id="T_c6c4b_row240_col2" class="data row240 col2" >30+ days ago</td>
      <td id="T_c6c4b_row240_col3" class="data row240 col3" >https://ca.indeed.com/jobs?q=Junior/Intermediate%20Hydrogeologist%20Stantec</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row241" class="row_heading level0 row241" >181</th>
      <td id="T_c6c4b_row241_col0" class="data row241 col0" >Junior Forecast Analyst</td>
      <td id="T_c6c4b_row241_col1" class="data row241 col1" > Reporting to the Director of Operations Support, the Junior Forecast Analyst contributes to Arctic Glacier’s success by developing accurate demand forecasts. </td>
      <td id="T_c6c4b_row241_col2" class="data row241 col2" >30+ days ago</td>
      <td id="T_c6c4b_row241_col3" class="data row241 col3" >https://ca.indeed.com/jobs?q=Junior%20Forecast%20Analyst%20Arctic%20Glacier</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row242" class="row_heading level0 row242" >183</th>
      <td id="T_c6c4b_row242_col0" class="data row242 col0" >Junior QA Developer [#3998]</td>
      <td id="T_c6c4b_row242_col1" class="data row242 col1" > Within an Agile development team (Scrum), the QA Developer is responsible for the development of test cases, the implementation and maintenance of automated and… </td>
      <td id="T_c6c4b_row242_col2" class="data row242 col2" >30+ days ago</td>
      <td id="T_c6c4b_row242_col3" class="data row242 col3" >https://ca.indeed.com/jobs?q=Junior%20QA%20Developer%20%5B%233998%5D%20Alteo</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row243" class="row_heading level0 row243" >184</th>
      <td id="T_c6c4b_row243_col0" class="data row243 col0" >Junior Full Stack Developer</td>
      <td id="T_c6c4b_row243_col1" class="data row243 col1" > Markdale Financial Management is looking for a part-time Junior Full Stack Web Developer to join our team. Currently an undergrad in Computer Science. </td>
      <td id="T_c6c4b_row243_col2" class="data row243 col2" >30+ days ago</td>
      <td id="T_c6c4b_row243_col3" class="data row243 col3" >https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20Markdale%20Financial%20Management</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row244" class="row_heading level0 row244" >185</th>
      <td id="T_c6c4b_row244_col0" class="data row244 col0" >Junior Full Stack Developer</td>
      <td id="T_c6c4b_row244_col1" class="data row244 col1" > As a Junior Full Stack Developer with Random Acronym (a division of Integrated Sustainability), your experience and skills will enable you to make a difference… </td>
      <td id="T_c6c4b_row244_col2" class="data row244 col2" >30+ days ago</td>
      <td id="T_c6c4b_row244_col3" class="data row244 col3" >https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20Integrated%20Sustainability</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row245" class="row_heading level0 row245" >168</th>
      <td id="T_c6c4b_row245_col0" class="data row245 col0" >Junior Developer</td>
      <td id="T_c6c4b_row245_col1" class="data row245 col1" > The University of Manitoba is a driving force of innovation, discovery and advancement. Our momentum is propelled by our campus community – UM faculty, staff… </td>
      <td id="T_c6c4b_row245_col2" class="data row245 col2" >30+ days ago</td>
      <td id="T_c6c4b_row245_col3" class="data row245 col3" >https://ca.indeed.com/jobs?q=Junior%20Developer%20University%20of%20Manitoba</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row246" class="row_heading level0 row246" >166</th>
      <td id="T_c6c4b_row246_col0" class="data row246 col0" >Junior Developer</td>
      <td id="T_c6c4b_row246_col1" class="data row246 col1" > Competitive wages, amazing benefits, yearly performance-based bonuses, RRSP matching, health and wellness programs, a literal award-winning culture, parental… </td>
      <td id="T_c6c4b_row246_col2" class="data row246 col2" >30+ days ago</td>
      <td id="T_c6c4b_row246_col3" class="data row246 col3" >https://ca.indeed.com/jobs?q=Junior%20Developer%20CARFAX%20Canada</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row247" class="row_heading level0 row247" >165</th>
      <td id="T_c6c4b_row247_col0" class="data row247 col0" >Junior Trader</td>
      <td id="T_c6c4b_row247_col1" class="data row247 col1" > And we swear by that every single day. They efficiently and accurately process client trade requests according to the directions received from clients. </td>
      <td id="T_c6c4b_row247_col2" class="data row247 col2" >30+ days ago</td>
      <td id="T_c6c4b_row247_col3" class="data row247 col3" >https://ca.indeed.com/jobs?q=Junior%20Trader%20Questrade%20Financial%20Group</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row248" class="row_heading level0 row248" >147</th>
      <td id="T_c6c4b_row248_col0" class="data row248 col0" >Junior Drupal Developer (Remote Friendly)</td>
      <td id="T_c6c4b_row248_col1" class="data row248 col1" > Acro Media is looking for a Drupal Software Developer to develop Drupal 8 and Commerce builds. If you’re desperate to break free from that office life where you… </td>
      <td id="T_c6c4b_row248_col2" class="data row248 col2" >30+ days ago</td>
      <td id="T_c6c4b_row248_col3" class="data row248 col3" >https://ca.indeed.com/jobs?q=Junior%20Drupal%20Developer%20%28Remote%20Friendly%29%20Acro%20Media</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row249" class="row_heading level0 row249" >148</th>
      <td id="T_c6c4b_row249_col0" class="data row249 col0" >Jr. Web Application Tester</td>
      <td id="T_c6c4b_row249_col1" class="data row249 col1" > For more than 40 years, Vistek has been a Canadian Success story, retailing photo, video and digital professional equipment solutions. Basic knowledge of T-SQL. </td>
      <td id="T_c6c4b_row249_col2" class="data row249 col2" >30+ days ago</td>
      <td id="T_c6c4b_row249_col3" class="data row249 col3" >https://ca.indeed.com/jobs?q=Jr.%20Web%20Application%20Tester%20Vistek%20LTD</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row250" class="row_heading level0 row250" >149</th>
      <td id="T_c6c4b_row250_col0" class="data row250 col0" >QA Analyst / Junior Software Engineer – Web/iOS</td>
      <td id="T_c6c4b_row250_col1" class="data row250 col1" > ARTERNAL CRM (Customer Relational Management) is an up-and-coming player in the technology of the contemporary art scene! Define and maintain test plans. </td>
      <td id="T_c6c4b_row250_col2" class="data row250 col2" >30+ days ago</td>
      <td id="T_c6c4b_row250_col3" class="data row250 col3" >https://ca.indeed.com/jobs?q=QA%20Analyst%20/%20Junior%20Software%20Engineer%20%E2%80%93%20Web/iOS%20Arternal</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row251" class="row_heading level0 row251" >150</th>
      <td id="T_c6c4b_row251_col0" class="data row251 col0" >Jr. Network Administrator</td>
      <td id="T_c6c4b_row251_col1" class="data row251 col1" > Able to provide tech support in/out office. Might occasionally have to give technical support to clients. Should be able to work after work hours (Saturdays… </td>
      <td id="T_c6c4b_row251_col2" class="data row251 col2" >30+ days ago</td>
      <td id="T_c6c4b_row251_col3" class="data row251 col3" >https://ca.indeed.com/jobs?q=Jr.%20Network%20Administrator%20BreezeMaxWeb</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row252" class="row_heading level0 row252" >151</th>
      <td id="T_c6c4b_row252_col0" class="data row252 col0" >Jr .Net</td>
      <td id="T_c6c4b_row252_col1" class="data row252 col1" > Strong on SQL server programming. T4 hire with option to train can be considered. 1 to 2 years of experience. Strong on SQL server programming. </td>
      <td id="T_c6c4b_row252_col2" class="data row252 col2" >30+ days ago</td>
      <td id="T_c6c4b_row252_col3" class="data row252 col3" >https://ca.indeed.com/jobs?q=Jr%20.Net%20Virtusa</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row253" class="row_heading level0 row253" >152</th>
      <td id="T_c6c4b_row253_col0" class="data row253 col0" >Junior Software Developer; AUI</td>
      <td id="T_c6c4b_row253_col1" class="data row253 col1" > We offer product record keeping and distribution systems, supporting a full range of investments, accounts and regulatory bodies. </td>
      <td id="T_c6c4b_row253_col2" class="data row253 col2" >30+ days ago</td>
      <td id="T_c6c4b_row253_col3" class="data row253 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%3B%20AUI%20RPM%20TECHNOLOGIES%20CORP</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row254" class="row_heading level0 row254" >153</th>
      <td id="T_c6c4b_row254_col0" class="data row254 col0" >Junior Devops Engineer</td>
      <td id="T_c6c4b_row254_col1" class="data row254 col1" > Want to join a small group of forward-thinking developers working in an agile environment? Scribendi, a leading online language services company, seeks a Junior… </td>
      <td id="T_c6c4b_row254_col2" class="data row254 col2" >30+ days ago</td>
      <td id="T_c6c4b_row254_col3" class="data row254 col3" >https://ca.indeed.com/jobs?q=Junior%20Devops%20Engineer%20Scribendi</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row255" class="row_heading level0 row255" >154</th>
      <td id="T_c6c4b_row255_col0" class="data row255 col0" >Junior Asset Management Consultant and Data Analyst</td>
      <td id="T_c6c4b_row255_col1" class="data row255 col1" > Junior Asset Management Consultant and Data Analyst. Our focus continues to ensure that our clients receive high-quality, innovative, practical and cost… </td>
      <td id="T_c6c4b_row255_col2" class="data row255 col2" >30+ days ago</td>
      <td id="T_c6c4b_row255_col3" class="data row255 col3" >https://ca.indeed.com/jobs?q=Junior%20Asset%20Management%20Consultant%20and%20Data%20Analyst%20GM%20BluePlan%20Engineering</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row256" class="row_heading level0 row256" >187</th>
      <td id="T_c6c4b_row256_col0" class="data row256 col0" >Industrial Engineer I</td>
      <td id="T_c6c4b_row256_col1" class="data row256 col1" > The Industrial Engineer I drives continuous improvement in all areas of the business. You, as an Industrial Engineer I, will work with multiple departments to… </td>
      <td id="T_c6c4b_row256_col2" class="data row256 col2" >30+ days ago</td>
      <td id="T_c6c4b_row256_col3" class="data row256 col3" >https://ca.indeed.com/jobs?q=Industrial%20Engineer%20I%20SCC%20UPS%20SCS%2C%20Inc.</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row257" class="row_heading level0 row257" >155</th>
      <td id="T_c6c4b_row257_col0" class="data row257 col0" >Développeur(se) Junior, Intelligence d'affaires</td>
      <td id="T_c6c4b_row257_col1" class="data row257 col1" > / Carry out projects with potential returns and economic benefits for Quebecers. / Collaborate on dynamic teams with high-level professionals committed to… </td>
      <td id="T_c6c4b_row257_col2" class="data row257 col2" >30+ days ago</td>
      <td id="T_c6c4b_row257_col3" class="data row257 col3" >https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%28se%29%20Junior%2C%20Intelligence%20d%27affaires%20Caisse%20de%20d%C3%A9p%C3%B4t%20et%20placement%20du%20Qu%C3%A9bec</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row258" class="row_heading level0 row258" >157</th>
      <td id="T_c6c4b_row258_col0" class="data row258 col0" >Analyste d'affaires, junior</td>
      <td id="T_c6c4b_row258_col1" class="data row258 col1" > / Carry out projects with potential returns and economic benefits for Quebecers. / Collaborate on dynamic teams with high-level professionals committed to… </td>
      <td id="T_c6c4b_row258_col2" class="data row258 col2" >30+ days ago</td>
      <td id="T_c6c4b_row258_col3" class="data row258 col3" >https://ca.indeed.com/jobs?q=Analyste%20d%27affaires%2C%20junior%20Caisse%20de%20d%C3%A9p%C3%B4t%20et%20placement%20du%20Qu%C3%A9bec</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row259" class="row_heading level0 row259" >158</th>
      <td id="T_c6c4b_row259_col0" class="data row259 col0" >Junior Lead Generator</td>
      <td id="T_c6c4b_row259_col1" class="data row259 col1" > ATS is the industry leader in using technology to revolutionize engineering and design processes. Learn and become the expert on data sources, uses, and ways to… </td>
      <td id="T_c6c4b_row259_col2" class="data row259 col2" >30+ days ago</td>
      <td id="T_c6c4b_row259_col3" class="data row259 col3" >https://ca.indeed.com/jobs?q=Junior%20Lead%20Generator%20Allied%20Technical%20Solutions</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row260" class="row_heading level0 row260" >159</th>
      <td id="T_c6c4b_row260_col0" class="data row260 col0" >JUNIOR SOFTWARE ENGINEER</td>
      <td id="T_c6c4b_row260_col1" class="data row260 col1" > Reporting to the IT Manager of Applications, the Junior Software Engineer will work on a close-knit team using agile development practices to develop OEC’s next… </td>
      <td id="T_c6c4b_row260_col2" class="data row260 col2" >30+ days ago</td>
      <td id="T_c6c4b_row260_col3" class="data row260 col3" >https://ca.indeed.com/jobs?q=JUNIOR%20SOFTWARE%20ENGINEER%20OEC%20Group%20%28Canada%29</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row261" class="row_heading level0 row261" >161</th>
      <td id="T_c6c4b_row261_col0" class="data row261 col0" >Junior Capital Accountant</td>
      <td id="T_c6c4b_row261_col1" class="data row261 col1" > We are currently looking for a motivated Junior Capital Accountant to join our Finance team within the Midstream Infrastructure division of our organization. </td>
      <td id="T_c6c4b_row261_col2" class="data row261 col2" >30+ days ago</td>
      <td id="T_c6c4b_row261_col3" class="data row261 col3" >https://ca.indeed.com/jobs?q=Junior%20Capital%20Accountant%20SECURE%20Energy%20Services%20Inc.</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row262" class="row_heading level0 row262" >162</th>
      <td id="T_c6c4b_row262_col0" class="data row262 col0" >Full Stack Engineer (Junior)</td>
      <td id="T_c6c4b_row262_col1" class="data row262 col1" > As a FullStack Engineer, you will be responsible for implementing real-time and highly scalable and distributed software for our Call Center As A Service (CCAAS… </td>
      <td id="T_c6c4b_row262_col2" class="data row262 col2" >30+ days ago</td>
      <td id="T_c6c4b_row262_col3" class="data row262 col3" >https://ca.indeed.com/jobs?q=Full%20Stack%20Engineer%20%28Junior%29%20Sangoma</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row263" class="row_heading level0 row263" >163</th>
      <td id="T_c6c4b_row263_col0" class="data row263 col0" >Technology Analyst I</td>
      <td id="T_c6c4b_row263_col1" class="data row263 col1" > Jobs by Category: Technology Solutions. You will be part of a future friendly national team. One that lives the TELUS values at its core while delivering our… </td>
      <td id="T_c6c4b_row263_col2" class="data row263 col2" >30+ days ago</td>
      <td id="T_c6c4b_row263_col3" class="data row263 col3" >https://ca.indeed.com/jobs?q=Technology%20Analyst%20I%20TELUS</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row264" class="row_heading level0 row264" >164</th>
      <td id="T_c6c4b_row264_col0" class="data row264 col0" >Junior Full Stack Developer</td>
      <td id="T_c6c4b_row264_col1" class="data row264 col1" > We deliver solutions to customers in markets ranging from Medical Devices, Aerospace &amp; Defence, Nuclear &amp; Energy, Transportation, and Advanced Manufacturing. </td>
      <td id="T_c6c4b_row264_col2" class="data row264 col2" >30+ days ago</td>
      <td id="T_c6c4b_row264_col3" class="data row264 col3" >https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20Prolucid%20Technologies</td>
    </tr>
    <tr>
      <th id="T_c6c4b_level0_row265" class="row_heading level0 row265" >156</th>
      <td id="T_c6c4b_row265_col0" class="data row265 col0" >Jr. Data/Reporting Analyst</td>
      <td id="T_c6c4b_row265_col1" class="data row265 col1" > The Jr Data/Reporting Analyst will be responsible for maintaining our clients Data and Reporting needs on a Weekly/Monthly bases. </td>
      <td id="T_c6c4b_row265_col2" class="data row265 col2" >30+ days ago</td>
      <td id="T_c6c4b_row265_col3" class="data row265 col3" >https://ca.indeed.com/jobs?q=Jr.%20Data/Reporting%20Analyst%20Scarsin</td>
    </tr>
  </tbody>
</table>





```python

```

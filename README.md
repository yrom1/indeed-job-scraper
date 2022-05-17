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





<table id="T_c71c4">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_c71c4_level0_col0" class="col_heading level0 col0" >titles</th>
      <th id="T_c71c4_level0_col1" class="col_heading level0 col1" >jobSnippets</th>
      <th id="T_c71c4_level0_col2" class="col_heading level0 col2" >dates</th>
      <th id="T_c71c4_level0_col3" class="col_heading level0 col3" >links</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_c71c4_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_c71c4_row0_col0" class="data row0 col0" >Data Scientist I</td>
      <td id="T_c71c4_row0_col1" class="data row0 col1" > Experience in spatial-temporal data analysis, data manipulation, and interpretation. Work with peer developers to ensure data solutions are consistent and… </td>
      <td id="T_c71c4_row0_col2" class="data row0 col2" >Just posted</td>
      <td id="T_c71c4_row0_col3" class="data row0 col3" >https://ca.indeed.com/jobs?q=Data%20Scientist%20I%20Global%20Spatial%20Technology%20Solutions%20Inc.</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_c71c4_row1_col0" class="data row1 col0" >Junior Data Scientist, Klarna Media Lab</td>
      <td id="T_c71c4_row1_col1" class="data row1 col1" > Have strong hands-on skills in data wrangling over massive datasets using distributed computing platform. Research, innovate and develop cutting-edge machine… </td>
      <td id="T_c71c4_row1_col2" class="data row1 col2" >Today</td>
      <td id="T_c71c4_row1_col3" class="data row1 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Scientist%2C%20Klarna%20Media%20Lab%20Klarna</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row2" class="row_heading level0 row2" >108</th>
      <td id="T_c71c4_row2_col0" class="data row2 col0" >Junior Software Developer (Vancouver)</td>
      <td id="T_c71c4_row2_col1" class="data row2 col1" > Software Engineering or Computer Science university degree; or. Related University Degree (math, physics etc) with software development experience. </td>
      <td id="T_c71c4_row2_col2" class="data row2 col2" >Just posted</td>
      <td id="T_c71c4_row2_col3" class="data row2 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20%28Vancouver%29%20Eigen%20Development%20Ltd.</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row3" class="row_heading level0 row3" >107</th>
      <td id="T_c71c4_row3_col0" class="data row3 col0" >Junior Software Developer</td>
      <td id="T_c71c4_row3_col1" class="data row3 col1" > Analyzing requirements, and designing, developing, and testing solutions. Adhere to software development practices through design and code reviews. </td>
      <td id="T_c71c4_row3_col2" class="data row3 col2" >Today</td>
      <td id="T_c71c4_row3_col3" class="data row3 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20Fieldshare</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row4" class="row_heading level0 row4" >106</th>
      <td id="T_c71c4_row4_col0" class="data row4 col0" >Part-time Low Code Junior Developer Experience@siemens</td>
      <td id="T_c71c4_row4_col1" class="data row4 col1" > Kick start your career journey! Experience@Siemens is an exciting opportunity for new Graduates from college or university to transition from academic to the… </td>
      <td id="T_c71c4_row4_col2" class="data row4 col2" >Today</td>
      <td id="T_c71c4_row4_col3" class="data row4 col3" >https://ca.indeed.com/jobs?q=Part-time%20Low%20Code%20Junior%20Developer%20Experience%40siemens%20Siemens%20Canada%20Limited</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row5" class="row_heading level0 row5" >223</th>
      <td id="T_c71c4_row5_col0" class="data row5 col0" >Nauczyciel online - Python i Scratch</td>
      <td id="T_c71c4_row5_col1" class="data row5 col1" > Jako doświadczony i zaawansowany start-up rozwijamy się wykładniczo w ponad 40 krajach, jednocześnie kształcąc ponad 15,000 dzieci na całym świecie. </td>
      <td id="T_c71c4_row5_col2" class="data row5 col2" >Hiring ongoing</td>
      <td id="T_c71c4_row5_col3" class="data row5 col3" >https://ca.indeed.com/jobs?q=Nauczyciel%20online%20-%20Python%20i%20Scratch%20Kodland</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row6" class="row_heading level0 row6" >224</th>
      <td id="T_c71c4_row6_col0" class="data row6 col0" >Application Release Engineer I</td>
      <td id="T_c71c4_row6_col1" class="data row6 col1" > Provides integrated guidance across business, product and technology organizations to provide best practices for releasing software — from how the software is… </td>
      <td id="T_c71c4_row6_col2" class="data row6 col2" >Today</td>
      <td id="T_c71c4_row6_col3" class="data row6 col3" >https://ca.indeed.com/jobs?q=Application%20Release%20Engineer%20I%20TD%20Bank</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row7" class="row_heading level0 row7" >2</th>
      <td id="T_c71c4_row7_col0" class="data row7 col0" >Junior Data Analyst</td>
      <td id="T_c71c4_row7_col1" class="data row7 col1" > Extracting data for feasibility studies, raw data pulls, sample pulls and data appends. Performing data conversion, data cleansing, data masking, de… </td>
      <td id="T_c71c4_row7_col2" class="data row7 col2" >Active 1 day ago</td>
      <td id="T_c71c4_row7_col3" class="data row7 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20Delvinia</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row8" class="row_heading level0 row8" >3</th>
      <td id="T_c71c4_row8_col0" class="data row8 col0" >Junior - Business Analyst (SDLC/UML)</td>
      <td id="T_c71c4_row8_col1" class="data row8 col1" > DLT Labs is built by pioneers with experience across a wide variety of sectors of business, technology, and distributed application architecture, development,… </td>
      <td id="T_c71c4_row8_col2" class="data row8 col2" >Active 1 day ago</td>
      <td id="T_c71c4_row8_col3" class="data row8 col3" >https://ca.indeed.com/jobs?q=Junior%20-%20Business%20Analyst%20%28SDLC/UML%29%20DLT%20Labs%20Technologies%20Private%20Limited</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row9" class="row_heading level0 row9" >110</th>
      <td id="T_c71c4_row9_col0" class="data row9 col0" >Junior Survey Programmer</td>
      <td id="T_c71c4_row9_col1" class="data row9 col1" > Taking ownership of and programming surveys in an online survey authoring platform (Decipher, Kinesis, Confirmit, Nebu, SurveyMonkey). </td>
      <td id="T_c71c4_row9_col2" class="data row9 col2" >Active 2 days ago</td>
      <td id="T_c71c4_row9_col3" class="data row9 col3" >https://ca.indeed.com/jobs?q=Junior%20Survey%20Programmer%20Canadian%20Viewpoint%20Inc</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row10" class="row_heading level0 row10" >113</th>
      <td id="T_c71c4_row10_col0" class="data row10 col0" >Junior Software Engineer</td>
      <td id="T_c71c4_row10_col1" class="data row10 col1" > Develop new and enhance existing single-page web applications and develop key system features. Serve as a developer on teams that will execute projects from… </td>
      <td id="T_c71c4_row10_col2" class="data row10 col2" >2 days ago</td>
      <td id="T_c71c4_row10_col3" class="data row10 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Engineer%20NielsenIQ</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row11" class="row_heading level0 row11" >225</th>
      <td id="T_c71c4_row11_col0" class="data row11 col0" >Junior Mechanical Engineer</td>
      <td id="T_c71c4_row11_col1" class="data row11 col1" > P.Eng. exercising initiative and independent judgment in performing assigned tasks. You will report to the V.P. of Operations and assist and advise the sales… </td>
      <td id="T_c71c4_row11_col2" class="data row11 col2" >Active 2 days ago</td>
      <td id="T_c71c4_row11_col3" class="data row11 col3" >https://ca.indeed.com/jobs?q=Junior%20Mechanical%20Engineer%20Green%20Matters%20Technologies</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row12" class="row_heading level0 row12" >226</th>
      <td id="T_c71c4_row12_col0" class="data row12 col0" >Cloud Engineer, I</td>
      <td id="T_c71c4_row12_col1" class="data row12 col1" > The perfect candidate will have excellent analysis and troubleshooting skills with attention to detail. Experience with cloud monitoring tools, observing, and… </td>
      <td id="T_c71c4_row12_col2" class="data row12 col2" >2 days ago</td>
      <td id="T_c71c4_row12_col3" class="data row12 col3" >https://ca.indeed.com/jobs?q=Cloud%20Engineer%2C%20I%20Zebra%20Technologies</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row13" class="row_heading level0 row13" >227</th>
      <td id="T_c71c4_row13_col0" class="data row13 col0" >Développeur PHP junior - Junior PHP Developper</td>
      <td id="T_c71c4_row13_col1" class="data row13 col1" > Nous faisons partie de Vivendi - un des groupes de médias les plus importants au monde - ce qui nous confère le pouvoir et les ressources pour établir des… </td>
      <td id="T_c71c4_row13_col2" class="data row13 col2" >2 days ago</td>
      <td id="T_c71c4_row13_col3" class="data row13 col3" >https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20PHP%20junior%20-%20Junior%20PHP%20Developper%20Gameloft</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row14" class="row_heading level0 row14" >112</th>
      <td id="T_c71c4_row14_col0" class="data row14 col0" >Junior Forecast Analyst-Shared Services</td>
      <td id="T_c71c4_row14_col1" class="data row14 col1" > Junior Forecast Analyst – Shared Services*. Reporting to the Director of Operations Support, the Junior Forecast Analyst contributes to Arctic Glacier’s success… </td>
      <td id="T_c71c4_row14_col2" class="data row14 col2" >Active 2 days ago</td>
      <td id="T_c71c4_row14_col3" class="data row14 col3" >https://ca.indeed.com/jobs?q=Junior%20Forecast%20Analyst-Shared%20Services%20Arctic%20Glacier</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row15" class="row_heading level0 row15" >4</th>
      <td id="T_c71c4_row15_col0" class="data row15 col0" >Junior Data Engineer - OpenRoad Auto Group</td>
      <td id="T_c71c4_row15_col1" class="data row15 col1" > Ensure high data integrity and quality from various data sources that are aligned to industry best practices. The Data Engineer is responsible for implementing … </td>
      <td id="T_c71c4_row15_col2" class="data row15 col2" >2 days ago</td>
      <td id="T_c71c4_row15_col3" class="data row15 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Engineer%20-%20OpenRoad%20Auto%20Group%20OpenRoad%20Auto%20Group</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row16" class="row_heading level0 row16" >5</th>
      <td id="T_c71c4_row16_col0" class="data row16 col0" >Business Operations Analyst I, AWS Commerce Platform Busines...</td>
      <td id="T_c71c4_row16_col1" class="data row16 col1" > At least 1+ years of experience with data warehousing and reporting. At least 1+ years of professional working experience in related occupations of Business… </td>
      <td id="T_c71c4_row16_col2" class="data row16 col2" >2 days ago</td>
      <td id="T_c71c4_row16_col3" class="data row16 col3" >https://ca.indeed.com/jobs?q=Business%20Operations%20Analyst%20I%2C%20AWS%20Commerce%20Platform%20Busines...%20Amazon%20Dev%20Centre%20Canada%20ULC</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row17" class="row_heading level0 row17" >230</th>
      <td id="T_c71c4_row17_col0" class="data row17 col0" >Junior Frontend Developer</td>
      <td id="T_c71c4_row17_col1" class="data row17 col1" > Wealth Management Applied Analytics and Innovation (WM AI) is responsible for developing and implementing a data and analytics strategy that delivers key… </td>
      <td id="T_c71c4_row17_col2" class="data row17 col2" >3 days ago</td>
      <td id="T_c71c4_row17_col3" class="data row17 col3" >https://ca.indeed.com/jobs?q=Junior%20Frontend%20Developer%20Royal%20Bank%20of%20Canada</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row18" class="row_heading level0 row18" >229</th>
      <td id="T_c71c4_row18_col0" class="data row18 col0" >Junior Systems Administrator</td>
      <td id="T_c71c4_row18_col1" class="data row18 col1" > Maintenance of the Ubuntu Linux server infrastructure. Ensures security and configuration compliance of hardware and software to comply with best practices. </td>
      <td id="T_c71c4_row18_col2" class="data row18 col2" >3 days ago</td>
      <td id="T_c71c4_row18_col3" class="data row18 col3" >https://ca.indeed.com/jobs?q=Junior%20Systems%20Administrator%20PSD</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row19" class="row_heading level0 row19" >228</th>
      <td id="T_c71c4_row19_col0" class="data row19 col0" >Junior Full Stack Developer</td>
      <td id="T_c71c4_row19_col1" class="data row19 col1" > Helcim is searching for an Junior Full Stack Developer to be responsible for helping develop a wide variety of features including both frontend and backend… </td>
      <td id="T_c71c4_row19_col2" class="data row19 col2" >3 days ago</td>
      <td id="T_c71c4_row19_col3" class="data row19 col3" >https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20Helcim</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row20" class="row_heading level0 row20" >127</th>
      <td id="T_c71c4_row20_col0" class="data row20 col0" >Junior Campaign Manager</td>
      <td id="T_c71c4_row20_col1" class="data row20 col1" > Based in downtown Guelph, ON, Adknown offers a competitive salary with bonus potential, a great benefits package, flexible scheduling and many other great perks… </td>
      <td id="T_c71c4_row20_col2" class="data row20 col2" >3 days ago</td>
      <td id="T_c71c4_row20_col3" class="data row20 col3" >https://ca.indeed.com/jobs?q=Junior%20Campaign%20Manager%20Adknown</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row21" class="row_heading level0 row21" >126</th>
      <td id="T_c71c4_row21_col0" class="data row21 col0" >Junior Capital Accountant</td>
      <td id="T_c71c4_row21_col1" class="data row21 col1" > We are currently looking for a motivated Junior Capital Accountant to join our Finance team within the Midstream Infrastructure division of our organization. </td>
      <td id="T_c71c4_row21_col2" class="data row21 col2" >3 days ago</td>
      <td id="T_c71c4_row21_col3" class="data row21 col3" >https://ca.indeed.com/jobs?q=Junior%20Capital%20Accountant%20Secure%20Energy</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row22" class="row_heading level0 row22" >125</th>
      <td id="T_c71c4_row22_col0" class="data row22 col0" >Junior Software Developer</td>
      <td id="T_c71c4_row22_col1" class="data row22 col1" > North Orca Technologies Inc is looking for an junior or intermediate software developer to work full time on our flight training scheduling system for Airlines… </td>
      <td id="T_c71c4_row22_col2" class="data row22 col2" >Active 3 days ago</td>
      <td id="T_c71c4_row22_col3" class="data row22 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20North%20Orca%20Technologies%20Inc</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row23" class="row_heading level0 row23" >124</th>
      <td id="T_c71c4_row23_col0" class="data row23 col0" >Jr. Developer</td>
      <td id="T_c71c4_row23_col1" class="data row23 col1" > Comfortable working with traditional desktop applications as well as the latest mobile application technologies, you will participate in various stages of the… </td>
      <td id="T_c71c4_row23_col2" class="data row23 col2" >Active 3 days ago</td>
      <td id="T_c71c4_row23_col3" class="data row23 col3" >https://ca.indeed.com/jobs?q=Jr.%20Developer%20Nexent%20Innovations%20Inc.</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row24" class="row_heading level0 row24" >123</th>
      <td id="T_c71c4_row24_col0" class="data row24 col0" >Junior Software Developer</td>
      <td id="T_c71c4_row24_col1" class="data row24 col1" > These projections and other insights are currently being delivered to our clients through a subscription package on our website, with daily, weekly, and monthly… </td>
      <td id="T_c71c4_row24_col2" class="data row24 col2" >Active 3 days ago</td>
      <td id="T_c71c4_row24_col3" class="data row24 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20Carbon%20Assessors</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row25" class="row_heading level0 row25" >121</th>
      <td id="T_c71c4_row25_col0" class="data row25 col0" >Junior Full Stack Developer (Calgary)</td>
      <td id="T_c71c4_row25_col1" class="data row25 col1" > Craft scalable TypeScript and Python code to integrate with customer websites, apps, and APIs. Flex your TypeScript muscle to design/develop single page web… </td>
      <td id="T_c71c4_row25_col2" class="data row25 col2" >Active 3 days ago</td>
      <td id="T_c71c4_row25_col3" class="data row25 col3" >https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20%28Calgary%29%20Leap%20Tools</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row26" class="row_heading level0 row26" >120</th>
      <td id="T_c71c4_row26_col0" class="data row26 col0" >Junior Capital Accountant</td>
      <td id="T_c71c4_row26_col1" class="data row26 col1" > The role will focus on capital projects and all associated financials, including variance analysis, reporting and all financial entries. </td>
      <td id="T_c71c4_row26_col2" class="data row26 col2" >3 days ago</td>
      <td id="T_c71c4_row26_col3" class="data row26 col3" >https://ca.indeed.com/jobs?q=Junior%20Capital%20Accountant%20SECURE%20Energy%20Services%20Inc.</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row27" class="row_heading level0 row27" >122</th>
      <td id="T_c71c4_row27_col0" class="data row27 col0" >Junior Front End Developer</td>
      <td id="T_c71c4_row27_col1" class="data row27 col1" > Collaborate with team members to review requirements and interface and application design specifications. Design beautiful interfaces with an elegant simplicity… </td>
      <td id="T_c71c4_row27_col2" class="data row27 col2" >Active 3 days ago</td>
      <td id="T_c71c4_row27_col3" class="data row27 col3" >https://ca.indeed.com/jobs?q=Junior%20Front%20End%20Developer%20Leap%20Tools</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row28" class="row_heading level0 row28" >118</th>
      <td id="T_c71c4_row28_col0" class="data row28 col0" >Junior Python Developer</td>
      <td id="T_c71c4_row28_col1" class="data row28 col1" > Work as part of a small engineer team to be the interconnect between business and tech divisions. Maintain uptime of some backend servers for internal use. </td>
      <td id="T_c71c4_row28_col2" class="data row28 col2" >Active 3 days ago</td>
      <td id="T_c71c4_row28_col3" class="data row28 col3" >https://ca.indeed.com/jobs?q=Junior%20Python%20Developer%20Track%20Revenue%20Ltd.</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row29" class="row_heading level0 row29" >6</th>
      <td id="T_c71c4_row29_col0" class="data row29 col0" >Junior Business Analyst- Travel Industry</td>
      <td id="T_c71c4_row29_col1" class="data row29 col1" > Collaborate with our development and support teams to answer business questions using data and business analysis best practices. </td>
      <td id="T_c71c4_row29_col2" class="data row29 col2" >3 days ago</td>
      <td id="T_c71c4_row29_col3" class="data row29 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst-%20Travel%20Industry%20Staffmax</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row30" class="row_heading level0 row30" >7</th>
      <td id="T_c71c4_row30_col0" class="data row30 col0" >Junior Asset Management Consultant and Data Analyst</td>
      <td id="T_c71c4_row30_col1" class="data row30 col1" > Develop and analyze asset data to support asset management planning. Create and manage asset inventories and data structures, including the development of… </td>
      <td id="T_c71c4_row30_col2" class="data row30 col2" >Active 3 days ago</td>
      <td id="T_c71c4_row30_col3" class="data row30 col3" >https://ca.indeed.com/jobs?q=Junior%20Asset%20Management%20Consultant%20and%20Data%20Analyst%20GM%20BluePlan%20Engineering</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row31" class="row_heading level0 row31" >119</th>
      <td id="T_c71c4_row31_col0" class="data row31 col0" >Junior Developer</td>
      <td id="T_c71c4_row31_col1" class="data row31 col1" > Competitive wages, amazing benefits, yearly performance-based bonuses, RRSP matching, health and wellness programs, a literal award-winning culture, parental… </td>
      <td id="T_c71c4_row31_col2" class="data row31 col2" >3 days ago</td>
      <td id="T_c71c4_row31_col3" class="data row31 col3" >https://ca.indeed.com/jobs?q=Junior%20Developer%20CARFAX%20Canada</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row32" class="row_heading level0 row32" >9</th>
      <td id="T_c71c4_row32_col0" class="data row32 col0" >Technical Operations Analyst - Junior</td>
      <td id="T_c71c4_row32_col1" class="data row32 col1" > Provide data analysis, process improvements, creative problem solving, and cross-functional collaboration. On behalf of our client in the Telco Sector, PROCOM… </td>
      <td id="T_c71c4_row32_col2" class="data row32 col2" >3 days ago</td>
      <td id="T_c71c4_row32_col3" class="data row32 col3" >https://ca.indeed.com/jobs?q=Technical%20Operations%20Analyst%20-%20Junior%20Procom</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row33" class="row_heading level0 row33" >8</th>
      <td id="T_c71c4_row33_col0" class="data row33 col0" >Junior Data Scientist</td>
      <td id="T_c71c4_row33_col1" class="data row33 col1" > Transfer Load (ETL) functionality between various data sources (APIs, SQL, FactSet) and local data. Researching and developing statistical learning models for… </td>
      <td id="T_c71c4_row33_col2" class="data row33 col2" >3 days ago</td>
      <td id="T_c71c4_row33_col3" class="data row33 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Scientist%20Guardian%20Capital%20Group%20Limited</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row34" class="row_heading level0 row34" >116</th>
      <td id="T_c71c4_row34_col0" class="data row34 col0" >Junior Backend Developer (Lagos / Accra / Kenya)</td>
      <td id="T_c71c4_row34_col1" class="data row34 col1" > Translation of the UI/UX design wireframes to actual code that will produce visual elements of the back-end product. Develop new user-facing features. </td>
      <td id="T_c71c4_row34_col2" class="data row34 col2" >3 days ago</td>
      <td id="T_c71c4_row34_col3" class="data row34 col3" >https://ca.indeed.com/jobs?q=Junior%20Backend%20Developer%20%28Lagos%20/%20Accra%20/%20Kenya%29%20HumanSquad%20Inc.</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row35" class="row_heading level0 row35" >117</th>
      <td id="T_c71c4_row35_col0" class="data row35 col0" >Junior Full Stack Developer New Graduate Opportunities</td>
      <td id="T_c71c4_row35_col1" class="data row35 col1" > Building smart and efficient code that works well within a service-based system architecture. Developing new features and systems, as well as maintaining… </td>
      <td id="T_c71c4_row35_col2" class="data row35 col2" >3 days ago</td>
      <td id="T_c71c4_row35_col3" class="data row35 col3" >https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20New%20Graduate%20Opportunities%20Helcim</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row36" class="row_heading level0 row36" >114</th>
      <td id="T_c71c4_row36_col0" class="data row36 col0" >Junior Software Developer</td>
      <td id="T_c71c4_row36_col1" class="data row36 col1" > This is a hands-on software development and support role where you will use your development skills to build and enhance innovative solutions and provide tier 2… </td>
      <td id="T_c71c4_row36_col2" class="data row36 col2" >3 days ago</td>
      <td id="T_c71c4_row36_col3" class="data row36 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20Bank%20of%20Canada</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row37" class="row_heading level0 row37" >14</th>
      <td id="T_c71c4_row37_col0" class="data row37 col0" >Junior Pricing Coordinator</td>
      <td id="T_c71c4_row37_col1" class="data row37 col1" > Manage data collection of internal systems utilized by Max Advanced Brakes. Manages key pricing programs and provides comprehensive reporting, tracking and… </td>
      <td id="T_c71c4_row37_col2" class="data row37 col2" >Active 4 days ago</td>
      <td id="T_c71c4_row37_col3" class="data row37 col3" >https://ca.indeed.com/jobs?q=Junior%20Pricing%20Coordinator%20Max%20Advanced%20Brakes</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row38" class="row_heading level0 row38" >232</th>
      <td id="T_c71c4_row38_col0" class="data row38 col0" >Junior Software Engineer</td>
      <td id="T_c71c4_row38_col1" class="data row38 col1" > GameDriver is looking to hire a full-time Junior Software Engineer to support the development of our patented test automation solution for video games, virtual… </td>
      <td id="T_c71c4_row38_col2" class="data row38 col2" >Active 4 days ago</td>
      <td id="T_c71c4_row38_col3" class="data row38 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Engineer%20GameDriver</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row39" class="row_heading level0 row39" >233</th>
      <td id="T_c71c4_row39_col0" class="data row39 col0" >Software Developer I</td>
      <td id="T_c71c4_row39_col1" class="data row39 col1" > We need people who are going to roll-up their sleeves and make things happen. Work may include any combination of the developing, maintaining, or deploying. </td>
      <td id="T_c71c4_row39_col2" class="data row39 col2" >Active 4 days ago</td>
      <td id="T_c71c4_row39_col3" class="data row39 col3" >https://ca.indeed.com/jobs?q=Software%20Developer%20I%20Genomadix</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row40" class="row_heading level0 row40" >11</th>
      <td id="T_c71c4_row40_col0" class="data row40 col0" >Junior Financial Planning Analyst</td>
      <td id="T_c71c4_row40_col1" class="data row40 col1" > Performs trend and variance analyses; incorporates data from different areas and synthesizes. This position is responsible for providing updates to daily,… </td>
      <td id="T_c71c4_row40_col2" class="data row40 col2" >4 days ago</td>
      <td id="T_c71c4_row40_col3" class="data row40 col3" >https://ca.indeed.com/jobs?q=Junior%20Financial%20Planning%20Analyst%20UNFI%20Canada</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row41" class="row_heading level0 row41" >128</th>
      <td id="T_c71c4_row41_col0" class="data row41 col0" >Programmer/Analyst Junior</td>
      <td id="T_c71c4_row41_col1" class="data row41 col1" > Position Type : Contract Starting : May 23, 2022. The successful candidate will be responsible for the development, deployment and support of Client's IT… </td>
      <td id="T_c71c4_row41_col2" class="data row41 col2" >4 days ago</td>
      <td id="T_c71c4_row41_col3" class="data row41 col3" >https://ca.indeed.com/jobs?q=Programmer/Analyst%20Junior%20CTConsultants</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row42" class="row_heading level0 row42" >15</th>
      <td id="T_c71c4_row42_col0" class="data row42 col0" >Data Steward I</td>
      <td id="T_c71c4_row42_col1" class="data row42 col1" > Complete metadata and data quality tasks. Identify and monitor the quality of critical data elements. Manage data work activities requiring coordination across… </td>
      <td id="T_c71c4_row42_col2" class="data row42 col2" >4 days ago</td>
      <td id="T_c71c4_row42_col3" class="data row42 col3" >https://ca.indeed.com/jobs?q=Data%20Steward%20I%20TD%20Bank</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row43" class="row_heading level0 row43" >132</th>
      <td id="T_c71c4_row43_col0" class="data row43 col0" >Junior PHP Backend Developer</td>
      <td id="T_c71c4_row43_col1" class="data row43 col1" > We are looking for a highly motivated Junior Application Developer to join DealTrack's highly collaborative and agile team. </td>
      <td id="T_c71c4_row43_col2" class="data row43 col2" >Active 4 days ago</td>
      <td id="T_c71c4_row43_col3" class="data row43 col3" >https://ca.indeed.com/jobs?q=Junior%20PHP%20Backend%20Developer%20DealTrack</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row44" class="row_heading level0 row44" >131</th>
      <td id="T_c71c4_row44_col0" class="data row44 col0" >Junior Resource Analyst</td>
      <td id="T_c71c4_row44_col1" class="data row44 col1" > Company: Ecora Engineering &amp; Resource Group. Location: Kelowna, Prince George or Vancouver, British Columbia. We are committed to delivering quality services to… </td>
      <td id="T_c71c4_row44_col2" class="data row44 col2" >Active 4 days ago</td>
      <td id="T_c71c4_row44_col3" class="data row44 col3" >https://ca.indeed.com/jobs?q=Junior%20Resource%20Analyst%20Ecora</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row45" class="row_heading level0 row45" >130</th>
      <td id="T_c71c4_row45_col0" class="data row45 col0" >Junior Support Analyst</td>
      <td id="T_c71c4_row45_col1" class="data row45 col1" > The Support Analyst will join a mid-sized team and will provide technical support for a core manufacturing data collection system. </td>
      <td id="T_c71c4_row45_col2" class="data row45 col2" >4 days ago</td>
      <td id="T_c71c4_row45_col3" class="data row45 col3" >https://ca.indeed.com/jobs?q=Junior%20Support%20Analyst%20Valley%20West%20Control%20Ltd.</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row46" class="row_heading level0 row46" >129</th>
      <td id="T_c71c4_row46_col0" class="data row46 col0" >Junior Front End Developer - Summer Student Internship</td>
      <td id="T_c71c4_row46_col1" class="data row46 col1" > MyMarketing is a unique digital marketing agency that provides businesses with a comprehensive, no-commitment digital marketing monthly subscription. </td>
      <td id="T_c71c4_row46_col2" class="data row46 col2" >4 days ago</td>
      <td id="T_c71c4_row46_col3" class="data row46 col3" >https://ca.indeed.com/jobs?q=Junior%20Front%20End%20Developer%20-%20Summer%20Student%20Internship%20myMarketing.io</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row47" class="row_heading level0 row47" >13</th>
      <td id="T_c71c4_row47_col0" class="data row47 col0" >Junior Financial Analyst</td>
      <td id="T_c71c4_row47_col1" class="data row47 col1" > Reporting to the Treasurer and Director of Finance, the analyst will work independently to review parish financial and statistical data by comparing and… </td>
      <td id="T_c71c4_row47_col2" class="data row47 col2" >Active 4 days ago</td>
      <td id="T_c71c4_row47_col3" class="data row47 col3" >https://ca.indeed.com/jobs?q=Junior%20Financial%20Analyst%20Anglican%20Diocese%20of%20Niagara</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row48" class="row_heading level0 row48" >10</th>
      <td id="T_c71c4_row48_col0" class="data row48 col0" >Data Control Coordinator I - 12 month contract</td>
      <td id="T_c71c4_row48_col1" class="data row48 col1" > Resolving and completing data input for all orders that fail auto upload. 0-1 years of experience in an administrative or data entry role. </td>
      <td id="T_c71c4_row48_col2" class="data row48 col2" >4 days ago</td>
      <td id="T_c71c4_row48_col3" class="data row48 col3" >https://ca.indeed.com/jobs?q=Data%20Control%20Coordinator%20I%20-%2012%20month%20contract%20Moneris%20Solutions</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row49" class="row_heading level0 row49" >12</th>
      <td id="T_c71c4_row49_col0" class="data row49 col0" >Junior Data Analyst</td>
      <td id="T_c71c4_row49_col1" class="data row49 col1" > Gain and update job knowledge to remain informed about innovation in the field, explore and implement use cases for data science/data analytics to improve… </td>
      <td id="T_c71c4_row49_col2" class="data row49 col2" >Active 4 days ago</td>
      <td id="T_c71c4_row49_col3" class="data row49 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20Beta-Calco</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row50" class="row_heading level0 row50" >135</th>
      <td id="T_c71c4_row50_col0" class="data row50 col0" >Systems Administrator I - 3rd Shift</td>
      <td id="T_c71c4_row50_col1" class="data row50 col1" > The System Administrator I will be responsible for managing their time appropriately while monitoring multiple assignment queues, their personal queue of open… </td>
      <td id="T_c71c4_row50_col2" class="data row50 col2" >5 days ago</td>
      <td id="T_c71c4_row50_col3" class="data row50 col3" >https://ca.indeed.com/jobs?q=Systems%20Administrator%20I%20-%203rd%20Shift%20Distributed%20Systems%20Services%2C%20Inc.</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row51" class="row_heading level0 row51" >134</th>
      <td id="T_c71c4_row51_col0" class="data row51 col0" >Data Analyst - Jr. Developer</td>
      <td id="T_c71c4_row51_col1" class="data row51 col1" > Our software can run all aspects of an automotive dealership with sales, service, inventory management, and accounting modules. Code merging and team debugging. </td>
      <td id="T_c71c4_row51_col2" class="data row51 col2" >5 days ago</td>
      <td id="T_c71c4_row51_col3" class="data row51 col3" >https://ca.indeed.com/jobs?q=Data%20Analyst%20-%20Jr.%20Developer%20PBS%20Systems</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row52" class="row_heading level0 row52" >133</th>
      <td id="T_c71c4_row52_col0" class="data row52 col0" >Jr Software Developer (Remote/Hybrid)</td>
      <td id="T_c71c4_row52_col1" class="data row52 col1" > Assisting the development manager with all aspects of software design and coding. Attending and contributing to company development meetings. </td>
      <td id="T_c71c4_row52_col2" class="data row52 col2" >Active 5 days ago</td>
      <td id="T_c71c4_row52_col3" class="data row52 col3" >https://ca.indeed.com/jobs?q=Jr%20Software%20Developer%20%28Remote/Hybrid%29%20CADdetails%20Ltd.</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row53" class="row_heading level0 row53" >16</th>
      <td id="T_c71c4_row53_col0" class="data row53 col0" >Spécialiste Junior Bilingue en Gestion des Données Junior /...</td>
      <td id="T_c71c4_row53_col1" class="data row53 col1" > Handling the data enrichment of the small to medium data customers by vertically coordinating with customers, Data Quality and IT for new data or current data… </td>
      <td id="T_c71c4_row53_col2" class="data row53 col2" >5 days ago</td>
      <td id="T_c71c4_row53_col3" class="data row53 col3" >https://ca.indeed.com/jobs?q=Sp%C3%A9cialiste%20Junior%20Bilingue%20en%20Gestion%20des%20Donn%C3%A9es%20Junior%20/...%20Equifax</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row54" class="row_heading level0 row54" >17</th>
      <td id="T_c71c4_row54_col0" class="data row54 col0" >Junior Data Analyst</td>
      <td id="T_c71c4_row54_col1" class="data row54 col1" > Profile and evaluate data to determine data quality gaps per identified criteria. You will work with SMEs across various Line of Business to analyze data, fix… </td>
      <td id="T_c71c4_row54_col2" class="data row54 col2" >5 days ago</td>
      <td id="T_c71c4_row54_col3" class="data row54 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20FCT</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row55" class="row_heading level0 row55" >236</th>
      <td id="T_c71c4_row55_col0" class="data row55 col0" >Junior Software Engineer</td>
      <td id="T_c71c4_row55_col1" class="data row55 col1" > Knowledge and use of several Integrated software development environment SDE tools and scripting languages (python, etc). Knowledge and use of databases. </td>
      <td id="T_c71c4_row55_col2" class="data row55 col2" >5 days ago</td>
      <td id="T_c71c4_row55_col3" class="data row55 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Engineer%20Safran%20Electronics%20%26%20Defense%20Canada</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row56" class="row_heading level0 row56" >237</th>
      <td id="T_c71c4_row56_col0" class="data row56 col0" >Junior Application Engineer (FT)</td>
      <td id="T_c71c4_row56_col1" class="data row56 col1" > Preparing software configuration packages using the product specification to create a set of configuration files tailored to the project: </td>
      <td id="T_c71c4_row56_col2" class="data row56 col2" >6 days ago</td>
      <td id="T_c71c4_row56_col3" class="data row56 col3" >https://ca.indeed.com/jobs?q=Junior%20Application%20Engineer%20%28FT%29%20Greenlight%20Innovation</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row57" class="row_heading level0 row57" >136</th>
      <td id="T_c71c4_row57_col0" class="data row57 col0" >Junior Software Developer</td>
      <td id="T_c71c4_row57_col1" class="data row57 col1" > You will support with architecting, developing, and maintaining internal and external facing solutions used for field data collection, document and data… </td>
      <td id="T_c71c4_row57_col2" class="data row57 col2" >6 days ago</td>
      <td id="T_c71c4_row57_col3" class="data row57 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20WSP</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row58" class="row_heading level0 row58" >137</th>
      <td id="T_c71c4_row58_col0" class="data row58 col0" >Junior Full Stack Developer</td>
      <td id="T_c71c4_row58_col1" class="data row58 col1" > The Full-Stack Developer is responsible for front-end and back- end development including database and integration, in addition to collaborating with both… </td>
      <td id="T_c71c4_row58_col2" class="data row58 col2" >Active 6 days ago</td>
      <td id="T_c71c4_row58_col3" class="data row58 col3" >https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20Immigration%2C%20Refugees%20and%20Citizenship%20Canada</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row59" class="row_heading level0 row59" >138</th>
      <td id="T_c71c4_row59_col0" class="data row59 col0" >Junior Python Developer (Calgary)</td>
      <td id="T_c71c4_row59_col1" class="data row59 col1" > You have a passion for solving complex problems and working on products that people will use on a daily basis. Our game nights are legendary.*. </td>
      <td id="T_c71c4_row59_col2" class="data row59 col2" >Active 6 days ago</td>
      <td id="T_c71c4_row59_col3" class="data row59 col3" >https://ca.indeed.com/jobs?q=Junior%20Python%20Developer%20%28Calgary%29%20Leap%20Tools</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row60" class="row_heading level0 row60" >139</th>
      <td id="T_c71c4_row60_col0" class="data row60 col0" >Conversion Analyst I</td>
      <td id="T_c71c4_row60_col1" class="data row60 col1" > Vertafore Canada is looking for a Conversion Analyst who is passionate about meeting customer needs and has Insurance industry experience. </td>
      <td id="T_c71c4_row60_col2" class="data row60 col2" >6 days ago</td>
      <td id="T_c71c4_row60_col3" class="data row60 col3" >https://ca.indeed.com/jobs?q=Conversion%20Analyst%20I%20Vertafore</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row61" class="row_heading level0 row61" >140</th>
      <td id="T_c71c4_row61_col0" class="data row61 col0" >Junior Analyst</td>
      <td id="T_c71c4_row61_col1" class="data row61 col1" > At Freeman Herbs we are passionate about herbs and vegetables. Each day we focus our efforts on quality, service, and innovation. </td>
      <td id="T_c71c4_row61_col2" class="data row61 col2" >6 days ago</td>
      <td id="T_c71c4_row61_col3" class="data row61 col3" >https://ca.indeed.com/jobs?q=Junior%20Analyst%20Freeman%20Herbs</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row62" class="row_heading level0 row62" >142</th>
      <td id="T_c71c4_row62_col0" class="data row62 col0" >Junior Automation Programming Specialist</td>
      <td id="T_c71c4_row62_col1" class="data row62 col1" > The Junior Automation Programming Specialist supports our team of Senior Programmers and Automation Specialists. </td>
      <td id="T_c71c4_row62_col2" class="data row62 col2" >6 days ago</td>
      <td id="T_c71c4_row62_col3" class="data row62 col3" >https://ca.indeed.com/jobs?q=Junior%20Automation%20Programming%20Specialist%20CDN%20Controls%20Ltd.</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row63" class="row_heading level0 row63" >143</th>
      <td id="T_c71c4_row63_col0" class="data row63 col0" >Junior Applications Developer – Summer Student</td>
      <td id="T_c71c4_row63_col1" class="data row63 col1" > Everyone is encouraged to take ownership of his/her ideas and to see them through to completion, collaborating with key influencers as required. </td>
      <td id="T_c71c4_row63_col2" class="data row63 col2" >6 days ago</td>
      <td id="T_c71c4_row63_col3" class="data row63 col3" >https://ca.indeed.com/jobs?q=Junior%20Applications%20Developer%20%E2%80%93%20Summer%20Student%20Careers%20at%20ECO%20Canada</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row64" class="row_heading level0 row64" >144</th>
      <td id="T_c71c4_row64_col0" class="data row64 col0" >Junior Programmer</td>
      <td id="T_c71c4_row64_col1" class="data row64 col1" > OCANDS extracts administrative data from participating agencies and harmonizes those data from different systems using in-house ETL tools and link them to data… </td>
      <td id="T_c71c4_row64_col2" class="data row64 col2" >6 days ago</td>
      <td id="T_c71c4_row64_col3" class="data row64 col3" >https://ca.indeed.com/jobs?q=Junior%20Programmer%20University%20of%20Toronto</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row65" class="row_heading level0 row65" >141</th>
      <td id="T_c71c4_row65_col0" class="data row65 col0" >SolidWorks & Systems Support Engineer, Junior</td>
      <td id="T_c71c4_row65_col1" class="data row65 col1" > The team’s mandate is to develop and implement structured but flexible processes and software solutions to support a wide variety of multidisciplinary… </td>
      <td id="T_c71c4_row65_col2" class="data row65 col2" >6 days ago</td>
      <td id="T_c71c4_row65_col3" class="data row65 col3" >https://ca.indeed.com/jobs?q=SolidWorks%20%26%20Systems%20Support%20Engineer%2C%20Junior%20WhiteWater%20West-</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row66" class="row_heading level0 row66" >18</th>
      <td id="T_c71c4_row66_col0" class="data row66 col0" >Junior Data Analyst</td>
      <td id="T_c71c4_row66_col1" class="data row66 col1" > An understanding of data pipelines, architectures and data sets. The hire will be responsible for participating in expanding and optimizing our data and data… </td>
      <td id="T_c71c4_row66_col2" class="data row66 col2" >6 days ago</td>
      <td id="T_c71c4_row66_col3" class="data row66 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20SAIT%20Polytechnic</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row67" class="row_heading level0 row67" >19</th>
      <td id="T_c71c4_row67_col0" class="data row67 col0" >Jr. DB2 Database Administrator</td>
      <td id="T_c71c4_row67_col1" class="data row67 col1" > Provide DB2 Administrative services to application development team. Design/develop/test/support DB2 LUW database. Performance tuning and trouble shooting. </td>
      <td id="T_c71c4_row67_col2" class="data row67 col2" >Active 6 days ago</td>
      <td id="T_c71c4_row67_col3" class="data row67 col3" >https://ca.indeed.com/jobs?q=Jr.%20DB2%20Database%20Administrator%20Dawn%20InfoTek%20Inc.</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row68" class="row_heading level0 row68" >146</th>
      <td id="T_c71c4_row68_col0" class="data row68 col0" >Linux & Product Support Specialist (Junior)</td>
      <td id="T_c71c4_row68_col1" class="data row68 col1" > Front line product support via email and phone. Troubleshooting a variety of technical issues our valued customers may have with their Linux systems. </td>
      <td id="T_c71c4_row68_col2" class="data row68 col2" >7 days ago</td>
      <td id="T_c71c4_row68_col3" class="data row68 col3" >https://ca.indeed.com/jobs?q=Linux%20%26%20Product%20Support%20Specialist%20%28Junior%29%20LinuxMagic</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row69" class="row_heading level0 row69" >24</th>
      <td id="T_c71c4_row69_col0" class="data row69 col0" >Business Analyst I</td>
      <td id="T_c71c4_row69_col1" class="data row69 col1" > Marketing tactics and channels have evolved rapidly and technology now allows unprecedented access to data and targeted analysis for better understanding and… </td>
      <td id="T_c71c4_row69_col2" class="data row69 col2" >7 days ago</td>
      <td id="T_c71c4_row69_col3" class="data row69 col3" >https://ca.indeed.com/jobs?q=Business%20Analyst%20I%20TELUS</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row70" class="row_heading level0 row70" >23</th>
      <td id="T_c71c4_row70_col0" class="data row70 col0" >Despins - SDE I - Toronto 22, Measurement Ad Tech Data Scien...</td>
      <td id="T_c71c4_row70_col1" class="data row70 col1" > Computer Science fundamentals in data structures. Strong knowledge of data structures, algorithms, and designing for performance, scalability, and availability. </td>
      <td id="T_c71c4_row70_col2" class="data row70 col2" >7 days ago</td>
      <td id="T_c71c4_row70_col3" class="data row70 col3" >https://ca.indeed.com/jobs?q=Despins%20-%20SDE%20I%20-%20Toronto%2022%2C%20Measurement%20Ad%20Tech%20Data%20Scien...%20Amazon%20Dev%20Centre%20Canada%20ULC</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row71" class="row_heading level0 row71" >22</th>
      <td id="T_c71c4_row71_col0" class="data row71 col0" >Junior Quantitative Hydrogeologist</td>
      <td id="T_c71c4_row71_col1" class="data row71 col1" > Data compilation, reduction, and preliminary interpretation, including water quality results, hydraulic response testing data analysis, water balance model,… </td>
      <td id="T_c71c4_row71_col2" class="data row71 col2" >7 days ago</td>
      <td id="T_c71c4_row71_col3" class="data row71 col3" >https://ca.indeed.com/jobs?q=Junior%20Quantitative%20Hydrogeologist%20GHD</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row72" class="row_heading level0 row72" >147</th>
      <td id="T_c71c4_row72_col0" class="data row72 col0" >Junior Developer</td>
      <td id="T_c71c4_row72_col1" class="data row72 col1" > Under the general supervision of the Manager, Application Development, the incumbent develops tests, implements and documents moderate computer programs and… </td>
      <td id="T_c71c4_row72_col2" class="data row72 col2" >7 days ago</td>
      <td id="T_c71c4_row72_col3" class="data row72 col3" >https://ca.indeed.com/jobs?q=Junior%20Developer%20University%20of%20Manitoba</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row73" class="row_heading level0 row73" >238</th>
      <td id="T_c71c4_row73_col0" class="data row73 col0" >SOC Analyst I</td>
      <td id="T_c71c4_row73_col1" class="data row73 col1" > Analyze incoming security signals in real time with a balance of accuracy and speed using a variety of forensic tools. </td>
      <td id="T_c71c4_row73_col2" class="data row73 col2" >7 days ago</td>
      <td id="T_c71c4_row73_col3" class="data row73 col3" >https://ca.indeed.com/jobs?q=SOC%20Analyst%20I%20eSentire</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row74" class="row_heading level0 row74" >20</th>
      <td id="T_c71c4_row74_col0" class="data row74 col0" >Jr. Information Analyst</td>
      <td id="T_c71c4_row74_col1" class="data row74 col1" > Critical thinking – leverage data and process information to streamline the final mile delivery network. Sound foundation in the concept of data; ability to use… </td>
      <td id="T_c71c4_row74_col2" class="data row74 col2" >Active 7 days ago</td>
      <td id="T_c71c4_row74_col3" class="data row74 col3" >https://ca.indeed.com/jobs?q=Jr.%20Information%20Analyst%20Ziing%20Final%20Mile%20INC</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row75" class="row_heading level0 row75" >21</th>
      <td id="T_c71c4_row75_col0" class="data row75 col0" >Administrator I, Database</td>
      <td id="T_c71c4_row75_col1" class="data row75 col1" > IT Applications, the Database Administrator I ensures the operational effectiveness of the University's central enterprise systems and databases. </td>
      <td id="T_c71c4_row75_col2" class="data row75 col2" >7 days ago</td>
      <td id="T_c71c4_row75_col3" class="data row75 col3" >https://ca.indeed.com/jobs?q=Administrator%20I%2C%20Database%20University%20of%20the%20Fraser%20Valley</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row76" class="row_heading level0 row76" >148</th>
      <td id="T_c71c4_row76_col0" class="data row76 col0" >Junior Software Testing Specialist</td>
      <td id="T_c71c4_row76_col1" class="data row76 col1" > Annual salary increases – 3% progression increases up to the salary job rate, and 2% performance increases from the job rate to the ceiling, of the salary range… </td>
      <td id="T_c71c4_row76_col2" class="data row76 col2" >7 days ago</td>
      <td id="T_c71c4_row76_col3" class="data row76 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Testing%20Specialist%20University%20of%20Victoria</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row77" class="row_heading level0 row77" >145</th>
      <td id="T_c71c4_row77_col0" class="data row77 col0" >Junior Full Stack Software Developer - New Grad Opportunity</td>
      <td id="T_c71c4_row77_col1" class="data row77 col1" > We are a fast-growing software company based in Toronto whose passion is developing innovative analytics and marketing technologies that help brick and mortar… </td>
      <td id="T_c71c4_row77_col2" class="data row77 col2" >7 days ago</td>
      <td id="T_c71c4_row77_col3" class="data row77 col3" >https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Software%20Developer%20-%20New%20Grad%20Opportunity%20Aislelabs</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row78" class="row_heading level0 row78" >25</th>
      <td id="T_c71c4_row78_col0" class="data row78 col0" >Junior Financial Data Analyst</td>
      <td id="T_c71c4_row78_col1" class="data row78 col1" > Reporting to the Senior Paralegal, and Partner responsible for project completions, this role will assist our high performing Real Estate legal group with… </td>
      <td id="T_c71c4_row78_col2" class="data row78 col2" >Active 7 days ago</td>
      <td id="T_c71c4_row78_col3" class="data row78 col3" >https://ca.indeed.com/jobs?q=Junior%20Financial%20Data%20Analyst%20Lawson%20Lundell%20LLP</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row79" class="row_heading level0 row79" >27</th>
      <td id="T_c71c4_row79_col0" class="data row79 col0" >Junior Data Engineer / Ingénieur/ingénieure de données subal...</td>
      <td id="T_c71c4_row79_col1" class="data row79 col1" > They will also support the team’s projects as they relate to data sourcing, cleaning and ensuring data use is auditable. Knowledge of dbt and Jinja templating. </td>
      <td id="T_c71c4_row79_col2" class="data row79 col2" >Active 8 days ago</td>
      <td id="T_c71c4_row79_col3" class="data row79 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Engineer%20/%20Ing%C3%A9nieur/ing%C3%A9nieure%20de%20donn%C3%A9es%20subal...%20Labour%20Market%20Information%20Council</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row80" class="row_heading level0 row80" >150</th>
      <td id="T_c71c4_row80_col0" class="data row80 col0" >Junior Programmer - Summer Position</td>
      <td id="T_c71c4_row80_col1" class="data row80 col1" > Start Date: Immediate Hours: Full-time Contract: Summer position - 16 weeks. Location: Burlington, ON (currently virtual) Compensation: </td>
      <td id="T_c71c4_row80_col2" class="data row80 col2" >Active 8 days ago</td>
      <td id="T_c71c4_row80_col3" class="data row80 col3" >https://ca.indeed.com/jobs?q=Junior%20Programmer%20-%20Summer%20Position%20HIEC</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row81" class="row_heading level0 row81" >149</th>
      <td id="T_c71c4_row81_col0" class="data row81 col0" >Jr ReactJS Developer</td>
      <td id="T_c71c4_row81_col1" class="data row81 col1" > This developer will be required to work full time for three months on our project, be able meet aggressive deadlines and will have several years of experience… </td>
      <td id="T_c71c4_row81_col2" class="data row81 col2" >Active 8 days ago</td>
      <td id="T_c71c4_row81_col3" class="data row81 col3" >https://ca.indeed.com/jobs?q=Jr%20ReactJS%20Developer%20Hypertext/Labs</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row82" class="row_heading level0 row82" >26</th>
      <td id="T_c71c4_row82_col0" class="data row82 col0" >Business Informatics, Analytics & Operations Consultant I</td>
      <td id="T_c71c4_row82_col1" class="data row82 col1" > Leveraging key tools such as SSIS (SQL Server Integration Services) in order to extract, transform and load data from multiple data sources into the reporting… </td>
      <td id="T_c71c4_row82_col2" class="data row82 col2" >8 days ago</td>
      <td id="T_c71c4_row82_col3" class="data row82 col3" >https://ca.indeed.com/jobs?q=Business%20Informatics%2C%20Analytics%20%26%20Operations%20Consultant%20I%20St%20Michael%27s%20hospital</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row83" class="row_heading level0 row83" >28</th>
      <td id="T_c71c4_row83_col0" class="data row83 col0" >Jr. Business Analyst</td>
      <td id="T_c71c4_row83_col1" class="data row83 col1" > The junior business analyst role is responsible for supporting the virtual care program, which will deploy and manage virtual care services and solutions. </td>
      <td id="T_c71c4_row83_col2" class="data row83 col2" >9 days ago</td>
      <td id="T_c71c4_row83_col3" class="data row83 col3" >https://ca.indeed.com/jobs?q=Jr.%20Business%20Analyst%20eHealth%20Saskatchewan</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row84" class="row_heading level0 row84" >239</th>
      <td id="T_c71c4_row84_col0" class="data row84 col0" >Junior DevOps Engineer</td>
      <td id="T_c71c4_row84_col1" class="data row84 col1" > Proficiency with a scripting language (python/ruby). Generous vacation allotments and flexible working hours. Extended health and wellness spending accounts. </td>
      <td id="T_c71c4_row84_col2" class="data row84 col2" >9 days ago</td>
      <td id="T_c71c4_row84_col3" class="data row84 col3" >https://ca.indeed.com/jobs?q=Junior%20DevOps%20Engineer%20Thrive%20Health</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row85" class="row_heading level0 row85" >151</th>
      <td id="T_c71c4_row85_col0" class="data row85 col0" >Junior Business Analyst</td>
      <td id="T_c71c4_row85_col1" class="data row85 col1" > Reports to: Director of Operations. As the Business Analyst, you are responsible for conducting market analyses, analyzing both product lines and the overall… </td>
      <td id="T_c71c4_row85_col2" class="data row85 col2" >9 days ago</td>
      <td id="T_c71c4_row85_col3" class="data row85 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20Norsat%20International%20Inc.</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row86" class="row_heading level0 row86" >30</th>
      <td id="T_c71c4_row86_col0" class="data row86 col0" >Junior Power BI</td>
      <td id="T_c71c4_row86_col1" class="data row86 col1" >Good power bi skills Excellent communication Eager to learn Primary Location: CA-ON-Toronto Schedule: Full Time Job Type: Experienced Travel: No Job Posting:…</td>
      <td id="T_c71c4_row86_col2" class="data row86 col2" >10 days ago</td>
      <td id="T_c71c4_row86_col3" class="data row86 col3" >https://ca.indeed.com/jobs?q=Junior%20Power%20BI%20Virtusa</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row87" class="row_heading level0 row87" >29</th>
      <td id="T_c71c4_row87_col0" class="data row87 col0" >Research Analyst I</td>
      <td id="T_c71c4_row87_col1" class="data row87 col1" > Assist with data collection and analysis and support manuscript preparation (e.g., organize and conduct interviews, transcriptions, thematic analysis, drafting… </td>
      <td id="T_c71c4_row87_col2" class="data row87 col2" >10 days ago</td>
      <td id="T_c71c4_row87_col3" class="data row87 col3" >https://ca.indeed.com/jobs?q=Research%20Analyst%20I%20University%20Health%20Network</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row88" class="row_heading level0 row88" >31</th>
      <td id="T_c71c4_row88_col0" class="data row88 col0" >Business Informatics, Analytics & Operations Consultant I</td>
      <td id="T_c71c4_row88_col1" class="data row88 col1" > Leveraging key tools such as SSIS (SQL Server Integration Services) in order to extract, transform and load data from multiple data sources into the reporting… </td>
      <td id="T_c71c4_row88_col2" class="data row88 col2" >10 days ago</td>
      <td id="T_c71c4_row88_col3" class="data row88 col3" >https://ca.indeed.com/jobs?q=Business%20Informatics%2C%20Analytics%20%26%20Operations%20Consultant%20I%20St.%20Michael%27s%20Hospital</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row89" class="row_heading level0 row89" >242</th>
      <td id="T_c71c4_row89_col0" class="data row89 col0" >Application Support Specialist I - Information Technology</td>
      <td id="T_c71c4_row89_col1" class="data row89 col1" > Reporting to the Manager, Broadcast Systems, you will provide primary and secondary application support for a suite of business systems through issue tracking,… </td>
      <td id="T_c71c4_row89_col2" class="data row89 col2" >10 days ago</td>
      <td id="T_c71c4_row89_col3" class="data row89 col3" >https://ca.indeed.com/jobs?q=Application%20Support%20Specialist%20I%20-%20Information%20Technology%20Corus%20Entertainment</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row90" class="row_heading level0 row90" >241</th>
      <td id="T_c71c4_row90_col0" class="data row90 col0" >Junior Hydrogeologist/ Groundwater Modeller</td>
      <td id="T_c71c4_row90_col1" class="data row90 col1" > + Work within a team of hydrogeologists, geologists, geochemists, and groundwater modellers on a wide variety of projects. </td>
      <td id="T_c71c4_row90_col2" class="data row90 col2" >10 days ago</td>
      <td id="T_c71c4_row90_col3" class="data row90 col3" >https://ca.indeed.com/jobs?q=Junior%20Hydrogeologist/%20Groundwater%20Modeller%20AECOM</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row91" class="row_heading level0 row91" >152</th>
      <td id="T_c71c4_row91_col0" class="data row91 col0" >Junior QA Analyst - Mobile</td>
      <td id="T_c71c4_row91_col1" class="data row91 col1" > You will be responsible for elevating the quality and stability of the Eventbase Mobile Platform. Quality Assurance Analysts are critical to our success at… </td>
      <td id="T_c71c4_row91_col2" class="data row91 col2" >10 days ago</td>
      <td id="T_c71c4_row91_col3" class="data row91 col3" >https://ca.indeed.com/jobs?q=Junior%20QA%20Analyst%20-%20Mobile%20eventbase</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row92" class="row_heading level0 row92" >240</th>
      <td id="T_c71c4_row92_col0" class="data row92 col0" >Analyst, Development Infrastructure - Junior</td>
      <td id="T_c71c4_row92_col1" class="data row92 col1" > The prospective employee will report to the Development Services manager and will be supporting the engineering community in a wide variety of work. </td>
      <td id="T_c71c4_row92_col2" class="data row92 col2" >10 days ago</td>
      <td id="T_c71c4_row92_col3" class="data row92 col3" >https://ca.indeed.com/jobs?q=Analyst%2C%20Development%20Infrastructure%20-%20Junior%20General%20Dynamics%20Missions%20Systems-Canada</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row93" class="row_heading level0 row93" >243</th>
      <td id="T_c71c4_row93_col0" class="data row93 col0" >Cloud Security Architect I Remote, Canada</td>
      <td id="T_c71c4_row93_col1" class="data row93 col1" > We employ official mentor schemes for junior members of staff to help them learn about the organization and work effectively in their role. </td>
      <td id="T_c71c4_row93_col2" class="data row93 col2" >10 days ago</td>
      <td id="T_c71c4_row93_col3" class="data row93 col3" >https://ca.indeed.com/jobs?q=Cloud%20Security%20Architect%20I%20Remote%2C%20Canada%20Herjavec%20Group</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row94" class="row_heading level0 row94" >157</th>
      <td id="T_c71c4_row94_col0" class="data row94 col0" >Junior Software Developer</td>
      <td id="T_c71c4_row94_col1" class="data row94 col1" > A subsidiary of LMG Finance, LMG LoanLink is a Canadian owned and operated software company supporting the needs of the finance and insurance (F&amp;I) industry. </td>
      <td id="T_c71c4_row94_col2" class="data row94 col2" >11 days ago</td>
      <td id="T_c71c4_row94_col3" class="data row94 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20LMG%20Finance</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row95" class="row_heading level0 row95" >156</th>
      <td id="T_c71c4_row95_col0" class="data row95 col0" >Technology Analyst I</td>
      <td id="T_c71c4_row95_col1" class="data row95 col1" > As a Technology Analyst within our Pharmacy Operations team, you will leverage your technical acumen, creative problem-solving, collaboration and interpersonal… </td>
      <td id="T_c71c4_row95_col2" class="data row95 col2" >11 days ago</td>
      <td id="T_c71c4_row95_col3" class="data row95 col3" >https://ca.indeed.com/jobs?q=Technology%20Analyst%20I%20TELUS</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row96" class="row_heading level0 row96" >155</th>
      <td id="T_c71c4_row96_col0" class="data row96 col0" >Junior/Intermediate Hydrogeologist</td>
      <td id="T_c71c4_row96_col1" class="data row96 col1" > As a Junior/Intermediate Hydrogeologist, you would be involved in a variety of projects related to hydrogeologic assessment, groundwater supply development, and… </td>
      <td id="T_c71c4_row96_col2" class="data row96 col2" >11 days ago</td>
      <td id="T_c71c4_row96_col3" class="data row96 col3" >https://ca.indeed.com/jobs?q=Junior/Intermediate%20Hydrogeologist%20Stantec</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row97" class="row_heading level0 row97" >33</th>
      <td id="T_c71c4_row97_col0" class="data row97 col0" >Junior Database Administrator</td>
      <td id="T_c71c4_row97_col1" class="data row97 col1" > Reporting to the Senior Database Manager, the Jr database administrator assists the Sr. Database in the Administration of all KEC databases ensuring that the… </td>
      <td id="T_c71c4_row97_col2" class="data row97 col2" >11 days ago</td>
      <td id="T_c71c4_row97_col3" class="data row97 col3" >https://ca.indeed.com/jobs?q=Junior%20Database%20Administrator%20Kahnawake%20Education%20Center</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row98" class="row_heading level0 row98" >244</th>
      <td id="T_c71c4_row98_col0" class="data row98 col0" >Conseiller(ère) Junior en plateformes de données et intellig...</td>
      <td id="T_c71c4_row98_col1" class="data row98 col1" > / Carry out projects with potential returns and economic benefits for Quebecers. / Collaborate on dynamic teams with high-level professionals committed to… </td>
      <td id="T_c71c4_row98_col2" class="data row98 col2" >11 days ago</td>
      <td id="T_c71c4_row98_col3" class="data row98 col3" >https://ca.indeed.com/jobs?q=Conseiller%28%C3%A8re%29%20Junior%20en%20plateformes%20de%20donn%C3%A9es%20et%20intellig...%20Caisse%20de%20d%C3%A9p%C3%B4t%20et%20placement%20du%20Qu%C3%A9bec</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row99" class="row_heading level0 row99" >34</th>
      <td id="T_c71c4_row99_col0" class="data row99 col0" >Associate Data Analyst</td>
      <td id="T_c71c4_row99_col1" class="data row99 col1" > Manage our ETL process for client data transfers to enrich our proprietary data set. 1+ years experience working with advanced Excel and data analysis,… </td>
      <td id="T_c71c4_row99_col2" class="data row99 col2" >11 days ago</td>
      <td id="T_c71c4_row99_col3" class="data row99 col3" >https://ca.indeed.com/jobs?q=Associate%20Data%20Analyst%20Kazoo</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row100" class="row_heading level0 row100" >32</th>
      <td id="T_c71c4_row100_col0" class="data row100 col0" >Junior Data Engineer</td>
      <td id="T_c71c4_row100_col1" class="data row100 col1" > Build and maintain data collection pipelines. Experience using Python to transform data. Manage data refresh intervals and resolve errors. </td>
      <td id="T_c71c4_row100_col2" class="data row100 col2" >11 days ago</td>
      <td id="T_c71c4_row100_col3" class="data row100 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Engineer%20Valsoft</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row101" class="row_heading level0 row101" >154</th>
      <td id="T_c71c4_row101_col0" class="data row101 col0" >Programmeur(se) junior</td>
      <td id="T_c71c4_row101_col1" class="data row101 col1" > Nous recherchons un Programmeur(se) junior. Minimum un (1) an d'expérience dans le domaine. Expérience dans l'application du HTML/CSS, PHP7, du MySQL, PHP,… </td>
      <td id="T_c71c4_row101_col2" class="data row101 col2" >11 days ago</td>
      <td id="T_c71c4_row101_col3" class="data row101 col3" >https://ca.indeed.com/jobs?q=Programmeur%28se%29%20junior%20votresite.ca</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row102" class="row_heading level0 row102" >245</th>
      <td id="T_c71c4_row102_col0" class="data row102 col0" >Junior ASIC Verification Engineer</td>
      <td id="T_c71c4_row102_col1" class="data row102 col1" > You will work closely with ASIC design and verification engineers to verify SOC function features, close function &amp; code coverage holes. </td>
      <td id="T_c71c4_row102_col2" class="data row102 col2" >12 days ago</td>
      <td id="T_c71c4_row102_col3" class="data row102 col3" >https://ca.indeed.com/jobs?q=Junior%20ASIC%20Verification%20Engineer%20NETINT%20Technologies%20Inc.</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row103" class="row_heading level0 row103" >246</th>
      <td id="T_c71c4_row103_col0" class="data row103 col0" >Junior Associate Director, Middle Office Operations, MOV</td>
      <td id="T_c71c4_row103_col1" class="data row103 col1" > Reporting to the Director, Middle Office and Valuation, you will have an important role in ensuring we provide quality fund administration services to our… </td>
      <td id="T_c71c4_row103_col2" class="data row103 col2" >12 days ago</td>
      <td id="T_c71c4_row103_col3" class="data row103 col3" >https://ca.indeed.com/jobs?q=Junior%20Associate%20Director%2C%20Middle%20Office%20Operations%2C%20MOV%20Mitsubishi%20UFJ%20Fund%20Services</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row104" class="row_heading level0 row104" >247</th>
      <td id="T_c71c4_row104_col0" class="data row104 col0" >Junior SoC Design Engineer</td>
      <td id="T_c71c4_row104_col1" class="data row104 col1" > The Vancouver ASIC team develops SoCs which power next generation NAND Solid State Drives (SSD) – a key enabler for our data hungry future. </td>
      <td id="T_c71c4_row104_col2" class="data row104 col2" >12 days ago</td>
      <td id="T_c71c4_row104_col3" class="data row104 col3" >https://ca.indeed.com/jobs?q=Junior%20SoC%20Design%20Engineer%20Solidigm</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row105" class="row_heading level0 row105" >248</th>
      <td id="T_c71c4_row105_col0" class="data row105 col0" >Junior Test Automation Specialist / Spécialiste en automatis...</td>
      <td id="T_c71c4_row105_col1" class="data row105 col1" > Develop Python automation scripts to optimize manual execution for: API, UI (Selenium), Mobile (Appium), Cloud (AWS). API, UI or Mobile development experience. </td>
      <td id="T_c71c4_row105_col2" class="data row105 col2" >12 days ago</td>
      <td id="T_c71c4_row105_col3" class="data row105 col3" >https://ca.indeed.com/jobs?q=Junior%20Test%20Automation%20Specialist%20/%20Sp%C3%A9cialiste%20en%20automatis...%20Aruba%20Networks</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row106" class="row_heading level0 row106" >158</th>
      <td id="T_c71c4_row106_col0" class="data row106 col0" >Junior Software Developer-AQE</td>
      <td id="T_c71c4_row106_col1" class="data row106 col1" > In this role you will be able to provide technical insights and expertise to support comprehensive automated verification. Previous experience in software QA. </td>
      <td id="T_c71c4_row106_col2" class="data row106 col2" >Active 12 days ago</td>
      <td id="T_c71c4_row106_col3" class="data row106 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer-AQE%20Keywords%20Studios</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row107" class="row_heading level0 row107" >35</th>
      <td id="T_c71c4_row107_col0" class="data row107 col0" >Jr. Business Analyst</td>
      <td id="T_c71c4_row107_col1" class="data row107 col1" > Experience with clinical data validation is an asset. A general understanding of clinical data workflow is an asset. </td>
      <td id="T_c71c4_row107_col2" class="data row107 col2" >12 days ago</td>
      <td id="T_c71c4_row107_col3" class="data row107 col3" >https://ca.indeed.com/jobs?q=Jr.%20Business%20Analyst%20Dapasoft%20Inc</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row108" class="row_heading level0 row108" >36</th>
      <td id="T_c71c4_row108_col0" class="data row108 col0" >Junior Development Assistant, Data - 060 - Rev Dev</td>
      <td id="T_c71c4_row108_col1" class="data row108 col1" > Your duties will include data entry, data clean up, and some basic data analysis. Reporting to the Senior Officer, Data Assets, you will participate in database… </td>
      <td id="T_c71c4_row108_col2" class="data row108 col2" >12 days ago</td>
      <td id="T_c71c4_row108_col3" class="data row108 col3" >https://ca.indeed.com/jobs?q=Junior%20Development%20Assistant%2C%20Data%20-%20060%20-%20Rev%20Dev%20BCSPCA</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row109" class="row_heading level0 row109" >159</th>
      <td id="T_c71c4_row109_col0" class="data row109 col0" >GIS Assistant</td>
      <td id="T_c71c4_row109_col1" class="data row109 col1" > The GIS Assistant is a junior role that supports the GIS Department with processing, tracking, and recording requests for services. </td>
      <td id="T_c71c4_row109_col2" class="data row109 col2" >13 days ago</td>
      <td id="T_c71c4_row109_col3" class="data row109 col3" >https://ca.indeed.com/jobs?q=GIS%20Assistant%20Lac%20Ste.%20Anne%20County</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row110" class="row_heading level0 row110" >161</th>
      <td id="T_c71c4_row110_col0" class="data row110 col0" >Junior Integration Analyst</td>
      <td id="T_c71c4_row110_col1" class="data row110 col1" > Your role will be to help develop applications, technological options and proposed solutions, from project design to implementation, mainly in production data… </td>
      <td id="T_c71c4_row110_col2" class="data row110 col2" >13 days ago</td>
      <td id="T_c71c4_row110_col3" class="data row110 col3" >https://ca.indeed.com/jobs?q=Junior%20Integration%20Analyst%20BBA%20inc.</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row111" class="row_heading level0 row111" >251</th>
      <td id="T_c71c4_row111_col0" class="data row111 col0" >DevOps Junior / Junior DevOps</td>
      <td id="T_c71c4_row111_col1" class="data row111 col1" > À propos d’OPAL-RT Technologies. OPAL-RT s’est donné comme ambitieux défi de démocratiser la simulation temps réel afin de la rendre accessible à chaque… </td>
      <td id="T_c71c4_row111_col2" class="data row111 col2" >13 days ago</td>
      <td id="T_c71c4_row111_col3" class="data row111 col3" >https://ca.indeed.com/jobs?q=DevOps%20Junior%20/%20Junior%20DevOps%20Opal-RT</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row112" class="row_heading level0 row112" >250</th>
      <td id="T_c71c4_row112_col0" class="data row112 col0" >Junior Pipeline TD</td>
      <td id="T_c71c4_row112_col1" class="data row112 col1" > We facilitate requests and make changes in a timely manner. A Junior Pipeline TD is an entry-level position in the Pipeline department. </td>
      <td id="T_c71c4_row112_col2" class="data row112 col2" >13 days ago</td>
      <td id="T_c71c4_row112_col3" class="data row112 col3" >https://ca.indeed.com/jobs?q=Junior%20Pipeline%20TD%20ICON%20Creative%20Studio</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row113" class="row_heading level0 row113" >249</th>
      <td id="T_c71c4_row113_col0" class="data row113 col0" >Junior Solutions Architect</td>
      <td id="T_c71c4_row113_col1" class="data row113 col1" > Provide technical leadership throughout the development life cycle and focus on delivery of quality solutions. Define standards to guide architectural designs. </td>
      <td id="T_c71c4_row113_col2" class="data row113 col2" >13 days ago</td>
      <td id="T_c71c4_row113_col3" class="data row113 col3" >https://ca.indeed.com/jobs?q=Junior%20Solutions%20Architect%20BIMM</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row114" class="row_heading level0 row114" >37</th>
      <td id="T_c71c4_row114_col0" class="data row114 col0" >Junior Data Analyst</td>
      <td id="T_c71c4_row114_col1" class="data row114 col1" > Providing technical expertise on data storage structures, data mining, and data cleansing. The Junior Data Analyst supports the Development Team by managing… </td>
      <td id="T_c71c4_row114_col2" class="data row114 col2" >Active 13 days ago</td>
      <td id="T_c71c4_row114_col3" class="data row114 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20HALIGHT%20Inc.</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row115" class="row_heading level0 row115" >38</th>
      <td id="T_c71c4_row115_col0" class="data row115 col0" >Analyst, Client Business I</td>
      <td id="T_c71c4_row115_col1" class="data row115 col1" > Works with media partners to distill and analyze their data. Experience using sales data (Nielsen, IRi) required. Manages and tracks all media campaigns. </td>
      <td id="T_c71c4_row115_col2" class="data row115 col2" >13 days ago</td>
      <td id="T_c71c4_row115_col3" class="data row115 col3" >https://ca.indeed.com/jobs?q=Analyst%2C%20Client%20Business%20I%20Mosaic%20North%20America</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row116" class="row_heading level0 row116" >160</th>
      <td id="T_c71c4_row116_col0" class="data row116 col0" >Junior Automation Engineer</td>
      <td id="T_c71c4_row116_col1" class="data row116 col1" > Responsible for programming, definition of technical characteristics and commissioning as part of tailor-made automation solutions; </td>
      <td id="T_c71c4_row116_col2" class="data row116 col2" >13 days ago</td>
      <td id="T_c71c4_row116_col3" class="data row116 col3" >https://ca.indeed.com/jobs?q=Junior%20Automation%20Engineer%20WSP</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row117" class="row_heading level0 row117" >162</th>
      <td id="T_c71c4_row117_col0" class="data row117 col0" >Junior Software Developer</td>
      <td id="T_c71c4_row117_col1" class="data row117 col1" > In this role you will be able to provide technical insights and expertise to support comprehensive automated verification. Fix bugs on existing scripts. </td>
      <td id="T_c71c4_row117_col2" class="data row117 col2" >Active 14 days ago</td>
      <td id="T_c71c4_row117_col3" class="data row117 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20Keywords%20Studios</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row118" class="row_heading level0 row118" >252</th>
      <td id="T_c71c4_row118_col0" class="data row118 col0" >Jr. 2LS Support Engineer</td>
      <td id="T_c71c4_row118_col1" class="data row118 col1" > In this role you can write scripts at a Unix/Linux level (bash, python). Provide Remote Technical Support (RTS) for the Network Services Platform and associated… </td>
      <td id="T_c71c4_row118_col2" class="data row118 col2" >14 days ago</td>
      <td id="T_c71c4_row118_col3" class="data row118 col3" >https://ca.indeed.com/jobs?q=Jr.%202LS%20Support%20Engineer%20NOKIA</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row119" class="row_heading level0 row119" >39</th>
      <td id="T_c71c4_row119_col0" class="data row119 col0" >Junior DBA (Database Administrator)</td>
      <td id="T_c71c4_row119_col1" class="data row119 col1" > Provide DB2 Administrative services to application development team. Design/develop/test/support DB2 LUW database. Performance tuning and trouble shooting. </td>
      <td id="T_c71c4_row119_col2" class="data row119 col2" >Active 14 days ago</td>
      <td id="T_c71c4_row119_col3" class="data row119 col3" >https://ca.indeed.com/jobs?q=Junior%20DBA%20%28Database%20Administrator%29%20Dawn%20InfoTek%20Inc.</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row120" class="row_heading level0 row120" >40</th>
      <td id="T_c71c4_row120_col0" class="data row120 col0" >Junior ESG Research Analyst - Turkish</td>
      <td id="T_c71c4_row120_col1" class="data row120 col1" > As a Junior ESG Research Analyst, you will play a crucial role in supporting RepRisk's growth and global reach by analyzing and entering risk incidents from… </td>
      <td id="T_c71c4_row120_col2" class="data row120 col2" >Active 14 days ago</td>
      <td id="T_c71c4_row120_col3" class="data row120 col3" >https://ca.indeed.com/jobs?q=Junior%20ESG%20Research%20Analyst%20-%20Turkish%20RepRisk</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row121" class="row_heading level0 row121" >41</th>
      <td id="T_c71c4_row121_col0" class="data row121 col0" >Junior Business Analyst</td>
      <td id="T_c71c4_row121_col1" class="data row121 col1" > Roles &amp; Responsibilities: • Elicits and documents requirements using a variety of methods, such as interviews, document analysis, requirements workshops,… </td>
      <td id="T_c71c4_row121_col2" class="data row121 col2" >16 days ago</td>
      <td id="T_c71c4_row121_col3" class="data row121 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20Pivotree</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row122" class="row_heading level0 row122" >164</th>
      <td id="T_c71c4_row122_col0" class="data row122 col0" >Financial Systems Analyst I</td>
      <td id="T_c71c4_row122_col1" class="data row122 col1" > You’ll utilize your customer service, server/network and end-user information technology expertise to support the daily operations of the division’s financial… </td>
      <td id="T_c71c4_row122_col2" class="data row122 col2" >17 days ago</td>
      <td id="T_c71c4_row122_col3" class="data row122 col3" >https://ca.indeed.com/jobs?q=Financial%20Systems%20Analyst%20I%20WorkSafeBC</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row123" class="row_heading level0 row123" >43</th>
      <td id="T_c71c4_row123_col0" class="data row123 col0" >Junior Business Analyst</td>
      <td id="T_c71c4_row123_col1" class="data row123 col1" > Ability to work with large data sets. To keep up with this growth, they have had to make some changes to their various systems. </td>
      <td id="T_c71c4_row123_col2" class="data row123 col2" >17 days ago</td>
      <td id="T_c71c4_row123_col3" class="data row123 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20International%20Financial%20Group</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row124" class="row_heading level0 row124" >42</th>
      <td id="T_c71c4_row124_col0" class="data row124 col0" >Junior AI/Database Administrator</td>
      <td id="T_c71c4_row124_col1" class="data row124 col1" > Databases – design and implement a database to track and monitor a predetermined set of data points. Excel – track and monitor predetermined set of data points… </td>
      <td id="T_c71c4_row124_col2" class="data row124 col2" >17 days ago</td>
      <td id="T_c71c4_row124_col3" class="data row124 col3" >https://ca.indeed.com/jobs?q=Junior%20AI/Database%20Administrator%20Tetra%20Tech</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row125" class="row_heading level0 row125" >253</th>
      <td id="T_c71c4_row125_col0" class="data row125 col0" >Junior Software Engineer</td>
      <td id="T_c71c4_row125_col1" class="data row125 col1" > Aviya provides expertise in program management, systems, software, mechanical, and hardware engineering to many of the top-tier Aerospace and Defense… </td>
      <td id="T_c71c4_row125_col2" class="data row125 col2" >17 days ago</td>
      <td id="T_c71c4_row125_col3" class="data row125 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Engineer%20Aviya%20Aerospace%20Systems</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row126" class="row_heading level0 row126" >163</th>
      <td id="T_c71c4_row126_col0" class="data row126 col0" >Junior Integration Analyst</td>
      <td id="T_c71c4_row126_col1" class="data row126 col1" > Your role will be to help develop applications, technological options and proposed solutions, from project design to implementation, mainly in production data… </td>
      <td id="T_c71c4_row126_col2" class="data row126 col2" >17 days ago</td>
      <td id="T_c71c4_row126_col3" class="data row126 col3" >https://ca.indeed.com/jobs?q=Junior%20Integration%20Analyst%20BBA</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row127" class="row_heading level0 row127" >254</th>
      <td id="T_c71c4_row127_col0" class="data row127 col0" >GIS Support Analyst I</td>
      <td id="T_c71c4_row127_col1" class="data row127 col1" > Compared with other competitive solutions, our products are the only ones that integrate fully with the ArcGIS platform, thereby letting organizations leverage… </td>
      <td id="T_c71c4_row127_col2" class="data row127 col2" >18 days ago</td>
      <td id="T_c71c4_row127_col3" class="data row127 col3" >https://ca.indeed.com/jobs?q=GIS%20Support%20Analyst%20I%20Lim%20Geomatics</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row128" class="row_heading level0 row128" >165</th>
      <td id="T_c71c4_row128_col0" class="data row128 col0" >Junior Web Developer(Digital)</td>
      <td id="T_c71c4_row128_col1" class="data row128 col1" > Reporting to the Solutions Architect, Digital, this role will provide support for front-end aspects of CFIB’s websites (ie. Cfib-fcei.ca and others), while… </td>
      <td id="T_c71c4_row128_col2" class="data row128 col2" >18 days ago</td>
      <td id="T_c71c4_row128_col3" class="data row128 col3" >https://ca.indeed.com/jobs?q=Junior%20Web%20Developer%28Digital%29%20CFIB</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row129" class="row_heading level0 row129" >45</th>
      <td id="T_c71c4_row129_col0" class="data row129 col0" >HR Regional Center Jr Data Analyst - New Westminster</td>
      <td id="T_c71c4_row129_col1" class="data row129 col1" > The HRRC Jr. DA is skilled in process improvement, project management, and data analysis, and they leverage a variety of PXT data platforms, processes, policies… </td>
      <td id="T_c71c4_row129_col2" class="data row129 col2" >18 days ago</td>
      <td id="T_c71c4_row129_col3" class="data row129 col3" >https://ca.indeed.com/jobs?q=HR%20Regional%20Center%20Jr%20Data%20Analyst%20-%20New%20Westminster%20AMZN%20CAN%20Fulfillment%20Svcs%2C%20ULC</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row130" class="row_heading level0 row130" >44</th>
      <td id="T_c71c4_row130_col0" class="data row130 col0" >Junior Analyst, Sales Operations & Planning</td>
      <td id="T_c71c4_row130_col1" class="data row130 col1" > Support sales data and information tracking related to new vendor onboarding. Strong knowledge of Qlikview or similar data analysis / reporting tools. </td>
      <td id="T_c71c4_row130_col2" class="data row130 col2" >18 days ago</td>
      <td id="T_c71c4_row130_col3" class="data row130 col3" >https://ca.indeed.com/jobs?q=Junior%20Analyst%2C%20Sales%20Operations%20%26%20Planning%20UNFI</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row131" class="row_heading level0 row131" >47</th>
      <td id="T_c71c4_row131_col0" class="data row131 col0" >Junior Pricing Analyst</td>
      <td id="T_c71c4_row131_col1" class="data row131 col1" > Two years office experience with knowledge of or exposure to data management philosophies and best practices. Verify and map products to vendor part numbers and… </td>
      <td id="T_c71c4_row131_col2" class="data row131 col2" >18 days ago</td>
      <td id="T_c71c4_row131_col3" class="data row131 col3" >https://ca.indeed.com/jobs?q=Junior%20Pricing%20Analyst%20Marks%20Supply%20Inc</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row132" class="row_heading level0 row132" >46</th>
      <td id="T_c71c4_row132_col0" class="data row132 col0" >Junior Clinical Trials Data Analyst (Hybrid)</td>
      <td id="T_c71c4_row132_col1" class="data row132 col1" > Process clients’ clinical trials data set. Using our tools you will analyze and mitigate the risk of re-identification for trial participants whose data appears… </td>
      <td id="T_c71c4_row132_col2" class="data row132 col2" >18 days ago</td>
      <td id="T_c71c4_row132_col3" class="data row132 col3" >https://ca.indeed.com/jobs?q=Junior%20Clinical%20Trials%20Data%20Analyst%20%28Hybrid%29%20IQVIA</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row133" class="row_heading level0 row133" >255</th>
      <td id="T_c71c4_row133_col0" class="data row133 col0" >Junior Cloud Engineer OTW</td>
      <td id="T_c71c4_row133_col1" class="data row133 col1" > Our CI/CD and System integration department plays a strategic role in making sure that the Cloud RAN solutions meet our customers’ expectations. </td>
      <td id="T_c71c4_row133_col2" class="data row133 col2" >18 days ago</td>
      <td id="T_c71c4_row133_col3" class="data row133 col3" >https://ca.indeed.com/jobs?q=Junior%20Cloud%20Engineer%20OTW%20Ericsson</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row134" class="row_heading level0 row134" >50</th>
      <td id="T_c71c4_row134_col0" class="data row134 col0" >Oracle Database Administrator Jr</td>
      <td id="T_c71c4_row134_col1" class="data row134 col1" > Understanding of relational and dimensional data modeling. By submitting your application, you consent to Equisoft collecting, using &amp; storing your personal… </td>
      <td id="T_c71c4_row134_col2" class="data row134 col2" >19 days ago</td>
      <td id="T_c71c4_row134_col3" class="data row134 col3" >https://ca.indeed.com/jobs?q=Oracle%20Database%20Administrator%20Jr%20Equisoft</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row135" class="row_heading level0 row135" >49</th>
      <td id="T_c71c4_row135_col0" class="data row135 col0" >Junior Data Entry Operator</td>
      <td id="T_c71c4_row135_col1" class="data row135 col1" > Job type: Temporary | Full time. 4% vacation pay paid out on each weekly pay cheque. Medical and dental benefits once qualified. </td>
      <td id="T_c71c4_row135_col2" class="data row135 col2" >19 days ago</td>
      <td id="T_c71c4_row135_col3" class="data row135 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Entry%20Operator%20Adecco%20Canada</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row136" class="row_heading level0 row136" >48</th>
      <td id="T_c71c4_row136_col0" class="data row136 col0" >Junior Financial Analyst</td>
      <td id="T_c71c4_row136_col1" class="data row136 col1" > Input data for structuring of deals, including rent rolls, proformas, and construction budgets. Write CIMs (including maps, tenant overviews, market data etc.),… </td>
      <td id="T_c71c4_row136_col2" class="data row136 col2" >19 days ago</td>
      <td id="T_c71c4_row136_col3" class="data row136 col3" >https://ca.indeed.com/jobs?q=Junior%20Financial%20Analyst%20Colliers%20International</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row137" class="row_heading level0 row137" >166</th>
      <td id="T_c71c4_row137_col0" class="data row137 col0" >Industrial Engineer I</td>
      <td id="T_c71c4_row137_col1" class="data row137 col1" > The Industrial Engineer I drives continuous improvement in all areas of the business. You, as an Industrial Engineer I, will work with multiple departments to… </td>
      <td id="T_c71c4_row137_col2" class="data row137 col2" >19 days ago</td>
      <td id="T_c71c4_row137_col3" class="data row137 col3" >https://ca.indeed.com/jobs?q=Industrial%20Engineer%20I%20SCC%20UPS%20SCS%2C%20Inc.</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row138" class="row_heading level0 row138" >167</th>
      <td id="T_c71c4_row138_col0" class="data row138 col0" >Développeur Python/Go junior</td>
      <td id="T_c71c4_row138_col1" class="data row138 col1" > Nous sommes une équipe multidisciplinaire de six développeurs au sein d’un groupe de transformation DevOps et d’adoption du Cloud. Une expérience avec un Cloud. </td>
      <td id="T_c71c4_row138_col2" class="data row138 col2" >19 days ago</td>
      <td id="T_c71c4_row138_col3" class="data row138 col3" >https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20Python/Go%20junior%20Banque%20Nationale%20du%20Canada</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row139" class="row_heading level0 row139" >256</th>
      <td id="T_c71c4_row139_col0" class="data row139 col0" >DevOps Specialist Junior</td>
      <td id="T_c71c4_row139_col1" class="data row139 col1" > **Excellent Knowledge of English and French are required for this position***. Equisoft, a world leader in digital business solutions for the insurance and… </td>
      <td id="T_c71c4_row139_col2" class="data row139 col2" >19 days ago</td>
      <td id="T_c71c4_row139_col3" class="data row139 col3" >https://ca.indeed.com/jobs?q=DevOps%20Specialist%20Junior%20Equisoft</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row140" class="row_heading level0 row140" >257</th>
      <td id="T_c71c4_row140_col0" class="data row140 col0" >Spécialiste DevOps Junior</td>
      <td id="T_c71c4_row140_col1" class="data row140 col1" > Automatiser et aligner le processus de construction (CI), de déploiement (CD), de maintenance et de mise à niveau des technologies supportant l'application. </td>
      <td id="T_c71c4_row140_col2" class="data row140 col2" >19 days ago</td>
      <td id="T_c71c4_row140_col3" class="data row140 col3" >https://ca.indeed.com/jobs?q=Sp%C3%A9cialiste%20DevOps%20Junior%20Equisoft</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row141" class="row_heading level0 row141" >258</th>
      <td id="T_c71c4_row141_col0" class="data row141 col0" >Junior Python /Go Developer</td>
      <td id="T_c71c4_row141_col1" class="data row141 col1" > In order to start new initiatives, we are looking for three more developers, with intermediate to senior levels. Good collaboration attitude and autonomy. </td>
      <td id="T_c71c4_row141_col2" class="data row141 col2" >19 days ago</td>
      <td id="T_c71c4_row141_col3" class="data row141 col3" >https://ca.indeed.com/jobs?q=Junior%20Python%20/Go%20Developer%20National%20Bank%20of%20Canada</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row142" class="row_heading level0 row142" >51</th>
      <td id="T_c71c4_row142_col0" class="data row142 col0" >Junior Data Engineer</td>
      <td id="T_c71c4_row142_col1" class="data row142 col1" > Work with data engineers, analysts, data scientists, and game developers to determine the data needs of our games. Experience with SQL and database management. </td>
      <td id="T_c71c4_row142_col2" class="data row142 col2" >19 days ago</td>
      <td id="T_c71c4_row142_col3" class="data row142 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Engineer%20Hothead%20Games</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row143" class="row_heading level0 row143" >169</th>
      <td id="T_c71c4_row143_col0" class="data row143 col0" >Technical Support Specialist I</td>
      <td id="T_c71c4_row143_col1" class="data row143 col1" > Our Technical Support Specialists manage and develop key relationships with our enterprise and small business customers as the first key point of contact for… </td>
      <td id="T_c71c4_row143_col2" class="data row143 col2" >20 days ago</td>
      <td id="T_c71c4_row143_col3" class="data row143 col3" >https://ca.indeed.com/jobs?q=Technical%20Support%20Specialist%20I%20Coconut%20Software</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row144" class="row_heading level0 row144" >168</th>
      <td id="T_c71c4_row144_col0" class="data row144 col0" >Jr. Internal Auditor</td>
      <td id="T_c71c4_row144_col1" class="data row144 col1" > Our Internal Audit function works closely with various departments to provide value throughout our organization. Provide regular written feedback on findings. </td>
      <td id="T_c71c4_row144_col2" class="data row144 col2" >20 days ago</td>
      <td id="T_c71c4_row144_col3" class="data row144 col3" >https://ca.indeed.com/jobs?q=Jr.%20Internal%20Auditor%20Bison%20Transport</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row145" class="row_heading level0 row145" >52</th>
      <td id="T_c71c4_row145_col0" class="data row145 col0" >Développeur BI junior</td>
      <td id="T_c71c4_row145_col1" class="data row145 col1" > La réussite de CGI repose sur le talent et l’engagement de nos professionnels. CGI favorise l’équité en matière d’emploi. </td>
      <td id="T_c71c4_row145_col2" class="data row145 col2" >20 days ago</td>
      <td id="T_c71c4_row145_col3" class="data row145 col3" >https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20BI%20junior%20CGI</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row146" class="row_heading level0 row146" >259</th>
      <td id="T_c71c4_row146_col0" class="data row146 col0" >Junior Python Solution Developer for Jeppesen - a Boeing Com...</td>
      <td id="T_c71c4_row146_col1" class="data row146 col1" > As a Junior Software Solution Developer, you will work on our various software solutions for commercial airlines. 2+ years of working in software development. </td>
      <td id="T_c71c4_row146_col2" class="data row146 col2" >20 days ago</td>
      <td id="T_c71c4_row146_col3" class="data row146 col3" >https://ca.indeed.com/jobs?q=Junior%20Python%20Solution%20Developer%20for%20Jeppesen%20-%20a%20Boeing%20Com...%20Sigma%20Software</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row147" class="row_heading level0 row147" >261</th>
      <td id="T_c71c4_row147_col0" class="data row147 col0" >Junior Site Reliability Engineer Developer</td>
      <td id="T_c71c4_row147_col1" class="data row147 col1" > This role reports to our Shared Capabilities organization, and you’ll have the opportunity to learn and grow, expanding your knowledge base and getting hands-on… </td>
      <td id="T_c71c4_row147_col2" class="data row147 col2" >21 days ago</td>
      <td id="T_c71c4_row147_col3" class="data row147 col3" >https://ca.indeed.com/jobs?q=Junior%20Site%20Reliability%20Engineer%20Developer%20Royal%20Bank%20of%20Canada</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row148" class="row_heading level0 row148" >260</th>
      <td id="T_c71c4_row148_col0" class="data row148 col0" >Junior Mechanical Engineer</td>
      <td id="T_c71c4_row148_col1" class="data row148 col1" > We are seeking a Junior Mechanical Engineer to join our Process and Mine Infrastructure Design team on a full-time basis based in our Sudbury or Mississauga… </td>
      <td id="T_c71c4_row148_col2" class="data row148 col2" >21 days ago</td>
      <td id="T_c71c4_row148_col3" class="data row148 col3" >https://ca.indeed.com/jobs?q=Junior%20Mechanical%20Engineer%20WSP</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row149" class="row_heading level0 row149" >170</th>
      <td id="T_c71c4_row149_col0" class="data row149 col0" >Junior Full Stack Web Developer</td>
      <td id="T_c71c4_row149_col1" class="data row149 col1" > Tradable Bits is the leading fan-based marketing software platform for music and sports. We’re charting the path to personalized fan experiences for online and… </td>
      <td id="T_c71c4_row149_col2" class="data row149 col2" >23 days ago</td>
      <td id="T_c71c4_row149_col3" class="data row149 col3" >https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Web%20Developer%20TradableBits%20Media%20Inc.</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row150" class="row_heading level0 row150" >54</th>
      <td id="T_c71c4_row150_col0" class="data row150 col0" >Junior Data Warehouse Engineer (Local or Remote)</td>
      <td id="T_c71c4_row150_col1" class="data row150 col1" > Participate in data analysis and data architecture direction with valuable client facing development insights. (bonus) Dimensional data modeling experience. </td>
      <td id="T_c71c4_row150_col2" class="data row150 col2" >23 days ago</td>
      <td id="T_c71c4_row150_col3" class="data row150 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Warehouse%20Engineer%20%28Local%20or%20Remote%29%20Stellaralgo</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row151" class="row_heading level0 row151" >53</th>
      <td id="T_c71c4_row151_col0" class="data row151 col0" >IT Support – Junior Data Coordinator</td>
      <td id="T_c71c4_row151_col1" class="data row151 col1" > Coordinate and manipulate all data that is derived from WM Systems. Create reports in Microsoft Excel, Word and PowerPoint as required. </td>
      <td id="T_c71c4_row151_col2" class="data row151 col2" >23 days ago</td>
      <td id="T_c71c4_row151_col3" class="data row151 col3" >https://ca.indeed.com/jobs?q=IT%20Support%20%E2%80%93%20Junior%20Data%20Coordinator%20Wellsite%20Masters</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row152" class="row_heading level0 row152" >171</th>
      <td id="T_c71c4_row152_col0" class="data row152 col0" >Jr. Aero/Mech Engineer</td>
      <td id="T_c71c4_row152_col1" class="data row152 col1" > Responsible to the Supervisor, CH149 Engineering, for the conduct of engineering support and life-cycle management of CH149 Cormorant airframe structures and/or… </td>
      <td id="T_c71c4_row152_col2" class="data row152 col2" >24 days ago</td>
      <td id="T_c71c4_row152_col3" class="data row152 col3" >https://ca.indeed.com/jobs?q=Jr.%20Aero/Mech%20Engineer%20IMP%20Group</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row153" class="row_heading level0 row153" >264</th>
      <td id="T_c71c4_row153_col0" class="data row153 col0" >COMPOSITOR - JUNIOR</td>
      <td id="T_c71c4_row153_col1" class="data row153 col1" > Great artistic sense and aesthetic a must. Strong Nuke proficiency, including good organization of scripts and workflow. Knowledge of Python coding is a bonus. </td>
      <td id="T_c71c4_row153_col2" class="data row153 col2" >24 days ago</td>
      <td id="T_c71c4_row153_col3" class="data row153 col3" >https://ca.indeed.com/jobs?q=COMPOSITOR%20-%20JUNIOR%20Tryptyc</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row154" class="row_heading level0 row154" >267</th>
      <td id="T_c71c4_row154_col0" class="data row154 col0" >Support Center Analyst I</td>
      <td id="T_c71c4_row154_col1" class="data row154 col1" > Scripting experience in one or more languages (bash, python). The Support Centre is responsible for providing 24x7x365 monitoring and operational support of our… </td>
      <td id="T_c71c4_row154_col2" class="data row154 col2" >25 days ago</td>
      <td id="T_c71c4_row154_col3" class="data row154 col3" >https://ca.indeed.com/jobs?q=Support%20Center%20Analyst%20I%20eSentire</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row155" class="row_heading level0 row155" >266</th>
      <td id="T_c71c4_row155_col0" class="data row155 col0" >Jr. Network Automation Developer</td>
      <td id="T_c71c4_row155_col1" class="data row155 col1" > The Nokia Network Management Engineering (NME) teams provide Professional Services in support of real-world deployments of Advanced Solutions across the ION (IP… </td>
      <td id="T_c71c4_row155_col2" class="data row155 col2" >25 days ago</td>
      <td id="T_c71c4_row155_col3" class="data row155 col3" >https://ca.indeed.com/jobs?q=Jr.%20Network%20Automation%20Developer%20NOKIA</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row156" class="row_heading level0 row156" >55</th>
      <td id="T_c71c4_row156_col0" class="data row156 col0" >Financial Analyst - Junior Level</td>
      <td id="T_c71c4_row156_col1" class="data row156 col1" > Influence business decisions through analysis of financial and operational data. ParaMed finance supports your development through company sponsored educational… </td>
      <td id="T_c71c4_row156_col2" class="data row156 col2" >25 days ago</td>
      <td id="T_c71c4_row156_col3" class="data row156 col3" >https://ca.indeed.com/jobs?q=Financial%20Analyst%20-%20Junior%20Level%20Extendicare%20Canada</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row157" class="row_heading level0 row157" >265</th>
      <td id="T_c71c4_row157_col0" class="data row157 col0" >Junior DevOps Engineer (Consumer Services Policy and Chargin...</td>
      <td id="T_c71c4_row157_col1" class="data row157 col1" > Be a part of a transformational journey with innovative talent and leading edge technologies. Your customer-centric ideas will drive improvements to our… </td>
      <td id="T_c71c4_row157_col2" class="data row157 col2" >25 days ago</td>
      <td id="T_c71c4_row157_col3" class="data row157 col3" >https://ca.indeed.com/jobs?q=Junior%20DevOps%20Engineer%20%28Consumer%20Services%20Policy%20and%20Chargin...%20TELUS</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row158" class="row_heading level0 row158" >268</th>
      <td id="T_c71c4_row158_col0" class="data row158 col0" >Scientifique des données marketing junior</td>
      <td id="T_c71c4_row158_col1" class="data row158 col1" > Vos tâches consisteront à préparer les données pour soutenir la construction de modèles, à communiquer avec les différentes parties prenantes (marketing, ventes… </td>
      <td id="T_c71c4_row158_col2" class="data row158 col2" >26 days ago</td>
      <td id="T_c71c4_row158_col3" class="data row158 col3" >https://ca.indeed.com/jobs?q=Scientifique%20des%20donn%C3%A9es%20marketing%20junior%20Pages%20Jaunes%20Solutions%20Num%C3%A9riques%20et%20M%C3%A9dias...</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row159" class="row_heading level0 row159" >56</th>
      <td id="T_c71c4_row159_col0" class="data row159 col0" >Junior, Cybersecurity Specialist Data Protection</td>
      <td id="T_c71c4_row159_col1" class="data row159 col1" > 1+ years of experience in administering data protection controls, data governance, regulatory requirements, PII and privacy protection, data risk assessments… </td>
      <td id="T_c71c4_row159_col2" class="data row159 col2" >26 days ago</td>
      <td id="T_c71c4_row159_col3" class="data row159 col3" >https://ca.indeed.com/jobs?q=Junior%2C%20Cybersecurity%20Specialist%20Data%20Protection%20Questrade%20Financial%20Group</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row160" class="row_heading level0 row160" >57</th>
      <td id="T_c71c4_row160_col0" class="data row160 col0" >Junior Marketing Data Scientist</td>
      <td id="T_c71c4_row160_col1" class="data row160 col1" > Experience in designing and developing ML model (data preparation, data validation, training tuning and production). Demonstrated Skill using SQL and Excel. </td>
      <td id="T_c71c4_row160_col2" class="data row160 col2" >26 days ago</td>
      <td id="T_c71c4_row160_col3" class="data row160 col3" >https://ca.indeed.com/jobs?q=Junior%20Marketing%20Data%20Scientist%20Pages%20Jaunes%20Solutions%20Num%C3%A9riques%20et%20M%C3%A9dias...</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row161" class="row_heading level0 row161" >172</th>
      <td id="T_c71c4_row161_col0" class="data row161 col0" >Développeur(se) Junior</td>
      <td id="T_c71c4_row161_col1" class="data row161 col1" > / Carry out projects with potential returns and economic benefits for Quebecers. / Collaborate on dynamic teams with high-level professionals committed to… </td>
      <td id="T_c71c4_row161_col2" class="data row161 col2" >26 days ago</td>
      <td id="T_c71c4_row161_col3" class="data row161 col3" >https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%28se%29%20Junior%20Caisse%20de%20d%C3%A9p%C3%B4t%20et%20placement%20du%20Qu%C3%A9bec</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row162" class="row_heading level0 row162" >269</th>
      <td id="T_c71c4_row162_col0" class="data row162 col0" >Jr. Full Stack Developer</td>
      <td id="T_c71c4_row162_col1" class="data row162 col1" > As a Jr. Full Stack Developer, you will work on the latest technologies and with a variety of clients ranging from the public sector and private to start-ups. </td>
      <td id="T_c71c4_row162_col2" class="data row162 col2" >26 days ago</td>
      <td id="T_c71c4_row162_col3" class="data row162 col3" >https://ca.indeed.com/jobs?q=Jr.%20Full%20Stack%20Developer%20AOT%20Technologies</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row163" class="row_heading level0 row163" >270</th>
      <td id="T_c71c4_row163_col0" class="data row163 col0" >Software Engineer I/II</td>
      <td id="T_c71c4_row163_col1" class="data row163 col1" > You will have opportunities to work on multiple layers of the technology stack, ranging from customer-focused user experience work, building scalable… </td>
      <td id="T_c71c4_row163_col2" class="data row163 col2" >26 days ago</td>
      <td id="T_c71c4_row163_col3" class="data row163 col3" >https://ca.indeed.com/jobs?q=Software%20Engineer%20I/II%20Microsoft</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row164" class="row_heading level0 row164" >174</th>
      <td id="T_c71c4_row164_col0" class="data row164 col0" >Junior Developer Analyst</td>
      <td id="T_c71c4_row164_col1" class="data row164 col1" > Looking for junior/intermediate candidates getting started in their career and have room to grow - Specifically (2 – 5 years of experience). </td>
      <td id="T_c71c4_row164_col2" class="data row164 col2" >27 days ago</td>
      <td id="T_c71c4_row164_col3" class="data row164 col3" >https://ca.indeed.com/jobs?q=Junior%20Developer%20Analyst%20Fujitsu</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row165" class="row_heading level0 row165" >58</th>
      <td id="T_c71c4_row165_col0" class="data row165 col0" >Junior Data Governance & Data Quality Specialist</td>
      <td id="T_c71c4_row165_col1" class="data row165 col1" > The candidate must be able to communicate effectively with team members and have an understanding of data analysis, data quality, data security, data movement,… </td>
      <td id="T_c71c4_row165_col2" class="data row165 col2" >27 days ago</td>
      <td id="T_c71c4_row165_col3" class="data row165 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Governance%20%26%20Data%20Quality%20Specialist%20Procom</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row166" class="row_heading level0 row166" >173</th>
      <td id="T_c71c4_row166_col0" class="data row166 col0" >Salesforce Technologist - Junior</td>
      <td id="T_c71c4_row166_col1" class="data row166 col1" > You will be supporting our customers through a wide range of scenarios including defining business process, analyzing requirements, implementing in the… </td>
      <td id="T_c71c4_row166_col2" class="data row166 col2" >27 days ago</td>
      <td id="T_c71c4_row166_col3" class="data row166 col3" >https://ca.indeed.com/jobs?q=Salesforce%20Technologist%20-%20Junior%20Procom</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row167" class="row_heading level0 row167" >59</th>
      <td id="T_c71c4_row167_col0" class="data row167 col0" >Summer Opportunity -Jr. Financial Analyst</td>
      <td id="T_c71c4_row167_col1" class="data row167 col1" > Assist in the maintenance of data models used for the annual budgeting process and ongoing. The Co-op Student, Jr. Financial Analyst will take on a supporting… </td>
      <td id="T_c71c4_row167_col2" class="data row167 col2" >28 days ago</td>
      <td id="T_c71c4_row167_col3" class="data row167 col3" >https://ca.indeed.com/jobs?q=Summer%20Opportunity%20-Jr.%20Financial%20Analyst%20Hazelview%20Properties%20Services%20Inc.</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row168" class="row_heading level0 row168" >271</th>
      <td id="T_c71c4_row168_col0" class="data row168 col0" >Rigging Artist (Junior/Senior)</td>
      <td id="T_c71c4_row168_col1" class="data row168 col1" > Various types of Rigging including human, creatures, and props in Maya. Proficiency in Mel/Python script. Work condition: Project Contract or Permanent full… </td>
      <td id="T_c71c4_row168_col2" class="data row168 col2" >Active 28 days ago</td>
      <td id="T_c71c4_row168_col3" class="data row168 col3" >https://ca.indeed.com/jobs?q=Rigging%20Artist%20%28Junior/Senior%29%20Studio%20Eon%20Productions</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row169" class="row_heading level0 row169" >175</th>
      <td id="T_c71c4_row169_col0" class="data row169 col0" >Junior Front-End Web Developer</td>
      <td id="T_c71c4_row169_col1" class="data row169 col1" > Entry to Intermediate (1-3 years working experience). Main responsibilities will include interpretation of UI/UX wireframes, creating an inventory of required… </td>
      <td id="T_c71c4_row169_col2" class="data row169 col2" >28 days ago</td>
      <td id="T_c71c4_row169_col3" class="data row169 col3" >https://ca.indeed.com/jobs?q=Junior%20Front-End%20Web%20Developer%20ONR</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row170" class="row_heading level0 row170" >313</th>
      <td id="T_c71c4_row170_col0" class="data row170 col0" >Junior Python Developer</td>
      <td id="T_c71c4_row170_col1" class="data row170 col1" > Production Technology is an umbrella term used to describe the group of people supporting, developing and improving the tools and technologies that artists use… </td>
      <td id="T_c71c4_row170_col2" class="data row170 col2" >30+ days ago</td>
      <td id="T_c71c4_row170_col3" class="data row170 col3" >https://ca.indeed.com/jobs?q=Junior%20Python%20Developer%20DNEG</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row171" class="row_heading level0 row171" >295</th>
      <td id="T_c71c4_row171_col0" class="data row171 col0" >Junior Software Developer (DataHub Team)</td>
      <td id="T_c71c4_row171_col1" class="data row171 col1" > You love solving problems and enjoy getting to the root cause of issues. You enjoy exploring new technologies to deliver a reliable, secure, and highly… </td>
      <td id="T_c71c4_row171_col2" class="data row171 col2" >30+ days ago</td>
      <td id="T_c71c4_row171_col3" class="data row171 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20%28DataHub%20Team%29%20Pason%20Systems%20Corp</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row172" class="row_heading level0 row172" >296</th>
      <td id="T_c71c4_row172_col0" class="data row172 col0" >BIOINFORMATICS SCIENTIST I - CA</td>
      <td id="T_c71c4_row172_col1" class="data row172 col1" > This position is responsible for in-depth in-silico bioinformatics analysis required for development of sequencing and other molecular methods, bio surveillance… </td>
      <td id="T_c71c4_row172_col2" class="data row172 col2" >30+ days ago</td>
      <td id="T_c71c4_row172_col3" class="data row172 col3" >https://ca.indeed.com/jobs?q=BIOINFORMATICS%20SCIENTIST%20I%20-%20CA%20Luminex</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row173" class="row_heading level0 row173" >297</th>
      <td id="T_c71c4_row173_col0" class="data row173 col0" >Junior Software Control Engineer</td>
      <td id="T_c71c4_row173_col1" class="data row173 col1" > Candu Energy Inc. is a leading full-service nuclear technology company and committed to design and deliver state-of-the-art CANDU® reactors, carry out life… </td>
      <td id="T_c71c4_row173_col2" class="data row173 col2" >30+ days ago</td>
      <td id="T_c71c4_row173_col3" class="data row173 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Control%20Engineer%20SNC-Lavalin</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row174" class="row_heading level0 row174" >298</th>
      <td id="T_c71c4_row174_col0" class="data row174 col0" >Software Engineer I - Quartz Core Developer</td>
      <td id="T_c71c4_row174_col1" class="data row174 col1" > Thousands of developers are using the highly-agile platform to deliver applications to thousands of end users. Linux compute farms on-tap. </td>
      <td id="T_c71c4_row174_col2" class="data row174 col2" >30+ days ago</td>
      <td id="T_c71c4_row174_col3" class="data row174 col3" >https://ca.indeed.com/jobs?q=Software%20Engineer%20I%20-%20Quartz%20Core%20Developer%20Bank%20of%20America</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row175" class="row_heading level0 row175" >299</th>
      <td id="T_c71c4_row175_col0" class="data row175 col0" >Junior Software Engineer - Full Stack</td>
      <td id="T_c71c4_row175_col1" class="data row175 col1" > Collaborate with team members to get a better understanding of your user stories. Develop elegant features and solutions for our web and mobile platforms. </td>
      <td id="T_c71c4_row175_col2" class="data row175 col2" >30+ days ago</td>
      <td id="T_c71c4_row175_col3" class="data row175 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Engineer%20-%20Full%20Stack%20RideCo</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row176" class="row_heading level0 row176" >300</th>
      <td id="T_c71c4_row176_col0" class="data row176 col0" >Junior Software Developers</td>
      <td id="T_c71c4_row176_col1" class="data row176 col1" > This position is responsible for the development, evaluation, implementation and maintenance of new software solutions, including maintenance and development of… </td>
      <td id="T_c71c4_row176_col2" class="data row176 col2" >30+ days ago</td>
      <td id="T_c71c4_row176_col3" class="data row176 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developers%20David%20Aplin%20Group</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row177" class="row_heading level0 row177" >301</th>
      <td id="T_c71c4_row177_col0" class="data row177 col0" >Junior DevOps Engineer</td>
      <td id="T_c71c4_row177_col1" class="data row177 col1" > This job involves development and maintenance of scalable, secure and highly-available services and infrastructure for online gaming such as player progression,… </td>
      <td id="T_c71c4_row177_col2" class="data row177 col2" >30+ days ago</td>
      <td id="T_c71c4_row177_col3" class="data row177 col3" >https://ca.indeed.com/jobs?q=Junior%20DevOps%20Engineer%20Hellbent%20Games</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row178" class="row_heading level0 row178" >302</th>
      <td id="T_c71c4_row178_col0" class="data row178 col0" >Junior Software Developer</td>
      <td id="T_c71c4_row178_col1" class="data row178 col1" > We encourage cross functional developers to not only learn programming languages, but also the related tools and supporting systems. </td>
      <td id="T_c71c4_row178_col2" class="data row178 col2" >30+ days ago</td>
      <td id="T_c71c4_row178_col3" class="data row178 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20Prolucid%20Technologies</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row179" class="row_heading level0 row179" >314</th>
      <td id="T_c71c4_row179_col0" class="data row179 col0" >Junior Systems Engineer (New Graduate)</td>
      <td id="T_c71c4_row179_col1" class="data row179 col1" > Aviya provides expertise in program management, systems, software, mechanical, and hardware engineering to many of the top-tier Aerospace and Defense… </td>
      <td id="T_c71c4_row179_col2" class="data row179 col2" >30+ days ago</td>
      <td id="T_c71c4_row179_col3" class="data row179 col3" >https://ca.indeed.com/jobs?q=Junior%20Systems%20Engineer%20%28New%20Graduate%29%20Aviya%20Aerospace%20Systems</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row180" class="row_heading level0 row180" >303</th>
      <td id="T_c71c4_row180_col0" class="data row180 col0" >Junior Software Developer</td>
      <td id="T_c71c4_row180_col1" class="data row180 col1" > Wedge Networks is seeking candidates to fill a junior software development position on our research and development team, developing software for our network… </td>
      <td id="T_c71c4_row180_col2" class="data row180 col2" >30+ days ago</td>
      <td id="T_c71c4_row180_col3" class="data row180 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20Wedge%20Networks</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row181" class="row_heading level0 row181" >305</th>
      <td id="T_c71c4_row181_col0" class="data row181 col0" >Junior Firmware Engineer</td>
      <td id="T_c71c4_row181_col1" class="data row181 col1" > Participate in the development of next-generation smart grid communication devices and equipment. Involve in system design discussions and provide comprehensive… </td>
      <td id="T_c71c4_row181_col2" class="data row181 col2" >30+ days ago</td>
      <td id="T_c71c4_row181_col3" class="data row181 col3" >https://ca.indeed.com/jobs?q=Junior%20Firmware%20Engineer%20Corinex%20Communications</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row182" class="row_heading level0 row182" >306</th>
      <td id="T_c71c4_row182_col0" class="data row182 col0" >Python Developer (Consultant I)</td>
      <td id="T_c71c4_row182_col1" class="data row182 col1" > Our delivery model provides market-leading business outcomes using EXL’s proprietary Business EXLerator Framework™, cutting-edge analytics, digital… </td>
      <td id="T_c71c4_row182_col2" class="data row182 col2" >30+ days ago</td>
      <td id="T_c71c4_row182_col3" class="data row182 col3" >https://ca.indeed.com/jobs?q=Python%20Developer%20%28Consultant%20I%29%20EXL%20Services</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row183" class="row_heading level0 row183" >307</th>
      <td id="T_c71c4_row183_col0" class="data row183 col0" >Junior Electronics Engineer - Integration and Testing</td>
      <td id="T_c71c4_row183_col1" class="data row183 col1" > Basic programming skills in C, Labview or python. Salary starting at $55,000 depending on experience. Training and development opportunities in a growing… </td>
      <td id="T_c71c4_row183_col2" class="data row183 col2" >30+ days ago</td>
      <td id="T_c71c4_row183_col3" class="data row183 col3" >https://ca.indeed.com/jobs?q=Junior%20Electronics%20Engineer%20-%20Integration%20and%20Testing%20Preciseley%20Microtechnology</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row184" class="row_heading level0 row184" >308</th>
      <td id="T_c71c4_row184_col0" class="data row184 col0" >Analyste junior autochtone (Poste pouvant être situé n'impor...</td>
      <td id="T_c71c4_row184_col1" class="data row184 col1" > La diversité et l’inclusion guident tout ce que nous faisons à la SCHL. Vous aurez également à utiliser les outils appropriés (y compris R ou Python) pour… </td>
      <td id="T_c71c4_row184_col2" class="data row184 col2" >30+ days ago</td>
      <td id="T_c71c4_row184_col3" class="data row184 col3" >https://ca.indeed.com/jobs?q=Analyste%20junior%20autochtone%20%28Poste%20pouvant%20%C3%AAtre%20situ%C3%A9%20n%27impor...%20CMHC</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row185" class="row_heading level0 row185" >309</th>
      <td id="T_c71c4_row185_col0" class="data row185 col0" >Junior Electrical Engineer</td>
      <td id="T_c71c4_row185_col1" class="data row185 col1" > Work collaboratively with clients, project managers, engineers, designers and drafters in the preparation of deliverables to BBA and client standards. </td>
      <td id="T_c71c4_row185_col2" class="data row185 col2" >30+ days ago</td>
      <td id="T_c71c4_row185_col3" class="data row185 col3" >https://ca.indeed.com/jobs?q=Junior%20Electrical%20Engineer%20BBA%20inc.</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row186" class="row_heading level0 row186" >310</th>
      <td id="T_c71c4_row186_col0" class="data row186 col0" >Junior Software Developer</td>
      <td id="T_c71c4_row186_col1" class="data row186 col1" > Financial Risk Analytics is part of the IHS Markit group and provides industry leading risk analytics solutions to sell side institutions within the financial… </td>
      <td id="T_c71c4_row186_col2" class="data row186 col2" >30+ days ago</td>
      <td id="T_c71c4_row186_col3" class="data row186 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20S%26P%20Global</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row187" class="row_heading level0 row187" >311</th>
      <td id="T_c71c4_row187_col0" class="data row187 col0" >Junior Electrical Engineer</td>
      <td id="T_c71c4_row187_col1" class="data row187 col1" > Work collaboratively with clients, project managers, engineers, designers and drafters in the preparation of deliverables to BBA and client standards. </td>
      <td id="T_c71c4_row187_col2" class="data row187 col2" >30+ days ago</td>
      <td id="T_c71c4_row187_col3" class="data row187 col3" >https://ca.indeed.com/jobs?q=Junior%20Electrical%20Engineer%20BBA</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row188" class="row_heading level0 row188" >312</th>
      <td id="T_c71c4_row188_col0" class="data row188 col0" >Développeur Python junior</td>
      <td id="T_c71c4_row188_col1" class="data row188 col1" > Veuillez noter que ce poste est en télétravail. Téléphone, Microsoft Teams ou Zoom, comme vous préférez ! Analyser les exigences des clients et des utilisateurs… </td>
      <td id="T_c71c4_row188_col2" class="data row188 col2" >30+ days ago</td>
      <td id="T_c71c4_row188_col3" class="data row188 col3" >https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%20Python%20junior%20Alithya</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row189" class="row_heading level0 row189" >294</th>
      <td id="T_c71c4_row189_col0" class="data row189 col0" >Junior Product Management Specialist</td>
      <td id="T_c71c4_row189_col1" class="data row189 col1" > The successful candidate will join the Product Management team and specialize in solution documentation. In this position you would be responsible for sourcing,… </td>
      <td id="T_c71c4_row189_col2" class="data row189 col2" >30+ days ago</td>
      <td id="T_c71c4_row189_col3" class="data row189 col3" >https://ca.indeed.com/jobs?q=Junior%20Product%20Management%20Specialist%20Fortinet</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row190" class="row_heading level0 row190" >304</th>
      <td id="T_c71c4_row190_col0" class="data row190 col0" >Jr. Photonic System Test Specialist</td>
      <td id="T_c71c4_row190_col1" class="data row190 col1" > Our Advanced Optics Team within the Fixed Networks Broadband Networks organization is looking for a Photonics System Test Specialist in Ottawa. </td>
      <td id="T_c71c4_row190_col2" class="data row190 col2" >30+ days ago</td>
      <td id="T_c71c4_row190_col3" class="data row190 col3" >https://ca.indeed.com/jobs?q=Jr.%20Photonic%20System%20Test%20Specialist%20NOKIA</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row191" class="row_heading level0 row191" >293</th>
      <td id="T_c71c4_row191_col0" class="data row191 col0" >Jr. / Int. Software Engineering (12mo fixed term)</td>
      <td id="T_c71c4_row191_col1" class="data row191 col1" > Magellan Aerospace, Winnipeg is looking for a high performing Entry Level (or Intermediate) Software Engineering/Developer to join our development team. </td>
      <td id="T_c71c4_row191_col2" class="data row191 col2" >30+ days ago</td>
      <td id="T_c71c4_row191_col3" class="data row191 col3" >https://ca.indeed.com/jobs?q=Jr.%20/%20Int.%20Software%20Engineering%20%2812mo%20fixed%20term%29%20Magellan%20Aerospace</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row192" class="row_heading level0 row192" >291</th>
      <td id="T_c71c4_row192_col0" class="data row192 col0" >Jr. Nuage/Cloud 2LS CS Engineer</td>
      <td id="T_c71c4_row192_col1" class="data row192 col1" > Ability to write scripts at a Unix/Linux level (bash, python). Provide Remote Technical Support (RTS) for the Nuage SDN solutions and associated network… </td>
      <td id="T_c71c4_row192_col2" class="data row192 col2" >30+ days ago</td>
      <td id="T_c71c4_row192_col3" class="data row192 col3" >https://ca.indeed.com/jobs?q=Jr.%20Nuage/Cloud%202LS%20CS%20Engineer%20NOKIA</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row193" class="row_heading level0 row193" >272</th>
      <td id="T_c71c4_row193_col0" class="data row193 col0" >Jr. Software Engineer</td>
      <td id="T_c71c4_row193_col1" class="data row193 col1" > With a strong, active and familial culture, Pub United is the agency’s social club, hosting events as wide reaching as Curling, Trivia Nights and more. </td>
      <td id="T_c71c4_row193_col2" class="data row193 col2" >30+ days ago</td>
      <td id="T_c71c4_row193_col3" class="data row193 col3" >https://ca.indeed.com/jobs?q=Jr.%20Software%20Engineer%20Publicis%20Worldwide</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row194" class="row_heading level0 row194" >273</th>
      <td id="T_c71c4_row194_col0" class="data row194 col0" >Junior Web Developer</td>
      <td id="T_c71c4_row194_col1" class="data row194 col1" > You will work with cutting-edge technologies, learn how they are applied in the ecommerce sector, and collaborate extensively with stakeholders and the… </td>
      <td id="T_c71c4_row194_col2" class="data row194 col2" >30+ days ago</td>
      <td id="T_c71c4_row194_col3" class="data row194 col3" >https://ca.indeed.com/jobs?q=Junior%20Web%20Developer%20Scribendi</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row195" class="row_heading level0 row195" >274</th>
      <td id="T_c71c4_row195_col0" class="data row195 col0" >Jr. Software Engineer - Lighthouse</td>
      <td id="T_c71c4_row195_col1" class="data row195 col1" > Work closely with clients to understand key business issues. Gather and analyze requirements to develop impactful recommendations and solutions. </td>
      <td id="T_c71c4_row195_col2" class="data row195 col2" >30+ days ago</td>
      <td id="T_c71c4_row195_col3" class="data row195 col3" >https://ca.indeed.com/jobs?q=Jr.%20Software%20Engineer%20-%20Lighthouse%20KPMG</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row196" class="row_heading level0 row196" >275</th>
      <td id="T_c71c4_row196_col0" class="data row196 col0" >Junior Python Solution Developer (FT)</td>
      <td id="T_c71c4_row196_col1" class="data row196 col1" > As a Junior Python Solution Developer, you will work on our various software solutions for commercial airlines. 2+ years of working in software development. </td>
      <td id="T_c71c4_row196_col2" class="data row196 col2" >30+ days ago</td>
      <td id="T_c71c4_row196_col3" class="data row196 col3" >https://ca.indeed.com/jobs?q=Junior%20Python%20Solution%20Developer%20%28FT%29%20Sigma%20Software</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row197" class="row_heading level0 row197" >276</th>
      <td id="T_c71c4_row197_col0" class="data row197 col0" >Junior C/C++ & Fortran Compiler Developer</td>
      <td id="T_c71c4_row197_col1" class="data row197 col1" > Software Developers at IBM are the backbone of our strategic initiatives to design, code, test, and provide industry-leading solutions that make the world run… </td>
      <td id="T_c71c4_row197_col2" class="data row197 col2" >30+ days ago</td>
      <td id="T_c71c4_row197_col3" class="data row197 col3" >https://ca.indeed.com/jobs?q=Junior%20C/C%2B%2B%20%26%20Fortran%20Compiler%20Developer%20IBM</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row198" class="row_heading level0 row198" >277</th>
      <td id="T_c71c4_row198_col0" class="data row198 col0" >DevSecOps Engineer</td>
      <td id="T_c71c4_row198_col1" class="data row198 col1" > We are seeking a Junior Data Science Developer to assist with the overall execution of our digital strategy to maximize usage of our full suite of CO2… </td>
      <td id="T_c71c4_row198_col2" class="data row198 col2" >30+ days ago</td>
      <td id="T_c71c4_row198_col3" class="data row198 col3" >https://ca.indeed.com/jobs?q=DevSecOps%20Engineer%20CarbonCure%20Technologies</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row199" class="row_heading level0 row199" >278</th>
      <td id="T_c71c4_row199_col0" class="data row199 col0" >Matchmove Artist - Junior</td>
      <td id="T_c71c4_row199_col1" class="data row199 col1" > You will be working with artists with a wealth of experience on various productions. It is important to have basic knowledge of Syntheyes and matchmove. </td>
      <td id="T_c71c4_row199_col2" class="data row199 col2" >30+ days ago</td>
      <td id="T_c71c4_row199_col3" class="data row199 col3" >https://ca.indeed.com/jobs?q=Matchmove%20Artist%20-%20Junior%20Track%20Visual%20Effects</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row200" class="row_heading level0 row200" >279</th>
      <td id="T_c71c4_row200_col0" class="data row200 col0" >Toronto - Junior Cloud Computing Engineer</td>
      <td id="T_c71c4_row200_col1" class="data row200 col1" > As a Junior Cloud Computing Engineer you will gain invaluable hands-on experience while helping large organizations make the shift from traditional IT methods… </td>
      <td id="T_c71c4_row200_col2" class="data row200 col2" >30+ days ago</td>
      <td id="T_c71c4_row200_col3" class="data row200 col3" >https://ca.indeed.com/jobs?q=Toronto%20-%20Junior%20Cloud%20Computing%20Engineer%20FDM%20Group</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row201" class="row_heading level0 row201" >280</th>
      <td id="T_c71c4_row201_col0" class="data row201 col0" >Junior Software Solution Developer for Jeppesen – a Boeing C...</td>
      <td id="T_c71c4_row201_col1" class="data row201 col1" > As a Junior Software Solution Developer, you will work on our various software solutions for commercial airlines. 2+ years of working in software development. </td>
      <td id="T_c71c4_row201_col2" class="data row201 col2" >30+ days ago</td>
      <td id="T_c71c4_row201_col3" class="data row201 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Solution%20Developer%20for%20Jeppesen%20%E2%80%93%20a%20Boeing%20C...%20Sigma%20Software</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row202" class="row_heading level0 row202" >281</th>
      <td id="T_c71c4_row202_col0" class="data row202 col0" >Junior Pipeline TD/ Software Engineer</td>
      <td id="T_c71c4_row202_col1" class="data row202 col1" > Stellar Creative Lab is hiring a Junior Pipeline TD, who can bring his or her talent and brains to the design and development of a facility-wide CG-Animation… </td>
      <td id="T_c71c4_row202_col2" class="data row202 col2" >30+ days ago</td>
      <td id="T_c71c4_row202_col3" class="data row202 col3" >https://ca.indeed.com/jobs?q=Junior%20Pipeline%20TD/%20Software%20Engineer%20Stellar%20Creative%20Lab</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row203" class="row_heading level0 row203" >282</th>
      <td id="T_c71c4_row203_col0" class="data row203 col0" >Software Engineering - Engineer I</td>
      <td id="T_c71c4_row203_col1" class="data row203 col1" > The candidate would be directly involved from POC to production deployment of a set of components that are well tested, fully automated, well designed, highly… </td>
      <td id="T_c71c4_row203_col2" class="data row203 col2" >30+ days ago</td>
      <td id="T_c71c4_row203_col3" class="data row203 col3" >https://ca.indeed.com/jobs?q=Software%20Engineering%20-%20Engineer%20I%20Live%20Nation</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row204" class="row_heading level0 row204" >283</th>
      <td id="T_c71c4_row204_col0" class="data row204 col0" >Junior Devops Engineer</td>
      <td id="T_c71c4_row204_col1" class="data row204 col1" > This role is for a fearless self-starter with good communication skills, a strong work ethic, and the ability to participate in all aspects of the software… </td>
      <td id="T_c71c4_row204_col2" class="data row204 col2" >30+ days ago</td>
      <td id="T_c71c4_row204_col3" class="data row204 col3" >https://ca.indeed.com/jobs?q=Junior%20Devops%20Engineer%20Scribendi</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row205" class="row_heading level0 row205" >284</th>
      <td id="T_c71c4_row205_col0" class="data row205 col0" >Solutions Architect I - AWS-T3210</td>
      <td id="T_c71c4_row205_col1" class="data row205 col1" > Bachelor’s degree or foreign equivalent in Computer Science, Engineering, Mathematics, or a related field. 1 year of experience in the job offered or related… </td>
      <td id="T_c71c4_row205_col2" class="data row205 col2" >30+ days ago</td>
      <td id="T_c71c4_row205_col3" class="data row205 col3" >https://ca.indeed.com/jobs?q=Solutions%20Architect%20I%20-%20AWS-T3210%20Amazon%20Web%20Services%20Canada%2C%20In</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row206" class="row_heading level0 row206" >285</th>
      <td id="T_c71c4_row206_col0" class="data row206 col0" >Junior Actuarial Associate - Corporate Actuarial</td>
      <td id="T_c71c4_row206_col1" class="data row206 col1" > This position is part of the Canadian Corporate Actuarial Team, which is responsible for actuarial activities associated with SCORâ€™s Canada Life &amp; Health… </td>
      <td id="T_c71c4_row206_col2" class="data row206 col2" >30+ days ago</td>
      <td id="T_c71c4_row206_col3" class="data row206 col3" >https://ca.indeed.com/jobs?q=Junior%20Actuarial%20Associate%20-%20Corporate%20Actuarial%20SCOR</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row207" class="row_heading level0 row207" >286</th>
      <td id="T_c71c4_row207_col0" class="data row207 col0" >Développeur(se) de logiciels junior</td>
      <td id="T_c71c4_row207_col1" class="data row207 col1" > Maritime International, une division de L3Harris, est un fournisseur mondial de premier plan de contrôles-commandes non ITAR et de solutions de simulation pour… </td>
      <td id="T_c71c4_row207_col2" class="data row207 col2" >30+ days ago</td>
      <td id="T_c71c4_row207_col3" class="data row207 col3" >https://ca.indeed.com/jobs?q=D%C3%A9veloppeur%28se%29%20de%20logiciels%20junior%20French%20Canadian%20Instance</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row208" class="row_heading level0 row208" >287</th>
      <td id="T_c71c4_row208_col0" class="data row208 col0" >Junior Pipeline TD -- Développeur du Pipeline Junior</td>
      <td id="T_c71c4_row208_col1" class="data row208 col1" > Cinesite is recruiting a Junior Pipeline TD who will be responsible to maintain and advance the Cinesite pipeline on our animated movies and VFX shows. </td>
      <td id="T_c71c4_row208_col2" class="data row208 col2" >30+ days ago</td>
      <td id="T_c71c4_row208_col3" class="data row208 col3" >https://ca.indeed.com/jobs?q=Junior%20Pipeline%20TD%20--%20D%C3%A9veloppeur%20du%20Pipeline%20Junior%20Cinesite-Montreal</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row209" class="row_heading level0 row209" >288</th>
      <td id="T_c71c4_row209_col0" class="data row209 col0" >Junior DevOps Engineer</td>
      <td id="T_c71c4_row209_col1" class="data row209 col1" > As a development team member, you will be responsible for ensuring the smooth operation of production systems and development/test environments. </td>
      <td id="T_c71c4_row209_col2" class="data row209 col2" >30+ days ago</td>
      <td id="T_c71c4_row209_col3" class="data row209 col3" >https://ca.indeed.com/jobs?q=Junior%20DevOps%20Engineer%20Global%20Relay</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row210" class="row_heading level0 row210" >289</th>
      <td id="T_c71c4_row210_col0" class="data row210 col0" >Actuarial Trainee</td>
      <td id="T_c71c4_row210_col1" class="data row210 col1" > If you are currently studying towards the Faculty and Institute of Actuaries (IFoA) examinations and have relevant actuarial work experience in the Life… </td>
      <td id="T_c71c4_row210_col2" class="data row210 col2" >30+ days ago</td>
      <td id="T_c71c4_row210_col3" class="data row210 col3" >https://ca.indeed.com/jobs?q=Actuarial%20Trainee%20Aviva</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row211" class="row_heading level0 row211" >290</th>
      <td id="T_c71c4_row211_col0" class="data row211 col0" >Jr. Web Application Tester</td>
      <td id="T_c71c4_row211_col1" class="data row211 col1" > For more than 40 years, Vistek has been a Canadian Success story, retailing photo, video and digital professional equipment solutions. Basic knowledge of T-SQL. </td>
      <td id="T_c71c4_row211_col2" class="data row211 col2" >30+ days ago</td>
      <td id="T_c71c4_row211_col3" class="data row211 col3" >https://ca.indeed.com/jobs?q=Jr.%20Web%20Application%20Tester%20Vistek%20LTD</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row212" class="row_heading level0 row212" >292</th>
      <td id="T_c71c4_row212_col0" class="data row212 col0" >Analog Design Engr, I</td>
      <td id="T_c71c4_row212_col1" class="data row212 col1" > You will be working with a cross functional team of analog and mixed signal circuit designers from a wide variety of backgrounds on our latest DDR and HBM IP… </td>
      <td id="T_c71c4_row212_col2" class="data row212 col2" >30+ days ago</td>
      <td id="T_c71c4_row212_col3" class="data row212 col3" >https://ca.indeed.com/jobs?q=Analog%20Design%20Engr%2C%20I%20Synopsys</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row213" class="row_heading level0 row213" >104</th>
      <td id="T_c71c4_row213_col0" class="data row213 col0" >Research Analyst I - Cancer Rehabilitation & Survivorship Pr...</td>
      <td id="T_c71c4_row213_col1" class="data row213 col1" > At minimum, one (1) to three (3) years of related research experience preferred (e.g., study coordination experience; database design/set-up; data collection… </td>
      <td id="T_c71c4_row213_col2" class="data row213 col2" >30+ days ago</td>
      <td id="T_c71c4_row213_col3" class="data row213 col3" >https://ca.indeed.com/jobs?q=Research%20Analyst%20I%20-%20Cancer%20Rehabilitation%20%26%20Survivorship%20Pr...%20University%20Health%20Network</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row214" class="row_heading level0 row214" >215</th>
      <td id="T_c71c4_row214_col0" class="data row214 col0" >Full Stack Engineer (Junior)</td>
      <td id="T_c71c4_row214_col1" class="data row214 col1" > As a FullStack Engineer, you will be responsible for implementing real-time and highly scalable and distributed software for our Call Center As A Service (CCAAS… </td>
      <td id="T_c71c4_row214_col2" class="data row214 col2" >30+ days ago</td>
      <td id="T_c71c4_row214_col3" class="data row214 col3" >https://ca.indeed.com/jobs?q=Full%20Stack%20Engineer%20%28Junior%29%20Sangoma</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row215" class="row_heading level0 row215" >222</th>
      <td id="T_c71c4_row215_col0" class="data row215 col0" >Junior Software Developer</td>
      <td id="T_c71c4_row215_col1" class="data row215 col1" > Through your knowledge of industry-proven technologies and methodologies (see below), you will be responsible for delivering high-quality, efficient code as… </td>
      <td id="T_c71c4_row215_col2" class="data row215 col2" >30+ days ago</td>
      <td id="T_c71c4_row215_col3" class="data row215 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20COVNEX</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row216" class="row_heading level0 row216" >79</th>
      <td id="T_c71c4_row216_col0" class="data row216 col0" >Associate Product Manager, Data</td>
      <td id="T_c71c4_row216_col1" class="data row216 col1" > Collaborate with stakeholders to define their big data needs for the business. You will help define and execute the vision for Big Data at Lightspeed. </td>
      <td id="T_c71c4_row216_col2" class="data row216 col2" >30+ days ago</td>
      <td id="T_c71c4_row216_col3" class="data row216 col3" >https://ca.indeed.com/jobs?q=Associate%20Product%20Manager%2C%20Data%20Lightspeed%20Commerce</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row217" class="row_heading level0 row217" >78</th>
      <td id="T_c71c4_row217_col0" class="data row217 col0" >Quality Assurance Specialist (Backend/Data) - Junior/Interme...</td>
      <td id="T_c71c4_row217_col1" class="data row217 col1" > Perform data analysis using SQL to ensure data quality and quality of programs. Practical experience with manipulating test data &amp; its validation techniques. </td>
      <td id="T_c71c4_row217_col2" class="data row217 col2" >30+ days ago</td>
      <td id="T_c71c4_row217_col3" class="data row217 col3" >https://ca.indeed.com/jobs?q=Quality%20Assurance%20Specialist%20%28Backend/Data%29%20-%20Junior/Interme...%20Klick%20Health</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row218" class="row_heading level0 row218" >77</th>
      <td id="T_c71c4_row218_col0" class="data row218 col0" >Clinical Data Manager I - REMOTE</td>
      <td id="T_c71c4_row218_col1" class="data row218 col1" > Actively cleaning data, managing CRF and query trends and data reporting to ensure a clean database lock ready for analysis. </td>
      <td id="T_c71c4_row218_col2" class="data row218 col2" >30+ days ago</td>
      <td id="T_c71c4_row218_col3" class="data row218 col3" >https://ca.indeed.com/jobs?q=Clinical%20Data%20Manager%20I%20-%20REMOTE%20Precision%20for%20Medicine</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row219" class="row_heading level0 row219" >76</th>
      <td id="T_c71c4_row219_col0" class="data row219 col0" >Junior Data Engineer</td>
      <td id="T_c71c4_row219_col1" class="data row219 col1" > Ensure the quality and integrity of data. Candidates must have strong collaboration skills to work with cross-functional teams and stakeholders to ensure… </td>
      <td id="T_c71c4_row219_col2" class="data row219 col2" >30+ days ago</td>
      <td id="T_c71c4_row219_col3" class="data row219 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Engineer%20CGI</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row220" class="row_heading level0 row220" >75</th>
      <td id="T_c71c4_row220_col0" class="data row220 col0" >Financial Analyst I</td>
      <td id="T_c71c4_row220_col1" class="data row220 col1" > Enters data to sub ledger systems. Gathers audit support data upon request. Prepares and gathers data to support proper transaction reporting. </td>
      <td id="T_c71c4_row220_col2" class="data row220 col2" >30 days ago</td>
      <td id="T_c71c4_row220_col3" class="data row220 col3" >https://ca.indeed.com/jobs?q=Financial%20Analyst%20I%20BGIS</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row221" class="row_heading level0 row221" >74</th>
      <td id="T_c71c4_row221_col0" class="data row221 col0" >Junior Database Analyst</td>
      <td id="T_c71c4_row221_col1" class="data row221 col1" > Maintain reliability, stability and data integrity of the databases. 1-2 years of experience as a data administrator in SQL server environment. </td>
      <td id="T_c71c4_row221_col2" class="data row221 col2" >30+ days ago</td>
      <td id="T_c71c4_row221_col3" class="data row221 col3" >https://ca.indeed.com/jobs?q=Junior%20Database%20Analyst%20HealthHub%20Solutions</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row222" class="row_heading level0 row222" >73</th>
      <td id="T_c71c4_row222_col0" class="data row222 col0" >Junior Settlement / Financial / Risk Analyst</td>
      <td id="T_c71c4_row222_col1" class="data row222 col1" > Programming and data science skills are a definite plus. Dynasty Power is currently looking to hire a Junior Settlement / Financial / Risk Analyst. </td>
      <td id="T_c71c4_row222_col2" class="data row222 col2" >30+ days ago</td>
      <td id="T_c71c4_row222_col3" class="data row222 col3" >https://ca.indeed.com/jobs?q=Junior%20Settlement%20/%20Financial%20/%20Risk%20Analyst%20Dynasty%20Power%20Inc.</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row223" class="row_heading level0 row223" >72</th>
      <td id="T_c71c4_row223_col0" class="data row223 col0" >Jr. Data Scientist</td>
      <td id="T_c71c4_row223_col1" class="data row223 col1" > Integration with 3rd party API’s for data collection and analysis, including weather data, time-series data, and event-based data sets. </td>
      <td id="T_c71c4_row223_col2" class="data row223 col2" >30+ days ago</td>
      <td id="T_c71c4_row223_col3" class="data row223 col3" >https://ca.indeed.com/jobs?q=Jr.%20Data%20Scientist%20SimpTek%20Technologies</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row224" class="row_heading level0 row224" >71</th>
      <td id="T_c71c4_row224_col0" class="data row224 col0" >Junior Power Analyst</td>
      <td id="T_c71c4_row224_col1" class="data row224 col1" > Analyze data to look for profitable trading strategies. Passion for trading, financial derivatives and financial data analysis considered an asset. </td>
      <td id="T_c71c4_row224_col2" class="data row224 col2" >30+ days ago</td>
      <td id="T_c71c4_row224_col3" class="data row224 col3" >https://ca.indeed.com/jobs?q=Junior%20Power%20Analyst%20Dynasty%20Power%20Inc.</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row225" class="row_heading level0 row225" >70</th>
      <td id="T_c71c4_row225_col0" class="data row225 col0" >Junior Business Analyst (remote)</td>
      <td id="T_c71c4_row225_col1" class="data row225 col1" > Analyzes and evaluates complex data processing systems both current and proposed, translating business area customer information systems requirements into… </td>
      <td id="T_c71c4_row225_col2" class="data row225 col2" >30+ days ago</td>
      <td id="T_c71c4_row225_col3" class="data row225 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20%28remote%29%20Software%20International</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row226" class="row_heading level0 row226" >69</th>
      <td id="T_c71c4_row226_col0" class="data row226 col0" >Montreal - Analyste Technique Junior ou chef de Projet Techn...</td>
      <td id="T_c71c4_row226_col1" class="data row226 col1" > Certains postes courants dans lesquels vous pourriez travailler incluent chef de projet junior, coordinateur de projet, analyste commercial et plus encore. </td>
      <td id="T_c71c4_row226_col2" class="data row226 col2" >30+ days ago</td>
      <td id="T_c71c4_row226_col3" class="data row226 col3" >https://ca.indeed.com/jobs?q=Montreal%20-%20Analyste%20Technique%20Junior%20ou%20chef%20de%20Projet%20Techn...%20FDM%20Group</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row227" class="row_heading level0 row227" >68</th>
      <td id="T_c71c4_row227_col0" class="data row227 col0" >Jr. Business Intelligence Developer, Enterprise Analytics</td>
      <td id="T_c71c4_row227_col1" class="data row227 col1" > Develop ETL procedures, SSIS packages and maintain data flow processes. Advanced understanding of data warehousing concepts and best practices required. </td>
      <td id="T_c71c4_row227_col2" class="data row227 col2" >30+ days ago</td>
      <td id="T_c71c4_row227_col3" class="data row227 col3" >https://ca.indeed.com/jobs?q=Jr.%20Business%20Intelligence%20Developer%2C%20Enterprise%20Analytics%20Southlake%20Regional%20Health%20Centre</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row228" class="row_heading level0 row228" >67</th>
      <td id="T_c71c4_row228_col0" class="data row228 col0" >Remote, Ontario – Junior Data Analytics Engineer</td>
      <td id="T_c71c4_row228_col1" class="data row228 col1" > Use large data sets to address business issues. Understanding of data warehousing concepts and NoSQL Databases. BS or MS in Computer Science or related fields. </td>
      <td id="T_c71c4_row228_col2" class="data row228 col2" >30+ days ago</td>
      <td id="T_c71c4_row228_col3" class="data row228 col3" >https://ca.indeed.com/jobs?q=Remote%2C%20Ontario%20%E2%80%93%20Junior%20Data%20Analytics%20Engineer%20CaseWare%20RCM</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row229" class="row_heading level0 row229" >66</th>
      <td id="T_c71c4_row229_col0" class="data row229 col0" >Electrical EIT, Data Centres</td>
      <td id="T_c71c4_row229_col1" class="data row229 col1" > Basic knowledge of power distribution topologies for data centres and familiarity with redundancy concepts; Provide support in preparation of engineering design… </td>
      <td id="T_c71c4_row229_col2" class="data row229 col2" >30+ days ago</td>
      <td id="T_c71c4_row229_col3" class="data row229 col3" >https://ca.indeed.com/jobs?q=Electrical%20EIT%2C%20Data%20Centres%20WSP</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row230" class="row_heading level0 row230" >65</th>
      <td id="T_c71c4_row230_col0" class="data row230 col0" >Junior Business Analyst</td>
      <td id="T_c71c4_row230_col1" class="data row230 col1" > Documenting and analyzing the required information and data to determine potential solutions from a technical and business perspective. </td>
      <td id="T_c71c4_row230_col2" class="data row230 col2" >30+ days ago</td>
      <td id="T_c71c4_row230_col3" class="data row230 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20RPM%20TECHNOLOGIES%20CORP</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row231" class="row_heading level0 row231" >64</th>
      <td id="T_c71c4_row231_col0" class="data row231 col0" >Junior Business Analyst</td>
      <td id="T_c71c4_row231_col1" class="data row231 col1" > Management of Excel spreadsheets, including updating and editing data as required. The Business Analysis team is seeking a full-time Junior Business Analyst… </td>
      <td id="T_c71c4_row231_col2" class="data row231 col2" >30+ days ago</td>
      <td id="T_c71c4_row231_col3" class="data row231 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20Centrecorp%20Management%20Services%20Limited</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row232" class="row_heading level0 row232" >63</th>
      <td id="T_c71c4_row232_col0" class="data row232 col0" >Junior Online Marketing Analyst</td>
      <td id="T_c71c4_row232_col1" class="data row232 col1" > Analytical Skills to interpret data and present recommendations. Ensure data from all sources is accurate and being captured appropriately. </td>
      <td id="T_c71c4_row232_col2" class="data row232 col2" >30+ days ago</td>
      <td id="T_c71c4_row232_col3" class="data row232 col3" >https://ca.indeed.com/jobs?q=Junior%20Online%20Marketing%20Analyst%20Core%20Online%20Marketing</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row233" class="row_heading level0 row233" >62</th>
      <td id="T_c71c4_row233_col0" class="data row233 col0" >Junior Data Analytics Engineer</td>
      <td id="T_c71c4_row233_col1" class="data row233 col1" > Use large data sets to address business issues. Understanding of data warehousing concepts and NoSQL Databases. BS or MS in Computer Science or related fields. </td>
      <td id="T_c71c4_row233_col2" class="data row233 col2" >30+ days ago</td>
      <td id="T_c71c4_row233_col3" class="data row233 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Analytics%20Engineer%20Tier1%20Financial%20Solutions</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row234" class="row_heading level0 row234" >61</th>
      <td id="T_c71c4_row234_col0" class="data row234 col0" >Business Analyst I, AWS Commerce Platform Business Operation...</td>
      <td id="T_c71c4_row234_col1" class="data row234 col1" > At least 1+ years of experience with data warehousing and reporting. At least 1+ years of professional working experience in related occupations of Business… </td>
      <td id="T_c71c4_row234_col2" class="data row234 col2" >30+ days ago</td>
      <td id="T_c71c4_row234_col3" class="data row234 col3" >https://ca.indeed.com/jobs?q=Business%20Analyst%20I%2C%20AWS%20Commerce%20Platform%20Business%20Operation...%20Amazon%20Dev%20Centre%20Canada%20ULC</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row235" class="row_heading level0 row235" >80</th>
      <td id="T_c71c4_row235_col0" class="data row235 col0" >Junior Project Finance Analyst (Montreal or Laval)</td>
      <td id="T_c71c4_row235_col1" class="data row235 col1" > 0 - 5 years of financial/data analysis experience. The primary focuses of this position include: evaluating construction job cost, data reporting/analysis for… </td>
      <td id="T_c71c4_row235_col2" class="data row235 col2" >30+ days ago</td>
      <td id="T_c71c4_row235_col3" class="data row235 col3" >https://ca.indeed.com/jobs?q=Junior%20Project%20Finance%20Analyst%20%28Montreal%20or%20Laval%29%20Kiewit%20Corporation</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row236" class="row_heading level0 row236" >81</th>
      <td id="T_c71c4_row236_col0" class="data row236 col0" >Junior Business Analyst, Strategic Partnerships and Performa...</td>
      <td id="T_c71c4_row236_col1" class="data row236 col1" > Practices diligence and care when maintaining, monitoring, calculating and summarizing data, records and confidential information. </td>
      <td id="T_c71c4_row236_col2" class="data row236 col2" >30+ days ago</td>
      <td id="T_c71c4_row236_col3" class="data row236 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%2C%20Strategic%20Partnerships%20and%20Performa...%20Vancouver%20Coastal%20Health</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row237" class="row_heading level0 row237" >82</th>
      <td id="T_c71c4_row237_col0" class="data row237 col0" >Junior Analyst, CRM & Business Intelligence</td>
      <td id="T_c71c4_row237_col1" class="data row237 col1" > Proficient with data visualization tools such as Tableau or Power BI. Primary point of contact for internal CRM related support tasks (e.g. assisting with data… </td>
      <td id="T_c71c4_row237_col2" class="data row237 col2" >30+ days ago</td>
      <td id="T_c71c4_row237_col3" class="data row237 col3" >https://ca.indeed.com/jobs?q=Junior%20Analyst%2C%20CRM%20%26%20Business%20Intelligence%20Vancouver%20Whitecaps%20FC</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row238" class="row_heading level0 row238" >83</th>
      <td id="T_c71c4_row238_col0" class="data row238 col0" >Montreal - Junior Finance/Compliance Analyst</td>
      <td id="T_c71c4_row238_col1" class="data row238 col1" > FDM Junior Finance/Compliance Analysts take on responsibilities such as conducting client due diligence, monitoring and reporting transactions to regulators,… </td>
      <td id="T_c71c4_row238_col2" class="data row238 col2" >30+ days ago</td>
      <td id="T_c71c4_row238_col3" class="data row238 col3" >https://ca.indeed.com/jobs?q=Montreal%20-%20Junior%20Finance/Compliance%20Analyst%20FDM%20Group</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row239" class="row_heading level0 row239" >103</th>
      <td id="T_c71c4_row239_col0" class="data row239 col0" >Credit Analyst Trainee, Business Banking - Hamilton</td>
      <td id="T_c71c4_row239_col1" class="data row239 col1" > Coordinates the management of databases; ensures alignment and integration of data in adherence with data governance standards. </td>
      <td id="T_c71c4_row239_col2" class="data row239 col2" >30+ days ago</td>
      <td id="T_c71c4_row239_col3" class="data row239 col3" >https://ca.indeed.com/jobs?q=Credit%20Analyst%20Trainee%2C%20Business%20Banking%20-%20Hamilton%20BMO%20Financial%20Group</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row240" class="row_heading level0 row240" >102</th>
      <td id="T_c71c4_row240_col0" class="data row240 col0" >Jr. Technical Business Analyst</td>
      <td id="T_c71c4_row240_col1" class="data row240 col1" > Understanding of data flow diagrams and technical specifications. 2-3 years of experience working with big data sets and ETL methodologies. </td>
      <td id="T_c71c4_row240_col2" class="data row240 col2" >30+ days ago</td>
      <td id="T_c71c4_row240_col3" class="data row240 col3" >https://ca.indeed.com/jobs?q=Jr.%20Technical%20Business%20Analyst%20Bond%20Brand%20Loyalty%20Inc</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row241" class="row_heading level0 row241" >101</th>
      <td id="T_c71c4_row241_col0" class="data row241 col0" >Junior/Intermediate Advanced Analytics Professional</td>
      <td id="T_c71c4_row241_col1" class="data row241 col1" > Apply professional experience with data science software to prepare, analyze, and model data. 1+ years of professional work experience in a data analysis… </td>
      <td id="T_c71c4_row241_col2" class="data row241 col2" >30+ days ago</td>
      <td id="T_c71c4_row241_col3" class="data row241 col3" >https://ca.indeed.com/jobs?q=Junior/Intermediate%20Advanced%20Analytics%20Professional%20Definity</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row242" class="row_heading level0 row242" >100</th>
      <td id="T_c71c4_row242_col0" class="data row242 col0" >Junior Pricing Analyst</td>
      <td id="T_c71c4_row242_col1" class="data row242 col1" > Collects data and maintains the database. Prepares financial and sku analysis reports, analyses margins and competitive market data. </td>
      <td id="T_c71c4_row242_col2" class="data row242 col2" >30+ days ago</td>
      <td id="T_c71c4_row242_col3" class="data row242 col3" >https://ca.indeed.com/jobs?q=Junior%20Pricing%20Analyst%20B%C3%A9langer%20UPT</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row243" class="row_heading level0 row243" >99</th>
      <td id="T_c71c4_row243_col0" class="data row243 col0" >Junior Data Analyst</td>
      <td id="T_c71c4_row243_col1" class="data row243 col1" > Acquire data from primary or secondary data sources and maintain databases/data systems. Proven working experience as a data analyst or business data analyst. </td>
      <td id="T_c71c4_row243_col2" class="data row243 col2" >30+ days ago</td>
      <td id="T_c71c4_row243_col3" class="data row243 col3" >https://ca.indeed.com/jobs?q=Junior%20Data%20Analyst%20OSL%20Retail%20Services%20Inc</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row244" class="row_heading level0 row244" >98</th>
      <td id="T_c71c4_row244_col0" class="data row244 col0" >Junior Business Analyst</td>
      <td id="T_c71c4_row244_col1" class="data row244 col1" > Work closely with IT team to satisfy data sampling, project analysis, testing verification, and other user requests from existing client databases. </td>
      <td id="T_c71c4_row244_col2" class="data row244 col2" >30+ days ago</td>
      <td id="T_c71c4_row244_col3" class="data row244 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20Dokainish%20%26%20Company</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row245" class="row_heading level0 row245" >97</th>
      <td id="T_c71c4_row245_col0" class="data row245 col0" >Toronto - Junior Data Engineer</td>
      <td id="T_c71c4_row245_col1" class="data row245 col1" > Understanding of data constructs, data modelling and data management tools. As a Junior Data Engineer, you will design, develop and test a large-scale, custom… </td>
      <td id="T_c71c4_row245_col2" class="data row245 col2" >30+ days ago</td>
      <td id="T_c71c4_row245_col3" class="data row245 col3" >https://ca.indeed.com/jobs?q=Toronto%20-%20Junior%20Data%20Engineer%20FDM%20Group</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row246" class="row_heading level0 row246" >96</th>
      <td id="T_c71c4_row246_col0" class="data row246 col0" >Junior Financial Analyst (8 MONTH CONTRACT)</td>
      <td id="T_c71c4_row246_col1" class="data row246 col1" > Key contact for Ad-hoc business unit and functional are support (modeling, reporting, analysis, data gathering). Bachelor’s degree or equivalent. </td>
      <td id="T_c71c4_row246_col2" class="data row246 col2" >30+ days ago</td>
      <td id="T_c71c4_row246_col3" class="data row246 col3" >https://ca.indeed.com/jobs?q=Junior%20Financial%20Analyst%20%288%20MONTH%20CONTRACT%29%20Cineplex</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row247" class="row_heading level0 row247" >95</th>
      <td id="T_c71c4_row247_col0" class="data row247 col0" >Analyst Shipping Channel I</td>
      <td id="T_c71c4_row247_col1" class="data row247 col1" > Demonstrated skill in data analysis with exposure to a variety of data file formats (XML, Json, CSV and FF). Analyze stakeholder’s requests and business issues… </td>
      <td id="T_c71c4_row247_col2" class="data row247 col2" >30+ days ago</td>
      <td id="T_c71c4_row247_col3" class="data row247 col3" >https://ca.indeed.com/jobs?q=Analyst%20Shipping%20Channel%20I%20Purolator</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row248" class="row_heading level0 row248" >315</th>
      <td id="T_c71c4_row248_col0" class="data row248 col0" >Junior Python Developer</td>
      <td id="T_c71c4_row248_col1" class="data row248 col1" > As an Juniour Python Developer (internally called ATD) you will perform a variety of tasks to assist the Pipeline Technical Directors (Pipeline TDs) to ensure… </td>
      <td id="T_c71c4_row248_col2" class="data row248 col2" >30+ days ago</td>
      <td id="T_c71c4_row248_col3" class="data row248 col3" >https://ca.indeed.com/jobs?q=Junior%20Python%20Developer%20ReDefine</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row249" class="row_heading level0 row249" >94</th>
      <td id="T_c71c4_row249_col0" class="data row249 col0" >Junior Financial Analyst, Treasury</td>
      <td id="T_c71c4_row249_col1" class="data row249 col1" > Support monthly capital management activities including monitoring and analyzing regular financial reports, investment data, and other information sources to… </td>
      <td id="T_c71c4_row249_col2" class="data row249 col2" >30+ days ago</td>
      <td id="T_c71c4_row249_col3" class="data row249 col3" >https://ca.indeed.com/jobs?q=Junior%20Financial%20Analyst%2C%20Treasury%20Definity</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row250" class="row_heading level0 row250" >92</th>
      <td id="T_c71c4_row250_col0" class="data row250 col0" >Jr. Power BI Developer</td>
      <td id="T_c71c4_row250_col1" class="data row250 col1" > Leading the design and development of consumer-facing reporting and analytics solutions, including data modeling and data visualization. </td>
      <td id="T_c71c4_row250_col2" class="data row250 col2" >30+ days ago</td>
      <td id="T_c71c4_row250_col3" class="data row250 col3" >https://ca.indeed.com/jobs?q=Jr.%20Power%20BI%20Developer%20Bond%20Brand%20Loyalty%20Inc</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row251" class="row_heading level0 row251" >91</th>
      <td id="T_c71c4_row251_col0" class="data row251 col0" >Junior CRM Business Analyst</td>
      <td id="T_c71c4_row251_col1" class="data row251 col1" > Assists in analytics with need-based support on reports data extraction, compiling and manipulation. CRM Business Analyst with the delivery of CRM initiatives,… </td>
      <td id="T_c71c4_row251_col2" class="data row251 col2" >30+ days ago</td>
      <td id="T_c71c4_row251_col3" class="data row251 col3" >https://ca.indeed.com/jobs?q=Junior%20CRM%20Business%20Analyst%20Educators%20Financial%20Group</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row252" class="row_heading level0 row252" >90</th>
      <td id="T_c71c4_row252_col0" class="data row252 col0" >Junior Database Administrator</td>
      <td id="T_c71c4_row252_col1" class="data row252 col1" > They act as strategic partners with each business unit to help Questrade leverage technology to gain competitive advantage. You have experience with GIT/GitLab. </td>
      <td id="T_c71c4_row252_col2" class="data row252 col2" >30+ days ago</td>
      <td id="T_c71c4_row252_col3" class="data row252 col3" >https://ca.indeed.com/jobs?q=Junior%20Database%20Administrator%20Questrade%20Financial%20Group</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row253" class="row_heading level0 row253" >89</th>
      <td id="T_c71c4_row253_col0" class="data row253 col0" >Scientist I/II, Process Development Analytics</td>
      <td id="T_c71c4_row253_col1" class="data row253 col1" > Strong practical knowledge of experimental design, and statistical analysis of data. Train and supervise junior staff members in supporting analytical… </td>
      <td id="T_c71c4_row253_col2" class="data row253 col2" >30+ days ago</td>
      <td id="T_c71c4_row253_col3" class="data row253 col3" >https://ca.indeed.com/jobs?q=Scientist%20I/II%2C%20Process%20Development%20Analytics%20BlueRock%20Therapeutics</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row254" class="row_heading level0 row254" >88</th>
      <td id="T_c71c4_row254_col0" class="data row254 col0" >Jr. SQL BI Developer</td>
      <td id="T_c71c4_row254_col1" class="data row254 col1" > This role will play an integral role in supporting Vox Mobile business and operations strategy by providing consultative and engineering services in the areas… </td>
      <td id="T_c71c4_row254_col2" class="data row254 col2" >30+ days ago</td>
      <td id="T_c71c4_row254_col3" class="data row254 col3" >https://ca.indeed.com/jobs?q=Jr.%20SQL%20BI%20Developer%20Vox%20Mobile</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row255" class="row_heading level0 row255" >87</th>
      <td id="T_c71c4_row255_col0" class="data row255 col0" >Game Data Analyst (Junior and Intermediate Level)</td>
      <td id="T_c71c4_row255_col1" class="data row255 col1" > Minimum 2 years experience as a data analyst. As a Game Data Analyst your responsibility is to find actionable insights from data to help guide the development… </td>
      <td id="T_c71c4_row255_col2" class="data row255 col2" >30+ days ago</td>
      <td id="T_c71c4_row255_col3" class="data row255 col3" >https://ca.indeed.com/jobs?q=Game%20Data%20Analyst%20%28Junior%20and%20Intermediate%20Level%29%20Hothead%20Games</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row256" class="row_heading level0 row256" >86</th>
      <td id="T_c71c4_row256_col0" class="data row256 col0" >Junior Business Analyst</td>
      <td id="T_c71c4_row256_col1" class="data row256 col1" > Extract data, compile reports, and develop customized reporting as required by users and management. Analyze, identify and validate key business requirements. </td>
      <td id="T_c71c4_row256_col2" class="data row256 col2" >30+ days ago</td>
      <td id="T_c71c4_row256_col3" class="data row256 col3" >https://ca.indeed.com/jobs?q=Junior%20Business%20Analyst%20The%20Skyline%20Group%20of%20Companies</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row257" class="row_heading level0 row257" >85</th>
      <td id="T_c71c4_row257_col0" class="data row257 col0" >Business Analyst I - TELUS Health</td>
      <td id="T_c71c4_row257_col1" class="data row257 col1" > Experience analysing and reporting on performance and utilisation data. The successful candidate must be a strong creative and analytical thinker with strong… </td>
      <td id="T_c71c4_row257_col2" class="data row257 col2" >30+ days ago</td>
      <td id="T_c71c4_row257_col3" class="data row257 col3" >https://ca.indeed.com/jobs?q=Business%20Analyst%20I%20-%20TELUS%20Health%20TELUS</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row258" class="row_heading level0 row258" >84</th>
      <td id="T_c71c4_row258_col0" class="data row258 col0" >Graduate Trainee Assistant Analyst - GTA</td>
      <td id="T_c71c4_row258_col1" class="data row258 col1" > Ability to utilize computer software programs for data management, such as Microsoft Excel. Work independently and as a part of engineering and technical teams… </td>
      <td id="T_c71c4_row258_col2" class="data row258 col2" >30+ days ago</td>
      <td id="T_c71c4_row258_col3" class="data row258 col3" >https://ca.indeed.com/jobs?q=Graduate%20Trainee%20Assistant%20Analyst%20-%20GTA%20Kinectrics</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row259" class="row_heading level0 row259" >93</th>
      <td id="T_c71c4_row259_col0" class="data row259 col0" >Junior Sales Data Coordinator</td>
      <td id="T_c71c4_row259_col1" class="data row259 col1" > Reporting to the National Sales &amp; Marketing Director, the Junior Sales Data Coordinator will be internal link between the pricing analyst and inside sales. </td>
      <td id="T_c71c4_row259_col2" class="data row259 col2" >30+ days ago</td>
      <td id="T_c71c4_row259_col3" class="data row259 col3" >https://ca.indeed.com/jobs?q=Junior%20Sales%20Data%20Coordinator%20B%C3%A9langer%20UPT</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row260" class="row_heading level0 row260" >60</th>
      <td id="T_c71c4_row260_col0" class="data row260 col0" >Mechanical EIT, Data Centres</td>
      <td id="T_c71c4_row260_col1" class="data row260 col1" > Basic knowledge of building mechanical systems to support data centres (DCs); Reporting directly to the Mechanical Engineering Team Lead or Manager, works under… </td>
      <td id="T_c71c4_row260_col2" class="data row260 col2" >30+ days ago</td>
      <td id="T_c71c4_row260_col3" class="data row260 col3" >https://ca.indeed.com/jobs?q=Mechanical%20EIT%2C%20Data%20Centres%20WSP</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row261" class="row_heading level0 row261" >176</th>
      <td id="T_c71c4_row261_col0" class="data row261 col0" >Junior DevOps Engineer</td>
      <td id="T_c71c4_row261_col1" class="data row261 col1" > As a Junior DevOps Engineer, your main priorities will be to work with our developers to help us build and maintain our technology stack in support of the… </td>
      <td id="T_c71c4_row261_col2" class="data row261 col2" >30+ days ago</td>
      <td id="T_c71c4_row261_col3" class="data row261 col3" >https://ca.indeed.com/jobs?q=Junior%20DevOps%20Engineer%20Navigator%20Games</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row262" class="row_heading level0 row262" >178</th>
      <td id="T_c71c4_row262_col0" class="data row262 col0" >Montreal - Développeur de Logiciels Junior</td>
      <td id="T_c71c4_row262_col1" class="data row262 col1" > Renseignez-vous sur les préparatifs de FDM pour le coronavirus (COVID-19) ici. Certains postes courants que vous pourriez occuper incluent Développeur Front-end… </td>
      <td id="T_c71c4_row262_col2" class="data row262 col2" >30+ days ago</td>
      <td id="T_c71c4_row262_col3" class="data row262 col3" >https://ca.indeed.com/jobs?q=Montreal%20-%20D%C3%A9veloppeur%20de%20Logiciels%20Junior%20FDM%20Group</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row263" class="row_heading level0 row263" >203</th>
      <td id="T_c71c4_row263_col0" class="data row263 col0" >Junior Software Developer</td>
      <td id="T_c71c4_row263_col1" class="data row263 col1" > Develop high quality code, that delights our customers and stakeholders, using your knowledge of ASP. Net web application development and SQL databases. </td>
      <td id="T_c71c4_row263_col2" class="data row263 col2" >30+ days ago</td>
      <td id="T_c71c4_row263_col3" class="data row263 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20NCM%20Associates</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row264" class="row_heading level0 row264" >204</th>
      <td id="T_c71c4_row264_col0" class="data row264 col0" >Junior Software Developer</td>
      <td id="T_c71c4_row264_col1" class="data row264 col1" > LifeLearnis looking to fill the position of Junior Software Developer, who, under the direction of the Director of Software Development, will be involved in the… </td>
      <td id="T_c71c4_row264_col2" class="data row264 col2" >30+ days ago</td>
      <td id="T_c71c4_row264_col3" class="data row264 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20LIFELEARN</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row265" class="row_heading level0 row265" >205</th>
      <td id="T_c71c4_row265_col0" class="data row265 col0" >Junior Guidewire Developer</td>
      <td id="T_c71c4_row265_col1" class="data row265 col1" > Learn from deep subject matter experts through mentoring and on the job coaching. Be encouraged to deepen your technical skills…whatever those may be. </td>
      <td id="T_c71c4_row265_col2" class="data row265 col2" >30+ days ago</td>
      <td id="T_c71c4_row265_col3" class="data row265 col3" >https://ca.indeed.com/jobs?q=Junior%20Guidewire%20Developer%20Deloitte</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row266" class="row_heading level0 row266" >207</th>
      <td id="T_c71c4_row266_col0" class="data row266 col0" >Junior Developer/Programmer</td>
      <td id="T_c71c4_row266_col1" class="data row266 col1" > Maintain software design consistency, aesthetics, and functionality of web application pages, communications systems, and data processing. </td>
      <td id="T_c71c4_row266_col2" class="data row266 col2" >30+ days ago</td>
      <td id="T_c71c4_row266_col3" class="data row266 col3" >https://ca.indeed.com/jobs?q=Junior%20Developer/Programmer%20SimplyCast</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row267" class="row_heading level0 row267" >208</th>
      <td id="T_c71c4_row267_col0" class="data row267 col0" >Jr. Software Developer</td>
      <td id="T_c71c4_row267_col1" class="data row267 col1" > Work Status: Temporary Contract (6 months). Working in a large Agile team and Reporting to the Manager of Enterprise Application and working with project… </td>
      <td id="T_c71c4_row267_col2" class="data row267 col2" >30+ days ago</td>
      <td id="T_c71c4_row267_col3" class="data row267 col3" >https://ca.indeed.com/jobs?q=Jr.%20Software%20Developer%20Corus%20Entertainment</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row268" class="row_heading level0 row268" >209</th>
      <td id="T_c71c4_row268_col0" class="data row268 col0" >Junior Quality Assurance Analyst</td>
      <td id="T_c71c4_row268_col1" class="data row268 col1" > Junior QA analyst will be working on legacy web applications testing and testing of newly created solutions in various environments, from . </td>
      <td id="T_c71c4_row268_col2" class="data row268 col2" >30+ days ago</td>
      <td id="T_c71c4_row268_col3" class="data row268 col3" >https://ca.indeed.com/jobs?q=Junior%20Quality%20Assurance%20Analyst%20TC%20Transcontinental</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row269" class="row_heading level0 row269" >210</th>
      <td id="T_c71c4_row269_col0" class="data row269 col0" >Junior Software Developer; Server</td>
      <td id="T_c71c4_row269_col1" class="data row269 col1" > We offer product record keeping and distribution systems, supporting a full range of investments, accounts and regulatory bodies. </td>
      <td id="T_c71c4_row269_col2" class="data row269 col2" >30+ days ago</td>
      <td id="T_c71c4_row269_col3" class="data row269 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%3B%20Server%20RPM%20TECHNOLOGIES%20CORP</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row270" class="row_heading level0 row270" >211</th>
      <td id="T_c71c4_row270_col0" class="data row270 col0" >Junior Software Developer</td>
      <td id="T_c71c4_row270_col1" class="data row270 col1" > You will make a difference in how our customers interact with our products and conduct business. Your knowledge of all layers in software will help us re-think… </td>
      <td id="T_c71c4_row270_col2" class="data row270 col2" >30+ days ago</td>
      <td id="T_c71c4_row270_col3" class="data row270 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20Martello%20Technologies</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row271" class="row_heading level0 row271" >212</th>
      <td id="T_c71c4_row271_col0" class="data row271 col0" >Analyste d'affaires, junior</td>
      <td id="T_c71c4_row271_col1" class="data row271 col1" > / Carry out projects with potential returns and economic benefits for Quebecers. / Collaborate on dynamic teams with high-level professionals committed to… </td>
      <td id="T_c71c4_row271_col2" class="data row271 col2" >30+ days ago</td>
      <td id="T_c71c4_row271_col3" class="data row271 col3" >https://ca.indeed.com/jobs?q=Analyste%20d%27affaires%2C%20junior%20Caisse%20de%20d%C3%A9p%C3%B4t%20et%20placement%20du%20Qu%C3%A9bec</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row272" class="row_heading level0 row272" >213</th>
      <td id="T_c71c4_row272_col0" class="data row272 col0" >Junior Full Stack Developer</td>
      <td id="T_c71c4_row272_col1" class="data row272 col1" > Markdale Financial Management is looking for a part-time Junior Full Stack Web Developer to join our team. Currently an undergrad in Computer Science. </td>
      <td id="T_c71c4_row272_col2" class="data row272 col2" >30+ days ago</td>
      <td id="T_c71c4_row272_col3" class="data row272 col3" >https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20Markdale%20Financial%20Management</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row273" class="row_heading level0 row273" >105</th>
      <td id="T_c71c4_row273_col0" class="data row273 col0" >Toronto - Junior Technical Business Analyst/ Junior Technica...</td>
      <td id="T_c71c4_row273_col1" class="data row273 col1" > These roles are crucial in helping organizations with the accuracy and timely presentation of data, in line with internal process, governance, and regulatory… </td>
      <td id="T_c71c4_row273_col2" class="data row273 col2" >30+ days ago</td>
      <td id="T_c71c4_row273_col3" class="data row273 col3" >https://ca.indeed.com/jobs?q=Toronto%20-%20Junior%20Technical%20Business%20Analyst/%20Junior%20Technica...%20FDM%20Group</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row274" class="row_heading level0 row274" >216</th>
      <td id="T_c71c4_row274_col0" class="data row274 col0" >Junior Full Stack Developer</td>
      <td id="T_c71c4_row274_col1" class="data row274 col1" > We deliver solutions to customers in markets ranging from Medical Devices, Aerospace &amp; Defence, Nuclear &amp; Energy, Transportation, and Advanced Manufacturing. </td>
      <td id="T_c71c4_row274_col2" class="data row274 col2" >30+ days ago</td>
      <td id="T_c71c4_row274_col3" class="data row274 col3" >https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20Prolucid%20Technologies</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row275" class="row_heading level0 row275" >217</th>
      <td id="T_c71c4_row275_col0" class="data row275 col0" >Junior Actuarial Analyst</td>
      <td id="T_c71c4_row275_col1" class="data row275 col1" > Participate in quarterly valuation processes involving the calculation of technical provisions and the analysis of results. 0 to 3 years of relevant experience. </td>
      <td id="T_c71c4_row275_col2" class="data row275 col2" >30+ days ago</td>
      <td id="T_c71c4_row275_col3" class="data row275 col3" >https://ca.indeed.com/jobs?q=Junior%20Actuarial%20Analyst%20SCOR</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row276" class="row_heading level0 row276" >218</th>
      <td id="T_c71c4_row276_col0" class="data row276 col0" >Junior Research Consultant</td>
      <td id="T_c71c4_row276_col1" class="data row276 col1" > As this role is within the marketing and communications team, the ideal candidate for this position will have excellent writing skills, with a keen interest in… </td>
      <td id="T_c71c4_row276_col2" class="data row276 col2" >30+ days ago</td>
      <td id="T_c71c4_row276_col3" class="data row276 col3" >https://ca.indeed.com/jobs?q=Junior%20Research%20Consultant%20Arksum%20Results</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row277" class="row_heading level0 row277" >219</th>
      <td id="T_c71c4_row277_col0" class="data row277 col0" >Junior Systems Administrator Fulltime- Permanent</td>
      <td id="T_c71c4_row277_col1" class="data row277 col1" > Moreover, this Junior Systems Administrator role will have elevated access within client environments, therefore, the added responsibility of ensuring the… </td>
      <td id="T_c71c4_row277_col2" class="data row277 col2" >30+ days ago</td>
      <td id="T_c71c4_row277_col3" class="data row277 col3" >https://ca.indeed.com/jobs?q=Junior%20Systems%20Administrator%20Fulltime-%20Permanent%20ProServeIT</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row278" class="row_heading level0 row278" >220</th>
      <td id="T_c71c4_row278_col0" class="data row278 col0" >Remote Training- Canada - Junior Software Developer</td>
      <td id="T_c71c4_row278_col1" class="data row278 col1" > As a Software Developer your main role will be to solve problems, upgrade existing systems and improve efficiency for the overall success of large software… </td>
      <td id="T_c71c4_row278_col2" class="data row278 col2" >30+ days ago</td>
      <td id="T_c71c4_row278_col3" class="data row278 col3" >https://ca.indeed.com/jobs?q=Remote%20Training-%20Canada%20-%20Junior%20Software%20Developer%20FDM%20Group</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row279" class="row_heading level0 row279" >202</th>
      <td id="T_c71c4_row279_col0" class="data row279 col0" >Junior Full Stack Developer</td>
      <td id="T_c71c4_row279_col1" class="data row279 col1" > We are seeking for a Junior Full Stack Developer to join our team who will be responsible for participating in all phases of the development life-cycle,… </td>
      <td id="T_c71c4_row279_col2" class="data row279 col2" >30+ days ago</td>
      <td id="T_c71c4_row279_col3" class="data row279 col3" >https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20Steelhaus%20Technologies</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row280" class="row_heading level0 row280" >201</th>
      <td id="T_c71c4_row280_col0" class="data row280 col0" >Stage étudiant - Développeur Junior</td>
      <td id="T_c71c4_row280_col1" class="data row280 col1" > Chef de file des applications d’affaires au Québec, JOVACO Solutions a laissé sa marque en matière de produits et services de qualité au cours des 35 dernières… </td>
      <td id="T_c71c4_row280_col2" class="data row280 col2" >30+ days ago</td>
      <td id="T_c71c4_row280_col3" class="data row280 col3" >https://ca.indeed.com/jobs?q=Stage%20%C3%A9tudiant%20-%20D%C3%A9veloppeur%20Junior%20Jovaco</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row281" class="row_heading level0 row281" >199</th>
      <td id="T_c71c4_row281_col0" class="data row281 col0" >Jr. Data/Reporting Analyst</td>
      <td id="T_c71c4_row281_col1" class="data row281 col1" > The Jr Data/Reporting Analyst will be responsible for maintaining our clients Data and Reporting needs on a Weekly/Monthly bases. </td>
      <td id="T_c71c4_row281_col2" class="data row281 col2" >30+ days ago</td>
      <td id="T_c71c4_row281_col3" class="data row281 col3" >https://ca.indeed.com/jobs?q=Jr.%20Data/Reporting%20Analyst%20Scarsin</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row282" class="row_heading level0 row282" >179</th>
      <td id="T_c71c4_row282_col0" class="data row282 col0" >Junior Software Developer</td>
      <td id="T_c71c4_row282_col1" class="data row282 col1" > Work closely with other developers in an agile and collaborative environment to foster continuous improvement at the team and company level. </td>
      <td id="T_c71c4_row282_col2" class="data row282 col2" >30+ days ago</td>
      <td id="T_c71c4_row282_col3" class="data row282 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%20Bioinformatics%20Solutions</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row283" class="row_heading level0 row283" >180</th>
      <td id="T_c71c4_row283_col0" class="data row283 col0" >Fullstack développeur Junior</td>
      <td id="T_c71c4_row283_col1" class="data row283 col1" > La Financière Fairstone est la première institution financière dont les opérations se déroulent entièrement dans le nuage AWS. </td>
      <td id="T_c71c4_row283_col2" class="data row283 col2" >30+ days ago</td>
      <td id="T_c71c4_row283_col3" class="data row283 col3" >https://ca.indeed.com/jobs?q=Fullstack%20d%C3%A9veloppeur%20Junior%20Fairstone</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row284" class="row_heading level0 row284" >181</th>
      <td id="T_c71c4_row284_col0" class="data row284 col0" >Junior Programmer Analyst</td>
      <td id="T_c71c4_row284_col1" class="data row284 col1" > Competition Number: WS_IP-17. Closing Date: Open until suitable candidates are found. Successful businesses understand their customers and their competitors. </td>
      <td id="T_c71c4_row284_col2" class="data row284 col2" >30+ days ago</td>
      <td id="T_c71c4_row284_col3" class="data row284 col3" >https://ca.indeed.com/jobs?q=Junior%20Programmer%20Analyst%20Advanis</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row285" class="row_heading level0 row285" >182</th>
      <td id="T_c71c4_row285_col0" class="data row285 col0" >Junior Web Developer</td>
      <td id="T_c71c4_row285_col1" class="data row285 col1" > Provide programming supports to lead developer on an Seed to Sale Cannabis Enterprise Software project. Develop documentation and assistance tools to support… </td>
      <td id="T_c71c4_row285_col2" class="data row285 col2" >30+ days ago</td>
      <td id="T_c71c4_row285_col3" class="data row285 col3" >https://ca.indeed.com/jobs?q=Junior%20Web%20Developer%20Trellis</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row286" class="row_heading level0 row286" >183</th>
      <td id="T_c71c4_row286_col0" class="data row286 col0" >Junior Web Developer</td>
      <td id="T_c71c4_row286_col1" class="data row286 col1" > Do you love tinkering with super geeky things? Are you technically creative and a natural problem solver? Do you love learning new technologies and stepping… </td>
      <td id="T_c71c4_row286_col2" class="data row286 col2" >30+ days ago</td>
      <td id="T_c71c4_row286_col3" class="data row286 col3" >https://ca.indeed.com/jobs?q=Junior%20Web%20Developer%20Outshinery%20Creative</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row287" class="row_heading level0 row287" >184</th>
      <td id="T_c71c4_row287_col0" class="data row287 col0" >Junior Developer - Quality Assurance</td>
      <td id="T_c71c4_row287_col1" class="data row287 col1" > With the arrival of transportation technologies such as CAV and Vehicle-to-Everything (V2X). The Junior Developer / QA Engineer will be entrusted to both test… </td>
      <td id="T_c71c4_row287_col2" class="data row287 col2" >30+ days ago</td>
      <td id="T_c71c4_row287_col3" class="data row287 col3" >https://ca.indeed.com/jobs?q=Junior%20Developer%20-%20Quality%20Assurance%20Fortran%20Traffic%20Systems</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row288" class="row_heading level0 row288" >185</th>
      <td id="T_c71c4_row288_col0" class="data row288 col0" >Junior Trader</td>
      <td id="T_c71c4_row288_col1" class="data row288 col1" > Questrade Financial Group (QFG) of Companies is committed to helping Canadians become much more financially successful and secure. </td>
      <td id="T_c71c4_row288_col2" class="data row288 col2" >30+ days ago</td>
      <td id="T_c71c4_row288_col3" class="data row288 col3" >https://ca.indeed.com/jobs?q=Junior%20Trader%20Questrade%20Financial%20Group</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row289" class="row_heading level0 row289" >186</th>
      <td id="T_c71c4_row289_col0" class="data row289 col0" >Student Internship - Junior Developer</td>
      <td id="T_c71c4_row289_col1" class="data row289 col1" > A leader in the business applications space in Quebec, JOVACO Solutions has made its mark of quality products and services over the past 35 years. </td>
      <td id="T_c71c4_row289_col2" class="data row289 col2" >30+ days ago</td>
      <td id="T_c71c4_row289_col3" class="data row289 col3" >https://ca.indeed.com/jobs?q=Student%20Internship%20-%20Junior%20Developer%20Jovaco</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row290" class="row_heading level0 row290" >187</th>
      <td id="T_c71c4_row290_col0" class="data row290 col0" >Junior Software Engineer</td>
      <td id="T_c71c4_row290_col1" class="data row290 col1" > Engineering focus areas for this position include wireless gateways, LAN/WAN switches, IoT nodes, interface units and sensors. </td>
      <td id="T_c71c4_row290_col2" class="data row290 col2" >30+ days ago</td>
      <td id="T_c71c4_row290_col3" class="data row290 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Engineer%20Optima%20Tele.com%2C%20Inc.</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row291" class="row_heading level0 row291" >177</th>
      <td id="T_c71c4_row291_col0" class="data row291 col0" >Operations Billing Analyst I</td>
      <td id="T_c71c4_row291_col1" class="data row291 col1" > At least 1+ years of professional working experience in related occupations of Systems Analyst, Business Operations Engineer, Business Operations Program… </td>
      <td id="T_c71c4_row291_col2" class="data row291 col2" >30+ days ago</td>
      <td id="T_c71c4_row291_col3" class="data row291 col3" >https://ca.indeed.com/jobs?q=Operations%20Billing%20Analyst%20I%20Amazon%20Dev%20Centre%20Canada%20ULC</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row292" class="row_heading level0 row292" >188</th>
      <td id="T_c71c4_row292_col0" class="data row292 col0" >Jr. Software Developer (WinForms)</td>
      <td id="T_c71c4_row292_col1" class="data row292 col1" > We are a top-tier GovTech software and service company focused on helping Municipal Governments simplify. Full-stack developer, develop user-facing features… </td>
      <td id="T_c71c4_row292_col2" class="data row292 col2" >30+ days ago</td>
      <td id="T_c71c4_row292_col3" class="data row292 col3" >https://ca.indeed.com/jobs?q=Jr.%20Software%20Developer%20%28WinForms%29%20MUNISIGHT</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row293" class="row_heading level0 row293" >190</th>
      <td id="T_c71c4_row293_col0" class="data row293 col0" >Junior Application Developer - Web</td>
      <td id="T_c71c4_row293_col1" class="data row293 col1" > Reporting to the Service Delivery Manager, you will be will be responsible for designing, coding, and modifying applications and or related web platforms. </td>
      <td id="T_c71c4_row293_col2" class="data row293 col2" >30+ days ago</td>
      <td id="T_c71c4_row293_col3" class="data row293 col3" >https://ca.indeed.com/jobs?q=Junior%20Application%20Developer%20-%20Web%20Western%20Financial%20Group</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row294" class="row_heading level0 row294" >191</th>
      <td id="T_c71c4_row294_col0" class="data row294 col0" >Junior Analyst</td>
      <td id="T_c71c4_row294_col1" class="data row294 col1" > A successful candidate offered employment at BCAA will need to provide proof of full vaccination prior to commencing employment. </td>
      <td id="T_c71c4_row294_col2" class="data row294 col2" >30+ days ago</td>
      <td id="T_c71c4_row294_col3" class="data row294 col3" >https://ca.indeed.com/jobs?q=Junior%20Analyst%20BCAA</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row295" class="row_heading level0 row295" >192</th>
      <td id="T_c71c4_row295_col0" class="data row295 col0" >Junior Full Stack Developer</td>
      <td id="T_c71c4_row295_col1" class="data row295 col1" > Our ideal developer will be comfortable with both backend (primarily PHP) and frontend (JS/CSS/HTML) development, along with associated activities such as… </td>
      <td id="T_c71c4_row295_col2" class="data row295 col2" >30+ days ago</td>
      <td id="T_c71c4_row295_col3" class="data row295 col3" >https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20Navitas</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row296" class="row_heading level0 row296" >193</th>
      <td id="T_c71c4_row296_col0" class="data row296 col0" >Toronto - Junior Tech-Ops Specialist</td>
      <td id="T_c71c4_row296_col1" class="data row296 col1" > A Technical Operations role lands well into the space supporting IT Applications and Services for the business through monitoring, maintenance, and incident… </td>
      <td id="T_c71c4_row296_col2" class="data row296 col2" >30+ days ago</td>
      <td id="T_c71c4_row296_col3" class="data row296 col3" >https://ca.indeed.com/jobs?q=Toronto%20-%20Junior%20Tech-Ops%20Specialist%20FDM%20Group</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row297" class="row_heading level0 row297" >194</th>
      <td id="T_c71c4_row297_col0" class="data row297 col0" >Junior C++ Software Developer</td>
      <td id="T_c71c4_row297_col1" class="data row297 col1" > We need software engineers who can help us develop and maintain systems that are always online and can handle hundreds of thousands of transactions per second. </td>
      <td id="T_c71c4_row297_col2" class="data row297 col2" >30+ days ago</td>
      <td id="T_c71c4_row297_col3" class="data row297 col3" >https://ca.indeed.com/jobs?q=Junior%20C%2B%2B%20Software%20Developer%20S%26P%20Global</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row298" class="row_heading level0 row298" >195</th>
      <td id="T_c71c4_row298_col0" class="data row298 col0" >Junior QA Developer [#3911]</td>
      <td id="T_c71c4_row298_col1" class="data row298 col1" > Alteo is looking for a Junior QA Developer for a permanent position based in Montreal. Within an Agile development team (Scrum), the QA Developer is responsible… </td>
      <td id="T_c71c4_row298_col2" class="data row298 col2" >30+ days ago</td>
      <td id="T_c71c4_row298_col3" class="data row298 col3" >https://ca.indeed.com/jobs?q=Junior%20QA%20Developer%20%5B%233911%5D%20Alteo</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row299" class="row_heading level0 row299" >196</th>
      <td id="T_c71c4_row299_col0" class="data row299 col0" >Junior Full Stack Developer</td>
      <td id="T_c71c4_row299_col1" class="data row299 col1" > Fairstone is the first Canadian financial institution operating 100% in the AWS Cloud. If you want to be part of our technology team’s journey, where nimbleness… </td>
      <td id="T_c71c4_row299_col2" class="data row299 col2" >30+ days ago</td>
      <td id="T_c71c4_row299_col3" class="data row299 col3" >https://ca.indeed.com/jobs?q=Junior%20Full%20Stack%20Developer%20Fairstone</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row300" class="row_heading level0 row300" >197</th>
      <td id="T_c71c4_row300_col0" class="data row300 col0" >Junior Software Developer; AUI</td>
      <td id="T_c71c4_row300_col1" class="data row300 col1" > RPM Technologies provides software solutions and services to the largest financial services companies in Canada. Interested in the Financial Tech Industry? </td>
      <td id="T_c71c4_row300_col2" class="data row300 col2" >30+ days ago</td>
      <td id="T_c71c4_row300_col3" class="data row300 col3" >https://ca.indeed.com/jobs?q=Junior%20Software%20Developer%3B%20AUI%20RPM%20TECHNOLOGIES%20CORP</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row301" class="row_heading level0 row301" >198</th>
      <td id="T_c71c4_row301_col0" class="data row301 col0" >Junior Analyst - GCLP (Toronto, ON)</td>
      <td id="T_c71c4_row301_col1" class="data row301 col1" > Guardian Capital Group Limited (GCLP) is a diversified financial services company which serves the needs. Of clients within the financial services sector. </td>
      <td id="T_c71c4_row301_col2" class="data row301 col2" >30+ days ago</td>
      <td id="T_c71c4_row301_col3" class="data row301 col3" >https://ca.indeed.com/jobs?q=Junior%20Analyst%20-%C2%A0GCLP%20%28Toronto%2C%20ON%29%20Guardian%20Capital%20Group%20Limited</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row302" class="row_heading level0 row302" >189</th>
      <td id="T_c71c4_row302_col0" class="data row302 col0" >QA Analyst</td>
      <td id="T_c71c4_row302_col1" class="data row302 col1" > Analyze, document, and prioritize bug reports. Define, implement, and maintain a testing suite. Create and document test scenarios. </td>
      <td id="T_c71c4_row302_col2" class="data row302 col2" >30+ days ago</td>
      <td id="T_c71c4_row302_col3" class="data row302 col3" >https://ca.indeed.com/jobs?q=QA%20Analyst%20SHIPTRACK%20INC.</td>
    </tr>
    <tr>
      <th id="T_c71c4_level0_row303" class="row_heading level0 row303" >316</th>
      <td id="T_c71c4_row303_col0" class="data row303 col0" >Support Engineer External I (L4)</td>
      <td id="T_c71c4_row303_col1" class="data row303 col1" > College or university degree, or equivalent industry experience. Three years IT or engineering experience. IT background with a focus on software deployment,… </td>
      <td id="T_c71c4_row303_col2" class="data row303 col2" >30+ days ago</td>
      <td id="T_c71c4_row303_col3" class="data row303 col3" >https://ca.indeed.com/jobs?q=Support%20Engineer%20External%20I%20%28L4%29%20Thinkbox%20Software%20Inc.</td>
    </tr>
  </tbody>
</table>





```python

```

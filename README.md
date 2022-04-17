```python
import pandas as pd
import subprocess
from pathlib import Path
```


```python
subprocess.run(["git", "pull", "--ff-only"])
```

    Updating 719bb1c..48bbc83
    Fast-forward
     README.md                                          | 3072 +-----------
     archive/2022-04-17_07:49:55.569633_data_junior.p   |  Bin 0 -> 39071 bytes
     archive/2022-04-17_07:50:42.276349_python_junior.p |  Bin 0 -> 50517 bytes
     archive/2022-04-17_07:51:32.670518_sql_junior.p    |  Bin 0 -> 48869 bytes
     read_local_pickle.nbconvert.ipynb                  | 4994 +-------------------
     5 files changed, 241 insertions(+), 7825 deletions(-)
     create mode 100644 archive/2022-04-17_07:49:55.569633_data_junior.p
     create mode 100644 archive/2022-04-17_07:50:42.276349_python_junior.p
     create mode 100644 archive/2022-04-17_07:51:32.670518_sql_junior.p


    From https://github.com/yrom1/indeed-job-scraper
       719bb1c..48bbc83  main       -> origin/main





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
#pd.set_option("display.max_colwidth", None)
# pd.set_option("display.max_rows", 999)
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
df.drop(columns=['locations','clean_dates'])
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>titles</th>
      <th>companyNames</th>
      <th>jobSnippets</th>
      <th>dates</th>
      <th>links</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Financial Analyst I</td>
      <td>BGIS</td>
      <td>Enters data to sub ledger systems. Gathers au...</td>
      <td>Today</td>
      <td>https://ca.indeed.com/jobs?q=Financial%20Analy...</td>
    </tr>
    <tr>
      <th>107</th>
      <td>Junior PHP backend developer</td>
      <td>Eversun Software Corp.</td>
      <td>Hands on experience with PHP 7, Mysql, MongoD...</td>
      <td>Today</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20PHP%20ba...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Jr. SQL BI Developer</td>
      <td>Vox Mobile</td>
      <td>This role will play an integral role in suppo...</td>
      <td>1 day ago</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20SQL%20BI%20...</td>
    </tr>
    <tr>
      <th>109</th>
      <td>Junior DevOps Developer</td>
      <td>Checkfront</td>
      <td>Your daily work will include CI systems, Kube...</td>
      <td>1 day ago</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20DevOps%2...</td>
    </tr>
    <tr>
      <th>110</th>
      <td>Junior Developer</td>
      <td>Silver Icing Inc</td>
      <td>As a Silver Icing Junior Developer, you have ...</td>
      <td>1 day ago</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Develope...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>196</th>
      <td>QA Analyst</td>
      <td>SHIPTRACK INC.</td>
      <td>Analyze, document, and prioritize bug reports...</td>
      <td>30+ days ago</td>
      <td>https://ca.indeed.com/jobs?q=QA%20Analyst%20SH...</td>
    </tr>
    <tr>
      <th>197</th>
      <td>Junior Developer - Quality Assurance</td>
      <td>Fortran Traffic Systems</td>
      <td>With the arrival of transportation technologi...</td>
      <td>30+ days ago</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Develope...</td>
    </tr>
    <tr>
      <th>198</th>
      <td>Junior Web Developer</td>
      <td>Outshinery Creative</td>
      <td>You will work closely with our CTO on various...</td>
      <td>30+ days ago</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Web%20De...</td>
    </tr>
    <tr>
      <th>200</th>
      <td>Junior Software Developer</td>
      <td>Bioinformatics Solutions</td>
      <td>Work closely with other developers in an agil...</td>
      <td>30+ days ago</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software...</td>
    </tr>
    <tr>
      <th>308</th>
      <td>Jr. / Int. Software Engineering (12mo fixed term)</td>
      <td>Magellan Aerospace</td>
      <td>Magellan Aerospace, Winnipeg is looking for a...</td>
      <td>30+ days ago</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20/%20Int.%20...</td>
    </tr>
  </tbody>
</table>
<p>294 rows × 5 columns</p>
</div>




```python

```

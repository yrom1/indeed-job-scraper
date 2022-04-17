```python
import pandas as pd
import subprocess
from pathlib import Path
```


```python
subprocess.run(["git", "pull", "--ff-only"])
```

    Updating 45124b9..719bb1c
    Fast-forward
     read_local_pickle.ipynb | 128 +-----------------------------------------------
     1 file changed, 2 insertions(+), 126 deletions(-)


    From https://github.com/yrom1/indeed-job-scraper
       45124b9..719bb1c  main       -> origin/main





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
      <th>100</th>
      <td>Junior PHP backend developer</td>
      <td>Eversun Software Corp.</td>
      <td>Hands on experience with PHP 7, Mysql, MongoD...</td>
      <td>Today</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20PHP%20ba...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Jr. SQL BI Developer</td>
      <td>Vox Mobile</td>
      <td>This role will play an integral role in suppo...</td>
      <td>1 day ago</td>
      <td>https://ca.indeed.com/jobs?q=Jr.%20SQL%20BI%20...</td>
    </tr>
    <tr>
      <th>222</th>
      <td>Junior Software Developer</td>
      <td>CardinalChain Software, Inc.</td>
      <td>Maintain and enhance enterprise financial sys...</td>
      <td>Active 1 day ago</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software...</td>
    </tr>
    <tr>
      <th>221</th>
      <td>Junior Fiscal Policy Analyst</td>
      <td>Validus Healthcare Economics Inc.</td>
      <td>Location: Winnipeg (Resident of Winnipeg or w...</td>
      <td>Active 1 day ago</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Fiscal%2...</td>
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
      <th>200</th>
      <td>Junior Drupal Developer (Remote Friendly)</td>
      <td>Acro Media</td>
      <td>Acro Media is looking for a Drupal Software D...</td>
      <td>30+ days ago</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Drupal%2...</td>
    </tr>
    <tr>
      <th>201</th>
      <td>Junior Software Developer</td>
      <td>i-Open Technologies</td>
      <td>You will be required to learn how to leverage...</td>
      <td>30+ days ago</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Software...</td>
    </tr>
    <tr>
      <th>202</th>
      <td>Junior Developer/Programmer</td>
      <td>SimplyCast</td>
      <td>Maintain software design consistency, aesthet...</td>
      <td>30+ days ago</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Develope...</td>
    </tr>
    <tr>
      <th>194</th>
      <td>Junior Developer</td>
      <td>University of Alberta Students' Union</td>
      <td>As part of an information technology team, th...</td>
      <td>30+ days ago</td>
      <td>https://ca.indeed.com/jobs?q=Junior%20Develope...</td>
    </tr>
    <tr>
      <th>311</th>
      <td>Data Processing Analyst I - 1 year contract (2)</td>
      <td>ERIS Info.</td>
      <td>ERIS has an immediate opportunity for a Data ...</td>
      <td>30+ days ago</td>
      <td>https://ca.indeed.com/jobs?q=Data%20Processing...</td>
    </tr>
  </tbody>
</table>
<p>297 rows × 5 columns</p>
</div>




```python

```

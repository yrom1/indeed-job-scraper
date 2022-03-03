"""Daily Indeed job posting scraper DAG."""
import sys

from datetime import datetime, timedelta
from textwrap import dedent

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python  import PythonOperator

# add local package
sys.path.insert(0, '/home/ryan')
from indeedScraper.src.main import main as indeed_scrape

with DAG(
    dag_id = 'indeed_scraper_v2',
    start_date=datetime(2021, 12, 3),
    schedule_interval=timedelta(days=1),
    catchup=False,
) as dag:

    t1 = PythonOperator(
        task_id='pickle_dataframe',
        python_callable=indeed_scrape,
        op_kwargs={
            'input': 'junior data',
            'pages_per_search': 10,
        }
    )

    t2 = BashOperator(
        task_id='s3_pickle',
        bash_command=f'aws s3 cp ~/pickleFrame/$(ls ~/pickleFrame -t | head -1) s3://indeed-pickle-bucket-s3',
    )

    t1 >> t2

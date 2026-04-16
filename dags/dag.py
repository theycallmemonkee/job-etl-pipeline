from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data


def etl_pipeline():
    data = extract_data()
    cleaned = transform_data(data)
    load_data(cleaned)


default_args = {
    "start_date": datetime(2024, 1, 1),
}

with DAG(
    dag_id="job_etl_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False
) as dag:

    run_etl = PythonOperator(
        task_id="run_etl",
        python_callable=etl_pipeline
    )

    run_etl
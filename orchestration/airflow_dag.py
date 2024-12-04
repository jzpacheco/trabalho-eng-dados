from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2024, 11, 22),
    'retries': 1
}

with DAG('data_lake_pipeline', default_args=default_args, schedule_interval='@daily') as dag:
    extract_task = BashOperator(
        task_id='extract_to_landing',
        bash_command='python3 /scripts/extract_landing.py'
    )

    transform_bronze_task = BashOperator(
        task_id='transform_to_bronze',
        bash_command='python3 /scripts/transform_bronze.py'
    )

    transform_silver_task = BashOperator(
        task_id='transform_to_silver',
        bash_command='python3 /scripts/transform_silver.py'
    )

    transform_gold_task = BashOperator(
        task_id='transform_to_gold',
        bash_command='python3 /scripts/transform_gold.py'
    )

    extract_task >> transform_bronze_task >> transform_silver_task >> transform_gold_task

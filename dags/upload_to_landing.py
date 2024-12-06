from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from scripts.landing_upload import landing_upload

dag = DAG(
    'upload_to_minio',
    default_args={'owner': 'airflow', 'retries': 3},
    schedule_interval=None,
    start_date=datetime(2024, 11, 24),
    catchup=False
)

# Tarefa para subir arquivos
upload_task = PythonOperator(
    task_id='upload_to_minio_task',
    python_callable=landing_upload,
    dag=dag
)


upload_task
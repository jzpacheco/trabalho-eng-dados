import os
from airflow import DAG
from datetime import datetime
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

dag = DAG(
    'upload_to_bronze',
    default_args={'owner': 'airflow', 'retries': 3},
    description='ETL pipeline using Spark and Minio',
    schedule_interval=None,
    start_date=datetime(2024, 12, 6),
    catchup=False
)


spark_submit_task = SparkSubmitOperator(
    task_id='spark_etl_task',
    application='/opt/airflow/scripts/bronze_upload.py',
    conn_id='spark_default',
    conf={
        'spark.executor.memory': '2g',
        'spark.driver.memory': '1g',
        'spark.master': 'spark://spark:7077',
        'spark.hadoop.fs.s3a.endpoint': 'http://minio:9000',
        'spark.jars.packages': 'org.apache.hadoop:hadoop-aws:3.4.1',
        'spark.hadoop.fs.s3a.access.key': os.getenv("MINIO_ROOT_USER"),
        'spark.hadoop.fs.s3a.secret.key': os.getenv("MINIO_ROOT_PASSWORD"),
        'spark.hadoop.fs.s3a.connection.ssl.enabled': 'false',
        'spark.hadoop.fs.s3a.impl': 'org.apache.hadoop.fs.s3a.S3AFileSystem'
    },
    name='spark_etl_job',
    verbose=True,
    dag=dag,
    
)

spark_submit_task

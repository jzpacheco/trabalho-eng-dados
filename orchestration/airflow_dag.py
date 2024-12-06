from airflow import DAG  # Importa a classe DAG para definir a orquestração
from airflow.operators.bash import BashOperator  # Operador para executar scripts Bash
from datetime import datetime  # Para definir a data de início da DAG

# Definição dos argumentos padrão da DAG
default_args = {
    'start_date': datetime(2024, 11, 22),  # Data de início da DAG
    'retries': 1  # Número de tentativas em caso de falha
}

# Definição da DAG
with DAG('data_lake_pipeline', default_args=default_args, schedule_interval='@daily') as dag:
    # Tarefa 1: Extrair dados para a camada Landing
    extract_task = BashOperator(
        task_id='extract_to_landing',
        bash_command='python3 /scripts/extract_landing.py'
    )

    # Tarefa 2: Transformar dados para a camada Bronze
    transform_bronze_task = BashOperator(
        task_id='transform_to_bronze',
        bash_command='python3 /scripts/transform_bronze.py'
    )

    # Tarefa 3: Transformar dados para a camada Silver
    transform_silver_task = BashOperator(
        task_id='transform_to_silver',
        bash_command='python3 /scripts/transform_silver.py'
    )

    # Tarefa 4: Criar a OBT na camada Gold
    transform_gold_task = BashOperator(
        task_id='transform_to_gold',
        bash_command='python3 /scripts/transform_gold.py'
    )

    # Definindo a ordem de execução das tarefas
    extract_task >> transform_bronze_task >> transform_silver_task >> transform_gold_task

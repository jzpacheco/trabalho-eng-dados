#Transformação para a Camada Silver (transform_silver.py)
#Objetivo: Normalizar e aplicar filtros para criar datasets consistentes e prontos para análise.

# Biblioteca necessária para usar Spark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Transform_Silver").getOrCreate()

input_path = "/data/bronze/"  # Dados brutos
output_path = "/data/silver/"  # Dados limpos

# Datasets que serão processados
datasets = ["Pacientes", "Medicos", "Consultas", "Diagnosticos", "Prescricoes"]

for dataset in datasets:
    df = spark.read.parquet(f"{input_path}/{dataset}")
    # Realiza uma limpeza nos dados, removendo registros com 'ID_Paciente' nulo
    df = df.filter(df["ID_Paciente"].isNotNull())
    
    # Salva os dados limpos no diretório de saída no formato Parquet
    df.write.mode("overwrite").parquet(f"{output_path}/{dataset}")

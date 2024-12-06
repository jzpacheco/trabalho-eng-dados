#2. Transformação para a Camada Bronze (transform_bronze.py)
#Objetivo: Fazer uma limpeza inicial nos dados da camada Landing e movê-los para a camada Bronze.
# Biblioteca para trabalhar com Spark
from pyspark.sql import SparkSession

# Inicializa a sessão do Spark com um nome descritivo
spark = SparkSession.builder.appName("Transform_Bronze").getOrCreate()

# Caminhos de entrada e saída
input_path = "/data/landing/"  
output_path = "/data/bronze/"  

# Lista dos conjuntos de dados a serem processados
datasets = ["Pacientes", "Medicos", "Consultas", "Diagnosticos", "Prescricoes"]

for dataset in datasets:
    # Lê o arquivo Parquet correspondente ao dataset
    df = spark.read.parquet(f"{input_path}/{dataset}")
    
    # Remove registros duplicados
    df = df.dropDuplicates()
    
    # Escreve o DataFrame processado no formato Parquet, sobrescrevendo arquivos existentes
    df.write.mode("overwrite").parquet(f"{output_path}/{dataset}")

# Finaliza a sessão do Spark
spark.stop()

#Extração para a Camada Landing (extract_landing.py)
#Objetivo: Coletar os dados brutos dos sistemas de origem (arquivos CSV) e armazená-los na camada Landing.

# Importa a biblioteca necessária

from pyspark.sql import SparkSession

# Inicializa a sessão do Spark com um nome descritivo
spark = SparkSession.builder.appName("Extract_Landing").getOrCreate()

# Lista dos arquivos CSV de entrada
input_files = [
    "Pacientes.csv",
    "Medicos.csv",
    "Consultas.csv",
    "Diagnosticos.csv",
    "Prescricoes.csv",
]

# Caminho de saída para os arquivos no formato Parquet
output_path = "/data/landing/"

# Processamento dos arquivos
for file in input_files:
    try:
        # Lê o arquivo CSV em um DataFrame do Spark
        df = spark.read.csv(file, header=True, inferSchema=True)
        
        # Escreve o DataFrame no formato Parquet, sobrescrevendo arquivos existentes
        df.write.mode("overwrite").parquet(f"{output_path}/{file.split('.')[0]}")
        
    except Exception as e: # caso de algum erro vai exibir a seguinte mensagem
        print(f"Erro ao processar o arquivo {file}: {e}")

# Finaliza a sessão do Spark
spark.stop()

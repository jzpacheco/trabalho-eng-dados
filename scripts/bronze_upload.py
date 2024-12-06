import os
from pyspark.sql import SparkSession

# Inicializando o SparkSession
spark = (SparkSession.builder
         .appName("ETL para Camada Bronze")
         .master("spark://spark:7077")
         .config("spark.hadoop.fs.s3a.endpoint", "http://minio:9000")
         .config("spark.hadoop.fs.s3a.access.key", os.getenv("MINIO_ROOT_USER"))
         .config("spark.hadoop.fs.s3a.secret.key", os.getenv("MINIO_ROOT_PASSWORD")) 
         .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false")
         .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
         .getOrCreate()
)
# Definir o caminho para os arquivos no Minio
landing_path = "s3a://data-engineering-project/landing/"

# Carregar os dados do Minio diretamente no Spark
pacientes_df = spark.read.option("header", "true").csv(f"{landing_path}Pacientes.csv")
medicos_df = spark.read.option("header", "true").csv(f"{landing_path}Medicos.csv")
diagnosticos_df = spark.read.option("header", "true").csv(f"{landing_path}Diagnosticos.csv")
medicamentos_df = spark.read.option("header", "true").csv(f"{landing_path}Medicamentos.csv")
consultas_df = spark.read.option("header", "true").csv(f"{landing_path}Consultas.csv")
prescricoes_df = spark.read.option("header", "true").csv(f"{landing_path}Prescricoes.csv")

# Realizar transformações se necessário (exemplo, converter tipos de dados para inteiro)
pacientes_df = pacientes_df.withColumn("ID_Paciente", pacientes_df["ID_Paciente"].cast("int"))
medicos_df = medicos_df.withColumn("ID_Medico", medicos_df["ID_Medico"].cast("int"))
diagnosticos_df = diagnosticos_df.withColumn("ID_Diagnostico", diagnosticos_df["ID_Diagnostico"].cast("int"))
medicamentos_df = medicamentos_df.withColumn("ID_Medicamento", medicamentos_df["ID_Medicamento"].cast("int"))
consultas_df = consultas_df.withColumn("ID_Consulta", consultas_df["ID_Consulta"].cast("int"))
prescricoes_df = prescricoes_df.withColumn("ID_Prescricao", prescricoes_df["ID_Prescricao"].cast("int"))

# Exemplo de transformação adicional (renomear colunas ou fazer alguma agregação)
# Se necessário, por exemplo, você pode juntar as tabelas de consultas com pacientes para gerar uma visão mais completa
consultas_com_pacientes_df = consultas_df.join(pacientes_df, consultas_df["ID_Paciente"] == pacientes_df["ID_Paciente"], "left")

# Gravar os dados na camada bronze (no Minio)
bronze_path = "s3a://data-engineering-project/bronze/"

# Gravar em formato Parquet (recomendado para maior eficiência)
consultas_com_pacientes_df.write \
    .option("header", "true") \
    .parquet(f"{bronze_path}consultas_com_pacientes.parquet")

# Fechar a sessão Spark após o processo
spark.stop()

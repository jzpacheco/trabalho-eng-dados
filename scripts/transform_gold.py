# Criação da OBT (One Big Table) na Camada Gold (transform_gold.py)
#Objetivo: Consolidar os dados das diferentes tabelas em uma única tabela ampla (OBT) na camada Gold, que será utilizada para análise e dashboards.

# Biblioteca para trabalhar com Spark (basicamente, o motor que manipula os dados)
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Transform_Gold").getOrCreate()

# Lendo os dados da camada silver
pacientes_df = spark.read.parquet("/data/silver/Pacientes")
consultas_df = spark.read.parquet("/data/silver/Consultas")
medicos_df = spark.read.parquet("/data/silver/Medicos")
diagnosticos_df = spark.read.parquet("/data/silver/Diagnosticos")

# Criando OBT com joins entre os datasets
obt_df = consultas_df.join(pacientes_df, "ID_Paciente") \
                     .join(medicos_df, consultas_df["Medico_Responsavel"] == medicos_df["ID_Medico"]) \  
                     .join(diagnosticos_df, "ID_Diagnostico")

# Reescrevendo a versão anterior
obt_df.write.mode("overwrite").parquet("/data/gold/one_big_table")

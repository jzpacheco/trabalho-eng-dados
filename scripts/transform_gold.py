from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Transform_Gold").getOrCreate()

pacientes_df = spark.read.parquet("/data/silver/Pacientes")
consultas_df = spark.read.parquet("/data/silver/Consultas")
medicos_df = spark.read.parquet("/data/silver/Medicos")
diagnosticos_df = spark.read.parquet("/data/silver/Diagnosticos")

# Criar OBT com joins
obt_df = consultas_df.join(pacientes_df, "ID_Paciente") \
                     .join(medicos_df, consultas_df["Medico_Responsavel"] == medicos_df["ID_Medico"]) \
                     .join(diagnosticos_df, "ID_Diagnostico")

# Salvar como Parquet
obt_df.write.mode("overwrite").parquet("/data/gold/one_big_table")

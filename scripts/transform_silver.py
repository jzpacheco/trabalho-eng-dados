from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Transform_Silver").getOrCreate()

input_path = "/data/bronze/"
output_path = "/data/silver/"

datasets = ["Pacientes", "Medicos", "Consultas", "Diagnosticos", "Prescricoes"]

for dataset in datasets:
    df = spark.read.parquet(f"{input_path}/{dataset}")
    df = df.filter(df["ID_Paciente"].isNotNull())  # Exemplo de limpeza
    df.write.mode("overwrite").parquet(f"{output_path}/{dataset}")

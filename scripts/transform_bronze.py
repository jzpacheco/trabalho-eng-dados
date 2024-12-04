from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Transform_Bronze").getOrCreate()

input_path = "/data/landing/"
output_path = "/data/bronze/"

datasets = ["Pacientes", "Medicos", "Consultas", "Diagnosticos", "Prescricoes"]

for dataset in datasets:
    df = spark.read.parquet(f"{input_path}/{dataset}")
    df = df.dropDuplicates()
    df.write.mode("overwrite").parquet(f"{output_path}/{dataset}")

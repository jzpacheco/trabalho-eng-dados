from pyspark.sql import SparkSession

# Inicializar SparkSession
spark = SparkSession.builder.appName("Extract_Landing").getOrCreate()

# Exemplo de leitura dos CSVs de origem
input_files = ["Pacientes.csv", "Medicos.csv", "Consultas.csv", "Diagnosticos.csv", "Prescricoes.csv"]
output_path = "/data/landing/"

for file in input_files:
    df = spark.read.csv(file, header=True, inferSchema=True)
    df.write.mode("overwrite").parquet(f"{output_path}/{file.split('.')[0]}")

import os
from minio import Minio

def landing_upload():
    client = Minio(
        "localhost:9000",
        access_key="minioadmin",
        secret_key="minioadmin",
        secure=False
    )

    # Directory where the data is stored in project
    data_dir = "./data"
    print('data_dir:', data_dir)
    print('os.listdir(data_dir):', os.listdir(data_dir))

    bucket_name = "data-engineering-project"

    # Verifying if bucket exists, if not, create it
    if not client.bucket_exists(bucket_name):
        client.make_bucket(bucket_name)
        
    for file in os.listdir(data_dir):
        file_path = os.path.join(data_dir, file)
        if os.path.isfile(file_path) and file.endswith('.csv'):
            client.fput_object(bucket_name, f"landing/{file}", file_path)
        print(f"Uploaded {file} to {bucket_name}/landing")
    
import os
from minio import Minio
import urllib3

def landing_upload():
    
    http_client = urllib3.PoolManager(cert_reqs='CERT_NONE')
    client = Minio(
        "minio:9000",
        access_key=os.getenv("MINIO_ACCESS_KEY"),
        secret_key=os.getenv("MINIO_SECRET_KEY"),
        secure=False,
        http_client=http_client
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
    
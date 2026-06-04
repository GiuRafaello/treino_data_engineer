from google.cloud import bigquery
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\giu_r\treino_data_engineer\credentials\google_drive_key.json"

client = bigquery.Client()

print("Projeto:", client.project)

for ds in client.list_datasets():
    print(ds.dataset_id)
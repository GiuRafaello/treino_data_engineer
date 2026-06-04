import os
import pandas as pd
from sqlalchemy import create_engine
from google.cloud import bigquery

# ==========================
# AUTENTICAÇÃO BIGQUERY
# ==========================

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = (
    r"C:\Users\giu_r\treino_data_engineer\credentials\google_drive_key.json"
)

PROJECT_ID = "treinodataengineer"
DATASET_ID = "treino_data_engineer"

# ==========================
# CONEXÃO POSTGRES
# ==========================

engine = create_engine(
    "postgresql+psycopg2://airflow:airflow@localhost:5432/airflow"
)

# ==========================
# CLIENT BIGQUERY
# ==========================

client = bigquery.Client(project=PROJECT_ID)

# ==========================
# TABELAS
# ==========================

tabelas = [
    "dim_clientes",
    "fato_vendas",
    "fato_selic",
    "gold_analitico_vendas"
]

# ==========================
# CARGA
# ==========================

for tabela in tabelas:

    print(f"\nLendo {tabela}...")

    df = pd.read_sql(
        f"SELECT * FROM {tabela}",
        engine
    )

    destino = f"{PROJECT_ID}.{DATASET_ID}.{tabela}"

    print(f"Enviando {len(df)} registros para {destino}")

    job = client.load_table_from_dataframe(
        df,
        destino
    )

    job.result()

    print(f"{tabela} carregada com sucesso!")
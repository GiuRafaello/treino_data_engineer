import os
import pandas as pd
from sqlalchemy import create_engine
from google.cloud import bigquery

# ==========================
# AUTENTICACAO BIGQUERY
# ==========================

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = (
    "credentials/google_drive_key.json"
)

PROJECT_ID = "treinodataengineer"
DATASET_ID = "treino_data_engineer"

# ==========================
# CONEXAO POSTGRES
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

    print(df.dtypes)

    if tabela == "gold_analitico_vendas":

        df["data_venda"] = pd.to_datetime(
            df["data_venda"],
            errors="coerce"
        )

        df["quantidade"] = pd.to_numeric(
            df["quantidade"],
            errors="coerce"
        )

        df["valor_unitario"] = pd.to_numeric(
            df["valor_unitario"],
            errors="coerce"
        )

        df["valor_total"] = pd.to_numeric(
            df["valor_total"],
            errors="coerce"
        )

        df["taxa_selic"] = pd.to_numeric(
            df["taxa_selic"],
            errors="coerce"
        )

    destino = f"{PROJECT_ID}.{DATASET_ID}.{tabela}"

    print(f"Enviando {len(df)} registros para {destino}")

    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_TRUNCATE"
    )

    job = client.load_table_from_dataframe(
        df,
        destino,
        job_config=job_config
    )

    job.result()

    print(f"{tabela} carregada com sucesso!")
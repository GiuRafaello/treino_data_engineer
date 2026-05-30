from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime
import requests
import pandas as pd
from pathlib import Path


def extrair_selic():

    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&dataInicial=20/05/2016&dataFinal=20/05/2026"

    response = requests.get(url)

    dados = response.json()

    df = pd.DataFrame(dados)

    df['data'] = pd.to_datetime(df['data'], dayfirst=True)

    df['valor'] = pd.to_numeric(df['valor'])

    pasta_raw = Path("/opt/airflow/raw/bcb_api")

    pasta_raw.mkdir(parents=True, exist_ok=True)

    df.to_csv(
        pasta_raw / "selic_raw.csv",
        index=False
    )

    print(df.head())


with DAG(
    dag_id='etl_bcb_selic',
    start_date=datetime(2026, 5, 20),
    schedule='@daily',
    catchup=False
) as dag:

    tarefa_extracao = PythonOperator(
        task_id='extrair_dados_selic',
        python_callable=extrair_selic
    )

    tarefa_extracao
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import psycopg2
from pathlib import Path


def extrair_clientes_postgres():
    conn = psycopg2.connect(
        host="postgres",
        database="airflow",
        user="airflow",
        password="airflow",
        port="5432"
    )

    query = "SELECT * FROM clientes"

    df = pd.read_sql(query, conn)

    output_path = Path("/opt/airflow/raw/postgres/clientes.csv")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_path, index=False)

    print("Dados salvos em:", output_path)
    print(df.head())

    conn.close()


with DAG(
    dag_id="etl_postgres_clientes",
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    tarefa_extracao = PythonOperator(
        task_id="extrair_clientes",
        python_callable=extrair_clientes_postgres
    )
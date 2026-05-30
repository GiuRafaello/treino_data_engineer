from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="extracao_postgres",
    start_date=datetime(2026, 5, 22),
    schedule_interval=None,
    catchup=False,
    tags=["postgres"],
) as dag:

    extrair_clientes = BashOperator(
        task_id="extrair_clientes",
        bash_command="python /opt/airflow/scripts/extrair_postgres.py"
    )
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="transformacao_bcb_api",
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["staging", "bcb"]
) as dag:

    transformar_selic = BashOperator(
        task_id="transformar_selic",
        bash_command="python /opt/airflow/scripts/transformar_bcb_api.py"
    )
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="extracao_google_drive",
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False
) as dag:

    extrair_arquivos = BashOperator(
        task_id="baixar_arquivos_drive",
        bash_command="python /opt/airflow/scripts/extrair_google_drive.py"
    )
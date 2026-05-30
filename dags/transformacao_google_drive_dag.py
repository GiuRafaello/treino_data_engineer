from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="transformacao_google_drive",
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["staging", "google_drive"],
) as dag:

    transformar_google_drive = BashOperator(
        task_id="transformar_google_drive",
        bash_command=(
            "python "
            "/opt/airflow/scripts/"
            "transformar_google_drive.py"
        )
    )

    transformar_google_drive
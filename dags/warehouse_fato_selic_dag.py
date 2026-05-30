from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="warehouse_fato_selic",
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["warehouse", "bcb_api"]
) as dag:

    criar_fato_selic = BashOperator(
        task_id="criar_fato_selic",
        bash_command=(
            "python "
            "/opt/airflow/scripts/"
            "criar_fato_selic.py"
        )
    )

    criar_fato_selic
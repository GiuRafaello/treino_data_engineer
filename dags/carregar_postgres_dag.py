from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "airflow"
}

with DAG(
    dag_id="carregar_postgres",
    default_args=default_args,
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["postgres"]
) as dag:

    carregar_postgres = BashOperator(
        task_id="carregar_postgres",
        bash_command=(
            "python "
            "/opt/airflow/scripts/"
            "carregar_warehouse_postgres.py"
        )
    )

    carregar_postgres
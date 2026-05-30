from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="warehouse_fato_vendas",
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["warehouse", "google_drive"]
) as dag:

    criar_fato_vendas = BashOperator(
        task_id="criar_fato_vendas",
        bash_command=(
            "python "
            "/opt/airflow/scripts/"
            "criar_fato_vendas.py"
        )
    )

    criar_fato_vendas
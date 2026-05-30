from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="warehouse_dim_clientes",
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["warehouse", "postgres"],
) as dag:

    criar_dim_clientes = BashOperator(
        task_id="criar_dim_clientes",
        bash_command=(
            "python "
            "/opt/airflow/scripts/"
            "criar_dim_clientes.py"
        )
    )

    criar_dim_clientes
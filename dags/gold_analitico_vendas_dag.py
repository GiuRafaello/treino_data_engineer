from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="gold_analitico_vendas",
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["gold", "analytics"]
) as dag:

    criar_gold = BashOperator(
        task_id="criar_gold_analitico_vendas",
        bash_command=(
            "python "
            "/opt/airflow/scripts/"
            "criar_gold_analitico_vendas.py"
        )
    )
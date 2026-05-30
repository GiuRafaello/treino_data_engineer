from airflow import DAG
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from datetime import datetime

with DAG(
    dag_id="pipeline_master",
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["master", "pipeline"]
) as dag:

    # ==========================
    # FLUXO SELIC
    # ==========================

    etl_bcb_selic = TriggerDagRunOperator(
        task_id="etl_bcb_selic",
        trigger_dag_id="etl_bcb_selic"
    )

    transformacao_bcb_api = TriggerDagRunOperator(
        task_id="transformacao_bcb_api",
        trigger_dag_id="transformacao_bcb_api"
    )

    warehouse_fato_selic = TriggerDagRunOperator(
        task_id="warehouse_fato_selic",
        trigger_dag_id="warehouse_fato_selic"
    )

    # ==========================
    # FLUXO CLIENTES
    # ==========================

    extracao_postgres = TriggerDagRunOperator(
        task_id="extracao_postgres",
        trigger_dag_id="extracao_postgres"
    )

    warehouse_dim_clientes = TriggerDagRunOperator(
        task_id="warehouse_dim_clientes",
        trigger_dag_id="warehouse_dim_clientes"
    )

    # ==========================
    # FLUXO VENDAS
    # ==========================

    extracao_google_drive = TriggerDagRunOperator(
        task_id="extracao_google_drive",
        trigger_dag_id="extracao_google_drive"
    )

    transformacao_google_drive = TriggerDagRunOperator(
        task_id="transformacao_google_drive",
        trigger_dag_id="transformacao_google_drive"
    )

    warehouse_fato_vendas = TriggerDagRunOperator(
        task_id="warehouse_fato_vendas",
        trigger_dag_id="warehouse_fato_vendas"
    )

    gold_analitico_vendas = TriggerDagRunOperator(
        task_id="gold_analitico_vendas",
        trigger_dag_id="gold_analitico_vendas"
    )

    # ==========================
    # ORQUESTRAÇÃO
    # ==========================

    etl_bcb_selic >> transformacao_bcb_api >> warehouse_fato_selic

    extracao_postgres >> warehouse_dim_clientes

    (
        extracao_google_drive
        >> transformacao_google_drive
        >> warehouse_fato_vendas
        >> gold_analitico_vendas
    )
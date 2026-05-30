import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

# ==========================
# CONEXÃO POSTGRES
# ==========================

DATABASE_URL = (
    "postgresql+psycopg2://"
    "airflow:airflow@postgres:5432/airflow"
)

engine = create_engine(DATABASE_URL)

# ==========================
# CAMINHOS DOS CSVs
# ==========================

dim_clientes_path = Path(
    "/opt/airflow/warehouse/dim_clientes/dim_clientes.csv"
)

fato_vendas_path = Path(
    "/opt/airflow/warehouse/fato_vendas/fato_vendas.csv"
)

fato_selic_path = Path(
    "/opt/airflow/warehouse/fato_selic/fato_selic.csv"
)

gold_path = Path(
    "/opt/airflow/gold/analitico_vendas/analitico_vendas.csv"
)

# ==========================
# LEITURA DOS DADOS
# ==========================

df_dim_clientes = pd.read_csv(
    dim_clientes_path,
    encoding="utf-8"
)

df_fato_vendas = pd.read_csv(
    fato_vendas_path,
    encoding="utf-8"
)

df_fato_selic = pd.read_csv(
    fato_selic_path,
    encoding="utf-8"
)

df_gold = pd.read_csv(
    gold_path,
    encoding="utf-8"
)

# ==========================
# CARGA NO POSTGRES
# ==========================

df_dim_clientes.to_sql(
    "dim_clientes",
    engine,
    if_exists="replace",
    index=False
)

df_fato_vendas.to_sql(
    "fato_vendas",
    engine,
    if_exists="replace",
    index=False
)

df_fato_selic.to_sql(
    "fato_selic",
    engine,
    if_exists="replace",
    index=False
)

df_gold.to_sql(
    "gold_analitico_vendas",
    engine,
    if_exists="replace",
    index=False
)

print("Dados carregados no PostgreSQL com sucesso!")
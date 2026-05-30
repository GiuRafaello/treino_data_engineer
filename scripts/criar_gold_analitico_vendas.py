import pandas as pd
from pathlib import Path
import os

# ==========================
# BASE PATH
# ==========================

if os.name == "nt":
    BASE_PATH = Path(".")
else:
    BASE_PATH = Path("/opt/airflow")

# ==========================
# CAMINHOS
# ==========================

vendas_path = (
    BASE_PATH /
    "warehouse/fato_vendas/fato_vendas.csv"
)

clientes_path = (
    BASE_PATH /
    "warehouse/dim_clientes/dim_clientes.csv"
)

selic_path = (
    BASE_PATH /
    "warehouse/fato_selic/fato_selic.csv"
)

output_path = (
    BASE_PATH /
    "gold/analitico_vendas/analitico_vendas.csv"
)

# ==========================
# LEITURA DOS DADOS
# ==========================

df_vendas = pd.read_csv(
    vendas_path,
    encoding="utf-8"
)

df_clientes = pd.read_csv(
    clientes_path,
    encoding="utf-8"
)

df_selic = pd.read_csv(
    selic_path,
    encoding="utf-8"
)

# ==========================
# TRATAMENTO DE DATAS
# ==========================

df_vendas["data_venda"] = pd.to_datetime(
    df_vendas["data_venda"]
)

df_selic["data_referencia"] = pd.to_datetime(
    df_selic["data_referencia"]
)

# ==========================
# JOIN CLIENTES
# ==========================

df = df_vendas.merge(
    df_clientes,
    on="id_cliente",
    how="left"
)

# ==========================
# JOIN SELIC
# ==========================

df = df.merge(
    df_selic,
    left_on="data_venda",
    right_on="data_referencia",
    how="left"
)

# ==========================
# SELEÇÃO FINAL
# ==========================

df = df[
    [
        "data_venda",
        "nome",
        "cidade",
        "estado",
        "produto",
        "quantidade",
        "valor_unitario",
        "valor_total",
        "taxa_selic"
    ]
]

# ordenar por data
df = df.sort_values(
    by="data_venda"
)

# ==========================
# SALVAR
# ==========================

output_path.parent.mkdir(
    parents=True,
    exist_ok=True
)

df.to_csv(
    output_path,
    index=False
)

print("Tabela Gold criada com sucesso!")
print("Salvo em:", output_path)
print(df.head())
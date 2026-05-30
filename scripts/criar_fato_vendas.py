import pandas as pd
from pathlib import Path

# ==========================
# CAMINHOS
# ==========================

input_path = Path(
    "/opt/airflow/staging/google_drive/vendas_staging.csv"
)

output_path = Path(
    "/opt/airflow/warehouse/fato_vendas/fato_vendas.csv"
)

# ==========================
# LEITURA
# ==========================

df = pd.read_csv(
    input_path,
    encoding="utf-8"
)

# ==========================
# TRANSFORMAÇÕES
# ==========================

# selecionar colunas necessárias
df = df[
    [
        "id_venda",
        "id_cliente",
        "data_venda",
        "produto",
        "quantidade",
        "valor_unitario",
        "valor_total"
    ]
]

# remover duplicados
df.drop_duplicates(inplace=True)

# padronizar texto
df["produto"] = (
    df["produto"]
    .astype(str)
    .str.strip()
)

# converter data
df["data_venda"] = pd.to_datetime(
    df["data_venda"]
)

# ordenar
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

print("Fato de vendas criada com sucesso!")
print("Salvo em:", output_path)
print(df.head())
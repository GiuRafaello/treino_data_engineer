import pandas as pd
from pathlib import Path

# ==========================
# CAMINHOS
# ==========================
input_path = Path(
    "/opt/airflow/raw/bcb_api/selic_raw.csv"
)

output_path = Path(
    "/opt/airflow/staging/bcb_api/selic_staging.csv"
)

# ==========================
# LEITURA DO CSV RAW
# ==========================

df = pd.read_csv(input_path)

# ==========================
# TRANSFORMAÇÕES
# ==========================

# renomear colunas
df.rename(columns={
    "data": "data_referencia",
    "valor": "taxa_selic"
}, inplace=True)

# converter data
df["data_referencia"] = pd.to_datetime(
    df["data_referencia"],
    format="%Y-%m-%d"
)

# converter taxa para float
df["taxa_selic"] = (
    df["taxa_selic"]
    .astype(str)
    .str.replace(",", ".", regex=False)
    .astype(float)
)

# remover duplicados
df.drop_duplicates(inplace=True)

# ordenar por data
df = df.sort_values("data_referencia")

# ==========================
# SALVAR STAGING
# ==========================

output_path.parent.mkdir(
    parents=True,
    exist_ok=True
)

df.to_csv(output_path, index=False)

print("Arquivo transformado com sucesso!")
print("Salvo em:", output_path)
print(df.head())
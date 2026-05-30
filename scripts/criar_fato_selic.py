import pandas as pd
from pathlib import Path

# ==========================
# CAMINHOS
# ==========================

input_path = Path(
    "/opt/airflow/staging/bcb_api/selic_staging.csv"
)

output_path = Path(
    "/opt/airflow/warehouse/fato_selic/fato_selic.csv"
)

# ==========================
# LEITURA
# ==========================

df = pd.read_csv(input_path)

# ==========================
# TRANSFORMAÇÕES
# ==========================

# selecionar colunas necessárias
df = df[
    [
        "data_referencia",
        "taxa_selic"
    ]
]

# remover duplicados
df.drop_duplicates(inplace=True)

# converter data
df["data_referencia"] = pd.to_datetime(
    df["data_referencia"]
)

# ordenar por data
df = df.sort_values(
    by="data_referencia"
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

print("Fato SELIC criada com sucesso!")
print("Salvo em:", output_path)
print(df.head())
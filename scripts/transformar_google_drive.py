import pandas as pd
from pathlib import Path

# ==========================
# CAMINHOS
# ==========================

input_path = Path(
    "/opt/airflow/raw/google_drive/vendas_2025_01.csv"
)

output_path = Path(
    "/opt/airflow/staging/google_drive/vendas_staging.csv"
)

# ==========================
# LEITURA CSV
# ==========================

df = pd.read_csv(input_path)

# ==========================
# TRANSFORMAÇÕES
# ==========================

# padronizar nomes colunas
df.columns = (
    df.columns
    .str.lower()
    .str.strip()
    .str.replace(" ", "_")
)

# remover duplicados
df.drop_duplicates(inplace=True)

# remover espaços extras texto
for coluna in df.select_dtypes(include=["object"]).columns:
    df[coluna] = df[coluna].str.strip()

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
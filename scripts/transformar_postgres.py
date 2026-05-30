import pandas as pd
from pathlib import Path

# ==========================
# DETECTAR AMBIENTE
# ==========================

if Path("/opt/airflow").exists():
    # Rodando no Docker / Airflow
    base_path = Path("/opt/airflow")
else:
    # Rodando local no Windows
    base_path = Path(__file__).resolve().parent.parent

# ==========================
# CAMINHOS
# ==========================

input_path = base_path / "raw" / "postgres" / "clientes.csv"

output_path = (
    base_path
    / "staging"
    / "postgres"
    / "clientes_staging.csv"
)

# ==========================
# LEITURA
# ==========================

df = pd.read_csv(input_path)

# ==========================
# TRANSFORMAÇÃO
# ==========================

# padronizar nomes das colunas
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# remover duplicados
df = df.drop_duplicates()

# remover linhas totalmente vazias
df = df.dropna(how="all")

# limpar espaços em texto
for coluna in df.select_dtypes(include="object").columns:
    df[coluna] = (
        df[coluna]
        .astype(str)
        .str.strip()
    )

# ==========================
# SALVAR
# ==========================

output_path.parent.mkdir(
    parents=True,
    exist_ok=True
)

df.to_csv(output_path, index=False)

print("Arquivo transformado com sucesso!")
print("Salvo em:", output_path)
print(df.head())
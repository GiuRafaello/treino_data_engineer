import pandas as pd
from pathlib import Path

# ==========================
# CAMINHOS
# ==========================

input_path = Path(
    "/opt/airflow/staging/postgres/clientes_staging.csv"
)

output_path = Path(
    "/opt/airflow/warehouse/dim_clientes/dim_clientes.csv"
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
        "id_cliente",
        "nome",
        "cidade",
        "estado",
        "data_cadastro"
    ]
]

# remover duplicados
df.drop_duplicates(inplace=True)

# padronizar texto
for coluna in ["nome", "cidade", "estado"]:
    df[coluna] = (
        df[coluna]
        .astype(str)
        .str.strip()
    )

# ordenar por id
df = df.sort_values(
    by="id_cliente"
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

print("Dimensão criada com sucesso!")
print("Salvo em:", output_path)
print(df.head())
import pandas as pd
import psycopg2
from pathlib import Path

# conexão com Postgres Docker
conn = psycopg2.connect(
    host="postgres",
    database="airflow",
    user="airflow",
    password="airflow",
    port="5432"
)

# query SQL
query = "SELECT * FROM clientes"

# carregar no pandas
df = pd.read_sql(query, conn)

# caminho de saída
output_path = Path("../raw/postgres/clientes.csv")

# criar pasta se não existir
output_path.parent.mkdir(parents=True, exist_ok=True)

# salvar CSV
df.to_csv(output_path, index=False)

print("Dados salvos em:", output_path)
print(df.head())

# fechar conexão
conn.close()
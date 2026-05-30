import requests
import pandas as pd
from pathlib import Path

# URL da API SELIC
url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&dataInicial=20/05/2016&dataFinal=20/05/2026"

# Buscar os dados
resp = requests.get(url)
data = resp.json()

# Transformar em DataFrame
df = pd.DataFrame(data)
df['data'] = pd.to_datetime(df['data'], dayfirst=True)
df['valor'] = pd.to_numeric(df['valor'], errors='coerce')

# Salvar CSV na pasta raw/bcb_api
raw_path = Path("../raw/bcb_api")
raw_path.mkdir(parents=True, exist_ok=True)
df.to_csv(raw_path / "selic_raw.csv", index=False)

print(f"Dados salvos em: {raw_path / 'selic_raw.csv'}")
print(df.head())
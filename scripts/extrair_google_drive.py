from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from pathlib import Path

# ==========================
# CONFIGURAÇÕES
# ==========================

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

SERVICE_ACCOUNT_FILE = (
    "/opt/airflow/credentials/google_drive_key.json"
)

PASTA_DRIVE_ID = "1wpqP54nRm0q1-cLUQ4XmrxbShlmistXN"

PASTA_SAIDA = Path(
    "/opt/airflow/raw/google_drive"
)

# ==========================
# AUTENTICAÇÃO
# ==========================

creds = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES
)

service = build('drive', 'v3', credentials=creds)

# ==========================
# LISTAR ARQUIVOS DA PASTA
# ==========================

resultado = service.files().list(
    q=f"'{PASTA_DRIVE_ID}' in parents",
    fields="files(id, name)"
).execute()

arquivos = resultado.get('files', [])

if not arquivos:
    print("Nenhum arquivo encontrado.")
    exit()

PASTA_SAIDA.mkdir(parents=True, exist_ok=True)

# ==========================
# BAIXAR ARQUIVOS
# ==========================

for arquivo in arquivos:

    file_id = arquivo['id']
    nome_arquivo = arquivo['name']

    print(f"Baixando: {nome_arquivo}")

    request = service.files().get_media(fileId=file_id)
    dados = request.execute()

    caminho_arquivo = PASTA_SAIDA / nome_arquivo

    with open(caminho_arquivo, 'wb') as f:
        f.write(dados)

print("\nDownload concluído!")
import os
import json
from dotenv import load_dotenv
from google_auth_oauthlib.flow import InstalledAppFlow

load_dotenv()

SCOPES = ["https://www.googleapis.com/auth/drive.file"]

# Jalankan OAuth flow
flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
creds = flow.run_local_server(port=0)

# Ambil info token
token_info = {
    "client_id": creds.client_id,
    "client_secret": creds.client_secret,
    "refresh_token": creds.refresh_token,
    "token_uri": creds.token_uri,
}

print("Token didapatkan! Simpan di .env sebagai GDRIVE_TOKEN")
print(token_info)

# Simpan di file .env
env_file = ".env"
with open(env_file, "r") as f:
    lines = f.readlines()

with open(env_file, "w") as f:
    for line in lines:
        if line.startswith("GDRIVE_TOKEN="):
            f.write(f"GDRIVE_TOKEN='{json.dumps(token_info)}'\n")
        else:
            f.write(line)

print(f"Token berhasil ditulis ke {env_file}")

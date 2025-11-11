from google_auth_oauthlib.flow import InstalledAppFlow
import json

SCOPES = ['https://www.googleapis.com/auth/drive.file']  # Atau 'drive' jika perlu semua akses

flow = InstalledAppFlow.from_client_secrets_file(
    'client_secret.json', scopes=SCOPES
)

creds = flow.run_local_server(port=0)  # Akan buka browser untuk login
# creds sekarang ada access_token dan refresh_token

# Simpan ke file JSON (bisa di .env juga, sebagai satu baris)
with open('token.json', 'w') as f:
    f.write(creds.to_json())

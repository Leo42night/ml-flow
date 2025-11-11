import os
import json
from dotenv import load_dotenv
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

load_dotenv()

# Ambil token dan folder_id dari env
GDRIVE_TOKEN = os.environ["GDRIVE_TOKEN"]
GDRIVE_FOLDER_ID = os.environ["GDRIVE_FOLDER_ID"]

print("Folder ID:", GDRIVE_FOLDER_ID)

# Load refresh token (disimpan sebagai secret di GitHub)
token_info = json.loads(GDRIVE_TOKEN)
# print("Token:", token_info["installed"]["client_id"][:10], "...")  # debug: tampilkan sebagian token
print("Token Full:", token_info)
creds = Credentials.from_authorized_user_info(token_info)

# Build Drive API
service = build('drive', 'v3', credentials=creds)

def upload_directory(local_dir_path, parent_drive_id):
    for item_name in os.listdir(local_dir_path):
        item_path = os.path.join(local_dir_path, item_name)
        if os.path.isdir(item_path):
            folder_meta = {
                'name': item_name,
                'mimeType': 'application/vnd.google-apps.folder',
                'parents': [parent_drive_id]
            }
            created_folder = service.files().create(
                body=folder_meta,
                fields='id'
            ).execute()
            upload_directory(item_path, created_folder['id'])
        else:
            media = MediaFileUpload(item_path, resumable=True)
            service.files().create(
                body={'name': item_name, 'parents': [parent_drive_id]},
                media_body=media,
                fields='id'
            ).execute()
            print(f"Uploaded file: {item_name}")

# Upload mlruns
local_mlruns_0 = "./mlruns/0"
for run_id in os.listdir(local_mlruns_0):
    run_id_path = os.path.join(local_mlruns_0, run_id)
    if os.path.isdir(run_id_path):
        folder = service.files().create(
            body={'name': run_id, 'mimeType': 'application/vnd.google-apps.folder', 'parents': [GDRIVE_FOLDER_ID]},
            fields='id'
        ).execute()
        upload_directory(run_id_path, folder['id'])

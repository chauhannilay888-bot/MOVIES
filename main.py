import streamlit as st
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Load credentials from secrets.toml
creds = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)

# Build the Drive API client
drive_service = build("drive", "v3", credentials=creds)

# Your target video file name
TARGET_NAME = "Dhurandhar 2 -The Revenge (2026) Bollywood Hindi Movie HQCam 1080p hevc.mkv"

# Your folder ID from Google Drive
FOLDER_ID = "1cbr28a9N7YcW-r0Lv5i99YJEh1KAYFbr"

# Search for the file inside the folder
results = drive_service.files().list(
    q=f"name='{TARGET_NAME}' and '{FOLDER_ID}' in parents and trashed=false",
    fields="files(id, name)"
).execute()

items = results.get("files", [])

import streamlit as st

st.title("Google Drive Video Viewer")

# Direct preview link for your video
video_url = "https://drive.google.com/file/d/15UwHNLatFJb8n4CUi0ciXM4nFsLMVhRg/preview"

# Display the video
st.video(video_url)

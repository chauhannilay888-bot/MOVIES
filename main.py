import streamlit as st
from google.oauth2 import service_account
from googleapiclient.discovery import build

st.set_page_config(layout="wide")
st.title("Google Drive Video Viewer")

# Load credentials from secrets.toml
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=["https://www.googleapis.com/auth/drive.readonly"]
)

# Build Drive API client
drive_service = build("drive", "v3", credentials=credentials)

# Your folder ID
folder_id = "1cbr28a9N7YcW-r0Lv5i99YJEh1KAYFbr"
video_name = "Dhurandhar 2 -The Revenge (2026) Bollywood Hindi Movie HQCam 1080p hevc.mkv"

# Search for the file inside the folder
query = f"'{folder_id}' in parents and name = '{video_name}'"
results = drive_service.files().list(q=query, fields="files(id, name)").execute()
items = results.get("files", [])

if items:
    file_id = items[0]["id"]
    preview_url = f"https://drive.google.com/file/d/{file_id}/preview"

    # Responsive fullscreen horizontal embed
    st.markdown(
        f"""
        <style>
        .video-fullscreen {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;   /* full viewport width */
            height: 100vh;  /* full viewport height */
            margin: 0;
            padding: 0;
            z-index: 9999;
        }}
        .video-fullscreen iframe {{
            width: 100%;
            height: 100%;
            border: none;
        }}
        </style>
        <div class="video-fullscreen">
            <iframe src="{preview_url}" allow="autoplay; encrypted-media" allowfullscreen></iframe>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.error("Video not found in the specified folder.")

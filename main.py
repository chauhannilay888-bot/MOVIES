import streamlit as st

st.title("Dhurandher 2 - The Revenge")

# Embed Google Drive preview player in an iframe
file_id = "15UwHNLatFJb8n4CUi0ciXM4nFsLMVhRg"
preview_url = f"https://drive.google.com/file/d/{file_id}/preview"

st.components.v1.iframe(preview_url, width=800, height=600)

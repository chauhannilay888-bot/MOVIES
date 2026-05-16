import streamlit as st

# Google Drive video embed link
video_url = "https://drive.google.com/file/d/15UwHNLatFJb8n4CUi0ciXM4nFsLMVhRg/preview"

# Use st.components.v1.html to render the iframe
st.components.v1.html(
    f'<iframe src="{video_url}" width="640" height="480" allow="autoplay"></iframe>',
    height=1080, width=1920
)

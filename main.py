import streamlit as st

st.set_page_config(layout="wide")  # ensures full-width layout
st.title("Google Drive Video Viewer")

file_id = "15UwHNLatFJb8n4CUi0ciXM4nFsLMVhRg"
preview_url = f"https://drive.google.com/file/d/{file_id}/preview"

# Fullscreen horizontal responsive iframe
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
        z-index: 9999;  /* keep it on top */
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

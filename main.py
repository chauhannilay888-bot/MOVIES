import streamlit as st

# Google Drive video embed link
video_url = "https://drive.google.com/file/d/15UwHNLatFJb8n4CUi0ciXM4nFsLMVhRg/preview"

# Responsive iframe with full-screen support
st.components.v1.html(
    f"""
    <style>
    .video-container {{
        position: relative;
        padding-bottom: 56.25%; /* 16:9 aspect ratio */
        height: 0;
        overflow: hidden;
        max-width: 100%;
    }}
    .video-container iframe {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border: 0;
    }}
    </style>
    <div class="video-container">
        <iframe src="{video_url}" allow="autoplay; fullscreen"></iframe>
    </div>
    """,
    height=600, width=800
)

import streamlit as st

st.title("Google Drive Video Viewer")

# Your Google Drive file ID
file_id = "15UwHNLatFJb8n4CUi0ciXM4nFsLMVhRg"
preview_url = f"https://drive.google.com/file/d/{file_id}/preview"

# Full-width responsive iframe
st.markdown(
    f"""
    <style>
    .video-container {{
        position: relative;
        width: 100%;
        height: 0;
        padding-bottom: 100%; /* Default square ratio, will stretch */
    }}
    .video-container iframe {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }}
    @media (max-width: 768px) {{
        .video-container {{
            padding-bottom: 75%; /* Adjust for mobile screens */
        }}
    }}
    </style>
    <div class="video-container">
        <iframe src="{preview_url}" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    </div>
    """,
    unsafe_allow_html=True
)

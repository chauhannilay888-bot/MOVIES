import streamlit as st

st.set_page_config(
    page_title="Video Player",
    layout="wide"
)

# Remove padding
st.markdown("""
<style>
.block-container {
    padding: 0rem !important;
    max-width: 100% !important;
}

video {
    width: 100% !important;
    height: auto !important;
    border-radius: 0px;
}
</style>
""", unsafe_allow_html=True)

# Google Drive direct download link
file_id = "15UwHNLatFJb8n4CUi0ciXM4nFsLMVhRg"

# Direct stream URL
video_url = f"https://drive.google.com/uc?export=download&id={file_id}"

# Native video player
st.video(video_url)

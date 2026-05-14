import streamlit as st

# Page setup
st.set_page_config(
    page_title="Google Drive Video Viewer",
    layout="wide"
)

# Minimal clean CSS
st.markdown("""
<style>
/* Remove Streamlit padding issues */
.block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
    padding-left: 0.5rem;
    padding-right: 0.5rem;
}

/* Responsive video wrapper */
.video-wrapper {
    width: 100%;
    height: 90vh;
    overflow: hidden;
    border-radius: 12px;
}

/* Mobile optimization */
@media (max-width: 768px) {
    .video-wrapper {
        height: 65vh;
    }
}
</style>
""", unsafe_allow_html=True)

st.title("Google Drive Video Viewer")

# Google Drive File ID
file_id = "15UwHNLatFJb8n4CUi0ciXM4nFsLMVhRg"

# IMPORTANT:
# Use /preview directly in iframe
preview_url = f"https://drive.google.com/file/d/{file_id}/preview"

# Native iframe
st.markdown(
    f"""
    <div class="video-wrapper">
        <iframe
            src="{preview_url}"
            width="100%"
            height="100%"
            allow="autoplay; fullscreen"
            allowfullscreen
            frameborder="0">
        </iframe>
    </div>
    """,
    unsafe_allow_html=True
)

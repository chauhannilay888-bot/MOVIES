import streamlit as st

st.set_page_config(
    page_title="Google Drive Video",
    layout="wide"
)

# Google Drive file
file_id = "15UwHNLatFJb8n4CUi0ciXM4nFsLMVhRg"
preview_url = f"https://drive.google.com/file/d/{file_id}/preview"

# Clean responsive CSS
st.markdown("""
<style>

/* Remove Streamlit default spacing */
.block-container {
    padding: 0 !important;
    margin: 0 !important;
    max-width: 100% !important;
}

.main {
    padding: 0 !important;
}

/* Fullscreen responsive wrapper */
.video-wrapper {
    position: relative;
    width: 100vw;
    height: 100vh;
    overflow: hidden;
    background: black;
}

/* Proper iframe sizing */
.video-wrapper iframe {
    position: absolute;
    top: 0;
    left: 0;

    width: 100%;
    height: 100%;

    border: none;
}

/* Mobile landscape optimization */
@media (max-width: 768px) {
    .video-wrapper {
        height: 100dvh;
    }
}

</style>
""", unsafe_allow_html=True)

# IMPORTANT:
# sandbox + allow attributes help mobile fullscreen behave better
st.markdown(
    f"""
    <div class="video-wrapper">
        <iframe
            src="{preview_url}"
            allow="autoplay; fullscreen; encrypted-media; picture-in-picture"
            allowfullscreen
            webkitallowfullscreen
            mozallowfullscreen
            frameborder="0">
        </iframe>
    </div>
    """,
    unsafe_allow_html=True
)

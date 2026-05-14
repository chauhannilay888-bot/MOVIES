import streamlit as st

st.set_page_config(
    page_title="Video Player",
    layout="wide"
)

# Remove Streamlit spacing completely
st.markdown("""
<style>

/* Remove default Streamlit padding */
.block-container {
    padding: 0rem !important;
    max-width: 100% !important;
}

/* Remove top menu spacing */
header, footer {
    visibility: hidden;
}

/* Full width container */
.main {
    padding: 0rem !important;
}

/* Responsive video wrapper */
.video-container {
    width: 100vw;
    height: 100vh;
    overflow: hidden;
    margin: 0;
    padding: 0;
}

/* iframe full size */
.video-container iframe {
    width: 100%;
    height: 100%;
    border: none;
}

</style>
""", unsafe_allow_html=True)

# Google Drive File
file_id = "15UwHNLatFJb8n4CUi0ciXM4nFsLMVhRg"

# Better embed URL
preview_url = f"https://drive.google.com/file/d/{file_id}/preview"

# Fullscreen capable iframe
st.markdown(
    f"""
    <div class="video-container">
        <iframe
            src="{preview_url}"
            allow="autoplay; fullscreen"
            allowfullscreen>
        </iframe>
    </div>
    """,
    unsafe_allow_html=True
)

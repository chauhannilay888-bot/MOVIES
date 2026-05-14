import streamlit as st

st.set_page_config(
    page_title="Drive Video",
    layout="wide"
)

file_id = "15UwHNLatFJb8n4CUi0ciXM4nFsLMVhRg"
preview_url = f"https://drive.google.com/file/d/{file_id}/preview"

st.markdown("""
<style>

/* Remove Streamlit spacing */
.block-container {
    padding: 0 !important;
    margin: 0 !important;
    max-width: 100% !important;
}

/* Fullscreen wrapper */
.video-shell {
    position: relative;
    width: 100vw;
    height: 100vh;
    overflow: hidden;
    background: black;
}

/* Zoom iframe slightly to hide controls */
.video-shell iframe {
    position: absolute;

    top: -60px;     /* hides top controls */
    left: 0;

    width: 100%;
    height: calc(100% + 120px);

    border: none;
}

/* Bottom overlay to hide timeline */
.bottom-mask {
    position: absolute;
    bottom: 0;
    left: 0;

    width: 100%;
    height: 80px;

    background: black;
    z-index: 9999;
}

/* Optional top overlay */
.top-mask {
    position: absolute;
    top: 0;
    left: 0;

    width: 100%;
    height: 60px;

    background: black;
    z-index: 9999;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    f"""
    <div class="video-shell">

        <iframe
            src="{preview_url}"
            allow="autoplay; fullscreen"
            allowfullscreen>
        </iframe>

        <div class="top-mask"></div>
        <div class="bottom-mask"></div>

    </div>
    """,
    unsafe_allow_html=True
)

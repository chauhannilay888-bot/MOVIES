import streamlit as st
import streamlit.components.v1 as components

# Page config
st.set_page_config(
    page_title="Google Drive Video Viewer",
    layout="wide"
)

# Custom CSS for mobile responsiveness
st.markdown("""
    <style>
        /* Remove extra padding on mobile */
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }

        /* Responsive iframe container */
        .video-container {
            position: relative;
            width: 100%;
            padding-bottom: 56.25%; /* 16:9 ratio */
            height: 0;
            overflow: hidden;
            border-radius: 12px;
        }

        .video-container iframe {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: none;
        }

        /* Better mobile title sizing */
        h1 {
            font-size: 2rem !important;
            text-align: center;
        }

        @media (max-width: 768px) {
            h1 {
                font-size: 1.5rem !important;
            }

            .block-container {
                padding-left: 0.5rem;
                padding-right: 0.5rem;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("Google Drive Video Viewer")

# Google Drive File ID
file_id = "15UwHNLatFJb8n4CUi0ciXM4nFsLMVhRg"
preview_url = f"https://drive.google.com/file/d/{file_id}/preview"

# Responsive iframe
components.html(
    f"""
    <div class="video-container">
        <iframe 
            src="{preview_url}" 
            allow="autoplay"
            allowfullscreen>
        </iframe>
    </div>
    """,
    height=600,
)

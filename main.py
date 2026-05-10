import streamlit as st
st.title("Dhurandhar 2 - The Revenge")
video_bytes = open('mov1.mp4', 'rb').read()
st.video(video_bytes)

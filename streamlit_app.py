import streamlit as st
from openai import OpenAI
from PIL import Image

# CSS for background image and container styles
st.markdown(
    """
    <style>
    .image-container {
        display: flex;
        flex-direction: row;
        position: absolute;
        top: 0px;
        right: 20px;
    }
    .image-container img {
        margin-right: 10px;
    }
    /* Background image for the entire page */
    .stApp {
        background-image: URL('https://raw.githubusercontent.com/julianamendez11/chatbot2/main/montañas.png');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.container():

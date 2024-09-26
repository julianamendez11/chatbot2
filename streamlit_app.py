import streamlit as st
from openai import OpenAI
from PIL import Image

# CSS for background image and container styles
st.markdown(
    f"""
    <style>
    .image-container {{
        display: flex;
        flex-direction: row;
        position: absolute;
        top: 0px;
        right: 20px;
    }}
    .image-container img {{
        margin-right: 10px;
    }}
    /* Background image for the entire page */
    .stApp {{
        background-image: url("data:image/jpg;base64,{st.image('montaña.jpg', use_column_width=True)}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

with st.container():
    st.markdown('<div class="image-container">', unsafe_allow_html=True)
    st.image("cuesta-logo.png", use_column_width=False, width

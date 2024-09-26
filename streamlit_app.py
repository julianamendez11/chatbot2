import streamlit as st
from openai import OpenAI
from PIL import Image
import base64

# Función para convertir una imagen en base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# CSS para la imagen de fondo y otros estilos
background_image = get_base64_image("montaña.jpg")
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
    /* Imagen de fondo para toda la página */
    .stApp {{
        background-image: url("data:image/jpg;base64,{background_image}");
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
    st.image("cuesta-logo.png", use_column_width=False, width=250)
    st.markdown('</div>', unsafe_allow_html=True)

# Título y descripción

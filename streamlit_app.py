import streamlit as st
import pandas as pd
import openai
from PIL import Image

# Estilos para la imagen
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
</style>
""",
    unsafe_allow_html=True
)

# Mostrar el logo
with st.container():
    st.markdown('<div class="image-container">', unsafe_allow_html=True)
    st.image("cuesta-logo.png", use_column_width=False, width=250)
    st.markdown('</div>', unsafe_allow_html=True)

# Mostrar título y descripción
st.title("Cuesta AI Chatbot")
st.write(
    "Este es un chatbot de Cuesta que utiliza el modelo GPT-3.5 de OpenAI para generar respuestas basadas en datos internos."
)

# Pedir al usuario que ingrese su clave de API de OpenAI
openai_api_key = st.text_input("Clave API de OpenAI", type="password")
if not openai_api_key:
    st.info("Por favor, ingresa tu clave API de OpenAI para continuar.", icon="🗝️")
else:
    # Inicializar el cliente OpenAI
    openai.api_key = openai_api_key
    
    # Función para lee

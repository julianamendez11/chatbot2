import streamlit as st
import openai
from PIL import Image

# CSS para colocar el logo en la esquina superior derecha
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

with st.container():
    st.markdown('<div class="image-container">', unsafe_allow_html=True)
    st.image("cuesta-logo.png", use_column_width=False, width=250)
    st.markdown('</div>', unsafe_allow_html=True)

# Mostrar título y descripción
st.title("Cuesta AI Chatbot")
st.write(
    "Este es un chatbot Cuesta que utiliza el modelo GPT-3.5 de OpenAI para generar respuestas basadas en datos internos."
)

# Solicitar la clave de API de OpenAI al usuario
openai_api_key = st.text_input("Clave API de OpenAI", type="password")
if not openai_api_key:
    st.info("Por favor, ingrese su clave API para continuar.", icon="🗝️")
else:
    # Cargar el archivo de contexto
    with open("contexto.txt", "r") as file:
        contexto = file.read()

    # Crear el cliente de OpenAI
    openai.api_key = openai_api_key

    # Crear una variable en el estado de sesión para almacenar los mensajes del chat
    if "messages" not in st.session_state:
        st.session_state.messages = []

        # Agregar el contexto como un mensaje inicial de `system`
        st.session_state.messages.append({
            "role": "system", 
            "content": contexto  # Agrega el contexto cargado aquí
        })

    # Mostrar los mensajes existentes del chat
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Crear el campo de entrada para el chat
    if prompt := st.chat_input("¿Qué te gustaría saber?"):

        # Almacenar y mostrar el mensaje actual del usuario
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generar una respuesta usando la API de OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages
        )

        # Obtener la respuesta del asistente y mostrarla
        assistant_message = response['choices'][0]['message']['content']
        st.session_state.messages.append({"role": "assistant", "content": assistant_message})

        with st.chat_message("assistant"):
            st.markdown(assistant_message)

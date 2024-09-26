import streamlit as st
from openai import OpenAI
from PIL import Image

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


# Show title and description.
st.title("Cuesta AI Chatbot")
st.write(
    "This is a Cuesta chatbot that uses OpenAI's GPT-3.5 model to generate responses based on internal data. "
)

# Ask user for their OpenAI API key via st.text_input.
# Alternatively, you can store the API key in ./.streamlit/secrets.toml and access it
# via st.secrets, see https://docs.streamlit.io/develop/concepts/connections/secrets-management
openai_api_key = st.text_input("OpenAI API Key", type="password")
if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")
else:

    # API Key de OpenAI
    client = openai.OpenAI(api_key=openai_api_key)
    
    # Función para leer el archivo Excel y convertirlo en texto
    def read_excel_as_context(file_path):
        df = pd.read_excel(file_path)  # Lee el archivo de Excel
        return df.to_string()  # Convierte el DataFrame en una representación textual
    
    # Cargar archivo de contexto (Excel)
    context_file_path = "ruta/del/archivo.xlsx"  # Cambia esto a la ruta real de tu archivo
    context_text = read_excel_as_context(context_file_path)  # Convertir el Excel a texto
    
    # Crear una variable en session_state para almacenar los mensajes
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Agregar el contenido del archivo Excel al contexto
    st.session_state.messages.append({"role": "system", "content": context_text})
    
    # Mostrar los mensajes existentes
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Crear un campo de entrada para el usuario
    if prompt := st.chat_input("What is up?"):
    
        # Almacenar y mostrar el prompt actual
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
    
        # Generar una respuesta usando la API de OpenAI
        stream = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
    
        # Mostrar la respuesta al chat usando st.write_stream, luego almacenarla en session_state
        with st.chat_message("assistant"):
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})

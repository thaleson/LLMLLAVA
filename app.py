import streamlit as st
from api.llava_api import query_llava_api



"""
Streamlit application for image analysis using the LLaVA model.

This application allows users to upload an image and ask a question about the content of the image.
The image is processed by the LLaVA model to generate a response based on the image and the user's input.

The application includes the following features:
- Image upload functionality.
- Text input field for the user to provide a question related to the image.
- A button to submit the question and process the image using the LLaVA model.
- Display of the uploaded image and the response from the model.
- Error handling for failed image processing or API interactions.

Dependencies:
    - Streamlit for the web interface.
    - The query_llava_api function for interacting with the LLaVA API.
"""



st.set_page_config(page_title="LLM LLAVA", page_icon="🤖")
st.title("Análise de Imagem com LLaVA 🤖")


image_file = st.file_uploader("Envie uma imagem", type=["png", "jpg", "jpeg"])


prompt = st.text_input("Digite abaixo sua pergunta sobre a imagem:")

if image_file is not None:
    st.image(image_file, caption="Imagem carregada", use_container_width=True)

    if st.button("Fazer Pergunta sobre a Imagem"):
        with st.spinner('Processando a imagem...'):
            try:
               
                modified_prompt = f"""
                Você é um modelo LLaVA especializado em análise de imagens. Quando receber uma imagem, 
                examine-a atentamente e forneça uma resposta detalhada para a pergunta a seguir. 
                Use todas as informações visíveis na imagem para construir sua resposta precisa e completa.
                Pergunta: {prompt}
                """
                response = query_llava_api(image_file, modified_prompt)
                st.markdown(f"**Resposta do modelo:** {response}", unsafe_allow_html=True)
              
            except Exception as e:
                st.error(f"Erro durante a execução do script: {e}")
else:
    st.warning("Por favor, envie uma imagem para começar.")

import base64
import streamlit as st

def encode_image_to_base64(image_file):
    """
    Converts an image to a base64 encoded string.

    Args:
        image_file (file-like object): The image file to be converted. Typically passed as a file uploaded via Streamlit.

    Returns:
        str: The base64 encoded string representing the image.

    Exceptions:
        - Exception: Any error that occurs during the image reading or encoding process is caught and displayed using Streamlit's error handler.
    
    This function reads the image from the file-like object, encodes it in base64, and returns the encoded string. If an error occurs, it displays an error message in the Streamlit interface and raises the exception.
    """
    try:
        
        image_bytes = image_file.read()
        encoded_image = base64.b64encode(image_bytes).decode("utf-8")
        return encoded_image
    except Exception as e:
        st.error(f"Erro ao converter a imagem: {e}")
        raise

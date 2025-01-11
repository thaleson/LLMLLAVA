import logging

def setup_logger():
    """Configura o logger para mensagens de erro e debug."""
    logger = logging.getLogger('llava_image_analysis')
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger

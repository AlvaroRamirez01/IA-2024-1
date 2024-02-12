import random

def get_response(message:str) -> str:
    mensaje = message.lower()
    if mensaje == 'hola':
        return '¡Hola!'
    return 'No entiendo lo que dices'
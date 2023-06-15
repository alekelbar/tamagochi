import pyttsx3
engine = pyttsx3.init()

# Establecer el idioma deseado (en este caso, español)
engine.setProperty('voice', 'es')

# Configurar la velocidad de habla (opcional)
engine.setProperty('rate', 135)

# Configurar el volumen de habla (opcional)
engine.setProperty('volume', 1.0)


def say(text: str):
    engine.say(text)
    engine.runAndWait()

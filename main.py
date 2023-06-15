from models.tamagochi import Tamagochi
from data.data import playWords, sleepingWords, howAreYouWords
import speech_recognition as sr
from flask import Flask, render_template
from flask_socketio import SocketIO

import pyttsx3
engine = pyttsx3.init()

# Establecer el idioma deseado (en este caso, español)
engine.setProperty('voice', 'es')

# Configurar la velocidad de habla (opcional)
engine.setProperty('rate', 150)

# Configurar el volumen de habla (opcional)
engine.setProperty('volume', 1.0)

tamagochi: Tamagochi = Tamagochi()


# def start_recognition():
#     r = sr.Recognizer()

#     with sr.Microphone() as source:
#         print("Di algo...")
#         audio = r.listen(source)

#     try:
#         text = r.recognize_google(audio, language="es-ES")
#         print("Dijiste: " + text)
#         return text.lower()
#     except sr.UnknownValueError:
#         print("Galeano no entendio.")
#     except sr.RequestError as e:
#         print("Galeano no pudo entender lo que dijiste; {0}".format(e))

#     return ""

app = Flask(__name__)  # constructor de la app
app.static_folder = 'static'
app.config['SECRET_KEY'] = "GALEANO ALCOHOLICO."  # secret key
socketio = SocketIO(app)  # asignación del servidor al socket

tamagochi.setSocket(socketio)


def main(keyword: str):
    # acá las palabras para comer
    eatingWords = ["come"]

    if keyword in playWords:
        tamagochi.play()

    if keyword in sleepingWords:
        tamagochi.sleep()

    if keyword in eatingWords:
        tamagochi.feed()

    if keyword in howAreYouWords:
        tamagochi.howAreYou()

    tamagochi.setImageUrl()


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('action')
def handle_message(msg):
    main(msg)


if __name__ == "__main__":
    socketio.run(app)
    # main()

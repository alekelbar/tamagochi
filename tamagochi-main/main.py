from models.tamagochi import Tamagochi
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()


def iniciar_reconocimiento():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Di algo...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="es-ES")
        print("Dijiste: " + text)
        return text.lower()
    except sr.UnknownValueError:
        print("Galeano no entendio.")
    except sr.RequestError as e:
        print("Galeano no pudo entender lo que dijiste; {0}".format(e))

    return ""


def main():

    tamagochi: Tamagochi = Tamagochi()
    while True:
        keyword = iniciar_reconocimiento()

        if "juega" in keyword:
            engine.setProperty("rate1", 150)
            text = "Vamos  a Jugar "
            engine.say(text)
            engine.runAndWait()
            tamagochi.play()

        if "duerme" in keyword:
            engine.setProperty("rate1", 150)

            text = "Voy a dormir "
            engine.say(text)
            engine.runAndWait()
            tamagochi.sleep()

        if "come" in keyword:
            engine.setProperty("rate1", 150)
            text = "Voy a comer "
            engine.say(text)
            engine.runAndWait()
            tamagochi.feed()

        if "dime cómo estás" in keyword:
            engine.setProperty("rate1", 150)
            text = "Te dire como me siento "
            engine.say(text)
            engine.runAndWait()
            tamagochi.howAreYou()

        if "apagado" in keyword:
            engine.setProperty("rate1", 150)
            text = "Apagando sistema "
            engine.say(text)
            engine.runAndWait()
            break


if __name__ == "__main__":
    main()

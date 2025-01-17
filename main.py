import speech_recognition as sr
from googletrans import Translator
import pyttsx3

def translate_and_speak():
    # Inicializar las herramientas
    recognizer = sr.Recognizer()
    translator = Translator()
    tts_engine = pyttsx3.init()
    tts_engine.setProperty('rate', 150)  # Velocidad de la voz

    with sr.Microphone() as source:
        print("Ajustando al ruido de fondo... espera unos segundos.")
        recognizer.adjust_for_ambient_noise(source, duration=3)
        print("Listo. Habla en español y se traducirá en inglés.")

        try:
            while True:
                print("Escuchando...")
                audio = recognizer.listen(source)
                try:
                    # Reconoce el audio en español
                    text_es = recognizer.recognize_google(audio, language="es-ES")
                    print(f"Texto en español: {text_es}")

                    # Traduce al inglés
                    translation = translator.translate(text_es, src='es', dest='en')
                    text_en = translation.text
                    print(f"Traducido al inglés: {text_en}")

                    # Reproduce la traducción
                    tts_engine.say(text_en)
                    tts_engine.runAndWait()

                except sr.UnknownValueError:
                    print("No se entendió lo que dijiste. Intenta de nuevo.")
                except sr.RequestError as e:
                    print(f"Error con el servicio de reconocimiento de voz: {e}")

        except KeyboardInterrupt:
            print("\nTraducción en tiempo real terminada.")

if __name__ == "__main__":
    translate_and_speak()

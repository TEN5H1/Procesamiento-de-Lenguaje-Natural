import speech_recognition as sr

#Diccionario
sustantivos = {"artista", "paisaje", "amanecer", "pájaros", "cielo", "río", "valle"}
verbos = {"pintó", "cantaban", "fluía"}
adjetivos = {"joven", "hermoso", "montañoso", "alegre", "despejado", "tranquilo"}
adverbios = {"alegremente"}

def clasificar_palabras(texto):
    palabras = texto.lower().split()

    # Diccionario para almacenar
    categorias = {
        "🔸Sustantivos": [],
        "🔸Verbos": [],
        "🔸Adjetivos": [],
        "🔸Adverbios": []
    }

    # Clasificar
    for palabra in palabras:
        if palabra in sustantivos:
            categorias["🔸Sustantivos"].append(palabra)
        elif palabra in verbos:
            categorias["🔸Verbos"].append(palabra)
        elif palabra in adjetivos:
            categorias["🔸Adjetivos"].append(palabra)
        elif palabra in adverbios:
            categorias["🔸Adverbios"].append(palabra)

    return categorias


# Reconocer el audio
def procesar_audio(archivo_audio):

    recognizer = sr.Recognizer()


    with sr.AudioFile(archivo_audio) as source:
        audio = recognizer.record(source)


    try:

        texto = recognizer.recognize_google(audio, language="es-ES")
        print("=== TEXTO RECONOCIDO === \n", texto)

        categorias = clasificar_palabras(texto)

        for categoria, palabras in categorias.items():
            print(f"{categoria}: {', '.join(palabras) if palabras else 'Ninguna'}")

    except sr.UnknownValueError:
        print("No se pudo entender el audio.")
    except sr.RequestError as e:
        print(f"Error en el servicio de reconocimiento de voz; {e}")

procesar_audio("prueba.wav")

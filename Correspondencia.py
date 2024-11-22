from collections import Counter
import string

oraciones_ingles = [
    "the sun is bright",
    "the planet is bright at night",
    "the planet, moon and stars",
    "the day and night",
    "the sky is blue",
]

oraciones_espanol = [
    "el sol es brillante",
    "el planeta es brillante por la noche",
    "el planeta, luna y las estrellas",
    "el día y noche",
    "el cielo es azul",
]

def limpiar_palabra(palabra):
    return palabra.translate(str.maketrans('', '', string.punctuation))

def contar_frecuencia_por_palabra(oraciones):
    frecuencias = Counter()
    for oracion in oraciones:
        palabras = oracion.lower().split()
        for palabra in palabras:
            palabra_limpia = limpiar_palabra(palabra)
            frecuencias[palabra_limpia] += 1
    return frecuencias

def contar_palabras_despues_de_the(oraciones):
    palabras_despues_de_the = Counter()
    for oracion in oraciones:
        palabras = oracion.lower().split()
        for i in range(len(palabras)-1):
            if palabras[i] == "the":
                palabra_siguiente = limpiar_palabra(palabras[i+1])
                palabras_despues_de_the[palabra_siguiente] += 1
    return palabras_despues_de_the

def mostrar_oraciones_y_traducciones(oraciones_ingles, oraciones_espanol):
    print("\n=== ORACIONES Y TRADUCCIONES ===")
    for oracion_ingles, oracion_espanol in zip(oraciones_ingles, oraciones_espanol):
        print(f"🔸 Inglés: {oracion_ingles}")
        print(f"🔹 Español: {oracion_espanol}")
        print()

def mostrar_frecuencia_y_operaciones(frecuencias, oraciones_ingles, oraciones_espanol):
    for palabra, frecuencia in frecuencias.items():
        print(f"\n🌟 Término: '{palabra}'")
        frases_con_palabra = []
        for oracion_ingles, oracion_espanol in zip(oraciones_ingles, oraciones_espanol):
            if palabra in oracion_ingles.lower().split():
                frases_con_palabra.append(oracion_espanol)

        print("🔶 Ejemplos en español donde aparece:")
        for frase in frases_con_palabra:
            print("  -", frase)

        total_palabras = 0
        for frase in frases_con_palabra:
            total_palabras += len(frase.split())

        print(f"🔹 Frecuencia de '{palabra}': {frecuencia} (cantidad)")
        print(f"🔹 Total de palabras en frases con '{palabra}': {total_palabras} (total)")
        print(f"🔹 Frecuencia relativa de '{palabra}' = {frecuencia} / {total_palabras} = {frecuencia / total_palabras:.2f}")

frecuencias_ingles = contar_frecuencia_por_palabra(oraciones_ingles)
palabras_despues_de_the = contar_palabras_despues_de_the(oraciones_ingles)

mostrar_oraciones_y_traducciones(oraciones_ingles, oraciones_espanol)

print("\n=== PRUEBA PALABRAS QUE SIGUEN SALTANDO THE ===")
for palabra, frecuencia in palabras_despues_de_the.most_common():
    frecuencia_relativa = frecuencia / len(oraciones_ingles)
    print(f"🌟 '{palabra}': aparece {frecuencia} veces (frecuencia relativa: {frecuencia_relativa:.2f})")

mostrar_frecuencia_y_operaciones(frecuencias_ingles, oraciones_ingles, oraciones_espanol)

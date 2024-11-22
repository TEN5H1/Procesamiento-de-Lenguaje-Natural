import PyPDF2

def leer_archivo_pdf(ruta):
    with open(ruta, "rb") as archivo_pdf:
        lector = PyPDF2.PdfReader(archivo_pdf)
        return " ".join([pagina.extract_text() for pagina in lector.pages])

def normalizar_texto(texto):
    return texto.lower()
def obtener_frecuencias(texto, colocaciones):
    texto_normalizado = normalizar_texto(texto) #pasa minusculas y masyusculas
    return {colocacion: texto_normalizado.count(colocacion.lower()) for colocacion in colocaciones}
def procesar_pdf_y_mostrar_frecuencias(ruta_pdf, colocaciones):
    texto_extraido = leer_archivo_pdf(ruta_pdf)
    frecuencias = obtener_frecuencias(texto_extraido, colocaciones)


    print("\n=== Frecuencias de colocaciones en el PDF ===")
    for colocacion, ocurrencias in frecuencias.items():
        print(f"- {colocacion}: {ocurrencias} veces")

    return frecuencias


archivo_pdf = "IA.pdf"
lista_colocaciones = [
    "Sistemas Basados en el Conocimiento",
    "artificial",
    "inteligencia"
]


frecuencias_ocurrencias = procesar_pdf_y_mostrar_frecuencias(archivo_pdf, lista_colocaciones)

colocacion_max_frecuencia = max(frecuencias_ocurrencias, key=frecuencias_ocurrencias.get)

print(f"\n>>> La colocación más frecuente es: '{colocacion_max_frecuencia}' apareciendo: {frecuencias_ocurrencias[colocacion_max_frecuencia]}")

import re
from collections import Counter
from PyPDF2 import PdfReader

def extraer_texto_pdf(ruta_pdf):
    lector = PdfReader(ruta_pdf)
    texto = ''
    for pagina in lector.pages:
        texto += pagina.extract_text()
    return texto



def contar_ocurrencias(texto, palabra1, palabra2):
    palabras = re.findall(r'\b\w+\b', texto.lower())
    ocurrencias_palabra1 = Counter(palabras)[palabra1]

    ocurrencias_consecutivas = 0
    for i in range(len(palabras) - 1):
        if palabras[i] == palabra1 and palabras[i + 1] == palabra2:
            ocurrencias_consecutivas += 1

    return ocurrencias_palabra1, ocurrencias_consecutivas

# ocurrencias_consecutivas  es el número de veces que "artificial" sigue a "inteligencia".
# ocurrencias_palabra1      es el número total de veces que aparece la palabra "inteligencia".
def calcular_probabilidad_condicional(ocurrencias_palabra1, ocurrencias_consecutivas):
    if ocurrencias_palabra1 == 0:
        return 0
    return (ocurrencias_consecutivas / ocurrencias_palabra1) * 100




ruta_pdf ="IA.pdf"
texto = extraer_texto_pdf(ruta_pdf)

palabra1 = 'inteligencia'
palabra2 = 'artificial'

ocurrencias_palabra1, ocurrencias_consecutivas = contar_ocurrencias(texto, palabra1, palabra2)
probabilidad = calcular_probabilidad_condicional(ocurrencias_palabra1, ocurrencias_consecutivas)

print("\n=== Frecuencias de colocaciones en el PDF ===")
print(f"\n>>> Numero de apariciones de '{palabra1}' {ocurrencias_palabra1} : veces <<<")
print(f"\n>>> Ocurrencias consecutivas de '{palabra1} {palabra2}': {ocurrencias_consecutivas} veces <<<")
print(f"\n>>> Probabilidad condicional de que despues de ({palabra2}) se encuentre la palabra ({palabra1}) = {probabilidad:.2f}% <<<")

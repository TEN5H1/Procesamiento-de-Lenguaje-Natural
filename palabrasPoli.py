import PyPDF2
import re



# Función para analizar el contexto de una palabra y determinar el significado
def identificar_significado(contexto):
    # Definimos palabras clave que indicarían los posibles significados
    palabras_medicas = ["cirugía", "paciente", "médico", "hospital", "intervención"]
    palabras_accion = ["realizar", "acción", "tarea", "proceso", "ejecutar", "conocimiento"]

    # Comprobar si el contexto tiene palabras relacionadas con la medicina
    if any(palabra in contexto for palabra in palabras_medicas):
        return "Se refiere a realizar una operación médica."
    elif any(palabra in contexto for palabra in palabras_accion):
        return "Se refiere a llevar a cabo una acción, tarea o proceso."
    else:
        return "No se puede determinar el significado específico en este contexto."


# Leer el archivo PDF
def leer_pdf(ruta_pdf):
    with open(ruta_pdf, 'rb') as archivo:
        lector_pdf = PyPDF2.PdfReader(archivo)
        texto_completo = ""
        for pagina in lector_pdf.pages:
            texto_completo += pagina.extract_text()
        return texto_completo


# Buscar la palabra y analizar contextos
def buscar_contextos(texto, palabra):
    contextos = []
    for match in re.finditer(r'\b{}\b'.format(re.escape(palabra)), texto):
        inicio = max(0, match.start() - 30)
        fin = min(len(texto), match.end() + 30)
        contexto = texto[inicio:fin]
        contextos.append((contexto, identificar_significado(contexto)))
    return contextos


# Programa principal
def main():
    ruta_pdf = "IA.pdf"
    texto = leer_pdf(ruta_pdf)

    # Solicitar palabra policémica al usuario
    palabra = input("Ingresa la palabra policémica a buscar (por ejemplo, 'operar'): ").strip().lower()

    # Buscar contextos y determinar significados
    contextos = buscar_contextos(texto, palabra)

    # Mostrar resultados
    if contextos:
        print(f"\n=== RESULTADOS PARA: '{palabra}' ===")
        for i, (contexto, significado) in enumerate(contextos, start=1):
            print(f"\n>>> CONTEXTO {i} <<< \n {contexto}")
            print(f"\n>>> INTERPRETACION <<< {significado}")
    else:
        print(f"No se encontró la palabra '{palabra}' en el documento.")


# Ejecutar el programa
main()

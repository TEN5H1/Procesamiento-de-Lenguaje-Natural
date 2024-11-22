import spacy
nlp = spacy.load("es_core_news_sm")

def detectar_simbolos_no_terminales(frase):
    doc = nlp(frase)

    sujeto = ""
    accion = ""
    determinantes = []
    sustantivos = []
    verbos = []
    objetos = []

    # Símbolos no terminales
    for token in doc:
        if token.dep_ in ['nsubj', 'nsubjpass']:  # Sujeto
            sujeto += token.text + " "
            sustantivos.append(token.text)
        elif token.dep_ == 'ROOT':  # Verbo
            accion += token.text + " "
            verbos.append(token.text)
        elif token.dep_ in ['dobj', 'attr']:  # Objeto
            objetos.append(token.text)
            accion += token.text + " "
        elif token.dep_ == 'amod':  # Modificador del nombre
            accion += token.text + " "
        elif token.dep_ == 'det':  # Determinantes
            determinantes.append(token.text)

    sujeto = sujeto.strip()
    accion = accion.strip()

    # Mostrar los símbolos no terminales detectados
    print("Símbolos No Terminales Detectados.")
    print("🔹 D :")
    print(f"   - {', '.join(determinantes) if determinantes else 'Ninguno'}")
    print("🔹 N :")
    print(f"   - {', '.join(sustantivos) if sustantivos else 'Ninguno'}")
    print("🔹 V :")
    print(f"   - {', '.join(verbos) if verbos else 'Ninguno'}")
    print("🔹 Obejeto:")
    print(f"   - {', '.join(objetos) if objetos else 'Ninguno'}\n")

    # Imprimir la estructura de la oración
    print(" S :")
    print(f" S → NP VP: La oración completa se descompone en un sujeto (NP) y una acción (VP).\n")
    print(f"🔸 NP → \"{sujeto}\": El sujeto en esta oración es \"{sujeto}\".")
    print(f"🔸 VP → \"{accion}\": La acción que realiza el sujeto es \"{accion}\".")

# Solicitar una frase al usuario
frase = input(" Favor de ingresar una oración:  \n")
detectar_simbolos_no_terminales(frase)

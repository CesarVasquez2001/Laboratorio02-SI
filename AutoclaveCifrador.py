def cifrador_vigenere(texto, clave):

    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    
    resultado = ""
    clave_index = 0
    # Definir los reemplazos de las tildes
    reemplazos = {
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u",
        "Á": "A",
        "É": "E",
        "Í": "I",
        "Ó": "O",
        "Ú": "U"
    }
    # Realizar los reemplazos en el texto y clave
    texto = "".join(reemplazos.get(c, c) for c in texto)
    clave = "".join(reemplazos.get(c, c) for c in clave)
    # Convertir el texto claro y clave a mayúsculas
    texto = texto.upper()
    clave = clave.upper()
    for caracter in texto:
        if caracter in alfabeto:
            # Obtener el índice del carácter en el alfabeto
            indice_caracter = alfabeto.index(caracter)
            # Obtener el carácter correspondiente de la clave
            clave_caracter = clave[clave_index % len(clave)]
            indice_clave = alfabeto.index(clave_caracter)
            # Aplicar el cifrado de Vigenère
            nuevo_indice = (indice_caracter + indice_clave) % len(alfabeto)
            nuevo_caracter = alfabeto[nuevo_indice]
            # Agregar el carácter cifrado al resultado
            resultado += nuevo_caracter
            # Avanzar al siguiente carácter de la clave
            clave_index += 1
        """
        else:
            # Conservar caracteres no presentes en el alfabeto (espacios, puntuaciones, etc.)
            resultado += caracter
        """
    return resultado


def descifrador_vigenere(texto, clave):
    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    resultado = ""
    clave_index = 0
    # Definir los reemplazos de las tildes
    reemplazos = {
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u",
        "Á": "A",
        "É": "E",
        "Í": "I",
        "Ó": "O",
        "Ú": "U"
    }
    # Realizar los reemplazos en el texto y clave
    texto = "".join(reemplazos.get(c, c) for c in texto)
    clave = "".join(reemplazos.get(c, c) for c in clave)
    # Convertir el texto claro y clave a mayúsculas
    texto = texto.upper()
    clave = clave.upper()
    for caracter in texto:
        if caracter in alfabeto:
            # Obtener el índice del carácter en el alfabeto
            indice_caracter = alfabeto.index(caracter)
            # Obtener el carácter correspondiente de la clave
            clave_caracter = clave[clave_index % len(clave)]
            indice_clave = alfabeto.index(clave_caracter)
            # Aplicar el descifrado de Vigenère
            nuevo_indice = (indice_caracter - indice_clave) % len(alfabeto)
            nuevo_caracter = alfabeto[nuevo_indice]
            # Agregar el carácter descifrado al resultado
            resultado += nuevo_caracter
            # Avanzar al siguiente carácter de la clave
            clave_index += 1
        """
        else:
            # Conservar caracteres no presentes en el alfabeto (espacios, puntuaciones, etc.)
            resultado += caracter
        """
    return resultado



def cifrador_autoclave(texto_claro, clave):
    texto = texto_claro[0:len(clave)]
    resultado = cifrador_vigenere(texto,clave)
    texto = texto_claro[len(clave):len(texto_claro)]
    resultado += cifrador_vigenere(texto,texto_claro)
    return resultado



texto_claro = "LOGOCFTKG"
clave = "LUNA"
auto_clave="AUTOCLAVE"
texto_descifrado = descifrador_autoclave(texto_claro, clave,auto_clave)
print("Texto descifrado:", texto_descifrado)


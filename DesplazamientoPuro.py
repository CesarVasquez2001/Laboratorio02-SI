def cifrador_desplazamiento(texto_claro, desplazamiento):
    # Definir el alfabeto módulo 27 con la letra Ñ
    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    
    # Convertir el texto claro a mayúsculas
    texto_claro = texto_claro.upper()
    
    texto_cifrado = ""
    for caracter in texto_claro:
        if caracter in alfabeto:
            # Obtener el índice del carácter en el alfabeto
            indice = alfabeto.index(caracter)
            # Aplicar el desplazamiento (Cifrado Cesar)
            nuevo_indice = (indice + desplazamiento) % len(alfabeto)
            # Obtener el nuevo carácter cifrado
            carac_cifrado = alfabeto[nuevo_indice]
            # Agregar el carácter cifrado al texto resultante
            texto_cifrado += carac_cifrado
        """
        else:
            # Conservar caracteres no presentes en el alfabeto (espacios, puntuaciones, etc.)
            texto_cifrado += caracter
        """
    return texto_cifrado

# Función para desencriptar utilizando el cifrador de desplazamiento
def descifrador_desplazamiento(texto_cifrado, desplazamiento):
    # Utilizar un desplazamiento negativo para desencriptar
    desplazamiento_negativo = -desplazamiento

    # Aplicar el cifrador de desplazamiento con el desplazamiento negativo
    texto_descifrado = cifrador_desplazamiento(texto_cifrado, desplazamiento_negativo)

    return texto_descifrado


# Ejemplo de uso
texto_claro = input("Ingrese el texto claro: ")
desplazamiento = int(input("Ingrese el desplazamiento: "))

texto_cifrado = cifrador_desplazamiento(texto_claro, desplazamiento)
print("Texto cifrado:", texto_cifrado)

texto_descifrado = descifrador_desplazamiento(texto_cifrado, desplazamiento)
print("Texto descifrado:", texto_descifrado)
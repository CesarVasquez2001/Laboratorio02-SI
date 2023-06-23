def cifrador_vigenere_ascii(texto, clave):
    resultado = ""
    clave_index = 0
    for ascii_caracter in texto:
        # Obtener el valor ASCII correspondiente de la clave
        ascii_clave = clave[clave_index % len(clave)]

        # Aplicar el cifrado de Vigenère en ASCII
        nuevo_ascii = (ascii_caracter + ascii_clave) % 256

        # Agregar el código ASCII cifrado al resultado
        resultado += chr(nuevo_ascii)

        # Avanzar al siguiente carácter de la clave
        clave_index += 1

    return resultado


# Ejemplo de uso
texto_claro_ascii = [9, 9, 1, 0, 1, 1, 5, 9, 7, 1, 1, 4]
clave = [122]

texto_cifrado = cifrador_vigenere_ascii(texto_claro_ascii, clave)
print("Texto cifrado:", texto_cifrado)

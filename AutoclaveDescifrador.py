def descifrador_autoclave(texto_cifrado, clave):
    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    resultado = ""
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
    texto_cifrado = "".join(reemplazos.get(c, c) for c in texto_cifrado)
    clave = "".join(reemplazos.get(c, c) for c in clave)
    # Convertir el texto cifrado y clave a mayúsculas
    texto_cifrado = texto_cifrado.upper()
    clave = clave.upper()
    
    z = len(alfabeto)
    max = len(texto_cifrado)
    maxk = len(clave)

    j = 0
    for i in range(max):
        car = texto_cifrado[i]
        cark = clave[i]
        pos = alfabeto.index(car)
        posk = alfabeto.index(cark)

        pos = (pos - posk) % z
        while pos < 0:
            pos += z
        car = alfabeto[pos]
        if i >= maxk - 1:
            clave += resultado[j]
            j += 1
        resultado += car

    return resultado

texto_cifrado = "XHGDQESDMPKÑDEEDKNGJZPFJSUIFZOLFCINFJCESVZTGBFXCIUDAYNUUDIZYWWZBEYNVQWIVUNKZEPHDODQUZZLBDNDRWTHQSERÑIVMLERCMGIFLSORZXTSDIGLOXQSDJHWVCIWQXQJCKMBPOKMPSKMUVIMNJDNBLCSZHXHNYYUIXDBSOXHZLXWVGDJGXHWLTDWKÑSAQIMZLNBVMLXHUOQQXIQGWGUFTWKZKMOKUDNINSIFJDUOZIJBSVVOWFAIEÑGYOWPSOAP"
clave = "UNODELOSMASGRANDESCRIPTOGRAFOS"

texto_descifrado = descifrador_autoclave(texto_cifrado, clave)
print(texto_descifrado)

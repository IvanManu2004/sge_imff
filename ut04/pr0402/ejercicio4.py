def contarPalabras(cadenaContar):
    i = 0
    for a in cadena.split(" "):
        i += 1
    return i
cadena = str(input("Introduce una cadena separada por espacios: "))
numPalabras = contarPalabras(cadena)
print("Hay " + str(numPalabras) + " palabras")
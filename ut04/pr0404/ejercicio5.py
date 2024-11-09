def invertirDiccionario(diccionario):
    claves = []
    valores = []
    for a in diccionario:
        claves.append(a)
        valores.append(diccionario[a])
    nuevoDiccionario = {}
    indice = 0
    while (indice < len(claves)):
        nuevoDiccionario[valores[indice]] = claves[indice]
        indice += 1
    return nuevoDiccionario

dicc = {
    "gato":"animal",
    "pelota":"juguete",
    "arbol":"planta"
}

diccInver = invertirDiccionario(dicc)
print(diccInver)
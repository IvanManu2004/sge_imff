def diccionarioCaracteres (cadena):
    listaLetras = list(cadena)
    indice = 0
    contadorLetras = 0
    for a in cadena:
        contadorLetras+=1
    diccionario = {}
    while (int(indice) < contadorLetras):
        diccionario["letra"+str(indice)] = listaLetras[indice]
        indice += 1
    print(diccionario)


frase = str(input("Introduce una cadena: "))
diccionarioCaracteres(frase)
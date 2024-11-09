def eliminarRepeticiones (cadena):
    contadorCadena = 0
    for a in cadena:
        contadorCadena+=1
    cadenaLista = list(cadena)
    indice = 1
    indiceAnterior = 0
    while (indice < contadorCadena):
        letra1 = cadenaLista[indiceAnterior]
        letra2 = cadenaLista[indice]
        if (letra1 == letra2):
            cadenaLista.pop(indice)
            contadorCadena-=1
        else:
            indiceAnterior+=1
            indice+=1
    nuevaCadena = ""
    for a in cadenaLista:
       nuevaCadena += a
    print(str(nuevaCadena)) 
    
frase = str(input("Introduce una cadena: "))
eliminarRepeticiones(frase)
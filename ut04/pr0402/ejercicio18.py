def rotar(cadena, numVeces):
    longitud = 0
    for a in cadena:
        longitud += 1
    if (longitud == numVeces):
        nuevaCadena = cadena
    else:
        if(numVeces > longitud):
            numVeces = numVeces % longitud
        nuevaCadena = cadena[numVeces:] + cadena[:numVeces] 
    print(nuevaCadena)
frase = str(input("Introduce una cadena: "))
numero = int(input("Introduce el n veces a rotar: "))
rotar(frase, numero)
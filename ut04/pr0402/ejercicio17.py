def separadorMil (num):
    numeros = list(num)
    longitud = 0
    for a in numeros:
        longitud+=1
    numDePuntos = int(longitud / 3)
    indice = 0
    apuntador = longitud - 3
    while(indice < numDePuntos):
        numeros.insert(apuntador, ".")
        indice +=1
        apuntador = apuntador - 3
    nuevoNumero = ""
    for a in numeros:
        nuevoNumero+= a
    print(nuevoNumero)

numero = str(input("Introduce un numero: "))
separadorMil(numero)
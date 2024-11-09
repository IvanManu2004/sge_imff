def compararASCII(cadena1, cadena2):
    palabrasCadena1 = cadena1.split(" ")
    palabrasCadena2 = cadena2.split(" ")
    contadorCadena1 = 0
    contadorCadena2 = 0
    for palabra in palabrasCadena1:
        for letra in palabra:
            contadorCadena1 += ord(letra)
    for palabra in palabrasCadena2:
        for letra in palabra: 
            contadorCadena2 += ord(letra)
    if(contadorCadena1 > contadorCadena2):
        print("La cadena 1 es mayor en valor ASCII")
    else :
        print("La cadena 2 es mayor en valor ASCII")
    print("Cadena1: " + str(contadorCadena1))
    print("Cadena2: " + str(contadorCadena2))


frase1 = str(input("Introduce una cadena: "))
frase2 = str(input("Introduce una cadena: "))
compararASCII(frase1, frase2)
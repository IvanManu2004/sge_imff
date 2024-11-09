cadena = str(input("Introduce una cadena: "))
cadenaSeparada = cadena.split(" ")
cadenaNueva = ""
numLetrasMax = 0
palabraMasLarga = ""
for palabra in cadenaSeparada:
    numLetras = 0
    for letra in palabra:
        numLetras += 1
    if(numLetras > numLetrasMax):
        palabraMasLarga = palabra
        numLetrasMax = numLetrasMax
print(palabraMasLarga)
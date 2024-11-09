longitudBase = int(input("Introduce un numero"))
if (longitudBase % 2 == 0):
    while (longitudBase % 2 == 0) :
        longitudBase = int(input("Introduce un numero impar"))

mitadNumero = (longitudBase + 1) / 2
espacio = ""
caracter = "*"
caracteres = ""
imprimir = ""
index = 0
while (index < mitadNumero):
    i = index
    espacio = ""
    while (i < (mitadNumero - 1)):
        espacio += " "
        i += 1
    if (index == 0):
        caracteres += caracter
    else :
        caracteres += caracter + caracter
    imprimir = espacio + caracteres
    print(imprimir)
    index += 1
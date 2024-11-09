cadena = str(input("Introduce una cadena: "))
contadorCadena = 0
cadenasSeparadas = cadena.split(" ")
for a in cadenasSeparadas:
    contadorCadena+=1
indice = 0
nuevaCadena = ""
while (contadorCadena > indice):
    contadorCadena -= 1
    palabra = cadenasSeparadas[contadorCadena]
    nuevaCadena += palabra + " "

print(str(nuevaCadena)) 
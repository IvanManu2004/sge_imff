cadena = str(input("Introduce una cadena: "))
contadorCadena = 0
for a in cadena:
    contadorCadena+=1
cadenaLista = list(cadena)
indice = 0
nuevaCadena = ""
while (indice < contadorCadena):
    letra = cadenaLista[indice]
    if (letra.isupper()):
        nuevaCadena += letra.lower()
    else :
        nuevaCadena += letra.upper()
    indice+=1

print(str(nuevaCadena)) 
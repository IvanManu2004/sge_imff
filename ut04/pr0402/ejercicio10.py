cadena = str(input("Introduce una cadena: "))
contadorCadena = 0
caracteres = list(cadena)
for a in caracteres:
    contadorCadena+=1
indice = 0
nuevaCadena = ""
while (indice < contadorCadena):
    letra = caracteres[indice]
    if(letra.isalnum() or letra==" "):
        nuevaCadena += letra
    indice += 1

print(str(nuevaCadena)) 
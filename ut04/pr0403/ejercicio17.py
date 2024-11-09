listaNumeros = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
media = 0
for a in listaNumeros:
    media += a
media = media / len(listaNumeros)
lista1 = []
lista2 = []
for b in listaNumeros:
    if (b >= media):
        lista1.append(b)
    else :
        lista2.append(b)
print(lista1)
print(lista2)
def elementosComunes(lista1, lista2):
    contador = 0
    nuevaLista = []
    while(contador < len(lista1)):
        a = lista1[contador]
        if(lista2.count(a) > 0):
            indice = lista1.index(a)
            nuevaLista.append(lista1.pop(indice))
        else:
            contador += 1
    return nuevaLista
lista01 = ["perro", "gato", "conejo", "lobo"]
lista02 = ["pelota", "gato", "zanahoria", "perro"]
lista03 = elementosComunes(lista01, lista02)
print(lista03)
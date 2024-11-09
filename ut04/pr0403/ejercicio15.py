def concatenarListas(lista1, lista2):
    contador = 0
    nuevaLista = []
    for a in lista1:
        nuevaLista.append(a)
        nuevaLista.append(lista2[contador])
        contador += 1
    return nuevaLista
lista01 = ["perro", "gato", "conejo", "lobo"]
lista02 = ["pelota", "rascador", "zanahoria", "pelaje"]
lista03 = concatenarListas(lista01, lista02)
print(lista03)
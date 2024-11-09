def listaInversa (lista):
    longitud = (len(lista) - 1)
    nuevaLista = []
    while (longitud >= 0):
        nuevaLista.append(lista[longitud])
        longitud -= 1
    return nuevaLista
lista1 = [1,"perro",3,4,True,5,"gato",7,8,False,10,11,12]
lista2 = listaInversa(lista1)
print(lista2)

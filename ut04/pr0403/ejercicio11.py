lista = [1, 1, 2, 3, 4, 4, 3, 6, 5, 9, 7, 3, 6, 5, 1]
listaNueva = []
for num in lista:
    if(listaNueva.count(num) == 0):
        listaNueva.append(num)
print(listaNueva)
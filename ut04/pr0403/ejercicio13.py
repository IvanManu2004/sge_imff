listaNumero = [1,2,3,4,5,5,6,7,8,9,10,11,12]
listaPares = []
for num in listaNumero:
    if(num % 2 == 0):
        listaPares.append(num)
print(listaPares)
import math
def valorMaxYMin (lista):
    numMax = 0
    numMin = math.inf
    for num in lista:
        if(num < numMin):
            numMin = num
        if(num > numMax):
            numMax = num
    print(str(numMax) + ", " + str(numMin))
listaNumero = [1,2,3,4,5,5,6,7,8,9,10,11,12]
valorMaxYMin(listaNumero)
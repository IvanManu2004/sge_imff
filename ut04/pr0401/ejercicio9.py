numMax = int(input("Introduce el n primeros numeros para la secuencia: "))
numAnterior = 0
guardarNum = 0
numAnteriorAnterior = 0
num = 0
index = 0
while (index < numMax):
    num = numAnterior + numAnteriorAnterior
    print(num)
    numAnteriorAnterior, numAnterior = numAnterior, num
    index += 1
    if(index == 1 and (numAnterior == 0 and numAnteriorAnterior == 0)):
        numAnterior = 1
    
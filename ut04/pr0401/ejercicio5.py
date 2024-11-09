import math
index = 0
numMax = 0
numMin = math.inf
while (index < 5):
    num = int(input("introduce un numero"))
    if (num >= numMax):
        numMax = num
    if (num < numMin):
        numMin = num
    index += 1
print("El numero mayor es " + str(numMax) + " y el numero minimo es " + str(numMin))

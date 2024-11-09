n = int(input("Introduce un numero"))
k = int(input("Introduce el numero de veces que lo quieres multiplicar"))
index = 0
while(int(index) <= int(k)):
    index += 1
    numMultiplicado = int(n)*index
    print(str(n) + " * " + str(index) + " = " + str(numMultiplicado))
    

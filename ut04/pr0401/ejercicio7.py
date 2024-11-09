from random import *
num = randint(1, 100)
numUsuario = int(input("Introduce un numero: ")) 
while (numUsuario!= num):
    if (numUsuario < num):
        print("El numero es mas grande")
    else:
        print("El numero es mas pequeño")
    numUsuario = int(input("Introduce un numero: ")) 
print("Has acertado el numero")
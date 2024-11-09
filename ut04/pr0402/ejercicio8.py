palabra1 = str(input("Introduce una palabra: "))
palabra2 = str(input("Introduce una palabra: "))
resultado = True
cadena1 = list(palabra1)
for a in cadena1:
    if(palabra2.count(a) == 0):
        resultado = False
if(resultado):
    print("Las dos palabras son anagramas") 
else:
    print("Las dos palabras no son anagramas") 
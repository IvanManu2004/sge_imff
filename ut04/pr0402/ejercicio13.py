def decodificarRLE (cadena):
    cadenaSeparada = cadena.split(" ")
    nuevaCadena = ""
    for palabra in cadenaSeparada:
        letraC = ""
        for letra in palabra:
            if letra.isalpha():
                letraC= letra
            elif letra.isdigit():
                nuevaCadena += letraC * int(letra)
        nuevaCadena += " "
    print(nuevaCadena)

    
frase = str(input("Introduce una cadena RLE: "))
decodificarRLE(frase)
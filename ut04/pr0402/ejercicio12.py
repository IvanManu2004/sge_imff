def codificarRLE (cadena):
    cadenaSeparada = cadena.split(" ")
    nuevaCadena = ""
    for palabra in cadenaSeparada:
        letraAnterior = ""
        for letra in palabra:
            if letraAnterior == "":
                letraAnterior = letra
                contador = 1
            elif letraAnterior == letra:
                contador += 1
            else:
                nuevaCadena += letraAnterior + str(contador)
                letraAnterior = letra
                contador = 1
        nuevaCadena += letraAnterior + str(contador)
        letraAnterior = letra
        contador = 1
        nuevaCadena += " "
    print(nuevaCadena)

    
frase = str(input("Introduce una cadena: "))
codificarRLE(frase)
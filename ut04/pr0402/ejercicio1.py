def cuantasLetras (cadena):
        i = 0
        cuentaVocales = 0
        vocales={"a", "e", "i", "o", "u"}
        for vocal in vocales:
           cuentaVocales += cadena.lower().count(vocal) 
        for a in cadena:
            i += 1
        cuentaConsonantes = i - cuentaVocales
        print("La cadena tiene " + str(cuentaVocales) + " vocales y " + str(cuentaConsonantes) + " consonantes")
palabras = str(input("Introduce una cadena: "))
cuantasLetras(palabras)
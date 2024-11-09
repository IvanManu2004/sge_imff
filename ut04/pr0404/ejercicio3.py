frase = str(input("Introduce una frase: "))

fraseSeparada = frase.split(" ")
diccionario = {}
for a in fraseSeparada:
        diccionario[a] = (diccionario[a] + 1) if diccionario.get(a) != None else 1
print(diccionario)
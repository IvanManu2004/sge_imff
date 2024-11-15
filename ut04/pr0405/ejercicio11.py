# Ejemplo de lista de entrada
alumnos = [("Ana", 4), ("Bruno", 7), ("Clara", 5), ("David", 8)]
# Resultado esperado: ['Bruno', 'Clara', 'David']
alumnosAprobados = filter(lambda x : x[1] >= 5, alumnos)
nombres = list(map(lambda x: x[0], alumnosAprobados))
print(nombres)
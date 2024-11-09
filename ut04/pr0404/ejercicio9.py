estudiantes = {
    "Ana": {"Matemáticas": 8.5, "Física": 9.0, "Programación": 7.8},
    "Carlos": {"Matemáticas": 9.2, "Física": 8.8, "Programación": 9.4},
    "Luis": {"Matemáticas": 7.6, "Física": 8.0, "Programación": 8.5},
    "María": {"Matemáticas": 9.5, "Física": 10.0, "Programación": 9.8},
    "Jorge": {"Matemáticas": 8.8, "Física": 8.4, "Programación": 7.9},
    "Sofía": {"Matemáticas": 9.1, "Física": 8.9, "Programación": 9.3}
}
diccionarioMediaEstudiante = {}
diccionarioMediaAsignatura = {}
for a in estudiantes:
    dicc = estudiantes[a]
    resultado = 0
    for b in dicc:
        resultado += dicc[b]
    resultado = resultado / len(dicc)
    diccionarioMediaEstudiante[a] = resultado
mates = 0
fisica = 0
progr = 0
for a in estudiantes:
    dicc = estudiantes[a]
    mates += dicc["Matemáticas"]
    fisica += dicc["Física"]
    progr += dicc["Programación"]
mates = mates / len(estudiantes)
fisica = fisica / len(estudiantes)
progr = progr / len(estudiantes)
diccionarioMediaAsignatura["Matemáticas"] = mates
diccionarioMediaAsignatura["Física"] = fisica
diccionarioMediaAsignatura["Programación"] = progr

print(diccionarioMediaEstudiante)
print(diccionarioMediaAsignatura)

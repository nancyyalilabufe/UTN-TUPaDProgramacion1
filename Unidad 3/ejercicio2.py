#Calificacion notas (También le agregué lo de excelente 10 porque practiqué antes y me pareció que queda más completo así)

nota = float(input("Ingrese por favor su nota de examen:"))

if nota == 10:
    print("Excelente, tiene 10!!")
elif nota >= 6:
    print("Ud. está aprobado")
else:
    print("Ud. está desaprobado")
    
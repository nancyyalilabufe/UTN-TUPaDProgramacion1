#Solicitar edad e indicar categoria.

edad = int(input("Por favor, ingrese su edad:"))

if edad < 12:
    print("Ud. pertenece a la categoría de Niño/a")
elif edad >= 12 and edad < 18:
    print("Ud. pertenece a la categoría de Adolescente")
elif edad >= 18 and edad <= 30:
    print("Ud. pertenece a la categoría de Adulto Joven")
else:
    print("Ud. pertenece a la categoría de Adulto")

#Nombre, opción y mayúscula/minúscula.

nombre = input("Ingrese por favor su nombre:")
opcion = input("""
Ingrese opción 1 si desea su nombre en MAYÚSCULA
Ingrese opción 2 si desea su nombre en minúscula
Ingrese opción 3 si desea la primera letra de su nombre en Mayúscula
""")

if opcion == "1":
    print((nombre.upper()))  #convierte a mayúscula el nombre
elif opcion == "2":          
    print(nombre.lower())     #convierte a minúscula el nombre
elif opcion == "3":
    print(nombre.title())       #convierte la primer letra a Mayúscula
else:
    print("Opción inválida, por favor ingrese 1, 2 o 3.")
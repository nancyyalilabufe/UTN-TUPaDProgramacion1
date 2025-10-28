#1) Dado el diccionario precios_frutas Añadir:  Naranja = 1200, Manzana = 1500 yPera = 2300
print("-" * 80)
print("EJERCICIO 1")
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas ['Naranja'] = 1200
precios_frutas ['Manzana'] = 1500
precios_frutas ['Pera'] = 2300


print(precios_frutas)

#2) 
print("-" * 80)
print("EJERCICIO 2")

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

#3)
print("-" * 80)
print("EJERCICIO 3")

frutas_sinprecio = ['Banana', 'Ananá', 'Melón', 'Uva', 'Naranja', 'Manzana', 'Pera']

print(frutas_sinprecio)


#4)
print("-" * 80)
print("EJERCICIO 4")
# Programa 1: Agenda de Teléfonos (BUSQUEDA POR NOMBRE) (no comprendí si ya estaban cargados los nombres o debia cargarlo el usuario por eso hice dos prog)

contactos = {
    'pedro': 3834458741, 
    'maría': 3834986542, 
    'gimena': 3834784985, 
    'ramón': 3834125474, 
    'oscar': 3834698145
    }
nombre = input("Ingrese el nombre del contacto que quiere consultar: ").lower()

if nombre in contactos:
    print(f"El número de {nombre} es {contactos[nombre]}")
else:
    print("Ese contacto no está en la agenda.")


# Programa 1: Agenda de Teléfonos (BUSQUEDA POR NOMBRE) 
agenda_telefonica = {}

# Cargamos los 5 contactos
print("-----------Carga Contactos----------")
for i in range(5):
    nombre = input(f"Ingrese por favor el nombre del contacto {i+1}: ").lower()
    numero = input(f"Ingrese el número de telefónico de {nombre}: ")

# Si el nombre ya existe, agregamos el número a su lista (para posibles nombres repetidos con diferentes numeros)
    if nombre in agenda_telefonica:
        agenda_telefonica[nombre].append(numero)
    else:
        agenda_telefonica[nombre] = [numero]


# Consultar por nombre
print("------------Consulta números------------")

while True:
    buscar_numero = input("Ingrese por favor el nombre del contacto a buscar(o 'salir' para terminar): ").lower()
    if buscar_numero.lower() == "salir":
        print("Fin del programa")
        break
    # utilicé .join()para unir los números de la lista en una sola cadena, separados por comas
    elif buscar_numero in agenda_telefonica:
        numeros = ", ".join(agenda_telefonica[buscar_numero])
        print(f"El número de {buscar_numero} es: {numeros}")

    else:
        print("Ese contacto no está en la agenda.")


#5)
print("-" * 80)
print("EJERCICIO 5")
#solicito una frase al usuario
frase = input("Ingrese una frase por favor: ").lower()

# contar palabras
palabras = frase.lower().split()

#Palabras únicas 
palabras_unicas = set(palabras)
print("\nPalabras únicas:")
print(palabras_unicas)


#cantidad de veces que aparece cada palabra
from collections import Counter
frecuencia = Counter(palabras)

print("\nCantidad de veces que aparece cada palabra:")
print(frecuencia)

#6)
print("-" * 80)
print("EJERCICIO 6")
# nombres de 3 alumnos, y para cada uno una tupla de 3 notas y mostrar el promedio

alumnos = {
    'Esteban': (9,7,8),
    'Juan': (10,6,3),
    'Renzo': (4,5,3)
    }

# Muestra el promedio de cada alumno
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: promedio = {promedio:.2f}")

#7) 
print("-" * 80)
print("EJERCICIO 7")
# dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2

parcial1 = {"Esteban", "María", "Gimena", "Oscar"}
parcial2 = {"Pedro", "Gimena", "Matias", "Oscar"}

# en ambos(intersección)
ambos = parcial1 & parcial2

# aprobados en uno solo de ellos: (dif simétrica)
solo_uno = parcial1 ^ parcial2

#aprobados en al menos un parcial: (unión)
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos:", sorted(ambos))
print("Aprobaron solo uno:", sorted(solo_uno))
print("Aprobaron al menos uno:", sorted(al_menos_uno))

#8) 
print("-" * 80)
print("EJERCICIO 8")

#Diccionario donde las claves sean nombres de productos y los valores su stock

tienda_limpieza = {
    "Jabón": 5, 
    "Detergente": 2, 
    "Aerosol para ambientes": 22, 
    "Raid": 8
    }

#consultar el stock de un producto ingresado
while True:
    producto = input("\nIngrese el nombre del producto (o 'salir' para terminar): ").lower()

    if producto.lower() == "salir":
        print("\nFin del programa. Stock final:")
        print(tienda_limpieza)
        break

    # Si el producto existe, muestro su stock
    if producto in tienda_limpieza:
        print(f"Actualmente hay {tienda_limpieza[producto]} unidades de {producto}.")
        agregar = input("¿Desea agregar unidades? (s/n): ").lower()
        if agregar == "s":
            cantidad = int(input("¿Cuántas unidades desea agregar?: "))
            tienda_limpieza[producto] = tienda_limpieza[producto] + cantidad
            print(f"Nuevo stock de {producto}: {tienda_limpieza[producto]}")
        else:
            print("No se agregaron unidades.")

#si el producto no existe, agregarlo
    else:
        print(f"El producto '{producto}' no existe en el stock.")
        agregar_nuevo = input("¿Desea agregarlo? (s/n): ").lower()
        if agregar_nuevo == "s":
            cantidad = int(input("Ingrese cuántas unidades desea agregar: "))

            tienda_limpieza[producto] = cantidad
            print(f"Producto '{producto}' agregado con {cantidad} unidades.")
        else:
            print("No se agregó el producto.")

#9) 
print("-" * 80)
print("EJERCICIO 9")
#agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.

agenda = {
    ("Lunes", "08:00"): "Daily Scrum con el equipo",
    ("Martes", "15:00"): "Clase de Inglés",
    ("Miercoles", "20:00"): "Gym",
    ("Jueves", "10:00"): "Médico",
    ("Viernes", "11:00"): "Cierre de Sprint"
}

# Consulta
dia = input("Ingrese el día(Lunes, martes, miercoles...etc.): ").capitalize()
hora = input("Ingrese la hora (por ejemplo 10:00): ")

clave = (dia, hora)

if clave in agenda:
    print(f"El evento programado para {dia} a las {hora} es: {agenda[clave]}")
else:
    print(f"No hay ningún evento programado para {dia} a las {hora}.")

#10) 
print("-" * 80)
print("EJERCICIO 10")
#diccionario que mapea nombres de países con sus capitales

nombre_paises = {"Australia": "Canberra", "Italia": "Roma", "Colombia": "Bogotá", "España": "Madrid"}

invertidos = {capital: pais for pais, capital in nombre_paises.items()}

print("\nPaíses con sus capitales:")
print(nombre_paises)

print("\nDiccionario invertido (capitales -> países):")
print(invertidos)
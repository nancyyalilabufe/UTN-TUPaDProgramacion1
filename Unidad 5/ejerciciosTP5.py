#EJERCICIO 1 - Lista de estudiantes 
print("-" * 40)
print("EJERCICIO 1")


notas_estudiantes = [6,7,4,8,3,8,1,10,9,7]
for notas in notas_estudiantes:
    print(notas)

suma = 0  #calculo la suma y cuento elementos usando un acumulador
contador = 0
for notas in notas_estudiantes:
    suma = suma + notas
    contador = contador + 1

promedio = suma / contador
print("El promedio de la clase es:", promedio)

nota_mayor = notas_estudiantes[0]   #para buscar tomo el primer elemento
nota_menor = notas_estudiantes[0]

for nota in notas_estudiantes:
    if nota > nota_mayor:
        nota_mayor = nota   #si encuentra nota mas grande, la guarda
    if nota < nota_menor:
        nota_menor = nota    #si encuentra nota más chica , la guarda

print("La nota más alta es:", nota_mayor)
print("La nota más baja es:", nota_menor)


#EJERCICIO 2 - Pedir al usuario 5 productos
print("-" * 40)
print("EJERCICIO 2")

productos = []   #Lista vacia aún
for i in range(5):
    produc = input(f"Ingrese un producto para la lista de compras {i+1}: ")    #muestra el numero de producto de 1 al 5 y los guarda
    productos.append(produc)   #para añadir cada producto al final de la lista

lista_productos = sorted(productos)   #los ordena alfabeticamente
print("Lista ordenada de productos:")
for pro in lista_productos:
    print(pro)



#EJERCICIO 3 - Numeros al azar - Pares - Impares - Repetidos
print("-" * 40)
print("EJERCICIO 3")

import random    #modulo de numeros aleatorios

numeros = []
for i in range(15):  #repetir 15 veces
    n = random.randint(1, 100)   #numeros aleatorios entrel 1 y el 100
    numeros.append(n)

for num in numeros:
    print(num)

par = []
impar = []
for n in numeros:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
        

print("Números pares:", par)
print("Números impares:", impar)



#EJERCICIO 4 - LISTA VALORES REPETIDOS
print("-" * 40)
print("EJERCICIO 4")

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
sin_duplicados = []

for elemento in datos:
    if elemento not in sin_duplicados:
        sin_duplicados.append(elemento)

print ("Lista datos duplicados:")
for elementos in datos:
    print(elementos, end=" ")
print()
        
print("Lista sin duplicados:")
for elementos in sin_duplicados:
    print(elementos, end=" ")
print()


#EJERCICIO 5 - NOMBRES DE ESTUDIANTES - AGREGAR O ELIMINAR
print("-" * 40)
print("EJERCICIO 5")

estudiantes = ["Juan", "Mateo", "Gimena", "Sofía", "Marta", "Esteban", "Lorena", "Pedro"]

print("Menú de opciones")
print("1 - Añadir estudiante")
print("2 - Eliminar estudiante")

opcion = int(input("Elija una opción (1 o 2): "))


if opcion == 1:
    añadir = input("Nombre del estudiante al que desea agregar:")
    estudiantes.append(añadir)
elif opcion == 2:
    eliminar = input("Nombre del estudiante al que deseas eliminar de la lista:")
    estudiantes.remove(eliminar)

print("Lista final:")
for a in estudiantes:
    print(a)

#EJERCICIO 6 - NOMBRES DE ESTUDIANTES - AGREGAR O ELIMINAR
print("-" * 40)
print("EJERCICIO 6")
print()

lista = [4,5,1,8,7,9,3]
print("Lista original:", lista)
print()

num_ult = lista[6]     #Guardo el ultimo numero de la lista (posicion)

for i in range(6, 0, -1): 
    lista[i] = lista[i - 1]      #desplazo elemnos a la derecha y cuento del 6 al 1

lista[0] = num_ult      #el ultimo en la primera posicion

print("Lista final:", lista)


#EJERCICIO 7 - ANIDADAS de 7x2 con las temperaturas mínimas y máximas de una semana.
print("-" * 40)
print("EJERCICIO 7") 


temperaturas = [                        #Lista anidada con mínimas y máximas (7 filas x 2 columnas)
    [12, 22],   # Día 1
    [10, 25],   # Día 2
    [15, 27],   # Día 3
    [13, 21],   # Día 4
    [11, 26],   # Día 5
    [14, 24],   # Día 6
    [13, 23]    # Día 7
]

suma_min = 0     #Variable para acumular las temperaturas
suma_max = 0


mayor_amplitud = 0       #variable para mayor amplitud
dia_mayor = 0    # guarda el número de día (1 a 7)


for i in range(7):    #recorre los 7 días
    minima = temperaturas[i][0]
    maxima = temperaturas[i][1]


    suma_min = suma_min + minima
    suma_max = suma_max + maxima


    amplitud = maxima - minima
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor = i + 1       # +1 para que sea día 1 a 7


promedio_min = suma_min / 7     #Calculo promedios
promedio_max = suma_max / 7


print("Promedio de temperaturas mínimas:", promedio_min)
print("Promedio de temperaturas máximas:", promedio_max)
print("Día con mayor amplitud térmica:", dia_mayor, "con una diferencia de", mayor_amplitud, "grados")



#EJERCICIO 8 - Matriz con las notas de 5 estudiantes en 3 materias 
print("-" * 40) 
print("EJERCICIO 8")

estudiantes = [
    ["Ana",   7, 4, 9],
    ["Pedro", 4, 8, 6],
    ["Lucía", 9,10, 2],
    ["Martín",5, 7, 8],
    ["Juan",  4, 3, 6]
]

print("Las notas de los estudiantes son:")

for i in estudiantes:      #para recorrer filas
    for nota in i:
        print(nota, end=" ")    #para que termine con un espacio
    print()

print("El promedio de cada estudiante es:")      #promedio por estudiante
for i in range(5):
    fila = estudiantes[i]
    suma = fila[1] + fila[2] + fila[3]
    promedio = suma / 3
    print(fila[0], "=", promedio)

print("El promedio por cada materia es:")
for e in range(1, 4):          #recorre las 3 materias 
    suma = 0
    for i in range(5):         #recorre los 5 estudiantes 
        suma += estudiantes[i][e]
    promedio = suma / 5        
    print("Materia", e, "=", promedio)


#EJERCICIO 9 - Tableto TA TE TI
print("-" * 40) 
print("EJERCICIO 9")

tablero = []

for i in range(3):
    fila = []
    for o in range(3):
        fila.append("-")
    tablero.append(fila)

for fila in tablero: 
    for celda in fila:
        print(celda, end = " ")

jugador = "X"      # arranca el jugador X
jugadas = 0        # contador de jugadas

while jugadas < 9:                    # mientras no se hagan 9 jugadas
    print("\nTurno del jugador", jugador)


    for fila in tablero:
        print(fila[0], fila[1], fila[2])

    f = int(input("Elegí FILA (0,1,2): "))      #pide fila y columna
    c = int(input("Elegí COLUMNA (0,1,2): "))

    if tablero[f][c] == "-":                 #verifica que la casilla este vacía
        tablero[f][c] = jugador   
        jugadas += 1             

        if jugador == "X":
            jugador = "O"
        else:
            jugador = "X"
    else:
        print("Esa casilla ya está ocupada. Probá otra.")


print("\nJuego terminado - tablero final:")       # Cuando se hacen las 9 jugadas
for fila in tablero:
    print(fila[0], fila[1], fila[2])

#EJERCICIO 10 - Ventas de 4 productos durante 7 días, en una matriz de 4x7
print("-" * 40)
print("EJERCICIO 10")

productos = 4
dias = 7

ventas = []
for a in range(productos):
    fila = []
    for d in range(dias):
        fila.append(0)
    ventas.append(fila)


#EJERCICIO 10 - Ventas de 4 productos durante 7 días, en una matriz de 4x7
print("-" * 40)
print("EJERCICIO 10")

ventas = [
    [4, 5, 3, 7, 8, 9, 1],   # Producto 1
    [6, 2, 5, 4, 7, 3, 8],   # Producto 2
    [1, 3, 4, 5, 2, 6, 7],   # Producto 3
    [9, 8, 7, 6, 5, 4, 3]    # Producto 4
]

total_productos = []       #total de productos

for p in range(4):       #recorre los 4 productos (filas)
    suma = 0
    for d in range(7):   #recorre los 7 días (columnas)
        suma += ventas[p][d]
    total_productos.append(suma)    #guardo el total de este producto
print("\nTotal vendido por cada producto:")
for p in range(4):
    print("Producto", p + 1, "=", total_productos[p])


mayor_ventas = 0       #mayor ventas
dia_mayor = 1      

for d in range(7):         #cada dia
    suma_dia = 0
    for p in range(4):           #sumo los 4 productos
        suma_dia += ventas[p][d]
    if suma_dia >= mayor_ventas:
        mayor_ventas = suma_dia
        dia_mayor = d + 1

print("\nDía con mayores ventas totales:",
    dia_mayor, "(total =", mayor_ventas, ")")


mayor_prod_total = 0        #producto mas vendido
producto_mayor = -1

for p in range(4):
    suma_prod = 0
    for d in range(7):
        suma_prod = suma_prod + ventas[p][d]
    if suma_prod > mayor_prod_total:
        mayor_prod_total = suma_prod
        producto_mayor = p + 1
print("\nProducto más vendido en la semana:",
    producto_mayor, "(total =", mayor_prod_total, ")")
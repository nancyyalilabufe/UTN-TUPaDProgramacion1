# EJERCICIO 1-  Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
print("-" * 40)
print("EJERCICIO 1") #Para que quede más ordenado y diferenciado

for i in range(0,101):
    print (i)


# EJERCICIO 2 - Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.
print("-" * 40)
print("EJERCICIO 2")  

num = int(input("Ingresa por favor un número:"))

contador = 0      # Para llevar la cuenta los dígitos
if num == 0:
    contador = 1

num = abs(num) # Convierto a positivo para evitar numeros negativos y que el código funcione
while num > 0:
    num = num // 10  # División para numeros enteros, elimina el último dígito
    contador += 1    # contador suma 1
print ("\nEl número tiene", contador, "dígitos")



# EJERCICIO 3 - Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
print("-" * 40)
print("EJERCICIO 3")

n1 = int(input("Ingrese por favor número entero:"))
n2 = int(input("Ingrese por favor otro número entero:"))

if n1 > n2:         #Para asegurar que n1 sea menor que n2 
    n1, n2 = n2, n1

suma = 0 

for i in range(n1+ 1, n2):     # Va del n1 al n2 excluyéndolos
    suma += i

print("\nLa suma de los números entre", n1, "y", n2, "es:", suma)


# EJERCICIO 4 - Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0
print("-" * 40)
print("EJERCICIO 4")

contador = 0
num = int(input("Ingresa un número (0 para terminar): "))      # pido una vez fuera del bucle para iniciar while

while num != 0:      # si no es 0, ingreso al bucle
    contador += num      #sumo el número al contador
    num = int(input("Ingresa un número (0 para terminar):"))      # pido de nuevo otro numero, sino sería infinito


print("\nLa suma de los números ingresados es:", contador)


# EJERCICIO 5 - Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random 

print("-" * 40)
print("EJERCICIO 5")
print("Bienvenido al juego del número secreto")
correcto = random.randint(0, 9)       #Num aleatorio entre 0 y 9
intento = -1     

while intento != correcto:
    intento = int(input("Adivina un número(entre 0 y 9):"))
    if intento < correcto:
        print("Muy bajo... intenta de nuevo por favor")
    elif intento > correcto:
        print("Muy Alto... intenta de nuevo por favor")
print("\nAdivinaste!! El número secreto era", correcto)

#EJERCICIO 6 - Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.
print("-" * 40)
print("EJERCICIO 6")

for i in range(100,0,-2):        #Para que imprima numeros pares, pongo que vaya decreciendo de a 2
    print(i)

#EJERCICIO 7 - Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
print("-" * 40)
print("EJERCICIO 7")

numero = int(input("Ingrese un número positivo por favor:"))
suma = 0

for i in range(1, numero + 1):      #Para que tome al numero ingresado por el usuario le sumo 1
    suma += i

print("\nLa suma de los números comprendidos entre 0 y", numero, "es:", suma)


#EJERCICIO 8: Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar:
#- cuántos de estos números son pares,
#- cuántos son impares,
#- cuántos son negativos,
#- y cuántos son positivos.
print("-" * 40)
print("EJERCICIO 8")


par = 0
impar = 0
positivo = 0
negativo = 0

for i in range(1, 101):           #Para probar, yo puse un numero más bajo, pero pongo el num que se pide en la consigna 
    numero = int(input(f"Ingrese el número {i}:"))
    if numero % 2 == 0:   #Par
        par += 1
    else:
        impar += 1     #Sino, impar
    if numero > 0:
        positivo += 1    #Positivo, negativo o cero
    elif numero < 0:
        negativo += 1      

print("\nResultado final:")
print("La cantidad de pares son:", par)
print("La cantidad de impares son:", impar)
print("La cantidad de positivos son:", positivo)
print("La cantidad de negativos son:", negativo)

# EJERCICIO 9 - Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. 
print("-" * 40)
print("EJERCICIO 9")

suma = 0
cantidad = 100            #Para probar, yo puse un numero más bajo, pero pongo el num que se pide en la consigna

for i in range(1, cantidad + 1):
    numero = int(input(f"Ingrese el número {i}: "))
    suma += numero       #Acumulo números para luego calcular la media

media = suma / cantidad    

print("\nLa media de los números ingresados es:", media)

#EJERCICIO 10 - Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
print("-" * 40)
print("EJERCICIO 10")

num = int(input("Ingrese un número de 2 o más dígitos:"))

invertido = 0

while num > 0:
    digito = num % 10   #Para obtener el ultimo digito
    invertido = invertido * 10 + digito    #Lo agrego al num invertido
    num = num // 10   #elimino el ultimo dígito del número dado por el usuario

print("\nEl número invertido es:", invertido)
print("-" * 40)
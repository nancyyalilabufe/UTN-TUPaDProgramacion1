#Ejercicio 1: Imprimir "Hola Mundo"
print("¡Hola Mundo!")

#Ejercicio 2: Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo.
nombre = input("Ingresa tu nombre: ")
print("Hola", nombre)

#Ejercicio 3: Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia.

nombre = input("Ingresa tu nombre, por favor:")
apellido = input("Ingresa tu apellido, por favor:")
edad = input("Ingresa tu edad:")
residencia = input("Ingresa tu lugar de residencia:")

print(f"Soy, {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Ejercicio 4: Crear un programa que pida al usuario el readio de un circulo e imprima su area y perimetro.

pi = 3.1416
radio = float(input("Ingresa el radio del círculo:"))

area = pi*radio**2
perimetro = 2*pi*radio

print(f"El área del círculo es {area}")
print(f"El perímetro del círculo es: {perimetro}")


#Ejercicio 5: Crear un programa que pida al usuario una cantidad de segundos y diga a cuantas hs equivale.

segundos = int(input("Ingresa cantidad de segundos:"))
horas = segundos/3600

print(f"{segundos} segundos equivalen a {horas} horas")

#Ejercicio 6: ) Crear un programa que pida al usuario un número y muestre su tabla de multiplicar.

numero_multiplicar = int(input("Ingrese un número para ver su tabla de multplicar, por favor:"))

numero_por_0 = numero_multiplicar * 0
numero_por_1 = numero_multiplicar * 1
numero_por_2 = numero_multiplicar * 2
numero_por_3 = numero_multiplicar * 3
numero_por_4 = numero_multiplicar * 4
numero_por_5 = numero_multiplicar * 5
numero_por_6 = numero_multiplicar * 6
numero_por_7 = numero_multiplicar * 7
numero_por_8 = numero_multiplicar * 8
numero_por_9 = numero_multiplicar * 9

print(f"""
{numero_multiplicar} x 0 = {numero_por_0}
{numero_multiplicar} x 1 = {numero_por_1}
{numero_multiplicar} x 2 = {numero_por_2}
{numero_multiplicar} x 3 = {numero_por_3}
{numero_multiplicar} x 4 = {numero_por_4}
{numero_multiplicar} x 5 = {numero_por_5}
{numero_multiplicar} x 6 = {numero_por_6}
{numero_multiplicar} x 7 = {numero_por_7}
{numero_multiplicar} x 8 = {numero_por_8}
{numero_multiplicar} x 9 = {numero_por_9}
""")

#Ejercicio 7: Crear un programa que pida al usuario dos números enteros distintos del 0.
# Muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero1 = int(input("Ingrese por favor un número entero, distinto al 0: "))
numero2 = int(input("INgrese el segundo número entero, distinto al 0:"))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = round(numero1 / numero2, 2)

print(f"""
Resultado de la suma: {suma}
Resultado de la resta: {resta}
Resultado de la multiplicación: {multiplicacion}
Resultado de la división: {division}
""")

# Ejercicio 8: Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal

peso = float(input("Por favor, ingrese su peso en kilogramos: "))
altura = float(input("Por favor, ingrese su altura en metros: "))

imc = peso / (altura*2)

print(f"Tu índice de masa corporal es: {imc:.2f}")

# Ejercicio 9: Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.

celsius = float(input("Ingresa la temperatura en grados Celsius:"))

fahrenheit = round((9/5)*celsius+32, 2)

print(f"{celsius} C equivalen a {fahrenheit} F°")

# Ejercicio 10: Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

num1= float(input("Por favor, ingrese el primer número: "))
num2 = float(input("Por favor, ingrese el segundo número: "))
num3 = float(input("Por favor, ingrese el tercer número: "))

sumaabc= num1 + num2 + num3

promediofinal = round(sumaabc/3, 2)

print(f"El promedio de los números ingresados es {promediofinal}.")
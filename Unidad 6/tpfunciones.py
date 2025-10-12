# =====================================
# EJERCICIO 1 - HOLA MUNDO
# =====================================
print("-" * 40)
print("EJERCICIO 1")

def imprimir_hola_mundo():
    print("Hola Mundo!")  

imprimir_hola_mundo()

# =====================================
# EJERCICIO 2 - SALUDAR USUARIO
# =====================================
print("-" * 40)
print("EJERCICIO 2")

def saludar_usuario(nombre):
    return f"Hola {nombre}!"              #se puede reutilizar

#PROGRAMA PRINCIPAL
nombre = input("Coloque su nombre, por favor: ")
print(saludar_usuario(nombre))


# =====================================
# EJERCICIO 3 - INFORMACION PERSONAL
# =====================================
print("-" * 40)
print("EJERCICIO 3")

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# PROGRAMA PRINCIPAL
nombre = input("Ingrese su nombre, por favor: ").title()
apellido = input("Ingrese su apellido, por favor: ").title()
while True:
    try:
        edad = int(input("Ingrese su edad: "))
        break
    except ValueError:
        print("Ingrese un número válido para la edad.")
residencia = input("Ingrese su lugar de residencia, por favor: ").title()

informacion_personal(nombre, apellido, edad, residencia)

# =====================================
# EJERCICIO 4 - AREA Y PERIMETRO
# =====================================
print("-" * 40)
print("EJERCICIO 4")

import math

def calcular_area_circulo(radio):
    area = math.pi * (radio ** 2)    # CALCULO AREA
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio  # CALCULO PERIMETRO
    return perimetro

# Pedido del radio con validación (una sola vez)
while True:
    try:
        radio = float(input("Ingrese por favor el radio del círculo: "))
        if radio < 0:
            print("Ingrese un valor no negativo para el radio.")
            continue
        break
    except ValueError:
        print("Ingrese un número válido para el radio.")

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"\nPara un círculo de radio {radio}:")
print(f"- El Área del círculo es: {area:.2f}")
print(f"- El Perímetro del círculo es: {perimetro:.2f}")


# =====================================
# EJERCICIO 5 - SEGUNDOS Y HORAS
# =====================================
print("-" * 40)
print("EJERCICIO 5")

def segundos_a_horas(segundos):
    horas = segundos / 3600       # ya que en una hora hay 3600 seg
    return horas

while True:
    try:
        segundos = float(input("Ingrese la cantidad de segundos: "))
        break
    except ValueError:
        print("Ingrese un número válido para los segundos.")

resultado = segundos_a_horas(segundos)
print(f"{segundos} equivalen a {resultado:.2f} horas.")

# =====================================
# EJERCICIO 6 - TABLA DE MULTIPLICAR
# =====================================
print("-" * 40)
print("EJERCICIO 6")

def tabla_multiplicar(numero):
    resultado = ""
    for i in range(1, 11):
        resultado += f"{numero} x {i} = {numero * i}\n"
    return resultado

while True:
    try:
        numero = int(input("Ingrese un número: "))
        break
    except ValueError:
        print("Ingrese un número entero válido.")

print(tabla_multiplicar(numero))

# =====================================
# EJERCICIO 7 - OPERACIONES BASICAS
# =====================================
print("-" * 40)
print("EJERCICIO 7")

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b           #evito dividir por 0
    else:
        division = "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)       #tupla

while True:
    try:
        numero1 = float(input("Ingrese un número por favor: "))
        numero2 = float(input("Ingrese otro número por favor: "))
        break
    except ValueError:
        print("Ingrese valores numéricos válidos.")

resultado = operaciones_basicas(numero1, numero2)

print(f"La suma entre {numero1} y {numero2} es = {resultado[0]}")
print(f"La resta entre {numero1} y {numero2} es = {resultado[1]}")
print(f"La multiplicacion entre {numero1} y {numero2} es = {resultado[2]}")
if isinstance(resultado[3], (int, float)):
    print(f"La division entre {numero1} y {numero2} es = {resultado[3]:.2f}")
else:
    print(f"La division entre {numero1} y {numero2} es = {resultado[3]}")


# =====================================
# EJERCICIO 8 - CALCULAR IMC
# =====================================
print("-" * 40)
print("EJERCICIO 8")

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)           # CALCULO IMC CON PESO Y ALTURA
    return imc

while True:
    try:
        peso = float(input("Ingrese su peso en kg, por favor: "))
        altura = float(input("Ingrese su altura en metros, por favor: "))
        break
    except ValueError:
        print("Ingrese valores numéricos válidos.")

if altura > 3:
    print("Detecté altura en centímetros. Convirtiendo a metros...")
    altura = altura / 100

if altura <= 0:
    print("La altura debe ser mayor a 0.")
else:
    resultado = calcular_imc(peso, altura)
    print(f"Tu índice de masa corporal (IMC) es: {resultado:.2f}")

    # INTERPRETO RESULTADO
    if resultado < 18.5:
        print("Estado: Bajo peso")
    elif resultado < 25:
        print("Estado: Peso normal")
    elif resultado < 30:
        print("Estado: Sobrepeso")
    else:
        print("Estado: Obesidad")

# =====================================
# EJERCICIO 9 - CELSIUS A FAHRENHEIT
# =====================================
print("-" * 40)
print("EJERCICIO 9")

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

while True:
    try:
        celsius = float(input("Ingrese la temperatura en grados Celsius: "))
        break
    except ValueError:
        print("Ingrese un número válido para la temperatura.")

resultado = celsius_a_fahrenheit(celsius)
print(f"{celsius:.1f}°C equivalen a {resultado:.1f}°F")

# =====================================
# EJERCICIO 10 - CALCULAR PROMEDIO
# =====================================
print("-" * 40)
print("EJERCICIO 10")

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

while True:
    try:
        numero1 = float(input("Ingrese un número: "))
        numero2 = float(input("Ingrese otro número: "))
        numero3 = float(input("Ingrese otro número: "))
        break
    except ValueError:
        print("Ingrese valores numéricos válidos.")

promedio = calcular_promedio(numero1, numero2, numero3)
print(f"El promedio entre {numero1}, {numero2} y {numero3} es: {promedio:.2f}")

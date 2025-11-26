#TRABAJO PRACTICO 9

# =====================================
#Ejercicio 1- Factorial de un número
# =====================================
print("-" * 40)
print("EJERCICIO 1")
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingrese un número entero positivo: "))
for i in range(1, numero + 1):
    print("Factorial de", i, "=", factorial(i))

# =====================================
#Ejercicio 2- Fibonacci
# =====================================
print("-" * 40)
print("EJERCICIO 2")
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

posicion = int(input("Ingrese la posición máxima de la serie de Fibonacci: "))
for i in range(posicion + 1):
    print("Fibonacci de", i, "=", fibonacci(i))

# =====================================
#Ejercicio 3- Potencia de un número
# =====================================
print("-" * 40)
print("EJERCICIO 3")

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = float(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente (entero >= 0): "))
print("Resultado:", potencia(base, exponente))

# =====================================
#Ejercicio 4- Decimal a binario
# =====================================
print("-" * 40)
print("EJERCICIO 4")
def decimal_a_binario(n):
    if n < 2:
        return str(n)
    return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("Ingrese un número entero positivo: "))
print("En binario es:", decimal_a_binario(numero))

# =====================================
#Ejercicio 5 -Palíndromo
# =====================================
print("-" * 40)
print("EJERCICIO 5")
def es_palindromo(palabra):
    palabra = palabra.lower()
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra: ")
if es_palindromo(texto):
    print("Es palíndromo")
else:
    print("No es palíndromo")

# =====================================
#Ejercicio 6 -Suma de dígitos
# =====================================
print("-" * 40)
print("EJERCICIO 6")
def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

numero = int(input("Ingrese un número entero positivo: "))
print("La suma de sus dígitos es:", suma_digitos(numero))

# =====================================
#Ejercicio 7 - Pirámide de bloques
# =====================================
print("-" * 40)
print("EJERCICIO 7")
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

niveles = int(input("Ingrese la cantidad de bloques del último nivel: "))
print("Total de bloques necesarios:", contar_bloques(niveles))

# =====================================
#Ejercicio 8: Contar ocurrencias de un dígito
# =====================================
print("-" * 40)
print("EJERCICIO 8")
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    ultimo = numero % 10
    resto = numero // 10
    if ultimo == digito:
        return 1 + contar_digito(resto, digito)
    return contar_digito(resto, digito)

num = int(input("Ingrese un número entero positivo: "))
d = int(input("Ingrese el dígito a buscar (0-9): "))
print("Aparece", contar_digito(num, d), "vez/veces")

# Número par o impar.

num = int(input("Ingrese por favor un número:"))

if (num % 2 == 0): 
    print("Ha ingresado un número par!")
else:
    print("Por favor, ingrese un número par")
    num = int(input("Ingrese nuevamente un número par: "))
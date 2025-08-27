#Palabra o frase termina en vocal o no.

frase_palabra = input("Ingrese por favor una palabra o frase:")

ultima_letra = frase_palabra[-1]

if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u":
    print(f"{frase_palabra}!")
else:
    print(f"{frase_palabra}")


# Otra forma de resolución, por lo que estuve leyendo es:

frase_palabra = input("Ingrese por favor una palabra o frase:")

ultima_letra = frase_palabra[-1]

if ultima_letra.lower() in "aeiou":         # usando el operador in(para lo que está en un grupo) y lower para que funcione si hay una mayuscula.
    print(f"{frase_palabra}!")
else:
    print(f"{frase_palabra}")
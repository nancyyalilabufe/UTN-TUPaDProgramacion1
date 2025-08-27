# Paquete statistics y random

import random
from statistics import mean, median, mode

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]  #lista de 50 numeros aleatorios

media = mean(numeros_aleatorios)   #promedio de la lista
mediana = median(numeros_aleatorios)       #valor del medio de la lista
moda = mode(numeros_aleatorios)         #valor que mas se repite

if media > mediana and mediana > moda:
    sesgo = "Positivo hacia la derecha"
elif media > mediana and mediana > moda:
    sesgo = "Negativo hacia la izquierda"
else:
    sesgo = "Sin sesgo"

print("Lista de los números:", numeros_aleatorios)
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)
print("Sesgo de la lista:", sesgo)

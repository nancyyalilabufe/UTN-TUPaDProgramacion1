# Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. (Yo agregué lo de menor de edad y 18 años porque me puse a practicar antes. )

edad = int(input("Ingrese su edad por favor:"))
if edad > 18:
    print("Ud. es mayor de edad")
elif edad < 18:
    print("Ud. es menor de edad")
else:
    print("Ud. tiene 18 años justos.")

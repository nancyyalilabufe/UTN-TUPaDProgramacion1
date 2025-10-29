#Abro el archivo en modo lectura 
productos = open("productos.txt", "r")

productos_lista = []

#Recorro cada línea dentro del archivo
for linea in productos:
    if linea.strip() == "":
        continue
#Quito los espacios y saltos de línea al final y separo los valores (nombre, precio, cantidad) usando la coma
    partes = linea.strip().split(",")
    nombre = partes[0]
    precio = partes[1]
    cantidad = partes[2]

    print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")


    #Creo un diccionario por cada producto y lo agrego a la lista
    producto = {"Producto": nombre, "Precio": precio, "Cantidad": cantidad}
    productos_lista.append(producto)

productos.close()

print("-" * 60)  
#para agregar un nuevo producto
producto_nuevo = input("Ingrese un nuevo producto (nombre, precio y cantidad): ")
productos = open("productos.txt", "a")
productos.write("\n" + producto_nuevo)
productos.close()

print("Producto agregado correctamente")


print("-" * 60) 
#lo agrego al dic también
nombre_n, precio_n, cantidad_n = producto_nuevo.split(",")
producto_dic = {"Producto": nombre_n, "Precio": precio_n, "Cantidad": cantidad_n}
productos_lista.append(producto_dic)

print("Producto agregado correctamente")

# Muestra lista actualizada
print("\nLista actualizada de productos:\n")
productos = open("productos.txt", "r")
for linea in productos:
    if linea.strip() == "":
        continue
    partes = linea.strip().split(",")
    nombre = partes[0]
    precio = partes[1]
    cantidad = partes[2]
    print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
productos.close()

# Muestra diccionario
print("\nDiccionarios cargados en memoria:")
for producto in productos_lista:
    print(producto)

print("-" * 60) 
# buscar producto por nombre
buscar = input("Ingrese el nombre del producto que desea buscar: ").strip()
encontrado = False

for producto in productos_lista:
    if producto["Producto"].lower() == buscar.lower():
        print(f"Producto: {producto['Producto']} | Precio: ${producto['Precio']} | Cantidad: {producto['Cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("El producto no existe.")

print("-" * 60) 
# Guardar productos actualizadoss (sobreescribir)
productos = open("productos.txt", "w")
for producto in productos_lista:
    linea = f"{producto['Producto']},{producto['Precio']},{producto['Cantidad']}\n"
    productos.write(linea)
productos.close()




#¿Se puede agregar más de un producto? Si, lo probé varias veces y se puede agregar mas de un producto, pero al principio se me dificultó, solo agregaba uno y despues me daba error.

#¿Se guarda todo correctamente? Si, tambien es lo que me costó, porque luego de guardar uno, daba error.. 

#¿Se muestra bien el resultado? Si, se muestra bien.
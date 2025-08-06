listaCompras = []
while True:
    producto = input("Ingrese el producto a agregar a la lista (o '0' para terminar): ")
    if producto == '0':
        break
    listaCompras.append(producto)
print("Lista de compras: ", listaCompras)
while True:
    ProductoEliminar= input("Deseas eliminar un producto de la lista? (si/no): ")
    if ProductoEliminar == "si":
        eliminar= input("Ingrese el producto a eliminar: ")
        if eliminar in listaCompras:
            listaCompras.remove(eliminar)
            print(f"Producto '{eliminar}' eliminado de la lista.")
        else:
            print(f"Producto '{eliminar}' no encontrado en la lista.")
    elif ProductoEliminar == "no":
        print("La lista de compras actual es: ", listaCompras)
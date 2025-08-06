producto=float(input("Ingrese el precio del producto: "))
descuento=float(input("Ingrese el porcentaje de descuento: "))
precioFinal= producto - (producto * descuento / 100)
print("El precio final del producto es: ", precioFinal)
lista_numeros = [10, 8, 4, 6, 12]

suma_total = 0
cantidad_elementos = 0

for numero in lista_numeros:
    suma_total = suma_total + numero
    cantidad_elementos = cantidad_elementos + 1

if cantidad_elementos > 0:
    promedio = suma_total / cantidad_elementos
    print("Promedio:", promedio)
else:
    print("La lista está vacía, no hay promedio.")
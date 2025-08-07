lista1 = input("Ingrese los elementos de la primera lista, separados por comas: ").split(",")
lista2 = input("Ingrese los elementos de la segunda lista, separados por comas: ").split(",")
comunes = []

for elemento in lista1:
    if elemento.strip() in [x.strip() for x in lista2]:
        if elemento.strip() not in comunes:
            comunes.append(elemento.strip())

print("Comunes:", comunes if comunes else "Ninguno")
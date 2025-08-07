lista = [3, 8, 15, 23, 42]
objetivo = int(input("Número a buscar: "))

encontrado = False
i = 0
while i < len(lista):
    if lista[i] == objetivo:
        encontrado = True
        break
    i = i + 1

if encontrado:
    print(objetivo, "está en", lista)
else:
    print(objetivo, "no está en", lista)

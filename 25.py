numeros = [12, 3213, 431123, 1234, 43213, 13234, 423]
aux = []

while len(numeros) > 0:
    menor = numeros[0]
    pos_menor = 0

    i = 1
    while i < len(numeros):
        if numeros[i] < menor:
            menor = numeros[i]
            pos_menor = i
        i += 1

    aux.append(menor)
    del numeros[pos_menor]

print(aux)

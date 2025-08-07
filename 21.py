entrada = input("Ingresa un entero: ")
numero = int(entrada)

if numero <= 1:
    es_primo = False
else:
    es_primo = True
    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            es_primo = False
            break
        divisor = divisor + 1

if es_primo:
    print(numero, "es primo")
else:
    print(numero, "no es primo")
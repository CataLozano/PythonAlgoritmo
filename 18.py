num=int(input("Ingrese un número para ver su tabla de multiplicar: "))
for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")

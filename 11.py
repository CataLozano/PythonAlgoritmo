temperatura=float(input("Introduce la temperatura de la habitacion: "))

if temperatura < 20:
    print("La temperatura de la habitacion es fria")
elif 20 <= temperatura <= 25:
    print("La temperatura de la habitacion es aceptable")
else:
    print("La temperatura de la habitacion es caliente")    

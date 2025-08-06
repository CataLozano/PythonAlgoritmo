asientosDisponibles = 100  # Número total de asientos disponibles
asientosReservados = 0  # Contador de asientos reservados
while True:
    print(f"Asientos Disponibles: {asientosDisponibles - asientosReservados}")
    reserva = input("¿Desea reservar un asiento? (si/no): ")

    if reserva == "si":
        cantidad = int(input("¿Cuántos asientos desea reservar?: "))
        if cantidad <= (asientosDisponibles - asientosReservados):
            asientosReservados += cantidad
            print(f"Has reservado {cantidad} asiento(s).")
        else:
            print("No hay suficientes asientos disponibles.")
        
    elif reserva == "no":
        print("Gracias por su visita.")
        break


        
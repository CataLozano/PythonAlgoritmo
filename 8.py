#pago mensual de un prestamo dado un monto, tasa de interes anual y numero de meses
monto= float(input("Ingrese el monto del préstamo: "))
tasa_interes = float(input("Ingrese la tasa de interés anual (en %): "))
numero_meses = int(input("Ingrese el número de meses para el préstamo: "))
# Calcular la tasa de interés mensual
tasa_interes_mensual = tasa_interes / 100 / 12 
pago_mensual = monto * (tasa_interes_mensual * (1 + tasa_interes_mensual) ** numero_meses) / ((1 + tasa_interes_mensual) ** numero_meses - 1)
print(f"El pago mensual del préstamo es: {pago_mensual:.2f}")
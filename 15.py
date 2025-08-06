presupuestoMensual = float(input("Ingrese su presupuesto mensual: "))
while True:
    gasto = float(input("Ingrese el gasto mensual (o -1 para salir): "))
    if gasto == -1:
        break
    presupuestoMensual -= gasto
    print(f"Presupuesto restante: {presupuestoMensual:.2f}")
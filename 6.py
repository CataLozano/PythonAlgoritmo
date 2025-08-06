Combustible= float(input("Ingrese el costo del combustible : "))
peajes=int(input("Cuantos peajes hay en todo el viaje: "))
valorPeaje=float(input("Ingrese el valor de cada peaje: "))
totalPeajes= peajes * valorPeaje
alojamiento=float(input("Ingrese el costo del alojamiento: "))

TotalViaje= Combustible + totalPeajes + alojamiento
print("El costo total del viaje es: ", TotalViaje)
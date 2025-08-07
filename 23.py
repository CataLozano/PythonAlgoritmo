mensaje_solicitud = "Temperatura en Celsius (q para salir): "
multiplicador = 9
divisor = 5
desplazamiento = 32

while True:
    entrada_usuario = input(mensaje_solicitud)
    if entrada_usuario == "exit":
        break
    temperatura_celsius = float(entrada_usuario)
    temperatura_fahrenheit = (temperatura_celsius * multiplicador) / divisor + desplazamiento
    print(temperatura_celsius, "°C =", temperatura_fahrenheit, "°F")
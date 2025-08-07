nombres = ["Ana","Luis","Marta","Jero","Sofi"]
fechas  = ["2001-03-15","1998-12-02","08/03/2001","21/01/2004","2020-12-25"]
meses   = ["Enero","Febrero","Marzo","Abril","Mayo","Junio",
           "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

nombres_ordenados = ["" for _ in range(len(nombres))]
k = 0

mes = 1
while mes <= 12:
    i = 0
    hubo = False
    while i < len(fechas):
        f = fechas[i]
        mm = 0
        if len(f) >= 7 and f[4] == '-':
            mm = int(f[5:7])
        elif len(f) >= 5 and f[2] == '/':
            mm = int(f[3:5])

        if mm == mes:
            if not hubo:
                print(meses[mes-1] + ":")
                hubo = True
            print("- " + nombres[i] + " (" + f + ")")
            nombres_ordenados[k] = nombres[i]
            k = k + 1
        i = i + 1
    if hubo:
        print()
    mes = mes + 1


salida = "["
j = 0
while j < k:
    if j > 0:
        salida = salida + ", "
    salida = salida + "'" + nombres_ordenados[j] + "'"
    j = j + 1
salida = salida + "]"
print("Nombres en orden (enero→diciembre):", salida)

import random
import time
listaCanciones=[]
agregar = input("Ingrese el nombre de la canción a agregar a la lista (o '0' para terminar): ") 
while agregar != '0':
    listaCanciones.append(agregar)
    agregar = input("Ingrese el nombre de la canción a agregar a la lista (o '0' para terminar): ")
def reproducirCancion(listaCanciones):
    while True:
        if listaCanciones:
            cancion = random.choice(listaCanciones)
            print(f"Reproduciendo la canción: {cancion}")
            time.sleep(2)
            
reproducirCancion(listaCanciones)        
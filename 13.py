import time

def semaforo():
    while True:
        print("🔴 Rojo - Detenerse")
        time.sleep(5)  # 5 segundos en rojo

        print("🟢 Verde - Avanzar")
        time.sleep(4)  # 4 segundos en verde

        print("🟡 Amarillo - Precaución")
        time.sleep(2)  # 2 segundos en amarillo
semaforo()        
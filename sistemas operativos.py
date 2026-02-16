import threading
import time

# Función para simular una tarea concurrente
def tarea_hilo(nombre):
    print(f"Hilo {nombre} en ejecución...")
    time.sleep(10) # Simula actividad
    print(f"Hilo {nombre} terminado.")

# Creación de hilos
hilo1 = threading.Thread(target=tarea_hilo, args=("A",))
hilo2 = threading.Thread(target=tarea_hilo, args=("B",))

hilo1.start()
hilo2.start()
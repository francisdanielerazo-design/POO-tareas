import threading
import time

contador = 0

lock = threading.Lock()

def incrementar():
    global contador

    for i in range(5):
        lock.acquire()  # bloquear recurso

        contador += 1
        print(f"Hilo {threading.current_thread().name} contador: {contador}")

        time.sleep(1)

        lock.release()  # liberar recurso

hilo1 = threading.Thread(target=incrementar)
hilo2 = threading.Thread(target=incrementar)

hilo1.start()
hilo2.start()
hilo1.join()
hilo2.join()
print("Valor final del contador:", contador)
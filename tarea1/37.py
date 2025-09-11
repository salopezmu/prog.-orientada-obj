import threading

# Variables compartidas
turno = 0  
contador = 0
lock = threading.Lock()  # Para proteger acceso a turno y contador

class Hilo1(threading.Thread):
    def run(self):
        global turno, contador
        for _ in range(10):
            while True:
                with lock:
                    if turno == 0:
                        contador += 1
                        print(f"Hilo1 entra a sección crítica. Contador: {contador}")
                        turno = 1  # Cede el turno a Hilo2
                        break

class Hilo2(threading.Thread):
    def run(self):
        global turno, contador
        for _ in range(10):
            while True:
                with lock:
                    if turno == 1:
                        contador += 1
                        print(f"Hilo2 entra a sección crítica. Contador: {contador}")
                        turno = 0  # Cede el turno a Hilo1
                        break

# Crear y lanzar los hilos
h1 = Hilo1()
h2 = Hilo2()
h1.start()
h2.start()
h1.join()
h2.join()

print("\nPrograma finalizado.")
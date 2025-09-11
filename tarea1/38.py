#no supe como hacer que se viera
import threading
import random
import time

DIM = 20
MUNDO = [[None for _ in range(DIM)] for _ in range(DIM)]
LOCK = threading.Lock()

def toroidal(x, y):
    return x % DIM, y % DIM

class Habitante(threading.Thread):
    def __init__(self, especie, sexo, x, y):
        super().__init__()
        self.especie = especie  # "pez" o "tiburon"
        self.sexo = sexo        # "M" o "F"
        self.x = x
        self.y = y
        self.vivo = True

    def mover(self):
        dx, dy = random.choice([(0,1), (0,-1), (1,0), (-1,0)])
        nx, ny = toroidal(self.x + dx, self.y + dy)
        return nx, ny

    def interaccion(self, otro):
        if otro is None:
            return "mover"
        if otro.especie != self.especie:
            return "comer" if self.especie == "tiburon" else "morir"
        if otro.sexo == self.sexo:
            return "aniquilar"
        else:
            return "reproducir"

    def run(self):
        while self.vivo:
            time.sleep(random.uniform(0.1, 0.3))
            with LOCK:
                nx, ny = self.mover()
                otro = MUNDO[nx][ny]
                accion = self.interaccion(otro)

                if accion == "mover":
                    MUNDO[self.x][self.y] = None
                    self.x, self.y = nx, ny
                    MUNDO[nx][ny] = self

                elif accion == "comer":
                    otro.vivo = False
                    MUNDO[nx][ny] = self
                    MUNDO[self.x][self.y] = None
                    self.x, self.y = nx, ny

                elif accion == "morir":
                    self.vivo = False
                    MUNDO[self.x][self.y] = None

                elif accion == "aniquilar":
                    otro.vivo = False
                    MUNDO[nx][ny] = self
                    MUNDO[self.x][self.y] = None
                    self.x, self.y = nx, ny

                elif accion == "reproducir":
                    sexo_hijo = random.choice(["M", "F"])
                    hijo = Habitante(self.especie, sexo_hijo, self.x, self.y)
                    hijo.start()
                    MUNDO[self.x][self.y] = hijo
                    self.x, self.y = nx, ny
                    MUNDO[nx][ny] = self

def poblar(especie, cantidad):
    habitantes = []
    for _ in range(cantidad):
        while True:
            x, y = random.randint(0, DIM-1), random.randint(0, DIM-1)
            if MUNDO[x][y] is None:
                sexo = random.choice(["M", "F"])
                h = Habitante(especie, sexo, x, y)
                MUNDO[x][y] = h
                habitantes.append(h)
                break
    return habitantes

# Crear 100 peces y 10 tiburones
peces = poblar("pez", 100)
tiburones = poblar("tiburon", 10)

# Iniciar todos los hilos
for h in peces + tiburones:
    h.start()
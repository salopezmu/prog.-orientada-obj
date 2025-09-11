class CuerpoCeleste:
    G = 6.67430e-11

    def __init__(self, id_unico, nombre, masa, densidad, diametro, distanciaSol):
        self.id = id_unico
        self.nombre = nombre
        self.masa = masa
        self.densidad = densidad 
        self.diametro = diametro 
        self.distanciaSol = distanciaSol 

    def mostrarInfo(self):
        print(f"ID: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Masa: {self.masa} kg")
        print(f"Densidad: {self.densidad} kg/m³")
        print(f"Diámetro: {self.diametro} m")
        print(f"Distancia al Sol: {self.distanciaSol} m")

    def fuerza_gravitacional(self, otro):
        distancia = abs(self.distanciaSol - otro.distanciaSol)
        if distancia == 0:
            print("Advertencia: los cuerpos tienen la misma órbita. Fuerza infinita.")
            return float('inf')

        fuerza = CuerpoCeleste.G * self.masa * otro.masa / distancia**2
        return fuerza
tierra = CuerpoCeleste(1, "Tierra", 5.972e24, 5514, 1.2742e7, 1.496e11)
marte = CuerpoCeleste(2, "Marte", 6.417e23, 3933, 6.779e6, 2.279e11)
tierra.mostrarInfo()
marte.mostrarInfo()
fuerza = tierra.fuerza_gravitacional(marte)
print(f"\nFuerza gravitacional entre {tierra.nombre} y {marte.nombre}: {fuerza:.2e} N")
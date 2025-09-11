class Vehiculo:
    def __init__(self, id_vehiculo, nombre, pasajeros, tripulacion, ruedas, fecha_matriculacion, medio):
        self.id = id_vehiculo
        self.nombre = nombre
        self.pasajeros = pasajeros
        self.tripulacion = tripulacion
        self.ruedas = ruedas
        self.fecha_matriculacion = fecha_matriculacion
        self.medio = medio

    def mostrar_info(self):
        print(f"\nVehículo ID: {self.id}")
        print(f"Tipo: {self.__class__.__name__}")
        print(f"Nombre: {self.nombre}")
        print(f"Pasajeros: {self.pasajeros}")
        print(f"Tripulación: {'Sí' if self.tripulacion else 'No'}")
        print(f"Ruedas: {self.ruedas}")
        print(f"Fecha de matriculación: {self.fecha_matriculacion}")
        print(f"Medio: {self.medio}")
#subclases
class Coche(Vehiculo):
    def __init__(self, *args, puertas):
        super().__init__(*args)
        self.puertas = puertas  

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Puertas: {self.puertas}")

class Moto(Vehiculo):
    def __init__(self, *args, cilindrada):
        super().__init__(*args)
        self.cilindrada = cilindrada  

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Cilindrada: {self.cilindrada} cc")

class Camion(Vehiculo):
    def __init__(self, *args, altura):
        super().__init__(*args)
        self.altura = altura  

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Altura: {self.altura} m")

#leer

def leer_vehiculo(i):
    print(f"\n--- Vehículo #{i + 1} ---")
    tipo = input("Tipo (coche/moto/camion): ").lower()
    nombre = input("Nombre: ")
    pasajeros = int(input("Número de pasajeros: "))
    tripulacion = input("¿Tiene tripulación? (s/n): ").lower() == 's'
    ruedas = int(input("Número de ruedas: "))
    fecha = input("Fecha de matriculación (AAAA-MM-DD): ")
    medio = input("Medio de desplazamiento: ")

    base_args = (i + 1, nombre, pasajeros, tripulacion, ruedas, fecha, medio)

    if tipo == "coche":
        puertas = int(input("¿Cuántas puertas tiene? (3 o 5): "))
        return Coche(*base_args, puertas=puertas)
    elif tipo == "moto":
        cilindrada = int(input("Cilindrada en cc: "))
        return Moto(*base_args, cilindrada=cilindrada)
    elif tipo == "camion":
        altura = float(input("Altura en metros: "))
        return Camion(*base_args, altura=altura)
    else:
        print("Tipo desconocido. Se crea como vehículo genérico.")
        return Vehiculo(*base_args)

#lista
vehiculos = []

for i in range(10):
    vehiculos.append(leer_vehiculo(i))

print("\n=== Listado de vehículos ===")
for v in vehiculos:
    v.mostrar_info()
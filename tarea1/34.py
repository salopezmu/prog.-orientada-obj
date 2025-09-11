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
        print(f"Nombre: {self.nombre}")
        print(f"Número de pasajeros: {self.pasajeros}")
        print(f"¿Tiene tripulación?: {'Sí' if self.tripulacion else 'No'}")
        print(f"Número de ruedas: {self.ruedas}")
        print(f"Fecha de matriculación: {self.fecha_matriculacion}")
        print(f"Medio de desplazamiento: {self.medio}")
def leer_vehiculo(i):
    print(f"\n--- Ingreso de datos para vehículo #{i + 1} ---")
    nombre = input("Nombre del vehículo: ")
    pasajeros = int(input("Número de pasajeros: "))
    tripulacion_input = input("¿Tiene tripulación? (s/n): ").lower()
    tripulacion = tripulacion_input == 's'
    ruedas = int(input("Número de ruedas: "))
    fecha = input("Fecha de matriculación (AAAA-MM-DD): ")
    medio = input("Medio de desplazamiento (terrestre/acuático/aéreo): ")

    return Vehiculo(i + 1, nombre, pasajeros, tripulacion, ruedas, fecha, medio)

vehiculos = []
for i in range(10):
    vehiculo = leer_vehiculo(i)
    vehiculos.append(vehiculo)

print("\n=== Listado de vehículos registrados ===")
for v in vehiculos:
    v.mostrar_info()
print("Ingrese líneas de texto. Para finalizar, presione ctrl+Z (Windows) o ctrl+D (Linux/macOS).")
try:
    while True:
        linea = input()
        print(f"Leído: {linea}")
except EOFError:
    print("\nFin de entrada detectado. Programa finalizado.")
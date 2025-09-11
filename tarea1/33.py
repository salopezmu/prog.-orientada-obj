import random
def mostrarArreglo(arr):
    print("[" + ", ".join(f"{x:.2f}" for x in arr) + "]")

# Algoritmo burbuja
def burbuja(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Algoritmo quicksort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivote = arr[0]
        menores = [x for x in arr[1:] if x <= pivote]
        mayores = [x for x in arr[1:] if x > pivote]
        return quicksort(menores) + [pivote] + quicksort(mayores)

if __name__ == "__main__":
    n = int(input("Ingrese el tamaño del arreglo: "))
    arreglo = []
    for i in range(n):
        numAleatorio = random.uniform(0, 100) 
        arreglo.append(numAleatorio)

    print("\nArreglo original:")
    mostrarArreglo(arreglo)

    print("\nElija el método de ordenamiento:")
    print("1 - Burbuja")
    print("2 - Quicksort")
    opcion = input("Opción: ")

    if opcion == "1":
        burbuja(arreglo)
        print("\nArreglo ordenado con Burbuja:")
        mostrarArreglo(arreglo)
    elif opcion == "2":
        arreglo = quicksort(arreglo)
        print("\nArreglo ordenado con Quicksort:")
        mostrarArreglo(arreglo)
    else:
        print("Opción inválida.")
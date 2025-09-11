print("Introduce números uno por uno. El programa terminará si repites el mismo número dos veces seguidas.")

numeros = []  
ultimo = None  

while True:
    try:
        entrada = input("Número: ")
        numero = int(entrada)

        numeros.append(numero)

        if numero == ultimo:
            print("\nNúmero repetido dos veces seguidas. Fin del programa.")
            break

        ultimo = numero
    except ValueError:
        print("Por favor, introduce un número entero válido.")

print("\nNúmeros ingresados:")
print(numeros)
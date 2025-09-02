def primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
veces = int(input("Ingrese un numero entero para la cantidad de veces que desea ejecutar el codigo: "))
for i in range(1,veces+1):
    print("si desea salir del programa digite un numero entero negativo")
    num = int(input("Ingrese un numero entero: "))
    if primo(num):
        print(f"el numero {num} es primo.")
    else:
        print(f"el numero {num} no es primo.")
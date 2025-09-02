def primo(n):
    count=0
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input("Ingrese un numero entero: "))
if primo(num):
    print(f"el numero {num} es primo.")
else:
    print(f"el numero {num} no es primo.")
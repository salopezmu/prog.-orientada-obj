continuar=True
def primo(n):
    count=0
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

while(continuar==True):
    num = int(input("Ingrese un numero entero: "))
    if num < 0:
        continuar=False
    elif primo(num):
        print(f"el numero {num} es primo.")
    else:
        print(f"el numero {num} no es primo.")
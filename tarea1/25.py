def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

def ackermann(m, n):
    if m==0:
        return n + 1
    elif m>0 and n==0:
        return ackermann(m - 1, 1)
    elif m>0 and n>0:
        return ackermann(m - 1, ackermann(m, n - 1))


numero = int(input("ingrese un numero entero para calcular su factorial: "))
resultado = factorial(numero)
print(f"El factorial de {numero} es: {resultado}")

x = int(input("ingrese el valor de m para ackermann: "))
y = int(input("ingrese el valor de n para ackermann: "))
resultado = ackermann(x, y)
print(f"ackermann({x}, {y}) = {resultado}")
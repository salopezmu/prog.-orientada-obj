def euclidesGcd(a, b):
    while b != 0:
        temp = b
        residuo = a % b
        a = temp
        b = residuo
    return a
num1 = int(input("ingrese el primer número entero: "))
num2 = int(input("ingrese el segundo número entero: "))
resultado = euclidesGcd(num1, num2)
print(f"El máximo común divisor de {num1} y {num2} es: {resultado}")
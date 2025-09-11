num1 = int(input("ingrese un numero entero: "))
num2 = int(input("ingrese un numero entero: "))
num3 = int(input("ingrese un numero entero: "))
if num1 <0 or num2 <0 or num3 <0:
    print("todos los números deben ser enteros positivos.")
elif num1==num2 and num2==num3:
    print("todos los numeros son iguales")
else:
    menor = min(num1, num2, num3)
    mayor = max(num1, num2, num3)
    print(f"el menor de los tres números es: {menor}")
    print(f"el mayor de los tres números es: {mayor}")
num = int(input("ingrese un número entero: "))
print(f"los numero impares menores que {num} son:")
for i in range(1,num):
    if i % 2 != 0:
        print(i)
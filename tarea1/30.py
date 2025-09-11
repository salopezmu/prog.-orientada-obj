limitesup = int(input("ingrese el número máximo para buscar primos: "))
print(f"los numeros primos entre 2 y {limitesup}:")
for num in range(2, limitesup + 1):
    es_primo = True
    for divisor in range(2, num):
        if num % divisor == 0:
            es_primo = False
            break
    if es_primo:
            print(num)
def gradosF_a_Celsius(f):
    return (5 / 9) * (f - 32)
print("cnversor de Fahrenheit a Celsius")
print("ingrese 999 para finalizar.\n")
while True:
    f = float(input("ingrese la temperatura en Fahrenheit: "))
    if f == 999:
        print("programa finalizado.")
        break
    c = gradosF_a_Celsius(f)
    print(f"{f}°F equivalen a {c:.2f}°C\n")
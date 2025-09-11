import math
a=float(input("ingrese el valor de a: "))
b=float(input("ingrese el valor de b: "))
c=float(input("ingrese el valor de c: "))
if a == 0:
    print("la ecuacion no es una ecuacion de segundo grado.")
else:
    discriminante = b**2 - 4*a*c
    if discriminante > 0:
            # Dos soluciones reales distintas
            x1 = (-b + math.sqrt(discriminante)) / (2*a)
            x2 = (-b - math.sqrt(discriminante)) / (2*a)
            print("La ecuacion tiene dos soluciones reales:")
            print(f"x1 = {x1}")
            print(f"x2 = {x2}")
    elif discriminante == 0:
        x = -b / (2*a)
        print("la ecuacion tiene una solucion real doble:")
        print(f"x = {x}")
    else:
         print("la ecuacion no tiene soluciones reales")

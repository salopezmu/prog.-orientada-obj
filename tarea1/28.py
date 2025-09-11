for i in range(1, 5):
    print(f"Valor actual: {i}")
    
    match i:
        case 1:
            print("primer caso.")
        case 2:
            print("segundo caso.")
        case 3:
            print("tercer mensaje aquí.")
        case _:
            print("Caso por defecto.")
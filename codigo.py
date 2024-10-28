def elegir_opcion() :
    print("elige una opcion\n", "1. Piedra\n", "2. Papel\n", "3. Tijera")
    opcion = int(input("escoge una opcion"))
    return opcion

print(elegir_opcion())
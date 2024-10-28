import random

def elegir_opcion() :
    print("elige una opcion\n", "1. Piedra\n", "2. Papel\n", "3. Tijera")
    opcion = int(input("escoge una opcion"))
    return opcion

def opcion_ordenador () :
    opcion_pc = random.randrange(1,3)
    return opcion_pc

print(elegir_opcion())
print(opcion_ordenador())
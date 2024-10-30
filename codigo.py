import random

def elegir_opcion() :
    print("elige una opcion\n", "Piedra\n", "Papel\n", "Tijera")
    opcion = input("escoge una opcion")
    return opcion

def opcion_ordenador () :
    opcion_pc = random.randrange(1,3)
    return opcion_pc

def ganador () :
    if (elegir_opcion () == "Piedra" and opcion_ordenador () == 1) :
        print("empate")
    elif (elegir_opcion () == "Piedra" and opcion_ordenador () == 2) :
        print("perdiste")
    elif (elegir_opcion () == "Piedra" and opcion_ordenador () == 3) :
        print("ganaste")
    elif (elegir_opcion () == "Papel" and opcion_ordenador () == 1) :
        print("ganaste")
    elif (elegir_opcion () == "Papel" and opcion_ordenador () == 2) :
        print("empate")
    elif (elegir_opcion () == "Papel" and opcion_ordenador () == 3) :
        print("perdiste")
    elif (elegir_opcion () == "Tijera" and opcion_ordenador () == 1) :
        print("perdiste")
    elif (elegir_opcion () == "Tijera" and opcion_ordenador () == 2) :
        print("ganaste")
    elif (elegir_opcion () == "Tijera" and opcion_ordenador () == 3) :
        print("empate")

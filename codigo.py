import random

def elegir_opcion() :
    print("elige una opcion\n", "Piedra\n", "Papel\n", "Tijera")
    opcion = input("escoge una opcion")
    return opcion

def opcion_ordenador () :
    opcion_pc = random.randrange(1,3)
    return opcion_pc

def ganador (contador1 = 0, contador2 = 0) :
    if (elegir_opcion () == "Piedra" and opcion_ordenador () == 1) :
        return "empate"
    elif (elegir_opcion () == "Piedra" and opcion_ordenador () == 2) :
        return "perdiste"
    elif (elegir_opcion () == "Piedra" and opcion_ordenador () == 3) :
        return "ganaste"
    elif (elegir_opcion () == "Papel" and opcion_ordenador () == 1) :
        return "ganaste"
    elif (elegir_opcion () == "Papel" and opcion_ordenador () == 2) :
        return "empate"
    elif (elegir_opcion () == "Papel" and opcion_ordenador () == 3) :
        return "perdiste"
    elif (elegir_opcion () == "Tijera" and opcion_ordenador () == 1) :
        return "perdiste"
    elif (elegir_opcion () == "Tijera" and opcion_ordenador () == 2) :
        return "ganaste"
    elif (elegir_opcion () == "Tijera" and opcion_ordenador () == 3) :
        return "empate"

while (contador1 < 3 or contador2 < 3) :
    elegir_opcion ()
    opcion_ordenador ()
print("cambio de prueba")
import random

def elegir_opcion() :
    print("elige una opcion\n", "Piedra\n", "Papel\n", "Tijera")
    opcion = input("escoge una opcion")
    return opcion

def opcion_ordenador () :
    opcion_pc = random.randrange(1,4)
    return opcion_pc

def ganador () :
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

contador1 = 0
contador2 = 0

opcion_ordenador ()

while (contador1 < 3 or contador2 < 3) :
    print (elegir_opcion ())
    opcion_ordenador ()
    print (ganador ())
    if ganador () == "perdiste" :
        print("perdiste la ronda")
        contador2 = contador2 + 1
    elif ganador () == "ganaste" :
        print("ganaste la ronda")
        contador1 == contador1 + 1
    else :
        print("empatasteis la ronda")
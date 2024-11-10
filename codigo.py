import random

def elegir_opcion() :
    print("elige una opcion\n", "Piedra\n", "Papel\n", "Tijera")
    opcion = input("")
    return opcion

def opcion_ordenador () :
    opcion_pc = random.randrange(1,4)
    return opcion_pc

def ordenador_tramposo (jugador, opcion_pc) :
    if jugador == "Piedra" :
        opcion_pc == 2
    elif jugador == "Papel" :
        opcion_pc == 3
    else :
        opcion_pc == 1
    print ("tramposo")
    return opcion_pc
 

def ganador (jugador, ordenador) :
    if (jugador == "Piedra" and ordenador == 1) :
        return "empate"
    elif (jugador == "Piedra" and ordenador == 2) :
        return "perdiste"
    elif (jugador == "Piedra" and ordenador == 3) :
        return "ganaste"
    elif (jugador == "Papel" and ordenador == 1) :
        return "ganaste"
    elif (jugador == "Papel" and ordenador == 2) :
        return "empate"
    elif (jugador == "Papel" and ordenador == 3) :
        return "perdiste"
    elif (jugador == "Tijera" and ordenador == 1) :
        return "perdiste"
    elif (jugador == "Tijera" and ordenador == 2) :
        return "ganaste"
    elif (jugador == "Tijera" and ordenador == 3) :
        return "empate"

contador1 = 0
contador2 = 0

while (contador1 < 3 and contador2 < 3) :
    jugador = elegir_opcion ()
    ordenador = opcion_ordenador ()

    if contador1 == 2 :
        ordenador_tramposo (jugador, ordenador)
    
    print ("tu eleccion ha sido", jugador, ", la del ordenador fue", ordenador)

    resultado = ganador(jugador, ordenador)

    print("resultado")

    if resultado == "perdiste" :
        print ("perdiste la ronda")
        contador2 = contador2 + 1
        print ("tu vas:", contador1, "\nel ordenador va:", contador2)
        print()
    elif resultado == "ganaste" :
        print("ganaste la ronda") 
        contador1 = contador1 + 1
        print ("tu vas:", contador1, "\nel ordenador va:", contador2)
        print ()
    else: 
        print("empataste la ronda")
        print ("tu vas:", contador1, "\nel ordenador va:", contador2)
        print()

if contador1 == 3:
    print("GANASTE!!!!!")
else:
    print("PERDISTE!!!!")
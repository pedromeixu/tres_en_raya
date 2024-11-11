import random

def elegir_opcion() -> str:
    '''
    esta funcion sirve para sacar la decision del jugador 
    '''
    print("elige una opcion\n", "Piedra\n", "Papel\n", "Tijera")
    opcion = input("")
    return opcion

def opcion_ordenador () -> str:
    '''
    esta funcion sirve para sacar la opcion aleatoria del ordenador
    '''
    opcion_pc = random.randrange(1,4)
    if opcion_pc == 1 :
        opcion_pc = "Piedra"
    elif opcion_pc == 2 :
        opcion_pc = "Papel"
    else :
        opcion_pc = "Tijera"
    return opcion_pc

def ordenador_tramposo (jugador: str, opcion_pc: str) -> str:
    '''
    esta funcion sirve para que el ordenador siempre saque la opcion ganadora contra el jugador
    '''
    if jugador == "Piedra" :
        opcion_pc = "Papel"
    elif jugador == "Papel" :
        opcion_pc = "Tijera"
    else :
        opcion_pc = "Piedra"
    return opcion_pc

def ganador (jugador: str, ordenador: str) -> str:
    '''
    esta funcion sirve para decidir el ganador teniendo en cuenta las opciones de cada uno
    '''
    if (jugador == "Piedra" and ordenador == "Piedra") :
        return "empate"
    elif (jugador == "Piedra" and ordenador == "Papel") :
        return "perdiste"
    elif (jugador == "Piedra" and ordenador == "Tijera") :
        return "ganaste"
    elif (jugador == "Papel" and ordenador == "Piedra") :
        return "ganaste"
    elif (jugador == "Papel" and ordenador == "Papel") :
        return "empate"
    elif (jugador == "Papel" and ordenador == "Tijera") :
        return "perdiste"
    elif (jugador == "Tijera" and ordenador == "Piedra") :
        return "perdiste"
    elif (jugador == "Tijera" and ordenador == "Papel") :
        return "ganaste"
    else :
        return "empate"

contador1 = 0
contador2 = 0
opcion = "si"

while opcion == "si" : 

    jugador = elegir_opcion ()
    ordenador = opcion_ordenador ()

    if contador1 == 2 :
        ordenador = ordenador_tramposo (jugador, ordenador)

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

    if contador1 == 3 or contador2 == 3 :
        if contador1 == 3:
            print("GANASTE!!!!!")
        elif contador2 == 3:
            print("PERDISTE!!!!")
        opcion = input("quieres jugar otra ronda? (si/no)")
        if opcion == "si" :
            contador1 = 0
            contador2 = 0
            continue
        break
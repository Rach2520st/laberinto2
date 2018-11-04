from input import input as input_flechas
import os
import random
import json
def intro_al_juego():
    print("UN POLLITO HA PERDIDO A SU MADRE")
    print("🐣🐣🐣🐣🐣🐣🐣🐣🐣🐣🐣🐣🐣🐣🐣🐣")
    print("¿Quieres ayudarlo a encontrar a su madre gallina?")


def nivel():
    lab = []
    sub = []
    for indice in range(15):
        for i in range(15):
            sub.append(random.randrange(0, 2))
        lab.append(sub)
        sub = []
    lab[0][0] = 2
    lab[14][14] = 3
    #coordenadas que indican la salida estandar del juego 
    lab[0][1] = 0
    lab[1][1] = 0
    lab[2][2] = 0
    lab[3][1] = 0
    lab[3][2] = 0
    lab[3][3] = 0
    lab[3][4] = 0
    lab[4][6] = 0
    lab[5][6] = 0
    lab[6][6] = 0
    lab[6][7] = 0
    lab[6][8] = 0
    lab[7][8] = 0
    lab[8][8] = 0
    lab[8][9] = 0
    lab[8][10] = 0
    lab[9][10] = 0
    lab[10][10] = 0
    lab[11][10] = 0
    lab[12][10] = 0
    lab[13][10] = 0
    lab[13][11] = 0
    lab[13][12] = 0
    lab[13][13] = 0
    lab[13][14] = 0
    lab[14][14] = 0
    return lab

def lento(lab):
    x = 0
    y = 0
    for linea in lab:
        #idea: ir creando movimientos aleatorios e ir guardandolos en archivos json y luego ejecutar los movimientos



def menu_psolucion(lab):
    valido = True
    while valido:
        print("""\n Seleccione la opción que desee realizar:
        1.- seguir jugando
        2.- encontrar la salida más rápida
        3.- ir por el camino más lento
        4.- ir por el camino estándar""")
        opcion = input()
        #si la opcion es 1 vuelve a llamar a la funcion del juego para que vuelva a jugar. 
        if opcion == "1":
            juego()
        
        elif opcion == "3":
                lento()

        else:
            print("esa opción no es válida, intentelo de nuevo")
            valido = False

    #el siguiente bloque hace que si la opcion que es ingresada no está en el menu, este
    #se vuelva a mostrar
    if valido is False:
        menu_psolucion()
def dibujar(lab):
    lab = lab
    x = 0
    y = 0
    pos_jugador_x = 0
    pos_jugador_y = 0
    for linea in lab:
        for item in linea:
            if pos_jugador_x == x and pos_jugador_y == y:
                print("🐥", end='')
                x = x + 1
            elif item == 1:
                print("x", end='')
                x = x + 1
            elif item == 3:
                print("🐔")
                x = x + 1
            elif item == 0:
                print(" ", end='')
                x = 0
                y = y + 1
            elif item == "-":
                print("-", end='')
            elif item == "\n":
                print("\n")
        print(" ")
def juego(lab):

    meta_x = 14
    meta_y = 14
    pos_jugador_x = 0
    pos_jugador_y = 0
    lab = lab

    while True:
        dibujar()
        tecla = input_flechas()
        if tecla.name == "arrow up":
            # si el cuadradito de arriba NO es una pared
            if lab(pos_jugador_x, pos_jugador_y - 1) != "x":
                # mover al jugador
                pos_jugador_y = pos_jugador_y - 1

        elif tecla.name == "arrow down":
            # si el cuadradito de abajo NO es una pared
            if lab(pos_jugador_x, pos_jugador_y + 1) != "x":
                pos_jugador_y = pos_jugador_y + 1  # mover

        elif tecla.name == "arrow right":
            # si el cuadradito a la derecha NO es una pared
            if lab(pos_jugador_x + 1, pos_jugador_y) != "x":
                pos_jugador_x = pos_jugador_x + 1
        elif tecla.name == "arrow left":
            # si el cuadradito a la izquierda NO es una pared
            if lab(pos_jugador_x - 1, pos_jugador_y) != "x":
                    pos_jugador_x = pos_jugador_x - 1
        #si la posicion es mayor o igual a 7,7 llama al menu
        elif pos_jugador_x >= 7 and pos_jugador_y >= 7:
            menu_psolucion()
        if pos_jugador_x == meta_x and pos_jugador_y == meta_y:
            os.system("clear")
            print("¡El pollito está con su mamá!")
            break


intro_al_juego()
lab = nivel()
dibujar(lab)
juego(lab)
lento(lab)
menu_psolucion(lab)
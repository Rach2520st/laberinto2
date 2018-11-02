from input import input as input_flechas
import os
import time
import random

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
    lab[0][1] = "-"
    #lab[1][1] = "-"
    #lab[1][2] = "-"
    #lab[2][2] = "-"
    #lab[3][1] = "-"
    #lab[3][2] = "-"
    #lab[3][3] = "-"
    lab[3][4] = "-"
    return lab

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
                print("  ", end='')
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
        dibujar(lab)
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

        if pos_jugador_x == meta_x and pos_jugador_y == meta_y:
            os.system("clear")
            print("¡El pollito está con su mamá!")
            break


intro_al_juego()
lab = nivel()
dibujar(lab)
juego(lab)

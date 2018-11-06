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
    #se crea un archivo que guarde los movimientos
    mov = {}
    with open('mov.json') as file:
        mov = json.load(file)
        #generador de movimientos aleatorios y los va guardando en el archivo mov
    for indice in range(15):
        random.randint(1, 4)
        if indice == 1:
            mov.append("arrow up")
        elif indice == 2:
            mov.append("arrow down")
        elif indice == 3:
            mov.append("arrow right")
        elif indice == 4:
            mov.append("arrow left")
        #llama a dibujar y se ejecuta el programa
        dibujar(mov)
        return mov
def estandar(lab):
    lab[0][1] = 5
    lab[1][1] = 5
    lab[2][2] = 5
    lab[3][1] = 5
    lab[3][2] = 5
    lab[3][3] = 5
    lab[3][4] = 5
    lab[4][6] = 5
    lab[5][6] = 5
    lab[6][6] = 5
    lab[6][7] = 5
    lab[6][8] = 5
    lab[7][8] = 5
    lab[8][8] = 5
    lab[8][9] = 5
    lab[8][10] = 5
    lab[9][10] = 5
    lab[10][10] = 5
    lab[11][10] = 5
    lab[12][10] = 5
    lab[13][10] = 5
    lab[13][11] = 5
    lab[13][12] = 5
    lab[13][13] = 5
    lab[13][14] = 5
    lab[14][14] = 5
    pos_jugador_x = 0
    pos_jugador_y = 0
    x = 0
    y = 0
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
                y = y + 1
            elif item == "-":
                print("-", end='')
        print(" ")
#esta funcion dibuja directamente la salida estandar del juego
def menu_psolucion(lab):
    valido = True
    while valido:
        print("""\n Seleccione la opción que desee realizar:
        1.- seguir jugando
        2.- ir por el camino más lento
        4.- ir por el camino estándar(más rápido)""")
        opcion = input()
        #si la opcion es 1 vuelve a llamar a la funcion del juego para que vuelva a jugar. 
        if opcion == "1":
            juego()
        elif opcion == "2":
            lento(lab)
        elif opcion == "3":
            estandar(lab)
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
    movi = {}
    while True:
        dibujar()
        tecla = input_flechas()
        if tecla.name == "arrow up":
            # si el cuadradito de arriba NO es una pared
            if lab(pos_jugador_x, pos_jugador_y - 1) != "x":
                # mover al jugador
                pos_jugador_y = pos_jugador_y - 1
                movi.append("arrow up")
        elif tecla.name == "arrow down":
            # si el cuadradito de abajo NO es una pared
            if lab(pos_jugador_x, pos_jugador_y + 1) != "x":
                pos_jugador_y = pos_jugador_y + 1  # mover
                movi.append("arrow down")
        elif tecla.name == "arrow right":
            # si el cuadradito a la derecha NO es una pared
            if lab(pos_jugador_x + 1, pos_jugador_y) != "x":
                pos_jugador_x = pos_jugador_x + 1
                movi.append("arrow right")
        elif tecla.name == "arrow left":
            # si el cuadradito a la izquierda NO es una pared
            if lab(pos_jugador_x - 1, pos_jugador_y) != "x":
                    pos_jugador_x = pos_jugador_x - 1
                    movi.append("arrow left")
        #si la posicion es mayor o igual a 7,7 llama al menu
        elif pos_jugador_x >= 7 and pos_jugador_y >= 7:
            menu_psolucion()
        if pos_jugador_x == meta_x and pos_jugador_y == meta_y:
            os.system("clear")
            print("¡El pollito está con su mamá!")
            break
    return movi

intro_al_juego()
lab = nivel()
dibujar(lab)
juego(lab)
lento(lab)
menu_psolucion(lab)
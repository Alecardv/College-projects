# -*- coding: utf-8 -*-
"""
Created on Tue Dec 08 13:25:22 2015

@author: J. Alejandro Cardona
"""
## NOTA DE CONVENCION:
##      Se usa un # (numeral) para comentario de una sola linea
##      Se usa dos # para comentario de varias lineas

import random

# Se declaran las siguientes variables para hacer mas legible el codigo
UP, LEFT, DOWN, RIGHT = 1, 2, 3, 4


class Board(object):

    def __init__(self, size=4, goal = 2048):
        ## size: Define el tamano del tablero, es un numero de un solo digito
        ##       ya que el tablero es cuadrado
        ## board: Se crea el tablero, es una lista de listas.
        ## goal: Numero con el cual se termina el juego cuando se consigue
        ## score : Puntuacion, si se unen 4 y 4, la puntuacion se incrementa en 8
        self.size = size
        ## -Nota acerca de board:
        ##      board se crea usando un concepto llamado: list comprehension
        ##      es una lista, se define con corchetes y se escribe un bulce for
        ##      que se antecede por una operacion cuyo resultado se agregara
        ##      como elemento a la lista que estamos creando.
        ##      para este caso puntual, se esta creando una lista de listas
        self.board = [[0 for i in range(size)] for i in range(size)]
        self.goal = self.check_goal(goal)        
        self.score = 0
        self.winner = False
        self.op = False
        self.insert() # Agrega un numero al tablero
        self.insert() # Agrega un numero al tablero

    def insert(self):
        ## Agrega un numero al tablero, escogido aleatoreamente de la siguiente
        ## lista: [2, 2, 2, 2, 2, 2, 2, 2, 2, 4]
        v = random.choice([2]*9+[4]) # v es un valor aleatoreo de la lista anteriormente mensionada
        empty = self.get_empty()
        if empty:
            xy = random.choice(empty)
            self.set(xy, v)
        else:
            # Si empty esta vacio significa que no hay casillas vacias y por lo 
            # tanto el juego termina
            self.winner = True

    def check_goal(self, goal):
        ## Sirve para verificar que el usuario ingreso un numero potencia de dos
        ## como objetivo para ganar el juego
        if goal in [2048, 4096, 8192, 16384]: return goal
        else: return 2048

    def get_empty(self):
        ## Devuelve una lista de pares de la forma: [(x1,y1), (x2,y2), (xn,yn)]
        ## que corresponden a la fila(x) y columna(y) que estan vacias (que contiene un 0)
        empty = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    empty.append((i,j))
        if not(empty): self.winner = True
        return empty

    def set(self, pos, value):
        # Establece una casilla (celda) con un valor dado
        self.board[pos[0]][pos[1]] = value

    def move(self, way):
        ## Dependiendo de la direccion del movimiento llama a una u otra funcion.
        ## Si el movimiento es derecha o izquierda llama a move_horizontal
        ## y finalmente a merge_horizontal que mueven las fichas y las suman respectivamente.
        ## De igual forma para arriba y abajo llama a las funicones verticales
        if self.check_valid_move(way):
            if way == LEFT or way == RIGHT:
                self.move_horizontal(way)
                self.merge_horizontal(way)
            else:
                self.move_vertical(way)
                self.merge_vertical(way)
            self.insert()
        for i in self.board:
            if self.goal in i:
                self.winner = True
        
    def move_horizontal(self, way):
        ## Mueve todas las fichas y las acopla en el extremo correspondiente
        ## Ya sea a la derecha o a la izquierda. Por ejemplo: para una sola fila [2,0,4,0]
        ## que se mueve a la derecha, el resultado seria: [0,0,2,4]
        for i in self.board: # Por cada fila dentro del tablero
            times = 0
            while 0 in i: # Mientras halla un 0 en la fila (casilla vacia)
                i.remove(0) # remueva el 0 de la fila
                times += 1 # Aumente en uno times
            if way == RIGHT: # Si la direccion es derecha
                for x in range(times): # Realize times veces
                    i.insert(0, 0) # insertar un cero adelante (en la posicion 0)
            else: # Si no entonces es la izquierda
                for x in range(times): # Realize times veces
                    i.append(0) # Insertar un 0 al final

    def merge_horizontal(self, way):
        ## Une las fichas que sean del mismo valor y que se encuentren juntas
        ## dependiendo de la direccion del movimiento.
        for i in self.board: # Por cada fila en el tablero
            n = self.size - 1
            if way == RIGHT: # Si se mueve a la derecha
                while n > 0: # Mientras n sea mayor que 0
                    if i[n] == i[n-1] and i[n] != 0: # Si la celda n es igual a la celda n-1 y no son 0
                        i[n] = i[n] + i[n] # La celda n se convierte en la suma
                        del(i[n-1]) # Se elimina la celda n-1
                        i.insert(0,0) # Se agrega un 0 al principio
                    n -= 1
            else: # izquierda
                for x in range(self.size-1): # Haga size-1 veces
                    if i[x] == i[x+1] and i[x] != 0: # Si la celda x es igual a la celda x+1 y no son 0
                        i[x] = i[x] + i[x] # La celda x se convierte en la suma
                        del(i[x+1]) #Se elimina la celda x+1
                        i.append(0) #Se agrega un 0 al final

    def move_vertical(self, way):
        ## Mueve todas las fichas y las acopla en el extremo correspondiente
        ## Ya sea arriba o abajo. Por ejemplo: para la siguiente columna con un 
        ## movimiento hacia abajo quedaria como se muestra enseguida
        # [2,      [0,
        #  0,  -->  0,
        #  4,       2,
        #  0]       4]
        temp_board = [] # Creo un tablero temporal
        for x in range(self.size): # haga size veces
            temp = [i[x] for i in self.board] # por cada fila en board tome el elemento x
            times = 0
            while 0 in temp: # Mientras halla un 0 en la columna
                temp.remove(0) # Remueva el 0
                times += 1 # Incremente times en uno
            if way == DOWN: #Si la direccion es hacia abajo
                for n in range(times): temp.insert(0, 0) # Inserte un 0 times veces al prinicipio
            else: # Sino entonces es hacia arriba
                for n in range(times): temp.append(0) # Incerte un 0 times veces al final
            temp_board.append(temp) #Agregue la columna como una fila al tablero temporal

        # Ahora hay que reorganizar el tablero:
        self.board = [] # Se vacea el tablero original
        for y in range(self.size): # Haga size veces
            temp = [i[y] for i in temp_board] # por cada fila en el tablero temporal tome el elemento y
            self.board.append(temp) # agregue temp

    def merge_vertical(self, way):
        temp_board = [] # Se crea un tablero temporal para poder desorganizar el original
        for x in range(self.size): # Haga size veces
            temp = [i[x] for i in self.board] # por cada fila en el tablero tome el elemento x, con lo que temp se vuelve una lista con todos los elementos de dicha columna
            if way == DOWN: # Si la direccion es hacia abajo
                n = self.size - 1
                while n > 0:
                    if temp[n] == temp[n-1] and temp[n] != 0:
                        temp[n] = temp[n] + temp[n]
                        del(temp[n-1])
                        temp.insert(0,0)
                    n -= 1
            else: # Si la direccion es hacia arriba
                for j in range(self.size-1):
                    if temp[j] == temp[j+1] and temp[j] != 0:
                        temp[j] = temp[j] + temp[j]
                        del(temp[j+1])
                        temp.append(0)
            temp_board.append(temp) # Agregue al tablero temporal
        #Hay que Reorganizar las filas como columnas, ya que en el paso anterior se invirtieron
        self.board = [] # Se vacea el tablero original
        for y in range(self.size): # Haga size veces
            temp = [t[y] for t in temp_board] # por cada fila en el tablero temporal tome el elemento y (las columnas se vuelven filas)
            self.board.append(temp) # Se agrega la fila y va quedando organizado

    def check_valid_move(self, way):
        if way == RIGHT or way == LEFT:
            for line in self.board:
                if self.check_valid_line(line, way): return True
        elif way == UP or way == DOWN:
            for i in range(self.size):
                templine = [n[i] for n in self.board]
                if self.check_valid_line(templine, way): return True
        return False

    def check_valid_line(self, line, way):
        #Si toda la linea es 0 ej:[0,0,0,0], no se mueve(retorna Falso):
        cero = True
        for i in range(self.size):
                if line[i] != 0: cero = False
        if cero: return False
        ##Hay numeros que se puedan sumar?
        ##Si no hay entonces el movimiento no es valido. ej:[2,4,8,4]
        for x in range(self.size-1):
            if line[x] != 0 and line[x] == line[x+1]: return True
        #Si hay un 0 despues de un numero se puede mover
        if way == RIGHT or way == DOWN:
            for n in range(self.size-1):
                if line[n] != 0 and line[n+1] == 0: return True
        if way == LEFT or way == UP:
            for n in range(self.size-1):
                if line[n] == 0 and line[n+1] != 0: return True
        return False
    
    def __str__(self):
        ## Se encarga de que al imprimir el tablero este se imprima una fila debajo
        ## de la otra
        rep = ''
        for i in self.board:
            rep += str(i) + '\n'
        return rep
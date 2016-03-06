# -*- coding: utf-8 -*-
"""
Created on Tue Dec 08 13:23:49 2015

@author: J. Alejandro Cardona
"""

import os
import sys
from Control import *

pygame.init()

size = width, height = 524, 524
speed = [2,2]
black = 0,0,0
white = 255,255,255
screen = pygame.display.set_mode(size)
#Las posiciones son relativas a la interface, por eso van en la vista
pos = {(0,0):(25,25), (0,1):(150,25), (0,2):(275,25), (0,3):(400,25),
       (1,0):(25,150), (1,1):(150,150), (1,2):(275,150), (1,3):(400,150),
       (2,0):(25,275), (2,1):(150,275), (2,2):(275,275), (2,3):(400,275),
       (3,0):(25,400), (3,1):(150,400), (3,2):(275,400), (3,3):(400,400)}

def draw_board():
    pygame.draw.line(screen, black, (0,0), (0,524), 50)
    pygame.draw.line(screen, black, (524,0), (524,524), 50)
    pygame.draw.line(screen, black, (0,0), (524,0), 50)
    pygame.draw.line(screen, black, (0,524), (524,524), 50)
    pygame.draw.line(screen, black, (137.5,0), (137.5,524), 25)
    pygame.draw.line(screen, black, (262.5,0), (262.5,524), 25)
    pygame.draw.line(screen, black, (387.5,0), (387.5,524), 25)
    pygame.draw.line(screen, black, (0,137.5), (534,137.5), 25)
    pygame.draw.line(screen, black, (0,262.5), (534,262.5), 25)
    pygame.draw.line(screen, black, (0,387.5), (534,387.5), 25)
    pygame.display.flip()

def draw_game():
    for i in range(juego.size):
        for j in range(juego.size):
            if juego.board[i][j] != 0:
                screen.blit(pygame.image.load(str(juego.board[i][j])+".jpg"), pos[(i,j)])
                pygame.display.flip()
                print juego

screen.fill(white)

while juego.winner == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            juego.move(UP)
            screen.fill(white)
        elif pressed[pygame.K_DOWN]:
            juego.move(DOWN)
            screen.fill(white)
        elif pressed[pygame.K_RIGHT]:
            juego.move(RIGHT)
            screen.fill(white)
        elif pressed[pygame.K_LEFT]:
            juego.move(LEFT)
            screen.fill(white)
        draw_board()
        draw_game()
    pygame.display.flip()
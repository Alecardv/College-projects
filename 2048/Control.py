# -*- coding: utf-8 -*-
"""
Created on Tue Dec 08 13:25:40 2015

@author: J. Alejandro Cardona
"""
from Board import *
import pygame

UP, LEFT, DOWN, RIGHT = 1, 2, 3, 4

juego = Board()

_2 = pygame.image.load("2.jpg"); _2re = _2.get_rect()
_4 = pygame.image.load("4.jpg"); _4re = _4.get_rect()
_8 = pygame.image.load("8.jpg"); _8re = _8.get_rect()
_16 = pygame.image.load("16.jpg"); _16re = _16.get_rect()
_32 = pygame.image.load("32.jpg"); _32re = _32.get_rect()
_64 = pygame.image.load("64.jpg"); _64re = _64.get_rect()
_128 = pygame.image.load("128.jpg"); _128re = _128.get_rect()
_256 = pygame.image.load("256.jpg"); _256re = _256.get_rect()
_512 = pygame.image.load("512.jpg"); _512re = _512.get_rect()
_1024 = pygame.image.load("1024.jpg"); _1024re = _1024.get_rect()
_2048 = pygame.image.load("2048.jpg"); _2048re = _2048.get_rect()

figs = {2:(_2, _2re), 4:(_4,_4re), 8:(_8,_8re), 16:(_16,_16re),
   32:(_32,_32re), 64:(_64,_64re), 128:(_128,_128re), 256:(_256,_256re),
   512:(_512,_512re), 1024:(_1024,_1024re), 2048:(_2048,_2048re)}

def read_key(key):
# Este metodo se usa solo para jugar en modo consola
    if key == 'w':
        juego.move(UP)
    elif key == 's':
        juego.move(DOWN)
    elif key == 'a':
        juego.move(LEFT)
    elif key == 'd':
        juego.move(RIGHT)
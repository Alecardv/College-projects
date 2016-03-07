import sys
import pygame
import pygame.gfxdraw
from triqui import *
pygame.init()

size = 500,500
white = 255, 255, 255
black = 0, 0, 0
screen = pygame.display.set_mode(size)

def drawCircle(pos):
	pygame.gfxdraw.aacircle(screen, pos[0]+83, pos[1]+83, int(500/9), black)
	pygame.gfxdraw.aacircle(screen, pos[0]+83, pos[1]+83, int(500/9)+1, black)
	pygame.gfxdraw.aacircle(screen, pos[0]+83, pos[1]+83, int(500/9)+2, black)
	pygame.gfxdraw.aacircle(screen, pos[0]+83, pos[1]+83, int(500/9)+3, black)
	pygame.display.flip()

def drawX(pos):
	pygame.draw.line(screen, black, (pos[0]+36, pos[1]+36), (pos[0]+130, pos[1]+130), 5)
	pygame.draw.line(screen, black, (pos[0]+130, pos[1]+36), (pos[0]+36, pos[1]+130), 5)
	pygame.display.flip()

def drawBoard(ratio):
	pygame.draw.line(screen, black, (0, ratio/3    ), (ratio, ratio/3    ), 5)
	pygame.draw.line(screen, black, (0, (ratio/3)*2), (ratio, (ratio/3)*2), 5)
	pygame.draw.line(screen, black, (0, (ratio/3)*3), (ratio, (ratio/3)*3), 5)
	pygame.draw.line(screen, black, (ratio/3,     0), (ratio/3,     ratio), 5)
	pygame.draw.line(screen, black, ((ratio/3)*2, 0), ((ratio/3)*2, ratio), 5)
	pygame.draw.line(screen, black, ((ratio/3)*3, 0), ((ratio/3)*3, ratio), 5)
	pygame.display.flip()

def Pos(i):#i es una tupla x y, en donde se presiono el mouse
	if i[0]<166 and (i[1]<500 and i[1]>333):
		return (0,333) #Uno
	elif (i[0]<333 and i[0]>166) and (i[1]<500 and i[1]>333):
		return (166,333) #Dos
	elif (i[0]<500 and i[0]>333) and (i[1]<500 and i[1]>333):
		return (333,333) #Tres
	elif i[0]<166 and (i[1]<333 and i[1]>166):
		return (0,166) #Cuatro
	elif (i[0]<333 and i[0]>166) and (i[1]<333 and i[1]>166):
		return (166,166) #Cinco
	elif (i[0]<500 and i[0]>333) and (i[1]<333 and i[1]>166):
		return (333,166) #Seis
	elif i[0]<166 and i[1]<166:
		return (0,0) #Siete
	elif (i[0]<333 and i[0]>166) and i[1]<166:
		return (166,0) #Ocho
	elif (i[0]<500 and i[0]>333) and i[1]<166:
		return (333,0) #Nueve

def Pos1to9(i):#i es una tupla x y
	if Pos(i) == (0,333): return 1
	elif Pos(i) == (166,333): return 2
	elif Pos(i) == (333,333): return 3
	elif Pos(i) == (0,166): return 4
	elif Pos(i) == (166,166): return 5
	elif Pos(i) == (333,166): return 6
	elif Pos(i) == (0,0): return 7
	elif Pos(i) == (166,0): return 8
	elif Pos(i) == (333,0): return 9

def PosXY(i):#i es un entero
	if i   == 0 : return (0,333)
	elif i == 1 : return (166,333)
	elif i == 2 : return (333,333)
	elif i == 3 : return (0,166)
	elif i == 4 : return (166,166)
	elif i == 5 : return (333,166)
	elif i == 6 : return (0,0)
	elif i == 7 : return (166,0)
	elif i == 8 : return (333,0)

def drawGame(vect):
	screen.fill(white)
	drawBoard(500)
	for i in range(len(vect)):
		if vect[i] == 2:
			drawCircle(PosXY(i))
		elif vect[i] == 1:
			drawX(PosXY(i))
	pygame.display.flip()

screen.fill(white)
drawBoard(500)
pygame.display.flip()
#Pass = True
while True:
	#Quien inicia el juego?
	#en el for: 6 Para el humano, 5 para la maquina
	for i in range(1,6):
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					Board = Play(Pos1to9(event.pos))
					if Ganador() != 0:
						print Score()
						drawGame(Board)
						while True:
							for event in pygame.event.get():
								if event.type == pygame.QUIT: sys.exit()
					else:
						drawGame(Board)
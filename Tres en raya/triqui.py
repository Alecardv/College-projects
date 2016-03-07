import os
from core import *
if os.name == 'nt':
	clear = 'cls'
else: clear = 'clear'
os.system(clear)

print "Seleccione la dificultad: "
LEVEL = int(raw_input("1. Facil\n2. Medio\n3. Imposible\n"))
while True:
	if LEVEL == 1 or LEVEL == 2 or LEVEL == 3:
		break
	else:
		os.system(clear)
		LEVEL = int(raw_input("Opcion incorrecta\n1. Facil\n2. Medio\n3. Imposible\n"))

Triqui = Triqui(LEVEL)

def Play(move):
	Triqui.humanMove(move)
	Triqui.comprobarVictoria()
	if Triqui.ganador != 0:
		print Score()
		return Triqui.getBoard()
	Triqui.pcMove()
	Triqui.comprobarVictoria()
	if Triqui.ganador != 0:
		print Score()
		return Triqui.getBoard()
	return Triqui.getBoard()

def Score():
	return Triqui.resultado()

def Ganador():
	return Triqui.ganador
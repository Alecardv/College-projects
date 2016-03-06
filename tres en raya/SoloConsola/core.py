import random
import os
#Human = 1
#PC = 2
class Triqui:

	def __init__(self,l):
		self.movpc   = random.randint(0,8)
		self.ganador = 0
		self.movhuman= 0
		self.level   = l
		self.printinit()
		print "\nLos movimientos se introducen indicando el numero de la casilla.\n"
		self.tablero = [0,0,0,0,0,0,0,0,0]

	def comprobarVictoria(self):
		#Human
		if (self.tablero[:3]==[1,1,1] or self.tablero[3:6]==[1,1,1] or self.tablero[6:]==[1,1,1] or
			(self.tablero[0]==1 and self.tablero[3]==1 and self.tablero[6]==1) or
			(self.tablero[1]==1 and self.tablero[4]==1 and self.tablero[7]==1) or
			(self.tablero[2]==1 and self.tablero[5]==1 and self.tablero[8]==1) or
			(self.tablero[0]==1 and self.tablero[4]==1 and self.tablero[8]==1) or
			(self.tablero[2]==1 and self.tablero[4]==1 and self.tablero[6]==1)):
			self.ganador=1
			return True
		#PC
		if (self.tablero[:3]==[2,2,2] or self.tablero[3:6]==[2,2,2] or self.tablero[6:]==[2,2,2] or
			(self.tablero[0]==2 and self.tablero[3]==2 and self.tablero[6]==2) or
			(self.tablero[1]==2 and self.tablero[4]==2 and self.tablero[7]==2) or
			(self.tablero[2]==2 and self.tablero[5]==2 and self.tablero[8]==2) or
			(self.tablero[0]==2 and self.tablero[4]==2 and self.tablero[8]==2) or
			(self.tablero[2]==2 and self.tablero[4]==2 and self.tablero[6]==2)):
			self.ganador=2
			return True
		else:
			self.ganador=0
			self.empate()
			return False

	def printinit(self):
		os.system("clear")
		print 7, '|', 8, '|', 9
		print "-"*9
		print 4, '|', 5, '|', 6
		print "-"*9
		print 1, '|', 2, '|', 3

	def printBoard(self):
		os.system("clear")
		print self.auxprint(self.tablero[6]),'|',self.auxprint(self.tablero[7]),'|',self.auxprint(self.tablero[8])
		print "-"*9	
		print self.auxprint(self.tablero[3]),'|',self.auxprint(self.tablero[4]),'|',self.auxprint(self.tablero[5])
		print "-"*9
		print self.auxprint(self.tablero[0]),'|',self.auxprint(self.tablero[1]),'|',self.auxprint(self.tablero[2])
	
	def auxprint(self,n):
		if   n == 0: return ' '
		elif n == 1: return "X"
		elif n == 2: return "O"

	def empate(self):
		n=9
		i=0
		for i in range(n):
			if self.tablero[i] == 0:
				return False
		self.ganador=3
		return True

	def resultado(self):
		if self.ganador==1:
			print "Ganaste !!"
		elif self.ganador==2:
			print "Perdiste !!"
		elif self.ganador==3:
			print "Empate !!"

	def humanMove(self):
		self.movhuman  = int(raw_input("Cual es tu movimiento? (1-9): "))
		self.movhuman -= 1
		while self.movhuman > 8 or self.movhuman < 0 or self.tablero[self.movhuman] == 1 or self.tablero[self.movhuman] == 2:
			self.movhuman = int(raw_input("Movimiento no valido, intente de nuevo (1-9): "))
			self.movhuman-= 1
		self.tablero[self.movhuman] = 1

	def pcMove(self):
		if   (self.level == 1):
			self.moveDummy()
		elif (self.level == 2):
			self.moveBlocker()
		elif (self.level == 3):
			self.moveGodMode()

	def moveDummy(self):
		self.movpc = random.randint(0,8)
		while self.tablero[self.movpc] == 1 or self.tablero[self.movpc] == 2:
			self.movpc = random.randint(0,8)
		self.tablero[self.movpc] = 2

	def moveBlocker(self):
		randPar = random.randrange(0,9,2)

		#Comprueba si esta iniciando el juego, de ser asi, usa el dummy
		for i in self.tablero:
			if i == 0:
				Vacio = True
			else:
				Vacio = False ; break
		if Vacio == True:
			return self.moveDummy()

		#Comprueba si es su primer turno o si ya ha jugado antes
		for i in range(len(self.tablero)):
			if (self.tablero[i] == 2) :
				turn = 2; break
			else:
				turn = 1
		
		#Si es Primer turno despues de humano, ejecuta movimientos ya pensados.
		if turn == 1:
			#Si humano a jugado en esquinas:
			if (self.tablero[0] == 1) or (self.tablero[2] == 1) or (self.tablero[6] == 1) or (self.tablero[8] == 1):
				self.tablero[4] = 2
			#Si humano a juegado en centro:
			elif self.tablero[4] == 1:
				while randPar == 4:
					randPar = random.randrange(0,9,2)
				self.tablero[randPar] = 2
			#Si humano a jugado en laterales
			elif (self.tablero[1] == 1) or (self.tablero[3] == 1) or (self.tablero[5] == 1) or (self.tablero[7] == 1):
				self.tablero[4] = 2

		#Si es Segundo turno, bloquea, sino hay que bloquear, usa dummy
		else:
			for i in range(len(self.tablero)):
				#Comprobacion de verticales:
				if   i == 0 or i == 3 or i == 6:
					if self.tablero[i] == 1:
						if self.tablero[i+1] == 1:
							if self.tablero[i+2] == 0: self.tablero[i+2] = 2 ; return 0
						elif self.tablero[i+2] == 1:
							if self.tablero[i+1] == 0: self.tablero[i+1] = 2 ; return 0

				elif i == 1 or i == 4 or i == 7:
					if self.tablero[i] == 1:
						if self.tablero[i+1] == 1:
							if self.tablero[i-1] == 0: self.tablero[i-1] = 2 ; return 0
						elif self.tablero[i-1] == 1:
							if self.tablero[i+1] == 0: self.tablero[i+1] = 2 ; return 0

				elif i == 2 or i == 5 or i == 8:
					if self.tablero[i] == 1:
						if self.tablero[i-1] == 1:
							if self.tablero[i-2] == 0: self.tablero[i-2] = 2 ; return 0
						elif self.tablero[i-2] == 1:
							if self.tablero[i-1] == 0: self.tablero[i-1] = 2 ; return 0

				#Comprobacion de horizontales:
				if   i == 0 or i == 1 or i == 2:
					if self.tablero[i] == 1:
						if self.tablero[i+3] == 1:
							if self.tablero[i+6] == 0: self.tablero[i+6] = 2 ; return 0
						elif self.tablero[i+6] == 1:
							if self.tablero[i+3] == 0: self.tablero[i+3] = 2 ; return 0

				elif i == 3 or i == 4 or i == 5:
					if self.tablero[i] == 1:
						if self.tablero[i+3] == 1:
							if self.tablero[i-3] == 0: self.tablero[i-3] = 2 ; return 0
						elif self.tablero[i-3] == 1:
							if self.tablero[i+3] == 0: self.tablero[i+3] = 2 ; return 0

				elif i == 6 or i == 7 or i == 8:
					if self.tablero[i] == 1:
						if self.tablero[i-3] == 1:
							if self.tablero[i-6] == 0: self.tablero[i-6] = 2 ; return 0
						elif self.tablero[i-6] == 1:
							if self.tablero[i-3] == 0: self.tablero[i-3] = 2 ; return 0

				#Comprobacion de diagonales:
				if i == 0 or i == 2 or i == 6 or i == 8:
					if self.tablero[i] == 1:
						if self.tablero[4] == 1:
							if   i==0:
								if self.tablero[i+8] == 0: self.tablero[i+8] = 2 ; return 0
							elif i==2:
								if self.tablero[i+4] == 0: self.tablero[i+4] = 2 ; return 0
							elif i==6:
								if self.tablero[i-4] == 0: self.tablero[i-4] = 2 ; return 0
							elif i==8:
								if self.tablero[i-8] == 0: self.tablero[i-8] = 2 ; return 0
						else:
							if   i==0:
								if self.tablero[i+8] == 1:
									if self.tablero[4] == 0: self.tablero[4] = 2 ; return 0
							elif i==2:
								if self.tablero[i+4] == 1:
									if self.tablero[4] == 0: self.tablero[4] = 2 ; return 0
							elif i==6:
								if self.tablero[i-4] == 1:
									if self.tablero[4] == 0: self.tablero[4] = 2 ; return 0
							elif i==8:
								if self.tablero[i-8] == 1:
									if self.tablero[4] == 0: self.tablero[4] = 2 ; return 0
				#Comprueba diagonales desde el centro
				elif i == 4:
					if self.tablero[4] == 1:
						if self.tablero[0] == 1:
							if self.tablero[8] == 0: self.tablero[8] = 2 ; return 0
						if self.tablero[2] == 1:
							if self.tablero[6] == 0: self.tablero[6] = 2 ; return 0
						if self.tablero[6] == 1:
							if self.tablero[2] == 0: self.tablero[2] = 2 ; return 0
						if self.tablero[8] == 1:
							if self.tablero[0] == 0: self.tablero[0] = 2 ; return 0
				#Si ninguna jugada se puede bloquear usa el dummy
			return self.moveDummy()

	def moveGodMode(self):
		posicion=0
		n=9
		aux=-9999
		mejor=-9999
		i=0
		for i in range (n):
			if self.tablero[i]==0:
				self.tablero[i]=2
				aux=self.minimo()
				if aux > mejor:
					mejor=aux
					posicion=i
				self.tablero[i]=0
		self.tablero[posicion] = 2

	def minimo(self):
		if self.comprobarVictoria() and self.ganador==2:
			return 1
		if self.empate():
			return 0
		n=9
		aux=9999
		mejor=9999
		i=0
		for i in range (n):
			if self.tablero[i]==0:
				self.tablero[i]=1
				aux=self.maximo()
				if aux < mejor:
					mejor=aux
				self.tablero[i]=0
		return mejor
	
	def maximo(self):
		if self.comprobarVictoria() and self.ganador==1:
			return -1
		if self.empate():
			return 0
		n=9
		aux=-9999
		mejor=-9999
		i=0
		for i in range (n):
			if self.tablero[i]==0:
				self.tablero[i]=2
				aux=self.minimo()
				if aux > mejor:
					mejor=aux
				self.tablero[i]=0
		return mejor
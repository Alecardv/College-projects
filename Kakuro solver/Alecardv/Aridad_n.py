import sys
#sys.setrecursionlimit(40)
def copy(origen):
	destino = []
	i = 0
	while (i < len(origen)):
		destino.append(origen[i])
		i += 1
	return destino

def hayarposibles(aridad, valor, posibles, dom, iteraciones, base):
	if (aridad == 0):
		print posibles
	else:
		i = 0
		j = 0
		k = 0
		ar = 0
		posi = []
		suma = 0
		
		if (len(dom) < aridad):
			iteraciones += 1
			#dominio = [1,2,3,4,5,6,7,8,9]
			dom = copy(base)
			
			if ( (len(posibles) == 0) and (iteraciones > 0) ):
				if (iteraciones > 9):
					hayarposibles(0, valor, posibles, dom, iteraciones, base)	
				else:
					dom = dom[1:9]
					base = copy(dom)
					hayarposibles(aridad, valor, posibles, dom, iteraciones, base)
			else:
				while (j < len(posibles)):
					while (k < len(posibles[j])):
						if (posibles[j][k] in dom):
							dom.remove(posibles[j][k])
							k += 1
						else:
							k += 1
					j += 1
					k = 0
				if (iteraciones > 9):
					hayarposibles(0, valor, posibles, dom, iteraciones, base)
				else:
					dom = dom[1:9]
					base = copy(dom)
					hayarposibles(aridad, valor, posibles, dom, iteraciones, base)


		else:
			#Paso los elementos posibles segun la aridad y no ingreso los repetidos
			while (ar < aridad):
				if (not (dom[ar] in posi)):
					posi.append(dom[ar])
					ar += 1
				else:
					ar += 1
			
			#Sumo los elementos del vector si estan correctos respecto a la aridad
			longitud = len(posi)
			if (longitud == aridad):
				
				for i in posi: suma += i
				#Compruebo el valor de su suma
				if (suma == valor):
					#Aqui va un backtraking
					posibles.append(posi)
					dom.remove(dom[aridad-1])
					hayarposibles(aridad, valor, posibles, dom, iteraciones, base)
				else:
					if ( (suma > valor) and (iteraciones > 9) ):
						#Condicion de parada
						hayarposibles(0, valor, posibles, dom, iteraciones, base)
					else:
						#Aqui va el backtraking
						dom.remove(dom[aridad-1])
						hayarposibles(aridad, valor, posibles, dom, iteraciones, base)
			else:
				#Aqui va el backtraking
				dom.remove(dom[aridad-1])
				hayarposibles(aridad, valor, posibles, dom, iteraciones, base)

def tabla(aridad, valor):
	if (valor == 37):
		exit()
	else:
		dominio = [1,2,3,4,5,6,7,8,9]
		dominiobase = [1,2,3,4,5,6,7,8,9]
		posibles = []
		print "Aridad: %i - Valor: %i" % (aridad,valor)
		hayarposibles(aridad, valor, posibles, dominio, 0, dominiobase)
		tabla(aridad,valor+1)

#tabla(3,2)

dominio = [1,2,3,4,5,6,7,8,9]
dominiobase = [1,2,3,4,5,6,7,8,9]
posibles = []
hayarposibles(3, 20, posibles, dominio, 0, dominiobase)
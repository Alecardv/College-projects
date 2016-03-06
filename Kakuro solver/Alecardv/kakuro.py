from domains import *
import os, sys, types, time, copy

PERMUTATION_RANGE_INCREMENT = 40

kakuro1 = [\
[-1, [-1,16], [-1, 39], -1, [-1, 8], [-1,10], -1, [-1,41], [-1,11]],\
[[14,-1], 0, 0, [11,-1],0,0,[11,15],0,0],\
[[15,-1],0,0,[17,14],0,0,0,0,0],\
[-1, [11,4],0,0,[-1,6],[15,8],0,0,[-1,17]],\
[[15,-1],0,0,0,0,0,[15,16],0,0],\
[[8,-1],0,0,[35,9],0,0,0,0,0],\
[-1,[4,10],0,0,[-1,3],[17,6],0,0,[-1,11]] ,\
[[18,-1],0,0,0,0,0,[5,-1],0,0],\
[[16,-1],0,0,[3,-1],0,0,[14,-1],0,0]]

kakuro2 = [\
[-1,-1,[-1,44],[-1,7],-1,-1,[-1,13],[-1,43],[-1,11]],\
[-1,[7,13],0,0,[-1,11],[8,-1],0,0,0],\
[[30,-1],0,0,0,0,[17,7],0,0,0],\
[[7,-1],0,0,[13,-1],0,0,0,0,[-1,14]],\
[[11,-1],0,0,[-1,14],[30,16],0,0,0,0],\
[[13,-1],0,0,0,0,[-1,3],[4,-1],0,0],\
[-1,[26,13],0,0,0,0,[3,7],0,0],\
[[7,-1],0,0,0,[18,-1],0,0,0,0],\
[[17,-1],0,0,0,-1,[5,-1],0,0,-1]]

kakuro4 = [\
[-1,-1,[-1,40],[-1,16],-1,-1,[-1,44],[-1,3]],\
[-1,[13,30],0,0,[-1,4],[8,-1],0,0],\
[[19,-1],0,0,0,0,[4,3],0,0],\
[[16,-1],0,0,[12,-1],0,0,0,[-1,11]],\
[[12,-1],0,0,[-1,17],[8,-1],0,0,0],\
[[18,-1],0,0,0,[-1,16],[12,-1],0,0],\
[-1,[18,17],0,0,0,[6,16],0,0],\
[[15,-1],0,0,[23,-1],0,0,0,0],\
[[17,-1],0,0,-1,[16,-1],0,0,-1]]

Kakuro = kakuro2

solutions = {}

rows = len(Kakuro)
cols = len(Kakuro[0])

def permitation(array):	
	numOfPermutations = 1	
	for i in range(len(array)):
		numOfPermutations = numOfPermutations * len(array[i])
	Index = [0]*len(array)
	List = []	
	for x in range(numOfPermutations):
		subList = []		
		for i in range(len(array)):
			subList.append(array[i][Index[i]])
		if len(set(subList)) == len(subList):	
			List.append(subList)
		for i in range(len(array)):
			Index[i] = Index[i] + 1
			if Index[i] != len(array[i]):
				break
			else:
				Index[i] = 0
	return List



# Itera sobre las celdas en recorrido vertical u horizontal
# buscando valores que proporcionen una solucion y agregarlos
# cuando se actualiza un dominio se remueven los valores que no
# son validos para los demas
# Nota: index ayuda a saber cuantas veces se ejecuto la funcion 
def removeIllegals(index):
	lastHint = nextHint = 0
	arrayIndexes = []
	# Horizontal
	for x in range(rows):
		for y in range(cols):		
			if isList(Kakuro[x][y]) and Kakuro[x][y][0]!=-1:
				nextHint = Kakuro[x][y][0]
			if Kakuro[x][y] > 0 and not isList(Kakuro[x][y]):
				arrayIndexes.append(Kakuro[x][y])
			if (Kakuro[x][y] == -1 or isList(Kakuro[x][y])) and lastHint != 0:					
				theBlock = []			
				for theIndex in arrayIndexes:
					theBlock.append(list(solutions[theIndex]))
				numOfPermutations = 1			
				for i in range(len(theBlock)):
					numOfPermutations = numOfPermutations * len(theBlock[i])
				print "Permutacion: ",PERMUTATION_RANGE_INCREMENT*index
				if numOfPermutations < PERMUTATION_RANGE_INCREMENT*index:
					mutations = permitation(theBlock)
					goodMutations = []
					for theMutation in mutations:
						print theMutation," Sum = ",sum(theMutation)," = ",lastHint
						if sum(theMutation) == lastHint:
							goodMutations.append(theMutation)
					if goodMutations == []:
						print "Tablero Inconsistente."
						print "bloque: %dx%d" %(x,y)
						sys.exit()
					for t in range(len(arrayIndexes)):
						theBlock = []				
						for s in range(len(goodMutations)):
							theBlock.append(goodMutations[s][t])
						solutions[arrayIndexes[t]] = set(theBlock)
				arrayIndexes = []
				lastHint = 0
			if nextHint:			
				lastHint = nextHint
				nextHint = 0
	# Vertical
	for y in range(cols):
		for x in range(rows):		
			if isList(Kakuro[x][y]) and Kakuro[x][y][1]!=-1:				
				nextHint = Kakuro[x][y][1]
			if Kakuro[x][y] > 0 and not isList(Kakuro[x][y]):
				arrayIndexes.append(Kakuro[x][y])
			if (Kakuro[x][y] == -1 or isList(Kakuro[x][y])) and lastHint != 0:					
				theBlock = []			
				for i in range(len(arrayIndexes)):
					theBlock.append(list(solutions[arrayIndexes[i]]))
				numOfPermutations = 1				
				for i in range(len(theBlock)):
					numOfPermutations = numOfPermutations * len(theBlock[i])
				if numOfPermutations < PERMUTATION_RANGE_INCREMENT*index:
					mutations = permitation(theBlock)
					goodMutations = []
					for theMutation in mutations:
						print theMutation," Sum = ",sum(theMutation)," = ",lastHint
						if sum(theMutation) == lastHint:
							goodMutations.append(theMutation)					
					if goodMutations == []:
						print "Tablero Inconsistente."
						print "bloque: %dx%d" %(x,y)
						print theBlock
						print lastHint
						print mutations
						sys.exit()
					for t in range(len(arrayIndexes)):
						theBlock = []				
						for s in range(len(goodMutations)):
							theBlock.append(goodMutations[s][t])
						solutions[arrayIndexes[t]] = set(theBlock)
				arrayIndexes = []
				lastHint = 0
			if nextHint:			
				lastHint = nextHint
				nextHint = 0

# Necesita ser documentado:
def removeDuplicates():
	lastHint = nextHint = 0
	arrayIndexes = []
	
	for x in range(rows):
		for y in range(cols):		
			if isList(Kakuro[x][y]) and Kakuro[x][y][0]!=-1:
				nextHint = Kakuro[x][y][0]
			if Kakuro[x][y] > 0 and not isList(Kakuro[x][y]):
				arrayIndexes.append(Kakuro[x][y])
			if (Kakuro[x][y] == -1 or isList(Kakuro[x][y])) and lastHint != 0:								
				for theIndex in arrayIndexes:			
					if len(solutions[theIndex])==1:
						for theOtherIndex in arrayIndexes:
							if theOtherIndex != theIndex:
								solutions[theOtherIndex] = solutions[theOtherIndex] - solutions[theIndex]
								
				lastHint = 0
				arrayIndexes = []
			if nextHint:			
				lastHint = nextHint
				nextHint = 0
	
	for y in range(cols):
		for x in range(rows):		
			if isList(Kakuro[x][y]) and Kakuro[x][y][1]!=-1:
				nextHint = Kakuro[x][y][1]
			if Kakuro[x][y] > 0 and not isList(Kakuro[x][y]):
				arrayIndexes.append(Kakuro[x][y])
			if (Kakuro[x][y] == -1 or isList(Kakuro[x][y])) and lastHint != 0:									
				for theIndex in arrayIndexes:			
					if len(solutions[theIndex])==1:
						for theOtherIndex in arrayIndexes:
							if theOtherIndex != theIndex:
								solutions[theOtherIndex] = solutions[theOtherIndex] - solutions[theIndex]
								
				lastHint = 0
				arrayIndexes = []
			if nextHint:			
				lastHint = nextHint
				nextHint = 0

# Retorna true si el kakuro fue resuelto satisfactoriamente
# false si no lo fue.
def isPuzzleSolved():
	for x in range(rows):
		for y in range(cols):		
			if Kakuro[x][y] > 0 and not isList(Kakuro[x][y]):
				if len(solutions[Kakuro[x][y]]) > 1:
					return 0
	for y in range(cols):
		for x in range(rows):		
			if Kakuro[x][y] > 0 and not isList(Kakuro[x][y]):
				if len(solutions[Kakuro[x][y]]) > 1:
					return 0
	return 1

# Esta funicon inicializa el diccionario de soluciones con todos los
# valores del dominio, osea de 1 a 9 (notese que NO SON los valores posibles)
# Teniendo en cuenta que solo son solucionables las "casillas" en donde 
# se ha marcado con 0
def initSolution():
	uniqueInt = 1
	for x in range(rows):
		for y in range(cols):
			if Kakuro[x][y] == 0:
				solutions[uniqueInt] = set([1,2,3,4,5,6,7,8,9])
				Kakuro[x][y] = uniqueInt
				uniqueInt = uniqueInt + 1

# Reduce el campo de busqueda de la solucion
# usando el diccionario de dominios que se encuentra en la
# libreria "domains.py" agregando ahora si solo los valores de solucion posibles.
def reduceScope(flag):
	lastHint = nextHint = 0
	arrayIndexes = []
	for x in range(rows):
		for y in range(cols):
			if isList(Kakuro[x][y]) and Kakuro[x][y][0] != -1:
				lastHint = Kakuro[x][y][0]
			elif not isList(Kakuro[x][y]) and Kakuro[x][y] != -1:
				arrayIndexes.append(Kakuro[x][y])
			elif Kakuro[x][y] == -1 or isList(Kakuro[x][y]) and lastHint:
				arity = len(arrayIndexes)
				for k in arrayIndexes:
					try:
						domine = domainsDict[(arity,lastHint)]
						if domine != 0:
							if(flag):
								solutions[k] = solutions[k] & set(domine)
							else:
								solutions[k] = set(domine)
					except KeyError:
						print 'No se encuentra solucion'
				arrayIndexes = []
				lastHint = 0

def reduceSearchSpace():
	reduceScope(0)
	reduceScope(1)


# Me dice si l es una lista, o no.
def isList(l):
	return hasattr(l, '__iter__') or (type(l) in (types.ListType, types.TupleType))



# Time to Resolve!! 
initSolution()
reduceSearchSpace()

puzzleSolved = 0
count = 0

while not puzzleSolved:
	removeIllegals(count*2)
	removeDuplicates()
	if isPuzzleSolved():
		puzzleSolved = 1
	count = count +1

if(puzzleSolved):
	print "\n\nKakuro solved! OHHH YEAH!! IN DA FACE!... See it:\n"
	print solutions
else:  
	print "No lo pude resolver y no tengo idea de porque. :("

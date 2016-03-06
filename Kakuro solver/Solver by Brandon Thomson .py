# Kakuro Solver -- Simple python solving engine for kakuro puzzles/cross sums
# Copyright (C) 2006 Brandon Thomson <gravix@gmail.com>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

import os, sys, types, time, copy
import pygame

PERMUTATION_THRESHOLD_INCREMENT = 40
WATCH_THE_LOGIC_MODE = False

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
puzzle2 = [\
[-1,-1,[-1,31],[-1,4],-1,[-1,23],[-1,4],-1,-1,[-1,19],[-1,5],-1,[-1,29],[-1,11]],\
[-1,[3,15],0,0,[12,3],0,0,[-1,34],[9,-1],0,0,[3,-1],0,0],\
[[31,-1],0,0,0,0,0,0,0,[13,4],0,0,[12,6],0,0],\
[[14,-1],0,0,[9,13],0,0,[9,14],0,0,0,[3,-1],0,0,-1],\
[-1,[15,-1],0,0,-1,[20,19],0,0,0,[-1,18],[11,8],0,0,[-1,13]],\
[-1,[8,8],0,0,[15,9],0,0,0,[12,12],0,0,[14,11],0,0],\
[[3,-1],0,0,[14,-1],0,0,[31,-1],0,0,0,0,0,0,0],\
[[10,-1],0,0,[11,-1],0,0,-1,[17,-1],0,0,[14,-1],0,0,-1]]

puzzle3 = [\
[-1,-1,[-1,40],[-1,16],-1,-1,[-1,44],[-1,3]],\
[-1,[13,30],0,0,[-1,4],[8,-1],0,0],\
[[19,-1],0,0,0,0,[4,3],0,0],\
[[16,-1],0,0,[12,-1],0,0,0,[-1,11]],\
[[12,-1],0,0,[-1,17],[8,-1],0,0,0],\
[[18,-1],0,0,0,[-1,16],[12,-1],0,0],\
[-1,[18,17],0,0,0,[6,16],0,0],\
[[15,-1],0,0,[23,-1],0,0,0,0],\
[[17,-1],0,0,-1,[16,-1],0,0,-1]]

puzzle4 = [\
[-1, [-1,16], [-1, 39], -1, [-1, 8], [-1,10], -1, [-1,41], [-1,11]],\
[[14,-1], 0, 0, [11,-1],0,0,[11,15],0,0],\
[[15,-1],0,0,[17,14],0,0,0,0,0],\
[-1, [11,4],0,0,[-1,6],[15,8],0,0,[-1,17]],\
[[15,-1],0,0,0,0,0,[15,16],0,0],\
[[8,-1],0,0,[35,9],0,0,0,0,0],\
[-1,[4,10],0,0,[-1,3],[17,6],0,0,[-1,11]] ,\
[[18,-1],0,0,0,0,0,[5,-1],0,0],\
[[16,-1],0,0,[3,-1],0,0,[14,-1],0,0],\
]

thePuzzle = kakuro2

solutionDict = {}
oldSolutionDict = {}

# This lookup table allows us to quickly eliminate many numbers
# in the game grid.
#
# Generating it does not take too long, but I think it is better
# to just save the data.
#
# The first number in the key is the number of boxes, the second
# is the hint. Zeros mean every digit is possible.
#
# BUG: this table is wrong. See value (3,24) for instance.
#
numberDict = {\
(2, 3) : [1, 2] ,\
(2, 4) : [1, 3] ,\
(2, 5) : [1, 2, 3, 4] ,\
(2, 6) : [1, 2, 4, 5] ,\
(2, 7) : [1, 2, 3, 4, 5, 6] ,\
(2, 8) : [1, 2, 3, 5, 6, 7] ,\
(2, 9) : [1, 2, 3, 4, 5, 6, 7, 8] ,\
(2, 10) : [1, 2, 3, 4, 6, 7, 8, 9] ,\
(2, 11) : [2, 3, 4, 5, 6, 7, 8, 9] ,\
(2, 12) : [3, 4, 5, 7, 8, 9] ,\
(2, 13) : [4, 5, 6, 7, 8, 9] ,\
(2, 14) : [5, 6, 8, 9] ,\
(2, 15) : [6, 7, 8, 9] ,\
(2, 16) : [7, 9] ,\
(2, 17) : [8, 9] ,\
(3, 6) : [1, 2, 3] ,\
(3, 7) : [1, 2, 4] ,\
(3, 8) : [1, 2, 3, 4, 5] ,\
(3, 9) : [1, 2, 3, 4, 5, 6] ,\
(3, 10) : [1, 2, 3, 4, 5, 6, 7] ,\
(3, 11) : [1, 2, 3, 4, 5, 6, 7, 8] ,\
(3, 12) : 0,\
(3, 13) : 0,\
(3, 14) : 0,\
(3, 15) : 0,\
(3, 16) : 0,\
(3, 17) : 0,\
(3, 18) : 0,\
(3, 19) : [2, 3, 4, 5, 6, 7, 8, 9] ,\
(3, 20) : [3, 4, 5, 6, 7, 8, 9] ,\
(3, 21) : [4, 5, 6, 7, 8, 9] ,\
(3, 22) : [5, 6, 7, 8, 9] ,\
(3, 23) : [6, 8, 9] ,\
(3, 24) : [7, 8, 9] ,\
(4, 10) : [1, 2, 3, 4] ,\
(4, 11) : [1, 2, 3, 5] ,\
(4, 12) : [1, 2, 3, 4, 5, 6] ,\
(4, 13) : [1, 2, 3, 4, 5, 6, 7] ,\
(4, 14) : [1, 2, 3, 4, 5, 6, 7, 8] ,\
(4, 15) : 0,\
(4, 16) : 0,\
(4, 17) : 0,\
(4, 18) : 0,\
(4, 19) : 0,\
(4, 20) : 0,\
(4, 21) : 0,\
(4, 22) : 0,\
(4, 23) : 0,\
(4, 24) : 0,\
(4, 25) : 0,\
(4, 26) : [2, 3, 4, 5, 6, 7, 8, 9] ,\
(4, 27) : [3, 4, 5, 6, 7, 8, 9] ,\
(4, 28) : [4, 5, 6, 7, 8, 9] ,\
(4, 29) : [5, 7, 8, 9] ,\
(4, 30) : [6, 7, 8, 9] ,\
(5, 15) : [1, 2, 3, 4, 5] ,\
(5, 16) : [1, 2, 3, 4, 6] ,\
(5, 17) : [1, 2, 3, 4, 5, 6, 7] ,\
(5, 18) : [1, 2, 3, 4, 5, 6, 7, 8] ,\
(5, 19) : 0,\
(5, 20) : 0,\
(5, 21) : 0,\
(5, 22) : 0,\
(5, 23) : 0,\
(5, 24) : 0,\
(5, 25) : 0,\
(5, 26) : 0,\
(5, 27) : 0,\
(5, 28) : 0,\
(5, 29) : 0,\
(5, 30) : 0,\
(5, 31) : 0,\
(5, 32) : [2, 3, 4, 5, 6, 7, 8, 9] ,\
(5, 33) : [3, 4, 5, 6, 7, 8, 9] ,\
(5, 34) : [4, 6, 7, 8, 9] ,\
(5, 35) : [5, 6, 7, 8, 9] ,\
(6, 21) : [1, 2, 3, 4, 5, 6] ,\
(6, 22) : [1, 2, 3, 4, 5, 7] ,\
(6, 23) : [1, 2, 3, 4, 5, 6, 7, 8] ,\
(6, 24) : 0,\
(6, 25) : 0,\
(6, 26) : 0,\
(6, 27) : 0,\
(6, 28) : 0,\
(6, 29) : 0,\
(6, 30) : 0,\
(6, 31) : 0,\
(6, 32) : 0,\
(6, 33) : 0,\
(6, 34) : 0,\
(6, 35) : 0,\
(6, 36) : 0,\
(6, 37) : [2, 3, 4, 5, 6, 7, 8, 9] ,\
(6, 38) : [3, 5, 6, 7, 8, 9] ,\
(6, 39) : [4, 5, 6, 7, 8, 9] ,\
(7, 28) : [1, 2, 3, 4, 5, 6, 7] ,\
(7, 29) : [1, 2, 3, 4, 5, 6, 8] ,\
(7, 30) : 0,\
(7, 31) : 0,\
(7, 32) : 0,\
(7, 33) : 0,\
(7, 34) : 0,\
(7, 35) : 0,\
(7, 36) : 0,\
(7, 37) : 0,\
(7, 38) : 0,\
(7, 39) : 0,\
(7, 40) : 0,\
(7, 41) : [2, 4, 5, 6, 7, 8, 9] ,\
(7, 42) : [3, 4, 5, 6, 7, 8, 9] ,\
(8, 36) : [1, 2, 3, 4, 5, 6, 7, 8] ,\
(8, 37) : [1, 2, 3, 4, 5, 6, 7, 9] ,\
(8, 38) : [1, 2, 3, 4, 5, 6, 8, 9] ,\
(8, 39) : [1, 2, 3, 4, 5, 7, 8, 9] ,\
(8, 40) : [1, 2, 3, 4, 6, 7, 8, 9] ,\
(8, 41) : [1, 2, 3, 5, 6, 7, 8, 9] ,\
(8, 42) : [1, 2, 4, 5, 6, 7, 8, 9] ,\
(8, 43) : [1, 3, 4, 5, 6, 7, 8, 9] ,\
(8, 44) : [2, 3, 4, 5, 6, 7, 8, 9] ,\
}


puzzleRows = len(thePuzzle)
puzzleCols = len(thePuzzle[0])

# Adjust this (and only this) to change the size of the window
# It can only be square for now (simplifies scaling the numbers) 
scalefactor = 65

height = puzzleRows * scalefactor
width = puzzleCols * scalefactor

# This function returns a rectangle for a particular cell on the game board.
def rectForXYcell(x,y):
	return pygame.Rect(width/puzzleCols*y,height/puzzleRows*x,width/puzzleCols+1,height/puzzleRows+1)

# This function determines all the possible combinations of the lists passed.
# For instance, if you pass [[2,4],[4,3]], this function would return
# [[2,7],[2,3],[4,7],[4,3].
#
# No duplicate numbers are allowed in the sets, so if you pass [[2,3],[2,4]]
# it will return [[2,4],[3,2],[3,4]]. The [2,2] item will be omitted.
#
# Is permutate even a word? Oops.
def permutate(array):	
	numOfPermutations = 1	
	for i in range(len(array)):
		numOfPermutations = numOfPermutations * len(array[i])
	theIndex = [0]*len(array)	
	theList = []	
	for x in range(numOfPermutations):
		subList = []		
		for i in range(len(array)):
			subList.append(array[i][theIndex[i]])
		if len(set(subList)) == len(subList):	
			theList.append(subList)
		for i in range(len(array)):
			theIndex[i] = theIndex[i] + 1
			if theIndex[i] != len(array[i]):
				break
			else:
				theIndex[i] = 0
	return theList

# This function waits for a keypress, and returns control
# to the parent function when one is received.
def waitForKeypress():
	while 1:
		event = pygame.event.wait()
		if event.type == pygame.QUIT: 
			sys.exit()
		if event.type == pygame.KEYDOWN:
			return


# This function iterates over the cells, checking permutations
# to find ones that add up to the hint. It then updates the
# solution matrix with the new data, eliminating any numbers
# that were in the solution matrix but weren't in any valid
# permutations. It is pretty slow.
#
# This function will need to be called multiple times
# before it will completely optimize the matrix.
#
# index should be a value indicating how many times this function
# has already run. The greater index is, the more tolerant this
# function will be of large permutations. By skipping these large
# permutations initially and focusing on the "easy" ones, we
# reduce the total amount of computation required to solve the puzzle.
#
# TODO: there is too much duplicate code in the "Horizontally" and
# "Vertically" sections. It should be fixed.
#
def removeIllegalValues(index):
	lastHint = nextHint = 0
	arrayIndexes = []
	# Horizontally
	statusBarMessage("Checking permutations by row. Ignoring rows > %d." % PERMUTATION_THRESHOLD_INCREMENT*index)
	for x in range(puzzleRows):
		for y in range(puzzleCols):		
			if isList(thePuzzle[x][y]) and thePuzzle[x][y][0]!=-1:
				nextHint = thePuzzle[x][y][0]
			if thePuzzle[x][y] > 0 and not isList(thePuzzle[x][y]):
				arrayIndexes.append(thePuzzle[x][y])
			if (thePuzzle[x][y] == -1 or isList(thePuzzle[x][y])) and lastHint != 0:					
				theBlock = []			
				for theIndex in arrayIndexes:
					theBlock.append(list(solutionDict[theIndex]))
				numOfPermutations = 1			
				for i in range(len(theBlock)):
					numOfPermutations = numOfPermutations * len(theBlock[i])
				if numOfPermutations < PERMUTATION_THRESHOLD_INCREMENT*index:
					mutations = permutate(theBlock)
					goodMutations = []
					for theMutation in mutations:
						if sum(theMutation) == lastHint:
							goodMutations.append(theMutation)
					if goodMutations == []:
						print "Puzzle Logically Inconsistent."
						print "block %dx%d" %(x,y)
						sys.exit()
					for t in range(len(arrayIndexes)):
						theBlock = []				
						for s in range(len(goodMutations)):
							theBlock.append(goodMutations[s][t])
						solutionDict[arrayIndexes[t]] = set(theBlock)
						if WATCH_THE_LOGIC_MODE:
							redrawAllWhiteBoxes() 
							waitForKeypress()
				arrayIndexes = []
				lastHint = 0
			if nextHint:			
				lastHint = nextHint
				nextHint = 0
	statusBarMessage("Checking permutations by column. Ignoring columns > %d." % PERMUTATION_THRESHOLD_INCREMENT*index)
	# Vertically
	for y in range(puzzleCols):
		for x in range(puzzleRows):		
			if isList(thePuzzle[x][y]) and thePuzzle[x][y][1]!=-1:				
				nextHint = thePuzzle[x][y][1]
			if thePuzzle[x][y] > 0 and not isList(thePuzzle[x][y]):
				arrayIndexes.append(thePuzzle[x][y])
			if (thePuzzle[x][y] == -1 or isList(thePuzzle[x][y])) and lastHint != 0:					
				theBlock = []			
				for i in range(len(arrayIndexes)):
					theBlock.append(list(solutionDict[arrayIndexes[i]]))
				numOfPermutations = 1				
				for i in range(len(theBlock)):
					numOfPermutations = numOfPermutations * len(theBlock[i])
				if numOfPermutations < PERMUTATION_THRESHOLD_INCREMENT*index:
					mutations = permutate(theBlock)
					goodMutations = []
					for theMutation in mutations:
						if sum(theMutation) == lastHint:
							goodMutations.append(theMutation)					
					if goodMutations == []:
						print "Puzzle Logically Inconsistent."
						print "block %dx%d" %(x,y)
						print theBlock
						print lastHint
						print mutations
						sys.exit()
					for t in range(len(arrayIndexes)):
						theBlock = []				
						for s in range(len(goodMutations)):
							theBlock.append(goodMutations[s][t])
						solutionDict[arrayIndexes[t]] = set(theBlock)
						if WATCH_THE_LOGIC_MODE:
							redrawAllWhiteBoxes() 
							waitForKeypress()
				arrayIndexes = []
				lastHint = 0
			if nextHint:			
				lastHint = nextHint
				nextHint = 0

# If any squares on the board have been solved, that is, reduced
# to one possible answer, then that answer can be removed as a
# possibility from all other cells in line with that cell. That
# is exactly what this function does.
#
# This function may create additional cells that only have one
# entry, so it should be run multiple times to ensure the
# board is fully optimized.
#
# TODO: there is too much duplicate code in the "Horizontally" and
# "Vertically" sections. It should be fixed.
#
# TODO: Detection of whether this function needs to be executed
# should be added to the other elimination functions
#
def removeDuplicateValues():
	lastHint = nextHint = 0
	arrayIndexes = []
	# Horizontally
	statusBarMessage("Removing duplicate values by row.")
	for x in range(puzzleRows):
		for y in range(puzzleCols):		
			if isList(thePuzzle[x][y]) and thePuzzle[x][y][0]!=-1:
				nextHint = thePuzzle[x][y][0]
			if thePuzzle[x][y] > 0 and not isList(thePuzzle[x][y]):
				arrayIndexes.append(thePuzzle[x][y])
			if (thePuzzle[x][y] == -1 or isList(thePuzzle[x][y])) and lastHint != 0:								
				for theIndex in arrayIndexes:			
					if len(solutionDict[theIndex])==1:
						for theOtherIndex in arrayIndexes:
							if theOtherIndex != theIndex:
								solutionDict[theOtherIndex] = solutionDict[theOtherIndex] - solutionDict[theIndex]
								if WATCH_THE_LOGIC_MODE:
									redrawAllWhiteBoxes() 
									waitForKeypress()
				lastHint = 0
				arrayIndexes = []
			if nextHint:			
				lastHint = nextHint
				nextHint = 0
	# Vertically
	statusBarMessage("Removing duplicate values by column.")
	for y in range(puzzleCols):
		for x in range(puzzleRows):		
			if isList(thePuzzle[x][y]) and thePuzzle[x][y][1]!=-1:
				nextHint = thePuzzle[x][y][1]
			if thePuzzle[x][y] > 0 and not isList(thePuzzle[x][y]):
				arrayIndexes.append(thePuzzle[x][y])
			if (thePuzzle[x][y] == -1 or isList(thePuzzle[x][y])) and lastHint != 0:									
				for theIndex in arrayIndexes:			
					if len(solutionDict[theIndex])==1:
						for theOtherIndex in arrayIndexes:
							if theOtherIndex != theIndex:
								solutionDict[theOtherIndex] = solutionDict[theOtherIndex] - solutionDict[theIndex]
								if WATCH_THE_LOGIC_MODE:
									redrawAllWhiteBoxes() 
									waitForKeypress()
				lastHint = 0
				arrayIndexes = []
			if nextHint:			
				lastHint = nextHint
				nextHint = 0

# This function returns true if the puzzle has been solved,
# false if it hasn't been.
#
# TODO: there is too much duplicate code in the "Horizontally" and
# "Vertically" sections. It should be fixed.
#
def isPuzzleSolved():
	# Horizontally
	for x in range(puzzleRows):
		for y in range(puzzleCols):		
			if thePuzzle[x][y] > 0 and not isList(thePuzzle[x][y]):
				if len(solutionDict[thePuzzle[x][y]]) > 1:
					return 0
	# Vertically
	for y in range(puzzleCols):
		for x in range(puzzleRows):		
			if thePuzzle[x][y] > 0 and not isList(thePuzzle[x][y]):
				if len(solutionDict[thePuzzle[x][y]]) > 1:
					return 0
	return 1

# This function initializes the elimination solution dictionary with
# the default values, that is, 1 through 9 for every square. It also
# replaces the zeros in the puzzle matrix with unique values for
# easy dictionary lookup.
#
# TODO: there is too much duplicate code in the "Horizontally" and
# "Vertically" sections. It should be fixed.
#
def initSolutionDict():
	uniqueInt = 1
	for x in range(puzzleRows):
		for y in range(puzzleCols):
			if thePuzzle[x][y] == 0:
				solutionDict[uniqueInt] = set([1,2,3,4,5,6,7,8,9])
				thePuzzle[x][y] = uniqueInt
				uniqueInt = uniqueInt + 1

# This function reduces the search space of the solution set by
# using the predefined lookup table at the top of the page.
# It is quick and effective, but probably less useful on
# puzzles of the "hard" type.
#
# There is no need to run this function more than once.
#
# TODO: there is too much duplicate code in the "Horizontally" and
# "Vertically" sections. It should be fixed.
#
def reduceSearchSpace():
	lastHint = nextHint = 0
	arrayIndexes = []
	statusBarMessage("Reducing row search space using table lookup.")
	#Horizontally
	for x in range(puzzleRows):
		for y in range(puzzleCols):
			if isList(thePuzzle[x][y]) and thePuzzle[x][y][0]!=-1:
				nextHint = thePuzzle[x][y][0]
			if thePuzzle[x][y] > 0 and not isList(thePuzzle[x][y]):
				arrayIndexes.append(thePuzzle[x][y])
			if (thePuzzle[x][y] == -1 or isList(thePuzzle[x][y])) and lastHint != 0:		
				for z in arrayIndexes:
					try:				
						entry = numberDict[(len(arrayIndexes),lastHint)]
						if entry != 0:
							solutionDict[z] = set(entry)
							if WATCH_THE_LOGIC_MODE:
								redrawAllWhiteBoxes() 
								waitForKeypress()
					except KeyError:
						print 'KeyError (puzzle inconsistent)'
				arrayIndexes = []
				lastHint = 0
			if nextHint:			
				lastHint = nextHint
				nextHint = 0
	# Vertically
	statusBarMessage("Reducing column search space using table lookup.")
	for y in range(puzzleCols):
		for x in range(puzzleRows):
			if isList(thePuzzle[x][y]) and thePuzzle[x][y][1]!=-1:
				nextHint = thePuzzle[x][y][1]
			if thePuzzle[x][y] > 0 and not isList(thePuzzle[x][y]):
				arrayIndexes.append(thePuzzle[x][y])
			if (thePuzzle[x][y] == -1 or isList(thePuzzle[x][y])) and lastHint != 0:		
				for z in arrayIndexes:
					try:
						entry = numberDict[(len(arrayIndexes),lastHint)]
						if entry != 0:			
							solutionDict[z] = solutionDict[z] & set(entry)
							if WATCH_THE_LOGIC_MODE:
								redrawAllWhiteBoxes() 
								waitForKeypress()
					except KeyError:
						print 'KeyError (puzzle inconsistent)'			
				arrayIndexes = []
				lastHint = 0
			if nextHint:			
				lastHint = nextHint
				nextHint = 0

# This function redraws the white box at the index x,y and the
# interior matrix
def redrawWhiteBox(x,y):
	# Necessary?	
	screen.fill([255,255,255],rectForXYcell(x,y))
	pygame.draw.rect(screen,[0,0,0],rectForXYcell(x,y),1)	
		
	try:	
		possibleSolutions = solutionDict[thePuzzle[x][y]]
		if len(possibleSolutions) == 1:
			# Can't think of a better way to do this =/			
			theDigit = possibleSolutions.pop()
			possibleSolutions.add(theDigit)
			therender = bigfont.render("%d" %theDigit,1,[0,0,255])
			screen.blit(therender,[width/puzzleCols*(y+0.5)-therender.get_width()/2,height/puzzleRows*(x+0.5)-therender.get_height()/2])
			return
		else:
			if(1 in possibleSolutions):
				string1 = "1 "
			else:
				string1 = "  "
			if(2 in possibleSolutions):
				string1 = string1 + "2 "
			else:
				string1 = string1 + "  "
			if(3 in possibleSolutions):
				string1 = string1 + "3"
			else:
				string1 = string1 + " "
			if(4 in possibleSolutions):
				string2 = "4 "
			else:
				string2 = "  "
			if(5 in possibleSolutions):
				string2 = string2 + "5 "
			else:
				string2 = string2 + "  "
			if(6 in possibleSolutions):
				string2 = string2 + "6"
			else:
				string2 = string2 + " "
			if(7 in possibleSolutions):
				string3 = "7 "
			else:
				string3 = "  "
			if(8 in possibleSolutions):
				string3 = string3 + "8 "
			else:
				string3 = string3 + "  "
			if(9 in possibleSolutions):
				string3 = string3 + "9"
			else:
				string3 = string3 + " "
	except KeyError:
		string1 = "1 2 3"
		string2 = "4 5 6"
		string3 = "7 8 9"		
		
	therender = monofont.render(string1,1,[0,128,0])
	screen.blit(therender,[width/puzzleCols*(y+0.5)-therender.get_width()/2,height/puzzleRows*(x+0.2)-therender.get_height()/2])
	therender = monofont.render(string2,1,[0,128,0])
	screen.blit(therender,[width/puzzleCols*(y+0.5)-therender.get_width()/2,height/puzzleRows*(x+0.5)-therender.get_height()/2])
	therender = monofont.render(string3,1,[0,128,0])
	screen.blit(therender,[width/puzzleCols*(y+0.5)-therender.get_width()/2,height/puzzleRows*(x+0.8)-therender.get_height()/2])

# This function redraws all the white boxes and the interior matricies.
# It also flips the double-buffered display surface.
def redrawAllWhiteBoxes():
	for x in range(puzzleRows):
		for y in range(puzzleCols):
			if thePuzzle[x][y] > 0 and not isList(thePuzzle[x][y]):		
				redrawWhiteBox(x,y)				
				try:
					if oldSolutionDict[thePuzzle[x][y]] != solutionDict[thePuzzle[x][y]]:
						pygame.draw.rect(screen,[255,0,0],rectForXYcell(x,y).inflate(-4,-4),3)
				except KeyError:
					None
	
	# Save the list for comparing to next time
	oldSolutionDict.update(solutionDict)
	pygame.display.flip()
	
def isList(l):
	"""Convenience method that works with all 2.x versions of Python
	to determine whether or not something is listlike."""
	return hasattr(l, '__iter__') \
		or (type(l) in (types.ListType, types.TupleType))

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

# This function prints a string to our status bar
def statusBarMessage(theMessage):
	screen.fill([0,0,0],pygame.Rect(0,height,width,30))
	therender = statusfont.render(theMessage,1,[255,255,255],[0,0,0])
	screen.blit(therender,[width/2-therender.get_width()/2,height+15-therender.get_height()/2])
	
pygame.init()
screen = pygame.display.set_mode([width+1,height+30])
thefont = pygame.font.Font(pygame.font.get_default_font(),scalefactor/3)
monofont = pygame.font.Font(pygame.font.match_font('Courier','Courier New','Monospaced'),scalefactor/3)
bigfont = pygame.font.Font(pygame.font.get_default_font(),scalefactor/1)
statusfont = pygame.font.Font(pygame.font.get_default_font(),16)

if monofont == None:
	print "No monospaced font could be found!"

# Draw The Board
for x in range(puzzleRows):
	for y in range(puzzleCols):
		# Black Box		
		if thePuzzle[x][y] == -1:
			screen.fill([0,0,0],rectForXYcell(x,y))
			pygame.draw.rect(screen,[255,255,255],rectForXYcell(x,y),1)
		# Black Box With Stripe and numbers
		elif isList(thePuzzle[x][y]):
			screen.fill([0,0,0],rectForXYcell(x,y))
			pygame.draw.rect(screen,[255,255,255],rectForXYcell(x,y),1)
			pygame.draw.line(screen, [255,255,255], [width/puzzleCols*y,height/puzzleRows*x], [width/puzzleCols*(y+1),height/puzzleRows*(x+1)], 1)
			if thePuzzle[x][y][0] != -1: 			
				therender = thefont.render("%d" %thePuzzle[x][y][0],1,[255,255,255],[0,0,0])
				screen.blit(therender,[width/puzzleCols*(y+0.75)-therender.get_width()/2,height/puzzleRows*(x+0.30)-therender.get_height()/2])
			if thePuzzle[x][y][1] != -1:			
				therender = thefont.render("%d" %thePuzzle[x][y][1],1,[255,255,255],[0,0,0])
				screen.blit(therender,[width/puzzleCols*(y+0.25)-therender.get_width()/2,height/puzzleRows*(x+0.75)-therender.get_height()/2])
		# White Box		
		else:
			redrawWhiteBox(x,y)		
			
pygame.display.flip()
waitForKeypress()

# Solve the Board
startTime = time.clock()
initSolutionDict()
reduceSearchSpace()

duration = time.clock() - startTime
grandStartTime = startTime
print "Search space reduction completed in %.2f seconds." %duration
puzzleSolved = 0
for count in range(100):
	for i in range(2):
		startTime = time.clock()
		removeIllegalValues(count*2-1+i)
		duration = time.clock() - startTime
		print "Illegal value iteration completed in %.2f seconds." %duration
	for i in range(2):
		startTime = time.clock()		
		removeDuplicateValues()
		duration = time.clock() - startTime
		print "Duplicate value iteration completed in %.2f seconds." %duration
	if isPuzzleSolved():
		puzzleSolved = 1
		break
duration = time.clock() - grandStartTime
if(puzzleSolved):
	print "Puzzle solved in %.3f seconds." %duration
else:  
	print "I couldn't solve this puzzle, but I tried for %.3f seconds." %duration 

redrawAllWhiteBoxes()                                      
# Beginning of Event Loop                                                                                                                  for i in range(len(a)):
while 1:
	event = pygame.event.wait()
	if event.type == pygame.QUIT: 
		sys.exit()
	if event.type == 1:
		None
	


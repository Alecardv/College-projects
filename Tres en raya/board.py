from graphics import*


class Tabla:
	win = ""
	dimension= ""

	def __init__(self, dimension):
		self.dimension= dimension
		self.win= GraphWin("Ta-Te-Ti", dimension, dimension)

		line1= Line(Point(dimension/3,0), Point(dimension/3,dimension))
		line1.draw(self.win)
		line2= Line(Point(2*dimension/3,0), Point(2*dimension/3,dimension))
		line2.draw(self.win)
		line3= Line(Point(0,dimension/3), Point(dimension, dimension/3))
		line3.draw(self.win)
		line4= Line(Point(0,2*dimension/3), Point(dimension, 2*dimension/3))
		line4.draw(self.win)

	def getMouse(self):
		self.win.getMouse() # Pause to view result

	def close(self):
		self.win.close()    # Close window when done

class Cell:
	pass

class Game:
	pass
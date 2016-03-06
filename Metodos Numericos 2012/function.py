from math import *
from sympy import *
from sympy.parsing.sympy_parser import *


class Function:
	
	def __init__(self,f,variables):##recibe la funcion y la lista de variables independientes
		self.variables = []#lista de variables independiente
		self.list_of_symbols = {}#diccionario para simbolizar las variables independientes
		self.f = parse_expr(f) if f.__class__ == ''.__class__ else f ## nuestra funcion
		self.createSymbols(variables)

	def createSymbols(self,var):
			self.list_of_symbols[var] = symbols(var)## crea un nuevo simbolo para la variable var
			self.variables = var

	def getDerivate(self,order = 1):##recibe la variable a derivar
		return Function(diff(self.f,self.list_of_symbols[self.variables],order),self.variables)#crea una nueva funcio a partir de la derivada del orden n-simo respecto a una variable

	def getIntegral(self):## recibe la variable a integrar
		return Function(integrate(self.f,self.list_of_symbols[self.variables]),self.variables)#crea una nueva funcion a partir de la integral respecto a una variable

	def printFunction(self):## permite ver mi funcion
		print self.f

	def getFunction(self):## devuelve la funcion f:Function
		return self.f

	def getAndEvalIntegral(self,interval):#recibe la variable a integrar y el intervalo a evaluar
		return integrate(self.f,(self.list_of_symbols[self.variables],interval[0],interval[1])).doit().evalf()## integra la funcion respecto a una variable y la evalua en el intervalo a,b

	def evalFunction(self,val):## evalua la funcion en un punto, recibe la lista de valores a evaluar respecto a la lista de variables a asignar
		g = self.f
		g = g.subs(self.list_of_symbols[self.variables],val)
		return g.evalf()*1.0
import function
from matplotlib.pyplot import *
from pylab import *
import numpy as np
import math

class NewtonRaphson:
	def __init__(self, fun, xi, error):
		self.fun = function.Function(fun,'x')
		self.dfun = self.fun.getDerivate()
		self.xi = xi
		self.error = error
		self.m = []
		self.x = []
		self.fig, self.ax = subplots()
	
	def relativeError(self):
		if(len(self.x) > 1):
			i = len(self.x)-1;
			e = ((self.x[i]-self.x[i-1])/self.x[i])*100.0
			return abs(e)
		return 100

	def graph(self):
		figure()
		root = self.method(self.xi)
		print 'Raiz = ',root
		Ox = np.arange(self.xi-10,root+10, 0.02)
		#Coordenadas para y:
		Oy = []
		for i in Ox:
			Oy.append( self.fun.evalFunction(i) )
		self.ax.plot(Ox, Oy)
		self.ax.plot([root],[self.m[len(self.m)-1]],'ro')
		show()

	def method(self,xi):
		self.x.append(xi)
		Ea = 100
		i = 0
		while  Ea >= self.error:

			m = self.dfun.evalFunction(self.x[i])
			self.m.append(self.fun.evalFunction(self.x[i]))
			self.x.append(self.x[i]-self.fun.evalFunction(self.x[i])/m)
			print 'Valor = ',self.x[i]
			x = np.arange(self.x[i]-5,self.x[i+1]+5)
			y = []
			for j in x:
				y.append(m*(j - self.x[i])+self.fun.evalFunction(self.x[i]))
			self.ax.plot(x,y,'-')
			self.ax.plot([self.x[i+1]],[0],'g*')
			Ea = self.relativeError()
			i = i + 1
		return self.x[i-1];

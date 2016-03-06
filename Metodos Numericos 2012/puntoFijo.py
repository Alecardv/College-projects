import function
from matplotlib.pyplot import *
from pylab import *
import numpy as np
import math

class PuntoFijo:
	def __init__(self, fun, gun,xi, error):
		self.fun = function.Function(fun,'x')
		self.gun = function.Function(gun,'x')
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
		root = self.method()
		print 'Raiz = ',root
		Ox = np.arange(self.xi-10,root+10, 0.02)
		Oy = []
		for i in Ox:
			Oy.append( self.fun.evalFunction(i) )
		self.ax.plot(Ox, Oy)
		self.ax.plot([root],[self.fun.evalFunction(root)],'ro')
		show()

	def method(self):
		self.x.append(self.xi)
		Ea = 100
		i = 0
		while  Ea >= self.error:
			self.x.append(self.gun.evalFunction(self.x[i]))
			print 'Valor = ',self.x[i]
			self.ax.plot([self.x[i]],[0],'rx')
			Ea = self.relativeError()
			i = i + 1
		return self.x[i-1];
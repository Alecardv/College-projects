import function
from matplotlib.pyplot import *
from pylab import *
import numpy as np
import math

class Bisection:
	def __init__(self, fun, xi, xf, error):
		self.fun = function.Function(fun,'x')
		self.xi = xi
		self.xf = xf
		self.error = error
		self.m = []
		self.fig, self.ax = subplots()
	
	def relativeError(self):
		if(len(self.m) > 1):
			i = len(self.m)-1;
			e = ((self.m[i]-self.m[i-1])/self.m[i])*100.0
			return abs(e)
		return 100

	def graph(self):
		figure()
		root = self.method(self.xi,self.xf,linspace(self.xi,self.xf, 0.02))
		print 'Raiz = ',root
		Ox = np.arange(self.xi-5,self.xf+5, 0.02)
		#Coordenadas para y:
		Oy = []
		for i in Ox:
			Oy.append( self.fun.evalFunction(i) )
		self.ax.plot(Ox, Oy)
		self.ax.plot([root],[self.fun.evalFunction(root)],'ro')
		show()

	def method(self,xi,xf,x):
		if self.fun.evalFunction(xi)*self.fun.evalFunction(xf) < 0.0 :
			m = (xi+xf)/2.0
			self.m.append(self.fun.evalFunction(m))
			self.ax.vlines(xi,0,self.fun.evalFunction(xi))
			self.ax.vlines(m,0,self.fun.evalFunction(m))
			self.ax.vlines(xf,0,self.fun.evalFunction(xf))
			print 'Valor = ',self.fun.evalFunction(m)
			if(self.relativeError() <= self.error or abs(self.fun.evalFunction(m)) <= 1e-8):
				return m
			elif self.fun.evalFunction(xi)*self.fun.evalFunction(m) < 0.0:
				return self.method(xi,m,x)
			elif self.fun.evalFunction(xf)*self.fun.evalFunction(m) < 0.0:
				return self.method(m,xf,x)

import function
from matplotlib.pyplot import *
from pylab import *
import numpy as np
import math

class Trapecio:
	def __init__(self, fun, xi, xf):
		self.fun = function.Function(fun,'x')
		self.a,self.b = xi,xf
		self.fig, self.ax = subplots()
	
	def relativeError(self):
		f = self.fun.getDerivate()
		Ea = ((self.b-self.a)**3/12)*((f.evalFunction(self.b) - f.evalFunction(self.a))/(self.b-self.a))
		return Ea

	def graph(self):
		figure()
		root = self.method()
		print 'AreaAprox = ',root
		print 'AreaReal = ',self.fun.getAndEvalIntegral([self.a,self.b])
		print 'Error = ',self.relativeError()
		Ox = np.arange(self.a-5,self.b+5, 0.02)
		Oy = []
		for i in Ox:
		    Oy.append( self.fun.evalFunction(i) )
		self.ax.plot(Ox, Oy, color = "blue",lw = 1,label="f(x)")
		self.ax.legend(loc=2)
		show()

	def px(self,x):
		return (self.fun.evalFunction(self.b)-self.fun.evalFunction(self.a))/(self.b-self.a)*(x-self.a) + self.fun.evalFunction(self.a)
	
	def method(self):
		I = (self.b-self.a)*((self.fun.evalFunction(self.a) + self.fun.evalFunction(self.b))/2)
		self.ax.vlines(self.a,0,self.fun.evalFunction(self.a))
		self.ax.vlines(self.b,0,self.fun.evalFunction(self.b))
		Ox = np.arange(self.a,self.b, 0.02)
		Oy = []
		for i in Ox:
			Oy.append(self.px(i))
		self.ax.plot(Ox, Oy,lw = 2)
		return I

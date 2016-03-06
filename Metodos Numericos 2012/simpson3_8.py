import function
from matplotlib.pyplot import *
from pylab import *
import numpy as np
import math

class Simpson38:
	def __init__(self, fun, xi, xf):
		self.fun = function.Function(fun,'x')
		self.a,self.b = xi,xf
		self.fig, self.ax = subplots()
	
	def relativeError(self):
		f = self.fun.getDerivate(3)
		Ea = ((self.b-self.a)**5/6480)*((self.fun.evalFunction(self.b) - self.fun.evalFunction(self.a))/(self.b-self.a))
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

	def px(self,x,xi):
		h = (self.b - self.a)/2.0;
		return (self.fun.evalFunction(self.a)*(x-xi)*(x-self.b)/2-self.fun.evalFunction(xi)*(x-self.a)*(x-self.b) + self.fun.evalFunction(self.b)*(x-self.a)*(x-xi)/2)/h**2
	
	def method(self):
		xi = (2*self.a+self.b)/3
		xj = (self.a+2*self.b)/3
		I = (self.b-self.a)*((self.fun.evalFunction(self.a) + 3*self.fun.evalFunction(xi) + 3*self.fun.evalFunction(xj) + self.fun.evalFunction(self.b))/8)
		return I;

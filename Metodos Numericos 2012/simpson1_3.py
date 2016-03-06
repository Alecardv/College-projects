import function
from matplotlib.pyplot import *
from pylab import *
import numpy as np
import math

class Simpson13:
	def __init__(self, fun, xi, xf):
		self.fun = function.Function(fun,'x')
		self.a,self.b = xi,xf
		self.fig, self.ax = subplots()
	
	def relativeError(self):
		f = self.fun.getDerivate(3)
		Ea = ((self.b-self.a)**5.0/2880.0)*((f.evalFunction(self.b) - f.evalFunction(self.a))/(self.b-self.a))
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
		xi = self.a + ((self.b-self.a)/2.0)
		I =(self.b-self.a)*((self.fun.evalFunction(self.a) + 4.0*(self.fun.evalFunction(xi)) + self.fun.evalFunction(self.b))/6.0)
		Ox = np.arange(self.a,self.b, 0.02)
		Oy = []
		for i in Ox:
			Oy.append(self.px(i,xi))
		self.ax.plot(Ox, Oy,color = "red",lw = 2)
		return I;

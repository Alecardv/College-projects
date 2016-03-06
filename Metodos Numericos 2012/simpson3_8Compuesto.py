import function
from matplotlib.pyplot import *
from pylab import *
import numpy as np
import math

class Simpson38Comp:
	def __init__(self, fun, xi, xf,n):
		self.fun = function.Function(fun,'x')
		self.a,self.b = xi,xf
		self.n = n
		self.fig, self.ax = subplots()

	def relativeError(self):
		f = self.fun.getDerivate(3)
		Ea = ((self.b-self.a)**5/6480*self.n)*((f.evalFunction(self.b) - f.evalFunction(self.a))/(self.b-self.a))
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
	def px(self,x,a,xi,b):
		h = (b - a)/self.n;
		return (self.fun.evalFunction(a)*(x-xi)*(x-b)/2-self.fun.evalFunction(xi)*(x-a)*(x-b) + self.fun.evalFunction(b)*(x-a)*(x-xi)/2)/h**2
	def method(self):
		Sum1=0
		Sum2=0
		xi=0
		h=float(self.b-self.a)/self.n
		i=1
		
		while i<self.n:
			if i%3 == 0:
				xi = self.a+i*h
				Sum1 = Sum1 + self.fun.evalFunction(xi)
			else:
				xi = self.a+i*h
				Sum2 = Sum2 + self.fun.evalFunction(xi)
			i=i+1
		I = ((3*h)/8.0)*(self.fun.evalFunction(self.a) + 2*Sum1 + 3*Sum2 + self.fun.evalFunction(self.b))
		return I;

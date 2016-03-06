import function
from matplotlib.pyplot import *
from pylab import *
import numpy as np
import math

class Simpson13Comp:
	def __init__(self, fun, xi, xf,n):
		self.fun = function.Function(fun,'x')
		self.a,self.b = xi,xf
		self.n = n
		self.fig, self.ax = subplots()
	
	def relativeError(self):
		f = self.fun.getDerivate(3)
		Ea = ((self.b-self.a)**5/180*self.n**4)*((f.evalFunction(self.b) - f.evalFunction(self.a))/(self.b-self.a))
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
		xi = 0
		i = 1
		dx = float(self.b-self.a)/self.n
		while i <=self.n-1:
			xi=self.a+i*(dx)
			Sum1 = Sum1 + self.fun.evalFunction(xi)
			Ox = np.arange(self.a+(i-1)*dx,xi+dx, 0.02)
			Oy = []
			for j in Ox:
				Oy.append(self.px(j,self.a+(i-1)*dx,xi,xi+dx))
			self.ax.plot(Ox, Oy,color = "red",lw = 2)
			i=i+2

		i = 2
		while i <=self.n-2:
			xi=self.a+i*(dx)
			Sum2 = Sum2 + self.fun.evalFunction(xi)
			Ox = np.arange(self.a+(i-1)*dx,xi+dx, 0.02)
			Oy = []
			for j in Ox:
				Oy.append(self.px(j,self.a+(i-1)*dx,xi,xi+dx))
			self.ax.plot(Ox, Oy,color = "green",lw = 2)
			i=i+2
		I=(self.b-self.a)*((self.fun.evalFunction(self.a) + 4*Sum1 + 2*Sum2 + self.fun.evalFunction(self.b))/3*self.n)
		
		return I;

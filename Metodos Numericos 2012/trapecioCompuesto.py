import function
from matplotlib.pyplot import *
from pylab import *
import numpy as np
import math

class TrapecioComp:
	def __init__(self, fun, xi, xf,n):
		self.fun = function.Function(fun,'x')
		self.a,self.b = xi,xf
		self.n = n
		self.fig, self.ax = subplots()

	def relativeError(self):
		f = self.fun.getDerivate(2)
		Ea = ((self.b-self.a)**3/12*self.n**2)*((f.evalFunction(self.b) - f.evalFunction(self.a))/(self.b-self.a))
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

	def px(self,a,b,x):
		return ((self.fun.evalFunction(b)-self.fun.evalFunction(a))/(b-a))*(x-a) + self.fun.evalFunction(a)

	def method(self):
		i=0
		S = 0
		dx = (self.b-self.a)/self.n;
		for i in range(1,(int(self.n))):
			xi = float(self.a+i*dx)
			S = 2*(self.fun.evalFunction(xi)) + S
			self.ax.vlines(self.a+(i-1)*dx,0,self.fun.evalFunction(self.a+(i-1)*dx))
			self.ax.vlines(xi+dx,0,self.fun.evalFunction(xi+dx))
			Ox = np.arange(self.a+(i-1)*dx,xi+dx, 0.02)
			Oy = []
			for i in Ox:
				Oy.append(self.px(self.a+(i-1)*dx,xi+dx,i))
			self.ax.plot(Ox, Oy,lw = 2)

		I = (self.b-self.a)*((self.fun.evalFunction(self.a) + self.fun.evalFunction(self.b) + S )/(2*self.n))
		return I

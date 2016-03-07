## Desarrollado por: Jose Alejandro Cardona V.

from __future__ import division #para dividir normalmente
from sympy import sympify, init_printing, solve, Eq, simplify, lambdify #Algebra
import numpy as np #Matematicas
import matplotlib.pyplot as plt #Graficos

init_printing(use_unicode=True)

class InterNewton(object):

    def __init__(self, entrada):
        self.a = self.verificarEntrada(entrada)
        self.p = sympify(self.crearEcuacion(self.a))
        self.reemplazar()
        self.vars = self.encontrarVars()
        self.polinomio = self.encontrarPol()

    def crearEcuacion(self, a):
        ec = 'b0'
        for i in range(1, len(a)):
            ec += ' + b' + str(i)
            for j in range(i):
                ec += '*(x-x' + str(j) + ')'
        return ec

    def verificarEntrada(self, p):
        p = p.replace('),', ';')
        p = p.replace('(', '')
        p = p.replace(')', '')
        p = p.split(';')
        p = [ (int(i.split(',')[0]), int(i.split(',')[1])) for i in p ]
        return p

    def reemplazar(self):
        for i in range(len(self.a)):
            self.p = self.p.subs('x'+str(i), self.a[i][0])

    def encontrarVars(self):
        aux = {}; temp = self.p
        for i in range(len(self.a)):
            if i == 0:
                aux['b0'] = self.p.subs( [ ('x', self.a[0][0]), ('b0', self.a[0][1]) ] )
            else:
                temp = temp.subs('b'+str(i-1), aux['b'+str(i-1)])
                aux['b'+str(i)] = solve(Eq(temp.subs('x', self.a[i][0]), self.a[i][1]))[0] 
        return aux

    def encontrarPol(self):
        temp = self.p.subs(self.vars)
        return simplify(temp)

    def graficar(self):
        #plt.ion()
        x = np.linspace(-10,10)
        f = lambdify('x', self.polinomio, "math")
        plt.plot(x, f(x), linewidth=2.5, linestyle="-")
        plt.plot([i[0] for i in self.a], [i[1] for i in self.a], 'or')
        plt.ylim(-100,100)
        plt.grid(True)
        plt.show()

#test = InterNewton('(1,0),(0,1),(2,3),(-1,-2)')
#print test.polinomio
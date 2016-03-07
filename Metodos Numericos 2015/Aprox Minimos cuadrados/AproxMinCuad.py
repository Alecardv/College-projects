## Desarrollado por: Jose Alejandro Cardona V.
## Metodos Numericos: Aproximacion por minimos cuadrados

import numpy as np
import matplotlib.pyplot as plt

class AproxLineal:
    def __init__(self, usrInput):
    ## Se espera una entrada como la siguiente:
    ## (1,2), (1,-2), (-1,2), (-1,-2)
    ## cualquier otro tipo de entrada devolvera error
        self.x = np.matrix(self.buildInput(usrInput)) #Una matriz con todos los puntos
        self.A = np.insert(np.matrix(self.x[:,0]), [0], 1, axis=1) #La matriz A
        self.Y = np.matrix(self.x[:,1]) #La matriz Y
        self.At = self.A.transpose() # A transpuesta
        self.InvATA = np.linalg.inv(self.At*self.A) #La inversa de A transpuesta por A
        self.Result = (self.InvATA*self.At)*self.Y
        self.data_x = [i.item() for i in self.x[:,0]] #Una lista con las coordenadas x (usada para dibujar los puntos)
        self.data_y = [j.item() for j in self.x[:,1]] #Una lista con las corrdenadas y (usada para dibujar los puntos)

    def plot(self):
        plt.ion() #Habilita el modo interactivo
        x = np.linspace(-5,5) #El rango
        y = self.Result.item(0) + self.Result.item(1)*x #La funcion
        plt.plot(x, y, linewidth=2.5, linestyle="-") #Dibujar el grafico
        plt.plot(self.data_x, self.data_y, 'or') #Dibujar los puntos
        plt.grid(True) #Mostrar cuadricula
        plt.draw() #Actualizar los cambios al grafico

    def buildInput(self, points):
        points = points.strip() #Borra espacios al principio y final
        points = points[0:len(points)-1] #Borra el ultimo parentesis
        points = points.replace('),', ';') #Reemplaza '),' con ';'
        points = points.replace('(', '') #Borra '('
        return points #1,2; 1,-2; -1,2; -1-2

class AproxCuadratica(AproxLineal):
    def __init__(self, usrInput):
        AproxLineal.__init__(self, usrInput) #Herencia de la clase AproxLineal
        counter = 0; aux = np.array(self.A[:,1]); #Contador y lista auxliar para crear los cuadrados de las componentes x
        for i in aux: #por cada elemento i dentro de aux
                aux.itemset(counter, i.item()**2); counter += 1 #Establezca el elemento en la posicion counter como si mismo al cuadrado y aumente contador en uno
        self.A = np.insert(np.matrix(self.A), [2], aux, axis=1) #Matriz A
        self.At = self.A.transpose() #Matriz traspuesta
        self.InvATA = np.linalg.inv(self.At*self.A) #Inversa de A transpuesta por A
        self.Result = (self.InvATA*self.At)*self.Y #Resultado final

    def buildInput(self, points):
        return AproxLineal.buildInput(self, points) #Herencia de la clase AproxLineal

    def plot(self):
        plt.ion() #Habilita el modo interactivo
        x = np.linspace(-5,5) #El rango
        y = self.Result.item(0) + self.Result.item(1)*x + self.Result.item(2)*x**2 #La funcion
        plt.plot(x, y, linewidth=2.5, linestyle="-") #Dibujar el grafico
        plt.plot(self.data_x,self.data_y, 'or') #Dibujar los puntos
        plt.grid(True) #Mostrar cuadricula
        plt.draw() #Actualizar los cambios al grafico

class AproxExponencial(AproxLineal):
    def __init__(self, usrInput):
        AproxLineal.__init__(self, usrInput)
        self.LA = 10**self.Result.item(0)
        self.LB = 10**self.Result.item(1)

    def buildInput(self, points):
        return AproxLineal.buildInput(self, points) #Herencia de la clase AproxLineal

    def plot(self):
        plt.ion() #Habilita el modo interactivo
        x = np.linspace(-5,5) #El rango
        y = self.LA * (self.LB**x) #La funcion
        plt.plot(x, y, linewidth=2.5, linestyle="-") #Dibujar el grafico
        plt.plot(self.data_x,self.data_y, 'or') #Dibujar los puntos
        plt.grid(True) #Mostrar cuadricula
        plt.draw() #Actualizar los cambios al grafico

##Data test:
# points = '(1,3), (-2,4), (7,0)'
# points1 = '(1,-3), (4,6), (-2,5), (3,-1)'
# points2 = '(2,3), (-1,2), (0,1), (-2,-5)'
# points3 = '(-1,3), (2,5), (3,4)'
# points4 = '(1,3), (-2,4), (7,0)'

# ejemplo = AproxLineal(points1)
# print ejemplo.Result
# ejemplo.plot()

# ejemplo = AproxCuadratica(points2)
# print ejemplo.Result
# ejemplo.plot()
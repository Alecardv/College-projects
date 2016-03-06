from collections import deque


class Bandeja(object):


    def __init__(self, numhojas=1):
        self.__hojas = numhojas

    def retirar_hoja(self):
        self.__hojas -= 1

    def add_hoja(self, n):
        self.__hojas += n

    def verificar(self):
        #Verifica que hayan hojas
        if self.__hojas <= 0: return False
        else: return True

"""
"""

class Cartucho(object):


    __NEGRO = False
    __COLOR = False

    def __init__(self, tipo):
        if tipo == 0:
            self.__NEGRO = True
        elif tipo == 1:
            self.__COLOR = True
        self.__nivel = 100
        self.__estado = True

    def verificar(self):
        #Verifica el nivel de tinta y el estado del cartucho
        if self.__nivel <= 10 or not self.__estado:
            return False
        else:
            return True

    def usar(self):
        self.__nivel -= 1

    def recargar(self, n):
        self.__nivel += n

    def tipo(self):
        if self.__NEGRO: return 'NEGRO'
        elif self.__COLOR: return 'COLOR'
        else: return 'NO DEFINIDO'

"""
"""

class ColaImpresion(object):

    
    def __init__(self):
        self.__cola = deque([])

    def liberar(self):
        return self.__cola.popleft()

    def encolar(self, elemento):
        self.__cola.append(elemento)

    def vacia(self):
        if len(self.__cola) == 0: return 1
        else: return 0

"""
"""

class PSL:
    def __init__(self, content):
        self.content = content


class PS:
    def __init__(self, content):
        self.content = content

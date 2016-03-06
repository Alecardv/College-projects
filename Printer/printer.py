from libprinter import *

class CartuchoError(Exception):
    def __init__(self, value_):
        self.value_ = value_

    def __str__(self):
        return repr(self.value_)

class BandejaError(Exception):
    def __init__(self, value_):
        self.value_ = value_

    def __str__(self):
        return repr(self.value_)

class Impresora(object):


    def __init__(self, numhojas=1, tintanegra=True, tintacolor=True):
        self.__bandeja = Bandeja(numhojas)
        self.__colaimpresion = ColaImpresion()
        if tintanegra:
            self.__tintanegra = Cartucho(0)
        if tintacolor:
            self.__tintacolor = Cartucho(1)

    def imprimir(self, elemento):
        self.__colaimpresion.encolar(elemento)
        
        try:
            self.verificar_cartuchos(self.__tintanegra)
            self.verificar_cartuchos(self.__tintacolor)
        except CartuchoError as e:
            print(e.value_)
            exit()
        try:
            self.verificar_bandeja()
        except BandejaError as e:
            print(e.value_)
            exit()

        self.__tintacolor.usar()
        self.__tintanegra.usar()
        self.__bandeja.retirar_hoja()
        print self.__colaimpresion.liberar()

    def verificar_cartuchos(self, cartucho):
        if not cartucho.verificar():
            raise CartuchoError('Sustituir catucho')
        else: return True

    def verificar_bandeja(self):
        if not self.__bandeja.verificar():
            raise BandejaError('Sin hojas disponibles')
        else: return True
"""
@author: J. Alejandro Cardona
"""

class GenericError(Exception):
    def __init__(self, value_):
        self.value_ = value_

    def __str__(self):
        return repr(self.value_)

class HouseThings(object):
    def __init__(self):
        self.__elements = {}
    
    def new(self, e, v=False):
        if e in self.__elements:
            print(str(e)+' alredy exists')
        else:
            self.__elements[e] = v

    def set(self, e, v, op=''):
        if e in self.__elements:
            if self.__elements[e] == self.get_value(v):
                raise GenericError('Ya estaba establecido')
            elif op !='':
                self.__elements[e][op] = self.get_value(v)
            else: self.__elements[e] = self.get_value(v)
        else:
            raise GenericError('Ese elemento no existe.')


    def get(self, e):
        if e in self.__elements:
            return self.__elements[e]
        else: return 'e does not exist'

    def get_value(self, v):
        if v.lower() == 'true' or v == 'si':
            return True
        return False

class Room(HouseThings) : pass
class Kitchen(HouseThings) : pass
class WC(HouseThings) : pass
class Garage(HouseThings) : pass
class Livingroom(HouseThings) : pass
class Hall(HouseThings) : pass

class Home(object):
    def __init__(self):
        self.KidRoom = Room()
        self.MainRoom = Room()
        self.Kitchen = Kitchen()
        self.Livingroom = Livingroom()
        self.Garage = Garage()
        self.Hall = Hall()
        self.Equi = {
            'garage' : self.Garage,
            'ninos' : self.KidRoom,
            'principal':self.MainRoom,
            'cocina':self.Kitchen,
            'sala':self.Livingroom,
            'comedor':self.Hall
        }

    def new(self, w, e, v=False):
        self.Equi[w].new(e,v)

    def set(self, w, e, v, op=''):
        self.Equi[w].set(e,v)

    def get(self, w, e):
        return self.Equi[w].get(e)
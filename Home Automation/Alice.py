"""
@author: J. Alejandro Cardona
"""

import string
import re

euro = unichr(0x20ac)

class Alice(object):
    def __init__(self):
        # Son las expresiones regulares
        self.keys = [re.compile(i[0], re.IGNORECASE) for i in gPats]
        # Son las respuestas
        self.values = [x[1] for x in gPats]

    def respond(self,text):
        for i in range(len(self.keys)):
            match = self.keys[i].match(text)
            if match:
                resp = self.values[i]
                return resp

def get_keywords(msg):
    pass

gPats = [
    ## Genericos, necesitan memoria:
    [r'.*(encienda|encender|enciende) la luz$',
    ['A que luz te refieres?', 'OPT,bombillo,True,']],
     
    [r'.*?(abra|abre) la puerta$',
    ['A que puerta te refieres?', 'OPT,puerta,True,abierta']],

    [r'.*(apague|apaga|apagar) la luz$',
    ['A que luz te refieres?', 'OPT,bombillo,False,']],
     
    [r'.*?(cierra|cierre) la puerta$',
    ['A que puerta te refieres?', 'OPT,puerta,False,abierta']],
    
    ## Abrir Puertas:
    [r'.*?(abra|abre) la puerta .*garage',
    ['Hecho', 'garage,puerta,True,abierta']],

    [r'.*?(abra|abre) la puerta .*ninos',
    ['Hecho', 'ninos,puerta,True,abierta']],

    [r'.*?(abra|abre) la puerta .*(alcoba|principal)',
    ['Hecho', 'principal,puerta,True,abierta']],
    
    [r'.*?(abra|abre) la puerta .*cocina',
    ['Hecho', 'cocina,puerta,True,abierta']],
     
    [r'.*?(abra|abre) la puerta .*sala',
    ['Hecho', 'sala,puerta,True,abierta']],
    
    [r'.*?(abra|abre) la puerta .*comedor',
    ['Hecho', 'comedor,puerta,True,abierta']],
    
    ## Cerrar Puertas:
    [r'.*?(cierra|cierre) la puerta .*garage',
    ['Hecho', 'garage,puerta,False,abierta']],

    [r'.*?(cierra|cierre) la puerta .*ninos',
    ['Hecho', 'ninos,puerta,False,abierta']],

    [r'.*?(cierra|cierre) la puerta .*(alcoba|principal)',
    ['Hecho', 'principal,puerta,False,abierta']],
    
    [r'.*?(cierra|cierre) la puerta .*cocina',
    ['Hecho', 'cocina,puerta,False,abierta']],
     
    [r'.*?(cierra|cierre) la puerta .*sala',
    ['Hecho', 'sala,puerta,False,abierta']],
    
    [r'.*?(cierra|cierre) la puerta .*comedor',
    ['Hecho', 'comedor,puerta,False,abierta']],

    ## Encender Luces:
    [r'.*(encienda|encender|enciende) la luz .*garage',
    ['Hecho', 'garage,bombillo,True,']],

    [r'.*(encienda|encender|enciende) la luz .*ninos',
    ['Hecho', 'ninos,bombillo,True,']],

    [r'.*(encienda|encender|enciende) la luz .*(alcoba|principal)',
    ['Hecho', 'principal,bombillo,True,']],
    
    [r'.*(encienda|encender|enciende) la luz .*cocina',
    ['Hecho', 'cocina,bombillo,True,']],
     
    [r'.*(encienda|encender|enciende) la luz .*sala',
    ['Hecho', 'sala,bombillo,True,']],
    
    [r'.*(encienda|encender|enciende) la luz .*comedor',
    ['Hecho', 'comedor,bombillo,True,']],

    ## Apagar Luces:
    [r'.*(apague|apaga|apagar) la luz .*garage',
    ['Hecho', 'garage,bombillo,False,']],

    [r'.*(apague|apaga|apagar) la luz .*ninos',
    ['Hecho', 'ninos,bombillo,False,']],

    [r'.*(apague|apaga|apagar) la luz .*(alcoba|principal)',
    ['Hecho', 'principal,bombillo,False,']],
    
    [r'.*(apague|apaga|apagar) la luz .*cocina',
    ['Hecho', 'cocina,bombillo,False,']],
     
    [r'.*(apague|apaga|apagar) la luz .*sala',
    ['Hecho', 'sala,bombillo,False,']],
    
    [r'.*(apague|apaga|apagar) la luz .*comedor',
    ['Hecho', 'comedor,bombillo,False,']],

    ## Quitar seguro de las puertas:
    [r'.*(quita|quitar|quite) .*seguro .*puerta .*garage',
    ['Hecho', 'garage,puerta,False,seguro']],

    [r'.*(quita|quitar|quite) .*seguro .*puerta .*ninos',
    ['Hecho', 'ninos,puerta,False,seguro']],

    [r'.*(quita|quitar|quite) .*seguro .*puerta .*(alcoba|principal)',
    ['Hecho', 'principal,puerta,False,seguro']],

    [r'.*(quita|quitar|quite) .*seguro .*puerta .*cocina',
    ['Hecho', 'cocina,puerta,False,seguro']],

    [r'.*(quita|quitar|quite) .*seguro .*puerta .*sala',
    ['Hecho', 'sala,puerta,False,seguro']],

    [r'.*(quita|quitar|quite) .*seguro .*puerta .*comedor',
    ['Hecho', 'comedor,puerta,False,seguro']],
    ## Poner seguro de las puertas:
    [r'.*(pon|ponle|poner) .*seguro .*puerta .*garage',
    ['Hecho', 'garage,puerta,True,seguro']],

    [r'.*(pon|ponle|poner) .*seguro .*puerta .*ninos',
    ['Hecho', 'ninos,puerta,True,seguro']],

    [r'.*(pon|ponle|poner) .*seguro .*puerta .*(alcoba|principal)',
    ['Hecho', 'principal,puerta,True,seguro']],

    [r'.*(pon|ponle|poner) .*seguro .*puerta .*cocina',
    ['Hecho', 'cocina,puerta,True,seguro']],

    [r'.*(pon|ponle|poner) .*seguro .*puerta .*sala',
    ['Hecho', 'sala,puerta,True,seguro']],

    [r'.*(pon|ponle|poner) .*seguro .*puerta .*comedor',
    ['Hecho', 'comedor,puerta,True,seguro']],

    ## Consultas:
    [r'.*?como esta la luz (.*?)garage',
    ['Ya te digo', 'QST,garage,bombillo,']],

    [r'.*?como esta la luz (.*?)ninos',
    ['Ya te digo', 'QST,ninos,bombillo,']],

    [r'.*?como esta la luz (.*?)principal',
    ['Ya te digo', 'QST,principal,bombillo,']],

    [r'.*?como esta la luz (.*?)cocina',
    ['Ya te digo', 'QST,cocina,bombillo,']],

    [r'.*?como esta la luz (.*?)sala',
    ['Ya te digo', 'QST,sala,bombillo,']],

    [r'.*?como esta la luz (.*?)comedor',
    ['Ya te digo', 'QST,comedor,bombillo,']],

    ## Complementos a respuestas, accionan la memoria:
    [r'.*? cocina$',
    ['Hecho', 'SLF,cocina']]

    ## Objetos varios:


    ## Conversacion:
    ]

def command_interface():
    print "Habla al programa escribiendo en espanol plano-"
    print 'No uses la letra enhe, signo de abrir pregunta ni tildes.'
    print 'Escribe "salir" para finalizar.'
    print '='*72
    print "Hola. Que deseas hacer hoy?"
    s = ""
    therapist = Alice();
    while s != "salir":
        s = raw_input(">")
        while s[-1] in "!.": s = s[:-1]
        print therapist.respond(s)

if __name__ == "__main__":
    command_interface()
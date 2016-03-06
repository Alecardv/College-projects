# -*- coding: utf-8 -*-
"""
@author: J. Alejandro Cardona
"""

from Home import *
from Alice import *
import random

escapes = [
    '$Lo siento, me he quedado sin palabras',
    '$Disculpa?',
    '$No he logrado entenderte',
    '$Podrias escribir mas claro, porfavor'
]

class Control():
    def __init__(self):
        self.IA = Alice()
        self.Home = Home()
        self.create_home()
        self.memory = []
    
    def create_home(self):
        self.Home.KidRoom.new('bombillo')
        self.Home.KidRoom.new('puerta', {'seguro':False, 'abierta':False})
        self.Home.KidRoom.new('ventana')
        self.Home.MainRoom.new('bombillo')
        self.Home.MainRoom.new('puerta', {'seguro':False, 'abierta':False})
        self.Home.MainRoom.new('ventana')
        self.Home.Kitchen.new('bombillo')
        self.Home.Kitchen.new('puerta', {'seguro':False, 'abierta':False})
        self.Home.Kitchen.new('estufa', {'boquilla1':False, 'boquilla2':False, 'boquilla3':False, 'boquilla4':False})
        self.Home.Livingroom.new('bombillo')
        self.Home.Livingroom.new('puerta', {'seguro':False, 'abierta':False})
        self.Home.Garage.new('bombillo')
        self.Home.Garage.new('puerta', {'seguro':False, 'abierta':False})
        self.Home.Hall.new('bombillo')
        self.Home.Hall.new('puerta', {'seguro':False, 'abierta':False})
        
    def interact_console(self):
        while True:
            reply = self.get_response(raw_input(">"))
            if not reply: return 0 #Si se envio salir, terminar.
            if reply[0] == '$': print reply[1:]; continue
            acts = reply[1].split(',')
            print acts
            if not self.memory: #Si no hay una conversacion pendiente
                #Si la respuesta tiene opciones, agreguelas a la memoria:
                if 'OPT' in reply[1]: self.memory.append(acts[1:])
                elif 'QST' in reply[1]: reply[0] = str(self.Home.get(acts[1],acts[2]))
                else:
                    try:
                        self.Home.set(acts[0], acts[1], acts[2], acts[3])
                    except GenericError as e:
                        reply[0] = e.value_
            else: #Si hay memoria
                if acts[0] == 'SLF': 
                    try:
                        self.Home.set(acts[1], self.memory[0][0], self.memory[0][1], self.memory[0][2])
                        self.memory = []
                    except GenericError as e:
                        reply[0] = e.value_
            print reply[0]

    def interact(self, msg):
        reply = self.get_response(msg)
        if not reply: exit() #Si se envio salir, terminar.
        if reply[0] == '$': return reply[1:]
        acts = reply[1].split(',')
        print acts
        if not self.memory: #Si no hay una conversacion pendiente
            #Si la respuesta tiene opciones, agreguelas a la memoria:
            if 'OPT' in reply[1]: self.memory.append(acts[1:])
            elif 'QST' in reply[1]: return str(self.Home.get(acts[1],acts[2]))
            else:
                try:
                    self.Home.set(acts[0], acts[1], acts[2], acts[3])
                except GenericError as e:
                    reply[0] = e.value_
        else: #Si hay memoria
            if acts[0] == 'SLF': 
                try:
                    self.Home.set(acts[1], self.memory[0][0], self.memory[0][1], self.memory[0][2])
                    self.memory = []
                except GenericError as e:
                    reply[0] = e.value_
        return reply[0]
            
    def get_response(self, msg):
        if msg == 'salir':
            return ""
        reply = self.IA.respond(msg)
        if reply == None:
            return random.choice(escapes)
        return reply

# control = Control()
# cont.interact()
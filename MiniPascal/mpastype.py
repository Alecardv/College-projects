# -*- coding: utf-8 -*-
# @Author: J. Alejandro Cardona Valdes

"""
Sistema de Tipos de MPascal
===========================
Este archivo define las clases de representacion de tipos.  Esta es una
clase general usada para representar todos los tipos.  Cada tipo es entonces
una instancia singleton de la clase tipo.

class MpasType(object):
    pass

int_type = MpasType("int",...)
float_type = MpasType("float",...)
"""


class MpasType(object):
    """
    Clase que representa un tipo en el lemguaje mpascal. Los tipos
    son declarados como instancias singleton de este tipo.
    """

    def __init__(self, name, default, bin_ops=set(), un_ops=set()):
        self.name = name
        self.bin_ops = bin_ops
        self.un_ops = un_ops
        self.default = default

    def __str__(self):
        return str(self.name + '_type').upper()

    def __repr__(self):
        return str(self.name + '_type').upper()


# Crear instancias especaficas de los tipos.
int_type = MpasType("int", 0,
                    {'MAS', 'MENOS', 'MULT', 'DIV', 'LE', 'LT', 'EQ', 'NE', 'GT', 'GE'},
                    {'MAS', 'MENOS'})

float_type = MpasType("float", 0.0,
                      {'MAS', 'MENOS', 'MULT', 'DIV', 'LE', 'LT', 'EQ', 'NE', 'GT', 'GE'},
                      {'MAS', 'MENOS'})
str_type = MpasType("string", '',{},{})
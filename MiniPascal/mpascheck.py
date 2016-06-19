# -*- coding: utf-8 -*-
# @Author: J. Alejandro Cardona Valdes

"""
Proyecto 3 : Chequeo del Programa
=================================
Aquí está una lista completa de todo lo que
debera comprobar:

1.  Nombres y símbolos:

    Todos los identificadores deben ser definidos antes de ser usados.  Esto incluye variables,
    constantes y nombres de tipo.  Por ejemplo, esta clase de código genera un error:

       a = 3;              // Error. 'a' no está definido.
       var a int;

    Nota: los nombres de tipo como "int", "float" y "string" son nombres incorporados que
    deben ser definidos al comienzo de un programa (función).

2.  Tipos de constantes

    A todos los símbolos constantes se le debe asignar un tipo como "int", "float" o "string".
    Por ejemplo:

       const a = 42;         // Tipo "int"
       const b = 4.2;        // Tipo "float"
       const c = "forty";    // Tipo "string"

    Para hacer esta asignación, revise el tipo de Python del valor constante y adjunte el
    nombre de tipo apropiado.

3.  Chequeo de tipo operación binaria.

    Operaciones binarias solamente operan sobre operandos del mismo tipo y produce un
    resultado del mismo tipo.  De lo contrario, se tiene un error de tipo.  Por ejemplo:

        var a int = 2;
        var b float = 3.14;

        var c int = a + 3;    // OK
        var d int = a + b;    // Error.  int + float
        var e int = b + 4.5;  // Error.  int = float

4.  Chequeo de tipo operador unario.

    Operadores unarios retornan un resultado que es del mismo tipo del operando.

5.  Operadores soportados

    Estos son los operadores soportados por cada tipo:

    int:      binario { +, -, *, /}, unario { +, -}
    float:    binario { +, -, *, /}, unario { +, -}
    string:   binario { + }, unario { }

    Los intentos de usar operadores no soportados debería dar lugar a un error.
    Por ejemplo:

        var string a = "Hello" + "World";     // OK
        var string b = "Hello" * "World";     // Error (op * no soportado)

6.  Asignación.

    Los lados izquierdo y derecho de una operación de asignación deben ser
    declarados del mismo tipo.

    Los valores sólo se pueden asignar a las declaraciones de variables, no
    a constantes.

Para recorrer el AST, use la clase NodeVisitor definida en mpasast.py.
Un caparazón de código se proporciona a continuación.
"""

import sys, re, string, types
from errors import error
from mpasast import *
from mpastype import int_type, float_type, str_type
import mpaslex


class SymbolTable(object):
    """
    Clase que representa una tabla de símbolos.  Debe proporcionar funcionabilidad
    para agregar y buscar nodos asociados con identificadores.
    """

    class SymbolDefinedError(Exception):
        """
        Exception disparada cuando el codigo trara de agragar un simbol
        a la tabla de simbolos, y este ya esta definido
        """
        def __init__(self, _msg):
            self._msg = _msg

        def __str__(self):
            return repr(_msg)

    class SymbolConflictError(Exception):
        def __init__(self, _msg):
            self._msg = _msg

        def __str__(self):
            return repr(_msg)

    def __init__(self, parent=None, name=None):
        """
        Crea una tabla de simbolos vacia con la tabla padre dada
        """
        self.name = name #Para dar un nombre o identificador a la tabla de simbolos
        self.symtab = {}
        self.parent = parent
        if self.parent is not None:
            self.parent.children.append(self)
        self.children = []

    def add(self, a, v):
        """
        Agrega un simbol con el valor dado a la tabla de simbolos

        func foo(x:int, y:int)
        x:float;
        """
        if self.symtab.has_key(a):
            raise SymbolTable.SymbolDefinedError("Error " + str(a) + " alredy defined")
        self.symtab[a] = v

    def lookup(self, a):
        if self.symtab.has_key(a):
            return self.symtab[a]
        else:
            if self.parent != None:
                return self.parent.lookup(a)
            else:
                return None


class CheckProgramVisitor(NodeVisitor):
    """
    Clase de Revisión de programa.  Esta clase usa el patrón visitor como está
    descrito en mpasast.py.  Es necesario definir métodos de la forma visit_NodeName()
    para cada tipo de nodo del AST que se desee procesar.

    Nota: Usted tendrá que ajustar los nombres de los nodos del AST si ha elegido
    nombres diferentes.
    """

    def __init__(self):
        # Se crea una tabla de simbolos vacia para el programa y se
        # asigna como la tabla de simbolos actual
        self.current = SymbolTable(name='program')
        self.symtab = self.current

    def push_symtab(self, node, n):
        self.current = SymbolTable(parent=self.current, name=n)
        node.symtab = self.current

    def pop_symbol(self):
        self.current = self.current.parent

    def visit_Program(self, node):
        # Se recorre cada funcion del programa
        for item in node.funlist:
            self.visit(item)
        # Se verifica que exista una funcion MAIN
        if 'main' not in self.symtab.symtab.keys():
            print("Error, no 'main' function found")
            exit()
        print('Finished ...')
        # print(self.symtab.symtab)
        # print(self.symtab.children[0].symtab)

    def visit_Function(self, node):
        # Se intenta agreagar el simbolo, si  ya existe se levanta una excepcion
        try:
            self.current.add(node.id, {'type':'undefined', 'params':None})
        except SymbolTable.SymbolDefinedError as e:
            print(node.lineno + ": " + e._msg)
            exit()
        # Se agrega una nueva tabla de simbolos para la funcion
        self.push_symtab(node, node.id)
        # Visito los parametros y los agrego a la tabla superior
        params = self.visit(node.paramlist)
        self.current.parent.lookup(node.id)['params'] = params
        # Visito las variables y las declaraciones:
        self.visit(node.varlist)
        self.visit(node.statements)
        # Se devuelve a la tabla de simbolos superior
        self.current = self.current.parent

    def visit_ParametersList(self, node):
        params = []
        for item in node.param_decl:
            params.append(self.visit(item))
        return params

    def visit_Parameter(self, node):
        v = {'type': node.typename, 'id': node.id}
        # Control para tipos indexados:
        if isinstance(v['type'], TypeIndexed):
            v['type'] = node.typename.typename
            v['index'] = node.typename.intliteral
        try:
            self.current.add(node.id, v)
        except SymbolTable.SymbolDefinedError as e:
            print(node.lineno + ": " + e._msg)
            exit()
        return v

    def visit_VariableList(self, node):
        for item in node.var_decl:
            self.visit(item)

    def visit_Statements(self, node):
        for item in node.statements:
            self.visit(item)

    def visit_AssignmentStatement(self, node):
        # Busco el id y verifico que el simbolo si exista
        sym = self.current.lookup(node.location.id)
        if not sym:
            error(node.lineno, node.id + " No symbol defined")
        # Visito la expresion
        v = self.visit(node.expr)
        try:
            # Verifico que los tipos sean compatibles
            if not v['type'] is self.current.symtab[node.location.id]['type']:
                error(node.lineno, "Uncompatible types")
        except:
            error(node.lineno, "Error while assigning")

    def visit_Literal(self, node):
        return {'type': node.typename, 'value': node.value}

    def visit_Location(self, node):
        # Verifico que el simbolo exista
        sym = self.current.lookup(node.id)
        if sym is None:
            error(node.lineno, node.id + " Unknow symbol")
        return sym

    def visit_LocationIndexed(self, node):
        sym = self.current.lookup(node.id)
        if sym is None:
            error(node.lineno, node.id + " Unknow symbol")
        if not self.visit(node.expr)['type'] is int_type:
            error(node.lineno, "Only integer can be used to declare index")
        return sym

    def visit_ArgumentsList(self, node):
        params = []
        for item in node.expr:
            params.append(self.visit(item))
        return params

    def visit_ReturnStatement(self, node):
        # Me aseguro de que no se haya definido un tipo de retorno antes
        if self.current.parent.lookup(self.current.name)['type'] != 'undefined':
            error(node.lineno, "So many returns")
        else:
            sym = self.visit(node.expr)
            if not sym:
                error(node.lineno, "Error while assigning return expression")
            else:
                self.current.parent.symtab[self.current.name]['type'] = sym['type']

    def visit_FunCall(self, node):
        # Verifico que la funcion exista en la tabla de simbolos
        sym = self.symtab.lookup(node.id)
        params = self.visit(node.params)
        try:
            # Verifico que el numero de parametros sea el mismo
            if len(params) == len(sym['params']):
                # Control para funciones sin parametros:
                if params == sym['params']: return {'type': sym['type']}
                # Verifico que los tipos sean compatibles:
                for i in range(len(params)):
                    if not params[i]['type'] is sym['params'][i]['type']:
                        error(node.lineno, " Uncompatible types while calling function")
            else:
                error(node.lineno, "Unexpected number of parameters")
            return {'type':sym['type']}
        except:
            error(node.lineno, "Error while calling function")

    def visit_ReadStatement(self, node):
        self.visit(node.location)

    def visit_PrintStatement(self, node):
        return {'type':str_type, 'value':node.string_literal}

    def visit_WriteStatement(self, node):
        self.visit(node.expr)

    def visit_WhileStatement(self, node):
        self.visit(node.condition)
        self.visit(node.body)

    def visit_RelationalOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        try:
            if not left['type'] is right['type']:
                error(node.lineno, "Uncompatible types")
        except:
            error(node.lineno, "Error while comparing expressions")
        return {'type': left['type']}

    def visit_UnaryRelation(self, node):
        return self.visit(node.relation)

    def visit_RelationGroup(self, node):
        return self.visit(node.relation)

    def visit_Group(self, node):
        return self.visit(node.expr)

    def visit_UnaryOp(self, node):
        # 1. Asegúrese que la operación es compatible con el tipo
        # 2. Ajuste el tipo resultante al mismo del operando
        sym = self.visit(node.left)
        if sym['type'] is str_type:
            error(node.lineno, "No supported operation")
        return sym

    def visit_BinaryOp(self, node):
        # 1. Asegúrese que los operandos left y right tienen el mismo tipo
        # 2. Asegúrese que la operación está soportada
        # 3. Asigne el tipo resultante
        left = self.visit(node.left)
        right = self.visit(node.right)
        try:
            if not left['type'] is right['type']:
                error(node.lineno, "Uncompatible types")
            return {'type': left['type']}
        except:
            error(node.lineno, "Error while trying to perform binary operation")
        return {'type': 'NONE'}

    def visit_BeginStatement(self, node):
        self.visit(node.statements)

    def visit_IfStatement(self, node):
        self.visit(node.condition)
        self.visit(node.then)

    def visit_IfElseStatement(self, node):
        self.visit(node.condition)
        self.visit(node.then)
        self.visit(node._else)

    def visit_BrakStatement(self, node):
        pass

    def visit_SkipStatement(self, node):
        pass

    def visit_Empty(self, node):
        pass


# ----------------------------------------------------------------------
#                       NO MODIFICAR NADA DE LO DE ABAJO
# ----------------------------------------------------------------------

def check_program(node):
    """
    Comprueba el programa suministrado (en forma de un AST)
    """
    checker = CheckProgramVisitor()
    checker.visit(node)


def main():
    import mpasparse
    import sys
    from errors import subscribe_errors
    parser = mpasparse.parser
    data = open("gcd.pas").read()
    with subscribe_errors(lambda msg: sys.stdout.write(msg + "\n")):
        program = parser.parse(data)
        check_program(program)

if __name__ == '__main__':
    main()

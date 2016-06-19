# @Author: J. Alejandro Cardona Valdes

import ply.yacc as yacc
from errors import error
from mpaslex import tokens
from mpastype import int_type, float_type
from mpasast import *

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'NOT'),
    ('left', 'LT', 'LE', 'GT', 'GE', 'EQ', 'NE'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULT', 'DIV'),
    ('right', 'UMINUS')
)

start = 'program'


# Programa
def p_program(p):
    """program : program function
               | function"""
    if len(p) == 3:
        p[0] = p[1]
        p[0].append(p[2])
    else:
        p[0] = Program([p[1]])


def p_function(p):
    """function : FUN ID paramlist varlist BEGIN statements END"""
    p[0] = Function(p[2], p[3], p[4], p[6], lineno=str(p.lineno(2)))


def p_parmlist(p):
    """
    paramlist : PARI paramlistitems PARD"""
    p[0] = p[2]


def p_paramlist_emtpy(p):
    """paramlist : PARI empty PARD"""
    p[0] = ParametersList([p[2]])

def p_paramlistitems(p):
    """
    paramlistitems : paramlistitems comparm
                   | parm
    """
    if len(p) == 3:
        p[0] = p[1]
        p[0].append(p[2])
    else:
        p[0] = ParametersList([p[1]])


def p_comparm(p):
    """comparm : COMA parm
               | parm"""
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = p[1]


def p_parm(p):
    """parm : ID DPUN typename"""
    p[0] = Parameter(p[1], p[3], lineno=str(p.lineno(2)))


def p_typename_int(p):
    """typename : INT"""
    p[0] = int_type


def p_typename_float(p):
    """typename : FLOAT"""
    p[0] = float_type


def p_typename_indexed_int(p):
    """typename : INT CORI expr CORD"""
    p[0] = TypeIndexed(int_type, p[3])


def p_typename_indexed_float(p):
    """typename : FLOAT CORI expr CORD"""
    p[0] = TypeIndexed(float_type, p[3])


def p_varlist(p):
    """
    varlist : declist optsemi
            | empty
    """
    p[0] = p[1]


def p_optsemi(p):
    """optsemi : PCOMA"""
    #p[0] = Node("Optional Semicolon", leaf=p[1])


def p_optsemi_empty(p):
    """optsemi : empty"""
    #p[0] = p[1]


def p_declist_var(p):
    """declist : vardecl"""
    p[0] = VariableList([p[1]])


def p_declist_declist_var(p):
    """declist : declist vardecl"""
    p[0] = p[1]
    p[0].append(p[2])


def p_declist(p):
    """declist : declist PCOMA vardecl"""
    p[0] = p[1]
    p[0].append(p[3])


def p_vardecl(p):
    """
    vardecl : parm
            | function
    """
    p[0] = p[1]


def p_statements_coma(p):
    """statements : statements PCOMA statement"""
    p[0] = p[1]
    p[0].append(p[3])


def p_statements(p):
    """statements : statement"""
    p[0] = Statements([p[1]])


def p_statement_asig(p):
    """statement : location ASIG expr"""
    p[0] = AssignmentStatement(p[1], p[3], lineno=str(p.lineno(2)))


def p_statement_funcall(p):
    """statement : ID PARI exprlist PARD"""
    p[0] = FunCall(p[1], p[3], lineno=str(p.lineno(1)))


def p_statement_print(p):
    """statement : PRINT PARI STRINGLITERAL PARD"""
    p[0] = PrintStatement(p[3])


def p_statement_read(p):
    """statement : READ PARI location PARD"""
    p[0] = ReadStatement(p[3])


def p_statement_while(p):
    """statement : WHILE relation DO statement"""
    p[0] = WhileStatement(p[2], p[4])


def p_statement_begin(p):
    """statement : BEGIN statements END"""
    p[0] = BeginStatement(p[2])


def p_statement_write(p):
    """statement : WRITE PARI expr PARD"""
    p[0] = WriteStatement(p[3])


def p_statement_return(p):
    """
    statement : RETURN expr
              | RETURN empty
    """
    p[0] = ReturnStatement(p[2], lineno=str(p.lineno(2)))


def p_statement_if(p):
    """statement : IF relation THEN statement"""
    p[3] = ThenStatement(p[4])
    p[0] = IfStatement(p[2], p[3])


def p_statement_ifelse(p):
    """statement : IF relation THEN statement ELSE statement"""
    p[3] = ThenStatement(p[4])
    p[5] = ElseStatement(p[6])
    p[0] = IfElseStatement(p[2], p[3], p[5])


def p_statement_break(p):
    """statement : BREAK"""
    p[0] = BreakStatement()


def p_statement_skip(p):
    """statement : SKIP"""
    p[0] = SkipStatement()


def p_location(p):
    """
    location : ID
             | ID CORI expr CORD
    """
    if len(p) == 2:
        p[0] = Location(p[1], lineno=str(p.lineno(1)))
    else:
        p[0] = LocationIndexed(p[1], p[3], lineno=str(p.lineno(1)))


def p_exprlist(p):
    """exprlist : exprlistitems"""
    p[0] = p[1]


def p_exprlistitems(p):
    """exprlistitems : exprlistitems comexpr"""
    p[0] = p[1]
    p[0].append(p[2])



def p_exprlistitems_expr(p):
    """exprlistitems : expr"""
    p[0] = ArgumentsList([p[1]])


def p_exprlist_empty(p):
    """exprlist : empty"""
    p[0] = ArgumentsList([p[1]])


def p_comexpr(p):
    """comexpr : COMA expr
               | expr"""
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = p[1]


def p_expr_bin(p):
    """
    expr : expr MAS expr
         | expr MENOS expr
         | expr MULT expr
         | expr DIV expr
    """
    p[0] = BinaryOp(p[2], p[1], p[3], lineno=str(p.lineno(2)))


def p_expr_unary_minus(p):
    """expr : MENOS expr %prec UMINUS"""
    p[0] = UnaryOp(p[1], p[2])


def p_expr_unary_plus(p):
    """expr : MAS expr %prec UMINUS"""
    p[0] = UnaryOp(p[1], p[2])


def p_expr_paren(p):
    """expr : PARI expr PARD"""
    p[0] = Group(p[2])


def p_expr_index(p):

    """expr : ID CORI expr CORD"""
    p[0] = LocationIndexed(p[1], p[3], lineno=str(p.lineno(1)))


def p_expr_int(p):
    """expr : NUMINTEGER"""
    p[0] = Literal(int_type, p[1], lineno=str(p.lineno(1)))


def p_expr_float(p):
    """expr : NUMFLOAT"""
    p[0] = Literal(float_type, p[1], lineno=str(p.lineno(1)))


def p_expr_funcall(p):
    """expr : ID PARI exprlist PARD %prec UMINUS"""
    p[0] = FunCall(p[1], p[3], lineno=str(p.lineno(1)))


def p_expr_id(p):
    """expr : ID"""
    p[0] = Location(p[1], lineno=str(p.lineno(1)))


def p_expr_int_cast(p):
    """expr : INT PARI expr PARD"""
    p[0] = IntCast(p[3])


def p_expr_float_cast(p):
    """expr : FLOAT PARI expr PARD"""
    p[0] = FloatCast(p[3])


def p_relation(p):
    """
    relation : expr LT expr
             | expr LE expr
             | expr GT expr
             | expr GE expr
             | expr EQ expr
             | expr NE expr
    """
    p[0] = RelationalOp(p[2], p[1], p[3], lineno=str(p.lineno(2)))


def p_relation_and_or(p):
    """
    relation : relation AND relation
             | relation OR relation
    """
    p[0] = RelationalOp(p[2], p[1], p[3])


def p_relation_not(p):
    """relation : NOT relation"""
    p[0] = UnaryRelation(p[1], p[2])


def p_relation_paren(p):
    """relation : PARI relation PARD"""
    p[0] = RelationGroup(p[2])


def p_empty(p):
    """empty :"""
    p[0] = Empty()


def p_error(p):
    if not p:
        print("Falta un token")
    else: print("\nERROR de sintaxis, Linea: " + str(p.lineno) + ", '" + str(p.value) + "' es incorrecto")


parser = yacc.yacc(start='program')

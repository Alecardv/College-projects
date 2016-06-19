import ply.lex as lex

# -----------------------------------------------------------------
# TOKENS
# -----------------------------------------------------------------

# Palabras reservadas
keywords = (
    'FUN', 'BEGIN', 'WHILE', 'IF', 'THEN', 'END', 'PRINT', 'AND',
    'WRITE', 'READ', 'RETURN', 'SKIP', 'BREAK', 'ELSE', 'DO',
    'OR', 'NOT', 'FLOAT', 'INT'
)

# Componentes lexicos
tokens = keywords + (
    # Operadores (+,-,*,/,>,<,<=,>=,!=,==)
    'MAS', 'MENOS', 'MULT', 'DIV', 'LE', 'LT', 'GT', 'GE', 'NE', 'EQ',

    # Delimitadores (  ) [  ] : ; := , .
    'PARI', 'PARD', 'CORI', 'CORD', 'DPUN', 'PCOMA', 'ASIG', 'COMA',

    # Literales (identificador, entero, flotante, cadena de caracteres)
    'ID', 'NUMINTEGER', 'NUMFLOAT', 'STRINGLITERAL'
)

# -----------------------------------------------------------------
# EXPRESIONES REGULARES:
# -----------------------------------------------------------------

# Expresiones regulares de operadores
t_MAS = r'\+'
t_MENOS = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_GT = r'\>'
t_LT = r'\<'
t_LE = r'\<='
t_GE = r'\>='
t_NE = r'!='
t_EQ = r'=='

# Expresiones regulares de Delimitadores
t_PARI = r'\('
t_PARD = r'\)'
t_CORI = r'\['
t_CORD = r'\]'
t_DPUN = r':'
t_PCOMA = r';'
t_ASIG = r'\:='
t_COMA = r'\,'

# Expresiones regulares para literales
t_STRINGLITERAL = r'\"(.|\n)*?\"'  # Cadenas de caracteres usadas dentro PRINT
t_NUMFLOAT = r'[0-9]+((\.[0-9]+)|\e(\+|\-)?[0-9]+)(\e(\+|\-)?[0-9]+)?'
t_NUMINTEGER = r'\d+'

# -----------------------------------------------------------------
# REGLAS PARA TOKENS (TOKEN RULES)
# -----------------------------------------------------------------

# Ignorar espacios en blanco y tabulaciones
t_ignore = ' \t'


# Ignorar comentarios
def t_ignore_COMMENT(t):
    r'\/\*(.|\n)*?\*\/'


# Saltos de linea
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += 1


# Identificadores
def t_ID(t):
    r'[_a-zA-Z][\w]*'
    if t.value.upper() in keywords:
        t.type = t.value.upper()
    return t


def t_error(t):
    print("caracter ilegal %s" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

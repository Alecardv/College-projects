#!/user/bin/env python

"""MiniPascal Compiler.

Usage:
  mpascal.py lex <file_name>
  mpascal.py ast <file_name>
  mpascal.py FILE
  mpascal.py -h | --help
  mpascal.py --version

Options: 
  -h --help     Show this screen.
  --version     Show version.
"""

import os
import sys
from errors import subscribe_errors
from mpascheck import check_program
from utils import DotVisitor
from mpasparse import parser
from mpaslex import lexer
from docopt import docopt

__author__ = "J. Alejandro Cardona Valdes"
__license__ = "unlicense"
__email__ = "alejandrocardona@outlook.com"


def ast(file_name):
    """Imprime el arbol de sintaxis abstracto"""
    f = open(str(file_name))
    data = f.read()
    v = DotVisitor()
    v.visit(parser.parse(data))
    print(v.dot)
    f.close()


def lex(file_name):
    """Realiza el analisis lexico"""
    f = open(str(file_name))
    data = f.read()
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
    f.close()


def check(file_name):
    """Realiza analisis semantico/sintactico y genera codigo ensamblador spark"""
    f = open(str(file_name))
    data = f.read()
    with subscribe_errors(lambda msg: sys.stdout.write(msg + "\n")):
        program = parser.parse(data)
        check_program(program)
    f.close()

    outname = os.path.splitext(file_name)[0] + '.s'
    if program:
        import mpasgen
        outfile = open(outname, "w")
        mpasgen.generate(outfile, program)
        outfile.close()


if __name__ == '__main__':
    arguments = docopt(__doc__, version='MiniPascal Compiler 1.0')
    if arguments['ast']:
        ast(arguments['<file_name>'])
    elif arguments['lex']:
        lex(arguments['<file_name>'])
    elif arguments['FILE']:
        check(arguments['FILE'])

#Sudoku Solver
##By Alejandro Cardona

Este SudokuSolver reduce al minimo los posibles candidatos para cada casilla incognita (Establece dominios) mediante el uso de las funciones:

reduce_lines():
    Reduce todos los dominios de forma vertical u horizontal
    Recibe un parametro que puede ser 'v' o 'h' para indicar si se debe reducir los dominios teniendo en cuenta filas o columnas

reduce_square():
    Reduce todos los dominios teniendo en cuenta los 9 cuadrantes

reduce_onlyone():
    Reduce todos los dominios que tengan un solo elemento estableciendo el mismo como una solucion para esa casilla

Luego verifica el estado actual del tablero para conocer si se ha solucionado, se ha llegado a un estado invalido o un estado continuable, de ser un estado continuable se intanta solucionar el tablero usando cada uno de los candidatos del primer dominio encontrado, finalmente uno de ellos debe llevar a un estado solucion

Informacion detallada de cada funcion se encuentra comentada en el codigo fuente

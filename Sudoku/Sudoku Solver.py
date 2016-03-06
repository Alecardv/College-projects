#@author: J. Alejandro Cardona
import copy
iterations = 0
class Sudoku_solver(object):

    def __init__(self, board):
    ## Se recibe un tablero y se estabelece un dominio inicial
    ## para todas las casillas vacias
        self.board = board
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    self.board[i][j] = [1,2,3,4,5,6,7,8,9]

    def reduce_lines(self, direction):
    ## direction establece si se intentara reducir los dominios
    ## de forma vertical u horizontal
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if type(self.board[i][j]) == list:
                    if direction == 'h':
                        temp = self.board[i]
                    elif direction == 'v':
                        temp = [n[j] for n in self.board]
                    for w in temp:
                        if type(w) == int:
                            if w in self.board[i][j]:
                                self.board[i][j].remove(w)

    def reduce_square(self):
    ## Reduccion del dominio por cuadrados:
    ## Se busca un dominio y se obtiene su 'cuadrante', con el se llama a get_square quien devuelve
    ## todos los elementos de dicho cuadrante en una lista, estos elementos se eliminan del dominio que se
    ## esta verificando y el resultado se establece como el nuevo dominio
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if type(self.board[i][j]) == list:
                    if (i<=2 and j<=2) and (i>=0 and j>=0):
                        self.board[i][j] = self._remove( self.board[i][j], self.get_square(2,2))
                    elif (i<=2 and j<=5) and (i>=0 and j>=3):
                        self.board[i][j] = self._remove( self.board[i][j], self.get_square(2,5))
                    elif (i<=2 and j<=8) and (i>=0 and j>=6):
                        self.board[i][j] = self._remove( self.board[i][j], self.get_square(2,8))
                    elif (i<=5 and j<=2) and (i>=3 and j>=0):
                        self.board[i][j] = self._remove( self.board[i][j], self.get_square(5,2))
                    elif (i<=5 and j<=5) and (i>=3 and j>=3):
                        self.board[i][j] = self._remove( self.board[i][j], self.get_square(5,5))
                    elif (i<=5 and j<=8) and (i>=3 and j>=6):
                        self.board[i][j] = self._remove( self.board[i][j], self.get_square(5,8))
                    elif (i<=8 and j<=2) and (i>=6 and j>=0):
                        self.board[i][j] = self._remove( self.board[i][j], self.get_square(8,2))
                    elif (i<=8 and j<=5) and (i>=6 and j>=3):
                        self.board[i][j] = self._remove( self.board[i][j], self.get_square(8,5))
                    elif (i<=8 and j<=8) and (i>=6 and j>=6):
                        self.board[i][j] = self._remove( self.board[i][j], self.get_square(8,8))

    def reduce_onlyone(self):
    ## Retorna true si se logro reducir almenos un elemento, de lo contrario False
        state = False
        for i in range(9):
            for j in range(9):
                if (type(self.board[i][j]) == list) and (len(self.board[i][j]) == 1):
                    self.board[i][j] = self.board[i][j][0]
                    state = True
        return state

    def reduce_all(self):
        while (True): #haga por siempre
            self.reduce_lines('h')
            self.reduce_lines('v')
            self.reduce_square()
            if not self.reduce_onlyone(): break
                
    def check_state(self):
    ## -1:No solucionable - 0:Continuable - 1:Solucionado
        state = 1
        for i in range(9):
            for j in range(9):
                if type(self.board[i][j]) == list:
                    state = 0 #Si se encontro una lista es seguro que no es solucion
                    if len(self.board[i][j]) == 0:
                        return -1 #Si una lista esta vacia es un estado invalido
        #Que no existan listas vacias no garantiza que el estado no sea invalido
        #por lo que se realiza una comprobacion mas exaustiva en la siguiente funcion
        if self._is_invalid(): state = -1
        return state

    def _is_invalid(self):
    ## Se verifica si el tablero es invalido usando dos metodos:
    ## - Primero verifica si el numero de candidatos es menor al numero de incognitas
    ##       en tal caso, el tablero es invalido
    ## - Finalmente, verifica que no existan elementos repetidos en filas y columnas
        for i in range(9):
        #Verifica filas:
            check_list = []
            lists_counter = 0
            for item in self.board[i]:
                if type(item) == list:
                    lists_counter += 1
                    check_list = self._merge(check_list, item)
            if len(check_list) < lists_counter:
                return True #Hay mas incognitas que candidatos
        #Verifica columnas:
            column = [x[i] for x in self.board]
            check_list = []
            lists_counter = 0
            for item in column:
                if type(item) == list:
                    lists_counter += 1
                    check_list = self._merge(check_list, item)
            if len(check_list) < lists_counter:
                return True #Hay mas incognitas que candidatos
        #Verifica repetidos:
        for i in range(9):
            check = []
            for item in self.board[i]:
                if type(item) == int:
                    if item in check: return True #Repetido
                    else: check.append(item)
            check = []
            column = [x[i] for x in self.board]
            for item in column:
                if type(item) == int:
                    if item in check: return True #Repetido
                    else: check.append(item)
        #Verificar repetidos en cuadrado:
        pos=[(2,2), (2,5), (2,8), (5,2), (5,5), (5,8), (8,2), (8,5), (8,8)]
        for i in pos:
            check = []
            for item in self.get_square(i[0],i[1]):
                if item in check: return True #Repetido
                else: check.append(item)
        return False

    def solve(self):
    ## Funcion maestra que intenta resolver el tablero:
        ## Se reducen todos los dominios y se verifica el estado del tablero
        self.reduce_all()
        state = self.check_state()
        if   state ==  1: print('SOLVED'); return True
        elif state == -1:
            global iterations
            iterations += 1
            return False
        
        #En este punto el estado no es solucion pero tampoco es invalido.
        #Viendo la solucion como arboles, existirian tantos arboles como elementos
        #en el dominio que escojamos. Asi que busco el primer dominio e intento resolver 
        #usando cada uno de sus elementos, alfin y al cabo uno de ellos me llevara al estado solucion
        for i in range(9):
            for j in range(9):
                if type(self.board[i][j]) == list:
                    t = [self.board[i][j], i, j] #Guardo el dominio y su posicion
                    break

        for item in t[0]:
            aux_board = copy.deepcopy(self.board)
            aux_board[t[1]][t[2]] = item
            sub = Sudoku_solver(aux_board) #Creo un nuevo tablero e intento resolverlo
            if sub.solve():
                self.board = copy.deepcopy(sub.board)
                return True
        return False

    def get_square(self,i,j):
    ## Devuelve una lista con los elementos que forman un cuadrado de 3x3
    ## donde la posicion i j corresponde a la esquina inferior izquierda del mismo
        aux = []
        for x in range(i-2,i+1): #Recorrido
            temp=j-2
            for y in range(3): #Repeticion
                if type(self.board[x][temp]) == int:
                    aux.append(self.board[x][temp])
                temp += 1 #Incremento en 1
        return aux

    def __str__(self):
    ## Sobrecarga del metodo __str__ que devuelve un string que representa
    ## al objeto.
        rpr = ""
        for i in self.board:
            for j in i:
                rpr += str(j) + ', '
            rpr += '\n'
        return rpr

    ## -----------------------------------------
    ## Funciones auxiliares para manejar listas:
    ## -----------------------------------------

    def _remove(self, x, y):
    ## Elimina de la lista x todos los elementos de la lista y
        for i in y:
            if i in x:#pregunta si i ya existe en x
                x.remove(i)#de ser asi lo remueve
        return x

    def _merge(self, x, y):
    ## Realiza una union excluyente entre X y Y
        for i in y:
            if i not in x:
                x.append(i)
        return x

if __name__ == '__main__':

    sudk1 = [[5,3,0,0,7,0,0,0,0], ##Facil
             [6,0,0,1,9,5,0,0,0],
             [0,9,8,0,0,0,0,6,0],
             [8,0,0,0,6,0,0,0,3],
             [4,0,0,8,0,3,0,0,1],
             [7,0,0,0,2,0,0,0,6],
             [0,6,0,0,0,0,2,8,0],
             [0,0,0,4,1,9,0,0,5],
             [0,0,0,0,8,0,0,7,9]]

    sudk2 = [[0,0,0,0,2,9,5,8,0], ##Dificil
             [0,6,0,4,0,0,0,0,0],
             [0,0,2,0,0,5,0,4,0],
             [1,0,4,0,0,2,0,0,0],
             [2,0,0,0,0,0,0,0,3],
             [0,0,0,9,0,0,4,0,5],
             [0,8,0,7,0,0,1,0,0],
             [0,0,0,0,0,4,0,6,0],
             [0,3,7,2,8,0,0,0,0]]

    sudk3 = [[0,0,0,8,0,0,9,0,0], ##Demonio
             [0,8,0,0,6,0,0,0,0],
             [0,0,2,0,3,9,0,0,0],
             [4,0,0,0,0,7,5,9,0],
             [0,5,3,0,0,8,4,2,0],
             [0,0,7,2,5,0,0,6,0],
             [5,0,0,9,7,0,2,0,0],
             [0,0,0,1,2,6,0,5,9],
             [0,0,0,0,0,0,0,7,0]]

    sudk4 = [[9,7,1,0,5,0,0,0,0], ##Demonio
             [0,0,3,2,0,0,0,0,8],
             [0,0,0,0,3,6,0,0,0],
             [0,5,9,0,0,0,0,0,2],
             [0,0,4,0,0,0,7,0,0],
             [6,0,0,0,0,0,8,9,0],
             [0,0,0,6,1,0,0,0,0],
             [3,0,0,0,0,8,4,0,0],
             [0,0,0,0,2,0,5,6,9]]

    sudk5 = [[0,0,0,0,4,0,0,5,0], ##Demonio
             [8,3,0,9,0,0,0,0,1],
             [2,0,6,0,0,0,0,0,0],
             [9,0,0,3,0,0,8,0,0],
             [6,8,0,0,0,0,0,2,9],
             [0,0,2,0,0,6,0,0,7],
             [0,0,0,0,0,0,9,0,3],
             [7,0,0,0,0,4,0,8,6],
             [0,6,0,0,1,0,0,0,0]]

    sudk6 = [[0,6,0,0,0,0,0,9,7], ##Demonio
             [9,0,0,0,2,1,0,0,0],
             [0,0,0,0,0,0,2,3,0],
             [7,0,0,0,8,3,0,4,0],
             [0,0,0,4,0,7,0,0,0],
             [0,2,0,9,6,0,0,0,1],
             [0,7,4,0,0,0,0,0,0],
             [0,0,0,1,3,0,0,0,6],
             [1,9,0,0,0,0,0,2,0]]

    sudk7 = [[0,0,0,0,0,1,5,0,4], ##Demonio
             [0,0,0,6,8,0,0,0,0],
             [0,0,7,0,0,0,1,0,2],
             [9,0,0,2,0,0,0,3,0],
             [0,8,0,0,9,0,0,5,0],
             [0,5,0,0,0,4,0,0,9],
             [4,0,2,0,0,0,8,0,0],
             [0,0,0,0,2,9,0,0,0],
             [6,0,1,5,0,0,0,0,0]]

    sudk8 = [[8,0,0,0,0,0,0,0,0], ##World hardest sudoku
             [0,0,3,6,0,0,0,0,0],
             [0,7,0,0,9,0,2,0,0],
             [0,5,0,0,0,7,0,0,0],
             [0,0,0,0,4,5,7,0,0],
             [0,0,0,1,0,0,0,3,0],
             [0,0,1,0,0,0,0,6,8],
             [0,0,8,5,0,0,0,1,0],
             [0,9,0,0,0,0,4,0,0]]

    sdk = Sudoku_solver(sudk8)
    sdk.solve()
    print (sdk)
    print ('In ' + str(iterations) + ' iterations.')
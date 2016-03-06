from Solver import Solver
from Board import Board

if __name__ == '__main__':

    ## No solucionables:
    #board = Board([[1,2,3],[4,5,6],[8,7,0]])

    ## Se desfazan en numero de pasos:
    #board = Board([[7,2,4],[5,0,6],[8,3,1]])
    #board = Board([[6,0,5],[8,7,4],[3,2,1]])
    board = Board([[8,6,7],[2,5,4],[3,0,1]])

    ## Solucionables de inmediato:
    #board = Board([[0,2,3],[1,4,6],[7,5,8]]) #4
    #board = Board([[1,8,2],[0,4,3],[7,6,5]]) #10
    #board = Board([[0,1,3],[4,2,5],[7,8,6]]) #5

    solver = Solver(board)
    print 'board:\n'
    print board
    print '\nsolution\n'
    print solver.moves()

    ##Take care of:
    #print len(solver.close)
    #print len(solver.opened)
    #print board
    #for i in board.neighbors():
    #    print i
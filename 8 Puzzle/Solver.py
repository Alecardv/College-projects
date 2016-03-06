## Important note:
## I have taken inspiration from this code:
## https://gist.github.com/thiagopnts/8015876


from Queue import PriorityQueue

class State(object):
    def __init__(board, weight, level, back_state):
        self.board = board
        self.weight = weight
        self.level = level
        self.back_state = back_state

class Solver(object):

    def __init__(self, board):
        self.queue = PriorityQueue()
        self.state = State(board, board.manhattan(), 0)
        self.queue.put(self.state)
        self.opened = []
        self.close = []

    def moves(self):
        level = 0
        while (not self.queue.empty()):
            current = self.queue.get()
            if current[2].isSolvable() and not self.is_in_closed(current[2]):
                if current[2].isGoal():
                    print 'encontre la solucion'
                    return self.print_list(current[3])
                else:
                    self.close.append(current[2])
                    current[2].neighbors()
                    level += 1
                    for i in current[2].neighborhood:
                        back_states = list(current[3])
                        back_states.append(current[2])
                        state = (
                            i.manhattan(),
                            level,
                            i,
                            back_states)
                        if not self.is_in_opened(i):
                            self.opened.append(i)
                            self.queue.put(state)
            else:
                continue
        return 'No tiene solucion'

    def print_list(self, _list):
        for i in _list:
            print i
        print str(len(_list))
        return 0

    def is_in_opened(self, board):
        for i in self.opened:
            if board == i:
                return True
        return False

    def is_in_closed(self, board):
        for i in self.close:
            if board == i:
                return True
        return False
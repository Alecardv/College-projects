import copy

class Board(object):

    def __init__(self, blocks):
        self.blocks = blocks

    def size(self):
        return len(self.blocks)

    def manhattan(self):
        manhattan = 0
        for i in range(self.size()):
            for j in range(self.size()):
                if self.blocks[i][j] == 0: continue
                row = (self.blocks[i][j] - 1) / self.size()
                col = (self.blocks[i][j] - 1) - self.size() * row
                manhattan += abs(row - i) + abs(col - j)
        return manhattan

    def isGoal(self):
        return self.manhattan() == 0

    def isSolvable(self):
        aux = []
        counter = 0
        w=len(self.blocks)
        for i in range(w):
            for j in range(w):
                aux.append(self.blocks[i][j])
        for i in range(w*w):
            for j in range(i+1,w*w):
                if(aux[i] and aux[j]) and aux[i] > aux[j]:
                    counter += 1
        return counter%2 == 0

    def neighbors(self):
        neighborhood = []
        for i in range(len(self.blocks)):
            for j in range(len(self.blocks[i])):
                if (self.blocks[i][j] == 0):
                    self.__neighbors_aux((i,j), (i,j+1), neighborhood)
                    self.__neighbors_aux((i,j), (i,j-1), neighborhood)
                    self.__neighbors_aux((i,j), (i+1,j), neighborhood)
                    self.__neighbors_aux((i,j), (i-1,j), neighborhood)
        return neighborhood

    def __neighbors_aux(self, a, b, neighborhood):
        new = copy.deepcopy(self.blocks)
        try:
            if b[0] < 0 or b[1] < 0:
                raise(IndexError)
            else:
                new[a[0]][a[1]] = new[b[0]][b[1]]
                new[b[0]][b[1]] = 0
                neighborhood.append(Board(new))
        except IndexError:
            pass

    def __eq__(self, b2):
        if type(b2) != Board:
            return False
        for i in range(len(self.blocks)):
            for j in range(len(self.blocks[i])):
                if self.blocks[i][j] == b2.blocks[i][j] : continue
                else: return False
        return True

    def __str__(self):
        out = ""#'%r\n\n' % self.size()
        for i in range(self.size()):
            for j in range(self.size()):
                out += ' %r' % self.blocks[i][j] if self.blocks[i][j] != 0 else '  '
            out += '\n'
        return out

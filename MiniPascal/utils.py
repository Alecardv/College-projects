from mpasast import NodeVisitor

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
class DotVisitor(NodeVisitor):  

        def __init__(self):
            self.id = 0
            self.stack = []
            self.dot = 'digraph AST {\n\tnode [shape=box]\n'

        
        def __str__(self):
            return self.dot + '}'
        

        def _id(self):
            self.id += 1
            return 'node%02d' % self.id

        
        def generic_visit(self, node):
            name = self._id()
            self.dot += '\t' + name + ' [label="' + node.__class__.__name__ + '"]\n'

            NodeVisitor.generic_visit(self,node)
            while len(self.stack) != 0:
                n = self.stack.pop()
                self.dot += '\t' + name + ' -> ' + n + '\n'
            self.stack.append(name)
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

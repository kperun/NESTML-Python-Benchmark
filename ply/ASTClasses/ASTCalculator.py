import ASTComputation
import ASTDeclaration

class ASTCalculator():
    __name = None
    __body = {}

    def __init__(self, name, body):
        self.name = name
        self.body = body

    def getName(self):
        return self.name

    def getBody(self):
        return self.body

    def getDeclarations(self):
        temp = []
        for i in self.body:
            if isinstance(i,ASTDeclaration.ASTDeclaration):
                temp.append(i)
            elif len(i) > 0:
                for d in i:
                    if isinstance(d,ASTDeclaration.ASTDeclaration):
                        for st in d.decl:
                            temp.append(st)
        return temp

    def getComputations(self):
        temp = []
        for i in self.body:
            if isinstance(i,ASTComputation.ASTComputation):
                temp.append(i)
            elif len(i) > 0:
                for d in i:
                    if isinstance(d,ASTComputation.ASTComputation):
                        for st in d.decl:
                            temp.append(st)
        #ret = [item for sublist in temp for item in sublist if item != []]

        return temp

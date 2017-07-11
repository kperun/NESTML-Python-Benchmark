import ASTStatement

class ASTComputation():
    decl = {}

    def __init__(self,decl):
        self.decl = decl

    def getDecl(self):
        temp = list()
        for dec in self.decl:
            if isinstance(dec,ASTStatement.ASTStatement):
                temp.append(dec)
            else:
                for de in dec:
                    temp.append(de)

        return temp
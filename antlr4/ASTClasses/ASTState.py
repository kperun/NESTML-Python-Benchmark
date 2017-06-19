class ASTState():
    decl = {}

    def __init__(self, decl):
        self.decl = decl

    def getDecl(self):
        return self.decl
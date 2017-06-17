class ASTState():
    decl = {}

    def ASTState(self, decl):
        self.decl = decl

    def getDecl(self):
        return self.decl
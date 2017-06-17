class ASTStatement:
    decl = None
    expr = None

    """
        Standard Constructor of this class.
    """
    def ASTStatement(self, decl, expr):
        self.decl = decl
        self.expr = expr

    """
        Returns the name.
    """
    def getName(self):
        return self.decl

    def getExpr(self):
        return self.expr

    def hasExpr(self):
        if self.expr is not None:
            return True
        else:
            return False

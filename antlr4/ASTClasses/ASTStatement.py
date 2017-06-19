class ASTStatement:
    decl = None
    expr = None

    """
        Standard Constructor of this class.
    """
    def __init__(self, decl, expr):
        self.decl = decl
        self.expr = expr

    """
        Some factory methods.
    """
    @classmethod
    def makeDeclWithExpression(cls,decl,expr):
        return cls(decl,expr)

    @classmethod
    def makeDecl(cls,decl):
        return cls(decl, None)

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

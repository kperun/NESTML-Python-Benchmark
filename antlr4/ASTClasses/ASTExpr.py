import ASTNumericLiteral
import ASTName

class ASTExpr:
    expr = None
    base = None
    exponent = None
    lhs = None
    rhs = None
    decl = None
    term = None
    isLeftBracket = False
    isRightBracket = False
    isPow = False
    isUnaryPlus = False
    isUnaryMinus = False
    isUnaryTilde = False
    isTimes = False
    isMinus = False
    isDiv = False
    isModulo = False
    isPlus = False

    def hasLeftBracket(self):
        return self.isLeftBracket

    def hasRightBracket(self):
        return self.isRightBracket

    def getIsPow(self):
        return self.isPow

    def getIsUnaryPlus(self):
        return self.isUnaryPlus

    def getIsUnaryMinus(self):
        return self.isUnaryMinus

    def getIsUnaryTilde(self):
        return self.isUnaryTilde

    def getIsTimes(self):
        return self.isTimes

    def getIsDiv(self):
        return self.isDiv

    def getIsModulo(self):
        return self.isModulo

    def getIsPlus(self):
        return self.isPlus

    def getIsMinus(self):
        return self.isMinus

    """
        The following are getters which can be used to check which type of expression it is.
    """
    def isExpression(self):
        return (self.expr is not None) and  (self.exponent is None)

    def isExponentExpression(self):
        return (self.base is not None) and (self.exponent is not None)

    def isCombinedExpression(self):
        return (self.lhs is not None) and (self.rhs is not None)

    def isDecl(self):
        return self.decl is not None

    def isTerm(self):
        return self.term is not None


    """
        Some getters.
    """
    def getExpr(self):
        return self.expr

    def getExponent(self):
        return self.exponent

    def getBase(self):
        return self.base

    def getLhs(self):
        return self.lhs

    def getRhs(self):
        return self.rhs

    def getDecl(self):
        return self.decl

    def getTerm(self):
        return self.term

    """
        The constructor for this class
    """
    def __init__(self,expr=None,base=None,exponent=None,lhs=None,rhs=None,term=None, decl = None):
        self.expr = expr
        self.base = base
        self.exponent = exponent
        self.lhs = lhs
        self.rhs = rhs
        self.term = term
        self.decl = decl

    @classmethod
    def makeExpr(cls,lhs,rhs,op):
        obj = cls(lhs=lhs, rhs=rhs)
        if op=="+":
            obj.isPlus = True
        elif op=="-":
            obj.isMinus = True
        elif op == "*":
            obj.isTimes = True
        elif op == "/":
            obj.isDiv = True
        elif op == "%":
            obj.isModulo = True
        return obj
    @classmethod
    def makeTerm(cls,term):
        return cls(term=term)

    @classmethod
    def makeDecl(cls, decl):
        return cls(decl = decl)

    @classmethod
    def makePow(cls, base, exponent):
        obj = cls(base=base, exponent=exponent)
        obj.isPow = True
        return obj

    def prettyPrint(self):
        if self.isExpression():
            if self.hasLeftBracket():
                print "(",
            self.getExpr().prettyPrint()
            if self.hasRightBracket():
                print ")"
        elif self.isTerm():
            if self.getIsUnaryPlus():
                print "+",
            elif self.getIsUnaryMinus():
                print "-",
            elif self.getIsUnaryTilde():
                print "~",
            self.getTerm().prettyPrint(),
        elif self.isExponentExpression():
            print "(",
            self.getBase().prettyPrint(),
            print ")^(",
            self.getExponent().prettyPrint(),
            print ")",
        elif self.isCombinedExpression():
            self.getLhs().prettyPrint(),
            if self.getIsPlus():
                print "+",
            elif self.getIsMinus():
                print "-",
            else:
                print "<>",
            self.getRhs().prettyPrint()
        elif self.isDecl():
            if isinstance(self.getDecl(),ASTNumericLiteral.ASTNumericLiteral):
                print self.getDecl().getValue(),
                if self.getDecl().hasUnit():
                    print self.getDecl().getUnit(),
            if isinstance(self.getDecl(),ASTName.ASTName):
                print self.getDecl().getName(),

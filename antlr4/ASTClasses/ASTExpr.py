import ASTNumericLiteral
import ASTName

class ASTExpr:
    expr = None
    base = None
    exponent = None
    lhs = None
    rhs = None
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


    def getTerm(self):
        return self.term

    """
        The constructor for this class
    """
    def __init__(self,expr=None,base=None,exponent=None,lhs=None,rhs=None,term=None):
        self.expr = expr
        self.base = base
        self.exponent = exponent
        self.lhs = lhs
        self.rhs = rhs
        self.term = term

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
    def makePow(cls, base, exponent):
        obj = cls(base=base, exponent=exponent)
        obj.isPow = True
        return obj

    def prettyPrint(self):
        temp = ""
        if self.isExpression():
            if self.hasLeftBracket():
                temp = temp + "("
            temp = temp + str(self.getExpr().prettyPrint())
            if self.hasRightBracket():
                temp = temp + ")"
        elif self.isTerm():
            if self.getIsUnaryPlus():
                temp = temp + "+"
            elif self.getIsUnaryMinus():
                temp = temp + "-"
            elif self.getIsUnaryTilde():
                temp = temp + "~"
            temp = temp + str(self.getTerm().prettyPrint())
        elif self.isExponentExpression():
            temp = temp + "("
            temp = temp + str(self.getBase().prettyPrint())
            temp = temp + ")^("
            temp = temp + str(self.getExponent().prettyPrint())
            temp = temp + ")"
        elif self.isCombinedExpression():
            temp = temp + self.getLhs().prettyPrint()
            if self.getIsPlus():
                temp = temp + "+"
            elif self.getIsMinus():
                temp = temp + "-"
            else:
                temp = temp + "<>"
            temp = temp + self.getRhs().prettyPrint()
        return temp

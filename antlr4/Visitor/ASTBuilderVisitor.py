import sys

sys.path.append('../ASTClasses')
import ASTNeuron
import ASTState
import ASTComputation
import ASTStatement
import ASTName
import ASTExpr
import ASTNumericLiteral
from antlr4 import *
from SimpleExpressionGrammerVisitor import SimpleExpressionGrammerVisitor


class ASTBuilder(ParseTreeVisitor):
    def visitAstNeuron(self, ctx):
        body = list()
        for child in ctx.astState():
            body.append(self.visit(child))
        for child in ctx.astComputation():
            body.append(self.visit(child))
        name = str(ctx.name.text)
        temp = ASTNeuron.ASTNeuron(name, body)
        return temp

    def visitAstState(self, ctx):
        decl = list()
        for child in ctx.astStatement():
            decl.append(self.visit(child))
        return ASTState.ASTState(decl)

    def visitAstComputation(self, ctx):
        decl = list()
        for child in ctx.astStatement():
            decl.append(self.visit(child))
        return ASTComputation.ASTComputation(decl)

    def visitAstDeclaration(self, ctx):
        return ASTStatement.ASTStatement.makeDecl(self.visit(ctx.astName()))

    def visitAstDeclarationWithAssignment(self, ctx):
        return ASTStatement.ASTStatement.makeDeclWithExpression((self.visit(ctx.astName())), self.visit(ctx.astExpr()))

    def visitAstName(self, ctx):
        return ASTName.ASTName(ctx.TString())

    def visitAstExpr(self, ctx):
        if ctx.unaryPlus != None:
            obj =  ASTExpr.ASTExpr.makeTerm(self.visit(ctx.expr))
            obj.isUnaryPlus = True
            return obj
        elif ctx.unaryMinus != None:
            obj = ASTExpr.ASTExpr.makeTerm(self.visit(ctx.expr))
            obj.isUnaryMinus = True
            return obj
        elif ctx.unaryTilde != None:
            obj = ASTExpr.ASTExpr.makeTerm(self.visit(ctx.expr))
            obj.isUnaryTilde = True
            return obj
        elif ctx.lhs != None and ctx.rhs != None:
            if ctx.times != None:
                return ASTExpr.ASTExpr.makeExpr(self.visit(ctx.lhs), self.visit(ctx.rhs), "*")
            elif ctx.div != None:
                return ASTExpr.ASTExpr.makeExpr(self.visit(ctx.lhs), self.visit(ctx.rhs), "/")
            elif ctx.modulo != None:
                return ASTExpr.ASTExpr.makeExpr(self.visit(ctx.lhs), self.visit(ctx.rhs), "%")
            elif ctx.plus != None:
                return ASTExpr.ASTExpr.makeExpr(self.visit(ctx.lhs), self.visit(ctx.rhs), "+")
            elif ctx.minus != None:
                return ASTExpr.ASTExpr.makeExpr(self.visit(ctx.lhs), self.visit(ctx.rhs), "-")
        elif ctx.base != None and ctx.exponent != None:
            temp = ASTExpr.ASTExpr.makePow(self.visit(ctx.base),self.visit(ctx.exponent))
            return temp
        elif ctx.leftBracket != None and ctx.rightBracket != None:
            obj = ASTExpr.ASTExpr.makeTerm( self.visit(ctx.expr))
            obj.isLeftBracket = True
            obj.isRightBracket = True
            return obj
        elif ctx.decl != None:
            return ASTExpr.ASTExpr.makeDecl(self.visit(ctx.decl))
        elif ctx.term != None:
            return ASTExpr.ASTExpr.makeDecl(self.visit(ctx.term))

    def visitAstNumericLiteral(self, ctx):
        if ctx.unit != None:
            return ASTNumericLiteral.ASTNumericLiteral.makeLiteralWithUnit(ctx.TNumber(),ctx.TString())
        else:
            return ASTNumericLiteral.ASTNumericLiteral.makeLiteral(ctx.TNumber())

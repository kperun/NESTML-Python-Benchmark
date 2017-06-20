import sys

sys.path.append('../ASTClasses')
import ASTNeuron
import ASTDeclaration
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
        for child in ctx.astDeclaration():
            body.append(self.visit(child))
        for child in ctx.astComputation():
            body.append(self.visit(child))
        name = str(ctx.name.text)
        temp = ASTNeuron.ASTNeuron(name, body)
        return temp

    def visitAstComputation(self, ctx):
        decl = list()
        for child in ctx.astStatement():
            decl.append(self.visit(child))
        return ASTComputation.ASTComputation(decl)

    def visitAstDeclaration(self, ctx):
        decl = list()
        for child in ctx.astStatement():
            decl.append(self.visit(child))
        return ASTDeclaration.ASTDeclaration(decl)

    def visitAstName(self, ctx):
        return ASTName.ASTName(ctx.TString())

    def visitAstStatement(self, ctx):
        if ctx.expr is None:
            return ASTStatement.ASTStatement(self.visit(ctx.decl),None)
        else:
            return ASTStatement.ASTStatement(self.visit(ctx.decl), self.visit(ctx.expr))

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
        elif ctx.term != None:
            return ASTExpr.ASTExpr.makeTerm(self.visit(ctx.term))

    def visitAstNumericLiteral(self, ctx):
        return ASTNumericLiteral.ASTNumericLiteral.makeLiteral(ctx.TNumber())

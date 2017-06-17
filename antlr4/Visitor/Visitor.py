import sys
from antlr4 import *

from SimpleExpressionGrammerVisitor import SimpleExpressionGrammerVisitor

class SimplePrettyPrinter(ParseTreeVisitor):
    def visitAstNeuron(self, ctx):
        print "neuron " + str(ctx.name.text) + ":"
        return self.visitChildren(ctx)

    def visitAstState(self, ctx):
        print "state:"
        return self.visitChildren(ctx)

    def visitAstComputation(self, ctx):
        print "computation:"
        return self.visitChildren(ctx)

    def visitAstDeclaration(self, ctx):
        print ctx.astName().TString()

    def visitAstDeclarationWithAssignment(self, ctx):
        print str(self.visit(ctx.astName())) + " = " + str(self.visit(ctx.astExpr()))


    def visitAstName(self, ctx):
        return ctx.TString()

    def visitAstExpr(self, ctx):
        if ctx.unaryPlus !=None:
            return "+" + str(self.visit(ctx.expr))
        elif ctx.unaryMinus !=None:
            return "-" + str(self.visit(ctx.expr))
        elif ctx.unaryTilde !=None:
            return "~" + str(self.visit(ctx.expr))
        elif ctx.lhs !=None and ctx.rhs !=None:
            if ctx.times !=None:
                return str(self.visit(ctx.lhs)) + "*" + str(self.visit(ctx.rhs))
            elif ctx.div != None:
                return str(self.visit(ctx.lhs)) + "/" + str(self.visit(ctx.rhs))
            elif ctx.modulo != None:
                return str(self.visit(ctx.lhs)) + "%" + str(self.visit(ctx.rhs))
            elif ctx.plus !=None:
                return str(self.visit(ctx.lhs)) + "+" + str(self.visit(ctx.rhs))
            elif ctx.minus !=None:
                return str(self.visit(ctx.lhs)) + "-" + str(self.visit(ctx.rhs))
        elif ctx.base!= None and ctx.exponent!=None:
            return str(self.visit(ctx.base)) + "**" + str(self.visit(ctx.exponent))
        elif ctx.leftBracket!=None and ctx.rightBracket!=None:
            return "(" + str(self.visit(ctx.expr)) + ")"
        elif ctx.decl !=None:
            return self.visit(ctx.decl)
        elif ctx.term !=None:
            return self.visit(ctx.term)


    def visitAstNumericLiteral(self, ctx):
        if ctx.unit != None:
            return str(ctx.TNumber()) + str(ctx.TString())
        else:
            return str(ctx.TNumber())

class ASTBuilder(ParseTreeVisitor):
    def visitAstNeuron(self, ctx):
        print "neuron " + str(ctx.name.text) + ":"
        return self.visitChildren(ctx)

    def visitAstState(self, ctx):
        print "state:"
        return self.visitChildren(ctx)

    def visitAstComputation(self, ctx):
        print "computation:"
        return self.visitChildren(ctx)

    def visitAstDeclaration(self, ctx):
        print ctx.astName().TString()

    def visitAstDeclarationWithAssignment(self, ctx):
        print str(self.visit(ctx.astName())) + " = " + str(self.visit(ctx.astExpr()))


    def visitAstName(self, ctx):
        return ctx.TString()

    def visitAstExpr(self, ctx):
        if ctx.unaryPlus !=None:
            return "+" + str(self.visit(ctx.expr))
        elif ctx.unaryMinus !=None:
            return "-" + str(self.visit(ctx.expr))
        elif ctx.unaryTilde !=None:
            return "~" + str(self.visit(ctx.expr))
        elif ctx.lhs !=None and ctx.rhs !=None:
            if ctx.times !=None:
                return str(self.visit(ctx.lhs)) + "*" + str(self.visit(ctx.rhs))
            elif ctx.div != None:
                return str(self.visit(ctx.lhs)) + "/" + str(self.visit(ctx.rhs))
            elif ctx.modulo != None:
                return str(self.visit(ctx.lhs)) + "%" + str(self.visit(ctx.rhs))
            elif ctx.plus !=None:
                return str(self.visit(ctx.lhs)) + "+" + str(self.visit(ctx.rhs))
            elif ctx.minus !=None:
                return str(self.visit(ctx.lhs)) + "-" + str(self.visit(ctx.rhs))
        elif ctx.base!= None and ctx.exponent!=None:
            return str(self.visit(ctx.base)) + "**" + str(self.visit(ctx.exponent))
        elif ctx.leftBracket!=None and ctx.rightBracket!=None:
            return "(" + str(self.visit(ctx.expr)) + ")"
        elif ctx.decl !=None:
            return self.visit(ctx.decl)
        elif ctx.term !=None:
            return self.visit(ctx.term)


    def visitAstNumericLiteral(self, ctx):
        if ctx.unit != None:
            return str(ctx.TNumber()) + str(ctx.TString())
        else:
            return str(ctx.TNumber())


import sys
from antlr4 import *
from SimpleExpressionGrammerVisitor import SimpleExpressionGrammerVisitor

class SimplePrettyPrinter(ParseTreeVisitor):
    def visitAstNeuron(self, ctx):
        print "calculator " + str(ctx.name.text) + ":"
        return self.visitChildren(ctx)

    def visitAstComputation(self, ctx):
        print "computation:"
        return self.visitChildren(ctx)

    def visitAstDeclaration(self, ctx):
        print "declaration:"
        return self.visitChildren(ctx)

    def visitAstStatement(self, ctx):
        if ctx.expr != None:
            print str(self.visit(ctx.astName())) + " = " + str(self.visit(ctx.astExpr()))
        else:
            print str(self.visit(ctx.astName()))


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
        elif ctx.term !=None:
            return self.visit(ctx.term)


    def visitAstNumericLiteral(self, ctx):
        return str(ctx.TNumber())


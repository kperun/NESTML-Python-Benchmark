# Generated from SimpleExpressionGrammer.g4 by ANTLR 4.7
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by SimpleExpressionGrammerParser.

class SimpleExpressionGrammerVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SimpleExpressionGrammerParser#neuron.
    def visitNeuron(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleExpressionGrammerParser#state.
    def visitState(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleExpressionGrammerParser#computation.
    def visitComputation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleExpressionGrammerParser#statementR.
    def visitStatementR(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleExpressionGrammerParser#exprR.
    def visitExprR(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleExpressionGrammerParser#termR.
    def visitTermR(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleExpressionGrammerParser#numericLiteralR.
    def visitNumericLiteralR(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleExpressionGrammerParser#nameR.
    def visitNameR(self, ctx):
        return self.visitChildren(ctx)



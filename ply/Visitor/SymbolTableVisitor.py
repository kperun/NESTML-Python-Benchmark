import sys

sys.path.append('../ASTClasses')
sys.path.append('../SymbolTable')
import ASTNeuron
import ASTDeclaration
import ASTComputation
import ASTStatement
import ASTName
import ASTExpr
import ASTNumericLiteral
import ASTBuilderVisitor
import SymbolTable
from antlr4 import *
from SimpleExpressionGrammerVisitor import SimpleExpressionGrammerVisitor

class SymbolTableBuilder(ParseTreeVisitor):
    def visitAstNeuron(self, ctx):
        table = SymbolTable.SimpleSymbolTable()
        expression_visitor = ASTBuilderVisitor.ASTBuilder()
        for child in ctx.astDeclaration():
            for child in child.astStatement():
                table.insert(str(child.decl.TString()),
                             expression_visitor.visit(child.expr))
        return table
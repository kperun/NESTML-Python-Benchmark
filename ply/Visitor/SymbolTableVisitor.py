import sys

sys.path.append('../ASTClasses')
sys.path.append('../SymbolTable')
import ASTCalculator
import ASTDeclaration
import ASTComputation
import ASTStatement
import ASTName
import ASTExpr
import ASTNumericLiteral
import ASTBuilderVisitor
from SymbolTable import SimpleSymbolTable
from antlr4 import *

class SymbolTableBuilder():
    def visitAstCalculator(self, ast):
        table = SimpleSymbolTable()
        for decl in ast.getDeclarations():
            if isinstance(decl,ASTStatement.ASTStatement):
                table.insert(decl.getName(),decl.getExpr())
            else:
                for st in decl:
                    table.insert(st.getName(),st.getExpr())
        return table
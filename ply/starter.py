import sys
from antlr4 import *
sys.path.append('build/Grammar')
sys.path.append('Visitor')
sys.path.append('ASTClasses')
sys.path.append('Symboltable/SymbolTable')
sys.path.append('CoCos')
sys.path.append('Backend')
import ply.lex as lex
import ply.yacc as yacc
from TreePrinter import TreePrinter
from SimpleExpressionGrammar import *
from SymbolTableVisitor import SymbolTableBuilder
from OnlyDeclared import OnlyDeclaredCoCo


def main(argv):
    input = FileStream("testExpession")
    # First build the lexer
    lexer = lex.lex()
    parser = yacc.yacc()
    lexer.input(str(input))
    #print str(input)
    #for tok in lexer:
    #    print(tok)
    print "Start generating AST",
    calculator = parser.parse(str(input))
    print "done"
    print "---------Print AST:---------"
    TreePrinter.printTree(calculator) # print the ast
    print "----------------------------"
    print "Creating Symbol table ...",
    visitor3 = SymbolTableBuilder()
    symbol_table = visitor3.visitAstCalculator(calculator)
    print "done"
    print "--------Symbol Table:-------"
    symbol_table.printTable()
    print "----------------------------"
    print "Check CoCos....",
    OnlyDeclaredCoCo.checkTree(calculator, symbol_table)
    print "done"

if __name__ == '__main__':
    main(sys.argv)

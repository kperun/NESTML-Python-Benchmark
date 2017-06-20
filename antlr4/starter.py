import sys
from antlr4 import *
sys.path.append('build/Grammar')
sys.path.append('Visitor')
sys.path.append('ASTClasses')
sys.path.append('Symboltable/SymbolTable')
sys.path.append('CoCos')

from ASTBuilderVisitor import *
from SimpleExpressionGrammerLexer import SimpleExpressionGrammerLexer
from PrettyPrinterVisitor import *
from SimpleExpressionGrammerParser import SimpleExpressionGrammerParser
from SymbolTableVisitor import *
from TreePrinter import *
from OnlyDeclared import *
from SymbolTable import *



def main(argv):
    input = FileStream("testExpession")
    lexer = SimpleExpressionGrammerLexer(input)
    stream = CommonTokenStream(lexer)
    parser = SimpleExpressionGrammerParser(stream)
    tree = parser.astNeuron()
    print "---------Print parse tree:---------"
    # first print the tree
    visitor = SimplePrettyPrinter()
    visitor.visit(tree)
    # now create an AST from the given tree
    print "---------Print AST:---------"
    visitor2 = ASTBuilder()
    calculator = visitor2.visit(tree)
    TreePrinter.printTree(calculator) # print the ast
    print "----------------------------"
    print "Creating Symbol table ..."
    visitor3 = SymbolTableBuilder()
    symbol_table = visitor3.visit(tree)
    print "--------Symbol Table:-------"
    symbol_table.printTable()
    print "----------------------------"
    print "Check CoCos...."
    OnlyDeclaredCoCo.checkTree(calculator, symbol_table)


if __name__ == '__main__':
    main(sys.argv)

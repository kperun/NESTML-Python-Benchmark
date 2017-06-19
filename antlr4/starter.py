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
    input = FileStream("testExpession.nestml")
    lexer = SimpleExpressionGrammerLexer(input)
    stream = CommonTokenStream(lexer)
    parser = SimpleExpressionGrammerParser(stream)
    tree = parser.astNeuron()
    visitor = SimplePrettyPrinter()
    visitor2 = ASTBuilder()
    visitor3 = SymbolTableBuilder()
    visitor.visit(tree)
    neuron  = visitor2.visit(tree)
    symbol_table = visitor3.visit(tree)
    print "-----------------"
    TreePrinter.printTree(neuron)
    print "-----------------"
    symbol_table.printTable()
    print "-----------------"
    OnlyDeclaredCoCo.checkTree(neuron, symbol_table)


if __name__ == '__main__':
    main(sys.argv)

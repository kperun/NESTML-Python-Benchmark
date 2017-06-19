import sys
from antlr4 import *
sys.path.append('build/Grammar')
sys.path.append('Visitor')
sys.path.append('ASTClasses')

from ASTBuilderVisitor import *
from SimpleExpressionGrammerLexer import SimpleExpressionGrammerLexer
from PrettyPrinterVisitor import *
from SimpleExpressionGrammerParser import SimpleExpressionGrammerParser
from TreePrinter import *



def main(argv):
    input = FileStream("testExpession.nestml")
    lexer = SimpleExpressionGrammerLexer(input)
    stream = CommonTokenStream(lexer)
    parser = SimpleExpressionGrammerParser(stream)
    tree = parser.astNeuron()
    visitor = SimplePrettyPrinter()
    visitor2 = ASTBuilder()
    visitor.visit(tree)
    neuron  = visitor2.visit(tree)
    print "-----------------"
    TreePrinter.printTree(neuron)


if __name__ == '__main__':
    main(sys.argv)

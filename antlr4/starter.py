import sys
from antlr4 import *
sys.path.append('build/Grammar')
sys.path.append('Visitor')

from SimpleExpressionGrammerLexer import SimpleExpressionGrammerLexer
from Visitor import *
from SimpleExpressionGrammerParser import SimpleExpressionGrammerParser




def main(argv):
    input = FileStream("testExpession.nestml")
    lexer = SimpleExpressionGrammerLexer(input)
    stream = CommonTokenStream(lexer)
    parser = SimpleExpressionGrammerParser(stream)
    tree = parser.astNeuron()
    visitor = SimplePrettyPrinter()
    visitor.visit(tree)


if __name__ == '__main__':
    main(sys.argv)

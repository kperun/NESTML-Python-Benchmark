from antlr4 import *
from SimpleExpressionGrammerLexer import SimpleExpressionGrammerLexer
#from SimpleExpressionGrammerListener import SimpleExpressionGrammerListener
from SimpleExpressionGrammerVisitor import SimpleExpressionGrammerVisitor
from SimpleExpressionGrammerParser import SimpleExpressionGrammerParser
import sys

class SimpleVisitor(ParseTreeVisitor):
    def visitNeuron(self, ctx):
        return self.visit(ctx.e(0))


def main(argv):
    input = FileStream(argv[1])
    lexer = SimpleExpressionGrammerLexer(input)
    stream = CommonTokenStream(lexer)
    parser = SimpleExpressionGrammerParser(stream)
    tree = parser.neuron()
    visitor = SimpleVisitor()
    string = tree.toStringTree(recog=parser)
    print string
    #walker = ParseTreeWalker()
    #walker.walk(visitor, tree)


if __name__ == '__main__':
    main(sys.argv)

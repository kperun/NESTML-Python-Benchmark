import sys
sys.path.append('ASTClasses')
from pyparsing import *
#from ASTCalculator import *
#from ASTStatement import *

# first the tokens
PLUS = Literal("+")
MINUS = Literal("-")
MULT = Literal("*")
DIV = Literal("/")
LPARAM = Literal("(").suppress()
RPARAM = Literal(")").suppress()
POW = Literal("^")
EQ = Literal("=")
NUMBER = Word(nums)
STRING = Word(alphas)
CALCULATOR = Literal("calculator")
DECLARATION = Literal("declaration")
COMPUTATION = Literal("computation")
END = Literal("end")
NL = Literal("\n")

tokens = []

def push( str, loc, toks ):
    tokens.append( toks[0] )

# now the grammar
# forwarddeclaration -> first define parts, then the overall one

astExpr = NUMBER

astStatement = (STRING + Optional(EQ + astExpr)).setParseAction(push)

astDeclaration = (DECLARATION + ':' + (NL) + astStatement + END).setParseAction(push)
astComputation = (COMPUTATION + ':'+ NL + astStatement + END).setParseAction(push)


astNeuron = (CALCULATOR + STRING + ':' + NL + Optional(astDeclaration) + Optional(astComputation) + END + StringEnd()).setParseAction(push)

testString = \
"calculator testCalculation: declaration: end end"

R = astNeuron.parseString(testString)
print R

import ply.lex as lex
import sys
sys.path.append('../ASTClasses')
import ASTNeuron

tokens = ('TNUMBER', 'END', 'CALCULATOR', 'TSTRING', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MODULO', 'POW',
          'LPARAN', 'RPARAN', 'COLON')

#Tokens

def t_END(t): r'end'; return t               # the end token
def t_CALCULATOR(t): r'calculator'; return t
t_TSTRING = '[a-zA-Z\\_]+'  # a string token
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_POW = r'\*\*'
t_DIVIDE = r'/'
t_MODULO = r'%'
t_LPARAN = r'\('
t_RPARAN = r'\)'
t_COLON = r':'


def t_TNumber(t):
    r"[0-9]+"  # a number token , e.g. 42
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore = ' \t'

# Precedence rules for the arithmetic operators
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    #('right', 'unaryMinus'),
    )


# store the overall context
calculator = None

def p_calculator(p):
    """astNeuron : CALCULATOR"""
    #calculator = ASTNeuron(p[2])
    print "aaaa"

def p_error(p):
    print("Syntax error at '%s'" % p.value)

"""
astNeuron : 'calculator' name=TString ':' EOL (astDeclaration|astComputation|EOL)* END EOL EOF;

astDeclaration : 'declaration' ':' EOL (astStatement)* END EOL;

astComputation : 'computation' ':' EOL (astStatement)* END EOL;

astStatement : decl=astName '=' expr=astExpr EOL;

astExpr   : leftBracket='(' expr=astExpr rightBracket=')'
       |<assorc=right> base=astExpr lpow='**' exponent=astExpr
       | (unaryPlus='+' | unaryMinus='-') expr=astExpr
       | lhs=astExpr (times='*' | div='/' | modulo='%') rhs=astExpr
       | lhs=astExpr (plus='+' | minus='-') rhs=astExpr
       | term=astTerm;

astTerm : astNumericLiteral | astName;

astNumericLiteral : value=TNumber;
"""



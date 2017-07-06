import ply.lex as lex
import sys

sys.path.append('../ASTClasses')
import ASTCalculator

tokens = ['NUMBER', 'END', 'CALCULATOR', 'STRING', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MODULO', 'POW',
          'LPAREN', 'RPAREN', 'COLON','NEWLINE','DECLARATION','COMPUTATION','EQ']

#Tokens

def t_END(t): r'end';return t
def t_CALCULATOR(t): r'calculator';return t
def t_DECLARATION(t): r'declaration';return t
def t_COMPUTATION(t): r'computation';return t
t_STRING = '[a-zA-Z\\_]+'  # a string token
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_POW = r'\*\*'
t_DIVIDE = r'/'
t_MODULO = r'%'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COLON = r':'
t_EQ = r'='

#t_NEWLINE = r'\n'

def t_NUMBER(t):
    r"[0-9]+"  # a number token , e.g. 42
    t.value = int(t.value)
    return t


def t_NEWLINE(t):
    r'\n+' # a new lie token
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore = ' \t \n'

# Precedence rules for the arithmetic operators
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    #('right', 'unaryMinus'),
    )


# store the overall context
calculator = None

start = 'astCalculator'


def p_expression_plus(p):
    'astCalculator : CALCULATOR STRING COLON astBody END'
    calculator = ASTCalculator.ASTCalculator(str(p[2]),[p[4]])
    


def p_body(p):
    """
    astBody : DECLARATION COLON astDeclaration 
            | COMPUTATION COLON astComputation 
    """
    #p[0] = p[1]

def p_declaration(p):
    """
    astDeclaration : STRING 
                   | STRING EQ astExpression
    """

def p_computation(p):
    'astComputation : STRING EQ astExpression'

def p_expression(p):
    """
    astExpression : NUMBER
                  | STRING
                  | LPAREN astExpression RPAREN
                  | astExpression POW astExpression
                  | PLUS astExpression
                  | MINUS astExpression
                  | astExpression TIMES astExpression
                  | astExpression DIVIDE astExpression
                  | astExpression PLUS astExpression
                  | astExpression MINUS astExpression
                  | astExpression MODULO astExpression
                  | 
    """




def p_error(p):
    print("Syntax error at '%s'" % p.value)

"""
astCalculator : 'calculator' name=TString ':' EOL (astDeclaration|astComputation|EOL)* END EOL EOF;

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



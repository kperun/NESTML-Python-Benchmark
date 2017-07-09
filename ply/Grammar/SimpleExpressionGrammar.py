import ply.lex as lex
import sys

sys.path.append('../ASTClasses')
import ASTCalculator
import ASTDeclaration
import ASTComputation
import ASTStatement
import ASTNumericLiteral
import ASTName
import ASTExpr


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


def p_astCalculator(p):
    'astCalculator : CALCULATOR STRING COLON astBody END'
    p[0] = ASTCalculator.ASTCalculator(str(p[2]),[p[4]])



def p_body(p):
    """
    astBody : DECLARATION COLON astDeclaration END
            | COMPUTATION COLON astComputation END
            | astBody astBody
    """
    if p[2] == ':' and p[1]=="declaration":#the header
        p[0] =  ASTDeclaration.ASTDeclaration([p[3]])
    elif p[2] == ':' and p[1]=="computation":
        p[0] = ASTComputation.ASTComputation([p[3]])
    else:
        p[0] = [p[1],p[2]]


def p_declaration(p):
    """
    astDeclaration : STRING 
                   | STRING EQ astExpression
                   | astDeclaration astDeclaration
    """
    if len(p) == 2:# case sole declration
        p[0] = ASTStatement.ASTStatement.makeDecl(p[1])
    elif len(p) == 4:
        p[0] = ASTStatement.ASTStatement.makeDeclWithExpression(p[1],p[3])
    else:
        p[0] = [p[1],p[2]]



def p_computation(p):
    'astComputation : STRING EQ astExpression'
    p[0] = ASTStatement.ASTStatement.makeDeclWithExpression(p[1],p[3])

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
    if len(p)==2:
        if type(p[1]) == int:
            p[0] = ASTNumericLiteral.ASTNumericLiteral.makeLiteral(p[1])
        else:
            p[0] = ASTName.ASTName(p[1])
    elif len(p)==3:
        if p[1]=='+':
            p[0] = ASTExpr.ASTExpr.makeTerm(p[2])
            p[0].isUnaryPlus = True
        else:
            p[0] = ASTExpr.ASTExpr.makeTerm(p[2])
            p[0].isUnaryMinus = True
    elif len(p)==4:
        if p[1]=='(' and p[3] == ')':
            p[0] = ASTExpr.ASTExpr.makeTerm(p[2])
            p[0].leftBracket = True
            p[0].rightBracket = True
        elif p[2]=='**':
            p[0] = ASTExpr.ASTExpr.makePow(p[1],p[3])
        else:
            p[0] = ASTExpr.ASTExpr.makeExpr(p[1],p[3],p[2])


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



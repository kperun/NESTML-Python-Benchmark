grammar SimpleExpressionGrammer;

astNeuron : 'calculator' name=TString ':' EOL (astDeclaration|astComputation|EOL)* END EOL EOF;

astDeclaration : 'declaration' ':' EOL (astStatement)* END EOL;

astComputation : 'computation' ':' EOL (astStatement)* END EOL;

astStatement : decl=astName '=' expr=astExpr EOL;

astExpr   : leftBracket='(' expr=astExpr rightBracket=')'
       |<assorc=right> base=astExpr lpow='**' exponent=astExpr
       | (unaryPlus='+' | unaryMinus='-' | unaryTilde='~') expr=astExpr
       | lhs=astExpr (times='*' | div='/' | modulo='%') rhs=astExpr
       | lhs=astExpr (plus='+' | minus='-') rhs=astExpr
       | term=astTerm;

astTerm : astNumericLiteral | astName;

astNumericLiteral : value=TNumber;

astName : TString;

TNumber : [0-9]+;


EOL : ('\r'?'\n'|'\r');

WS : (' '|'\t') -> skip;



END : 'end';

TString : [a-zA-Z\\_]+;


grammar SimpleExpressionGrammer;

astNeuron : 'neuron' name=TString ':' EOL (astState|astComputation|EOL)* END EOL EOF;

astState : 'state' ':' EOL (astStatement)* END EOL;

astComputation : 'computation' ':' EOL (astStatement)* END EOL;

astStatement : decl=astName EOL #astDeclaration | decl=astName '=' expr=astExpr EOL #astDeclarationWithAssignment;

astExpr   : leftBracket='(' expr=astExpr rightBracket=')'
       |<assorc=right> base=astExpr lpow='**' exponent=astExpr
       | (unaryPlus='+' | unaryMinus='-' | unaryTilde='~') expr=astExpr
       | lhs=astExpr (times='*' | div='/' | modulo='%') rhs=astExpr
       | lhs=astExpr (plus='+' | minus='-') rhs=astExpr
       | decl=astName
       | term=astTerm;

astTerm : astNumericLiteral | astName;

astNumericLiteral : value=TNumber (unit=TString)?;

astName : TString;

TNumber : [0-9]+;


EOL : ('\r'?'\n'|'\r');

WS : (' '|'\t') -> skip;



END : 'end';

TString : [a-zA-Z\\_]+;


grammar SimpleExpressionGrammer;

neuron : 'neuron' name=TString ':' (state|computation|EOL)* END EOF;


state : 'state' ':' (EOL|statementR)* END;

computation : 'computation' ':' (EOL|statementR)* END;

statementR : exprR EOL | nameR '=' exprR EOL;

exprR   : '(' exprR ')'
       |<assorc=right> base=exprR lpow='**' exponent=exprR //(a**b**c == a ** (b ** c))
       | ('+' | '-' | '~') term=exprR
       | exprR ('*' | '/' | '%') exprR
       | exprR ('+' | '-') exprR
       | termR;

termR : numericLiteralR | nameR;

numericLiteralR : TNumber (TString)?;

nameR : TString;

TNumber : [0-9]+;

EOL : '\n';

END : 'end';

TString : [a-zA-Z\\_]+;


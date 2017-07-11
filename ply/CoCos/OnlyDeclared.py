import ASTCalculator
import ASTComputation
import ASTDeclaration
import ASTNumericLiteral
import ASTStatement

class OnlyDeclaredCoCo:
    @classmethod
    def checkTree(cls,calculator,symbol_table):
        for block in calculator.getBody():
            if isinstance(block,ASTComputation.ASTComputation):
                for statement in block.getDecl():
                    if not statement.hasExpr():
                        raise DeclarationInComputationBlockException
                    for var in statement.getExpr().getVariables():
                        isDefined = False
                        for block in calculator.getBody():
                            if isinstance(block, ASTDeclaration.ASTDeclaration):
                                for statement in block.getDecl():
                                    if str(statement.getName().prettyPrint()) == str(var):
                                        isDefined = True
                        if not isDefined:
                            raise NotDefinedVariableException


            elif isinstance(block,ASTDeclaration.ASTDeclaration):
                for statement in block.getDecl():
                    if len(statement.getExpr().getVariables()):
                        print statement.getExpr().getVariables()
                        raise VariablesInDeclarationsBlockException
            elif len(block)>0:
                for subblock in block:
                    if isinstance(subblock, ASTComputation.ASTComputation):
                        for statement in subblock.getDecl():
                            if not statement.hasExpr():
                                raise DeclarationInComputationBlockException
                            for var in statement.getExpr().getVariables():
                                if symbol_table.lookUp(var) is None:
                                    raise NotDefinedVariableException

                    # only numbers, no variables allowed in the declaration block
                    elif isinstance(subblock, ASTDeclaration.ASTDeclaration):
                        for statement in subblock.getDecl():
                            if isinstance(statement,ASTStatement.ASTStatement) and len(statement.getExpr().getVariables())>0:
                                print statement.getExpr().getVariables()
                                raise VariablesInDeclarationsBlockException
                            elif (not isinstance(statement,ASTStatement.ASTStatement)) and len(statement)>0:
                                for elem in statement:
                                    if (not isinstance(elem.getExpr,ASTNumericLiteral.ASTNumericLiteral)):#and len(elem.getExpr().getVariables())
                                        if len(elem.getExpr().getVariables()):
                                            print elem.getExpr().getVariables()
                                            raise VariablesInDeclarationsBlockException
    @classmethod
    def isDefined(cls,symbol,symbol_table):
        if symbol in symbol_table:
            return True
        else:
            return False


class DeclarationInComputationBlockException(Exception):
    pass

class VariablesInDeclarationsBlockException(Exception):
    pass

class NotDefinedVariableException(Exception):
    pass
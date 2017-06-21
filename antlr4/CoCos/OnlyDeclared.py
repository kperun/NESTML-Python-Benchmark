import ASTNeuron
import ASTComputation
import ASTDeclaration


class OnlyDeclaredCoCo:
    @classmethod
    def checkTree(cls,neuron,symbol_table):
        for block in neuron.getBody():
            if isinstance(block,ASTComputation.ASTComputation):
                for statement in block.getDecl():
                    if not statement.hasExpr():
                        raise DeclarationInComputationBlockException
                    for var in statement.getExpr().getVariables():
                        isDefined = False
                        for block in neuron.getBody():
                            if isinstance(block, ASTDeclaration.ASTDeclaration):
                                for statement in block.getDecl():
                                    if str(statement.getName().prettyPrint()) == str(var):
                                        isDefined = True
                        if not isDefined:
                            raise NotDefinedVariableException


            if isinstance(block,ASTDeclaration.ASTDeclaration):
                for statement in block.getDecl():
                    if len(statement.getExpr().getVariables()):
                        print statement.getExpr().getVariables()
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
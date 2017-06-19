import ASTNeuron
import ASTComputation

class OnlyDeclaredCoCo:
    @classmethod
    def checkTree(cls,neuron,symbol_table):
        for block in neuron.getBody():
            if isinstance(block,ASTComputation.ASTComputation):
                for statement in block.getDecl():
                    if not statement.hasExpr():
                        raise DeclarationInComputationBlockException
                    

    @classmethod
    def isDefined(cls,symbol,symbol_table):
        if symbol in symbol_table:
            return True
        else:
            return False


class DeclarationInComputationBlockException(Exception):
    pass
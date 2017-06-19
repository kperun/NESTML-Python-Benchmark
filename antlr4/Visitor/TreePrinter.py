import ASTNeuron
import ASTState
import ASTComputation
import ASTStatement
import ASTName
import ASTExpr
import ASTNumericLiteral
import types

class TreePrinter:
    @classmethod
    def printTree(cls,elem):
        if isinstance(elem,ASTNeuron.ASTNeuron):
            print "neuron " + str(elem.getName()) + ":"
            for part in elem.getBody():
                TreePrinter.printTree(part)
            print "end"
        if isinstance(elem,ASTState.ASTState):
            print "state: "
            for part in elem.getDecl():
                TreePrinter.printTree(part)
            print "end"
        if isinstance(elem,ASTComputation.ASTComputation):
            print "computation: "
            for part in elem.getDecl():
                TreePrinter.printTree(part)
            print "end"
        if isinstance(elem,ASTStatement.ASTStatement):
            if elem.hasExpr():
                print str(elem.getName().getName()),
                print " = ",
                TreePrinter.printTree(elem.getExpr())
                print ""
            else:
                print str(elem.getName().getName())
        if isinstance(elem,ASTExpr.ASTExpr):
            elem.prettyPrint()

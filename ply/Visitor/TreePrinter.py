import ASTCalculator
import ASTDeclaration
import ASTComputation
import ASTStatement
import ASTName
import ASTExpr
import ASTNumericLiteral
import types

class TreePrinter:
    @classmethod
    def printTree(cls,elem):
        if isinstance(elem,ASTCalculator.ASTCalculator):
            print "calculator " + str(elem.getName()) + ":"
            for part in elem.getBody()[0]:
                TreePrinter.printTree(part)
            print "end"
        if isinstance(elem,ASTDeclaration.ASTDeclaration):
            print "declaration: "
            for part in elem.getDecl():
                if isinstance(part,ASTStatement.ASTStatement):
                    TreePrinter.printTree(part)
                else:
                    for p in part:
                        TreePrinter.printTree(p)
            print "end"
        if isinstance(elem,ASTComputation.ASTComputation):
            print "computation: "
            for part in elem.getDecl():
                if isinstance(part, ASTStatement.ASTStatement):
                    TreePrinter.printTree(part)
                else:
                    for p in part:
                        TreePrinter.printTree(p)
            print "end"
        if isinstance(elem,ASTStatement.ASTStatement):
            if elem.hasExpr():
                print str(elem.getName()),
                print " = ",
                TreePrinter.printTree(elem.getExpr())
            else:
                print str(elem.getName())
        if isinstance(elem,ASTExpr.ASTExpr):
            print elem.prettyPrint()

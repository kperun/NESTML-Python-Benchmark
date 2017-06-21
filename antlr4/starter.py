import sys
from antlr4 import *
sys.path.append('build/Grammar')
sys.path.append('Visitor')
sys.path.append('ASTClasses')
sys.path.append('Symboltable/SymbolTable')
sys.path.append('CoCos')
sys.path.append('Backend')

from ASTBuilderVisitor import *
from SimpleExpressionGrammerLexer import SimpleExpressionGrammerLexer
from PrettyPrinterVisitor import *
from SimpleExpressionGrammerParser import SimpleExpressionGrammerParser
from SymbolTableVisitor import *
from TreePrinter import *
from OnlyDeclared import *
from SymbolTable import *
from Cheetah.Template import Template
import os


def main(argv):
    input = FileStream("testExpession")
    lexer = SimpleExpressionGrammerLexer(input)
    stream = CommonTokenStream(lexer)
    parser = SimpleExpressionGrammerParser(stream)
    tree = parser.astNeuron()
    print "---------Print parse tree:---------"

    # first print the tree
    visitor = SimplePrettyPrinter()
    visitor.visit(tree)
    # now create an AST from the given tree
    print "---------Print AST:---------"
    visitor2 = ASTBuilder()
    calculator = visitor2.visit(tree)
    TreePrinter.printTree(calculator) # print the ast
    print "----------------------------"
    print "Creating Symbol table ..."
    visitor3 = SymbolTableBuilder()
    symbol_table = visitor3.visit(tree)
    print "--------Symbol Table:-------"
    symbol_table.printTable()
    print "----------------------------"
    print "Check CoCos...."
    OnlyDeclaredCoCo.checkTree(calculator, symbol_table)
    print "Start printing with Cheetah..."
    nameSpace = {'name':calculator.getName(),'decl':calculator.getDeclarations(),'comp':calculator.getComputations()}
    t = Template(file='Backend/Cheetah/template.tmpl',searchList=nameSpace)
    # open a file and write the generated code
    with open("cheetah_code.cpp", "w+") as f:
        f.write(str(t))

if __name__ == '__main__':
    main(sys.argv)

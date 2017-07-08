import sys
from antlr4 import *
sys.path.append('build/Grammar')
sys.path.append('Visitor')
sys.path.append('ASTClasses')
sys.path.append('Symboltable/SymbolTable')
sys.path.append('CoCos')
sys.path.append('Backend')
import ply.lex as lex
import ply.yacc as yacc
from TreePrinter import TreePrinter
from SimpleExpressionGrammar import *

def main(argv):
    input = FileStream("testExpession")
    # First build the lexer
    lexer = lex.lex()
    parser = yacc.yacc()
    lexer.input(str(input))
    #print str(input)
    #for tok in lexer:
    #    print(tok)
    print "Start generating AST",
    calculator = parser.parse(str(input))
    print "done"
    print "---------Print AST:---------"
    TreePrinter.printTree(calculator) # print the ast

    """
    lexer = SimpleExpressionGrammerLexer(input)
    stream = CommonTokenStream(lexer)
    parser = SimpleExpressionGrammerParser(stream)
    tree = parser.astNeuron()
    print "---------Print parse tree:---------"

    # first print the tree
    visitor = SimplePrettyPrinter()
    visitor.visit(tree)
    # now create an AST from the given tree
    visitor2 = ASTBuilder()
    calculator = visitor2.visit(tree)
    print "---------Print AST:---------"
    TreePrinter.printTree(calculator) # print the ast
    print "----------------------------"
    print "Creating Symbol table ..."
    visitor3 = SymbolTableBuilder()
    symbol_table = visitor3.visit(tree)
    print "--------Symbol Table:-------"
    symbol_table.printTable()
    print "----------------------------"
    print "Check CoCos....",
    OnlyDeclaredCoCo.checkTree(calculator, symbol_table)
    print "done"
    print "Start printing with Cheetah...",
    nameSpace = {'name':calculator.getName(),'decl':calculator.getDeclarations(),'comp':calculator.getComputations()}
    tC = Template(file='Backend/Cheetah/template.tmpl',searchList=nameSpace)
    # open a file and write the generated code
    with open("cheetah_code.cpp", "w+") as f:
        f.write(str(tC))
    print "done"
    # now print it by means of jinja
    print "Start printing with Jinja...",
    env = Environment(loader=FileSystemLoader('Backend/Jinja'))
    tJ = env.get_template('template.html')
    output = tJ.render(nameSpace)
    with open("jinja_code.cpp", "w+") as f:
        f.write(str(output))
    print "done"
    # now print it by means of tenjin
    print "Start printing with Tenjin...",
    engine = tenjin.Engine(path=['Backend/Tenjin/'])
    output = engine.render('template.pyhtml',nameSpace)
    with open("tenjin_code.cpp", "w+") as f:
        f.write(str(output))
    print "done"
    """


if __name__ == '__main__':
    main(sys.argv)

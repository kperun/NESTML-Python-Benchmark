# Generated from SimpleExpressionGrammer.g4 by ANTLR 4.7
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2")
        buf.write(u"\24g\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3")
        buf.write(u"\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write(u"\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3")
        buf.write(u"\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17")
        buf.write(u"\3\20\6\20Y\n\20\r\20\16\20Z\3\21\3\21\3\22\3\22\3\22")
        buf.write(u"\3\22\3\23\6\23d\n\23\r\23\16\23e\2\2\24\3\3\5\4\7\5")
        buf.write(u"\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35")
        buf.write(u"\20\37\21!\22#\23%\24\3\2\4\3\2\62;\6\2C\\^^aac|\2h\2")
        buf.write(u"\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write(u"\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write(u"\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write(u"\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2")
        buf.write(u"\2%\3\2\2\2\3\'\3\2\2\2\5.\3\2\2\2\7\60\3\2\2\2\t\66")
        buf.write(u"\3\2\2\2\13B\3\2\2\2\rD\3\2\2\2\17F\3\2\2\2\21H\3\2\2")
        buf.write(u"\2\23K\3\2\2\2\25M\3\2\2\2\27O\3\2\2\2\31Q\3\2\2\2\33")
        buf.write(u"S\3\2\2\2\35U\3\2\2\2\37X\3\2\2\2!\\\3\2\2\2#^\3\2\2")
        buf.write(u"\2%c\3\2\2\2\'(\7p\2\2()\7g\2\2)*\7w\2\2*+\7t\2\2+,\7")
        buf.write(u"q\2\2,-\7p\2\2-\4\3\2\2\2./\7<\2\2/\6\3\2\2\2\60\61\7")
        buf.write(u"u\2\2\61\62\7v\2\2\62\63\7c\2\2\63\64\7v\2\2\64\65\7")
        buf.write(u"g\2\2\65\b\3\2\2\2\66\67\7e\2\2\678\7q\2\289\7o\2\29")
        buf.write(u":\7r\2\2:;\7w\2\2;<\7v\2\2<=\7c\2\2=>\7v\2\2>?\7k\2\2")
        buf.write(u"?@\7q\2\2@A\7p\2\2A\n\3\2\2\2BC\7?\2\2C\f\3\2\2\2DE\7")
        buf.write(u"*\2\2E\16\3\2\2\2FG\7+\2\2G\20\3\2\2\2HI\7,\2\2IJ\7,")
        buf.write(u"\2\2J\22\3\2\2\2KL\7-\2\2L\24\3\2\2\2MN\7/\2\2N\26\3")
        buf.write(u"\2\2\2OP\7\u0080\2\2P\30\3\2\2\2QR\7,\2\2R\32\3\2\2\2")
        buf.write(u"ST\7\61\2\2T\34\3\2\2\2UV\7\'\2\2V\36\3\2\2\2WY\t\2\2")
        buf.write(u"\2XW\3\2\2\2YZ\3\2\2\2ZX\3\2\2\2Z[\3\2\2\2[ \3\2\2\2")
        buf.write(u"\\]\7\f\2\2]\"\3\2\2\2^_\7g\2\2_`\7p\2\2`a\7f\2\2a$\3")
        buf.write(u"\2\2\2bd\t\3\2\2cb\3\2\2\2de\3\2\2\2ec\3\2\2\2ef\3\2")
        buf.write(u"\2\2f&\3\2\2\2\5\2Ze\2")
        return buf.getvalue()


class SimpleExpressionGrammerLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    TNumber = 15
    EOL = 16
    END = 17
    TString = 18

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'neuron'", u"':'", u"'state'", u"'computation'", u"'='", u"'('", 
            u"')'", u"'**'", u"'+'", u"'-'", u"'~'", u"'*'", u"'/'", u"'%'", 
            u"'\n'", u"'end'" ]

    symbolicNames = [ u"<INVALID>",
            u"TNumber", u"EOL", u"END", u"TString" ]

    ruleNames = [ u"T__0", u"T__1", u"T__2", u"T__3", u"T__4", u"T__5", 
                  u"T__6", u"T__7", u"T__8", u"T__9", u"T__10", u"T__11", 
                  u"T__12", u"T__13", u"TNumber", u"EOL", u"END", u"TString" ]

    grammarFileName = u"SimpleExpressionGrammer.g4"

    def __init__(self, input=None, output=sys.stdout):
        super(SimpleExpressionGrammerLexer, self).__init__(input, output=output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



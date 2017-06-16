# Generated from SimpleExpressionGrammer.g4 by ANTLR 4.7
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\24c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write(u"\4\b\t\b\4\t\t\t\3\2\3\2\3\2\3\2\3\2\3\2\7\2\31\n\2\f")
        buf.write(u"\2\16\2\34\13\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3%\n\3")
        buf.write(u"\f\3\16\3(\13\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4\60\n\4\f")
        buf.write(u"\4\16\4\63\13\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write(u"\5\5\5?\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6I\n\6")
        buf.write(u"\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6T\n\6\f\6\16")
        buf.write(u"\6W\13\6\3\7\3\7\5\7[\n\7\3\b\3\b\5\b_\n\b\3\t\3\t\3")
        buf.write(u"\t\2\3\n\n\2\4\6\b\n\f\16\20\2\5\3\2\13\r\3\2\16\20\3")
        buf.write(u"\2\13\f\2i\2\22\3\2\2\2\4 \3\2\2\2\6+\3\2\2\2\b>\3\2")
        buf.write(u"\2\2\nH\3\2\2\2\fZ\3\2\2\2\16\\\3\2\2\2\20`\3\2\2\2\22")
        buf.write(u"\23\7\3\2\2\23\24\7\24\2\2\24\32\7\4\2\2\25\31\5\4\3")
        buf.write(u"\2\26\31\5\6\4\2\27\31\7\22\2\2\30\25\3\2\2\2\30\26\3")
        buf.write(u"\2\2\2\30\27\3\2\2\2\31\34\3\2\2\2\32\30\3\2\2\2\32\33")
        buf.write(u"\3\2\2\2\33\35\3\2\2\2\34\32\3\2\2\2\35\36\7\23\2\2\36")
        buf.write(u"\37\7\2\2\3\37\3\3\2\2\2 !\7\5\2\2!&\7\4\2\2\"%\7\22")
        buf.write(u"\2\2#%\5\b\5\2$\"\3\2\2\2$#\3\2\2\2%(\3\2\2\2&$\3\2\2")
        buf.write(u"\2&\'\3\2\2\2\')\3\2\2\2(&\3\2\2\2)*\7\23\2\2*\5\3\2")
        buf.write(u"\2\2+,\7\6\2\2,\61\7\4\2\2-\60\7\22\2\2.\60\5\b\5\2/")
        buf.write(u"-\3\2\2\2/.\3\2\2\2\60\63\3\2\2\2\61/\3\2\2\2\61\62\3")
        buf.write(u"\2\2\2\62\64\3\2\2\2\63\61\3\2\2\2\64\65\7\23\2\2\65")
        buf.write(u"\7\3\2\2\2\66\67\5\n\6\2\678\7\22\2\28?\3\2\2\29:\5\20")
        buf.write(u"\t\2:;\7\7\2\2;<\5\n\6\2<=\7\22\2\2=?\3\2\2\2>\66\3\2")
        buf.write(u"\2\2>9\3\2\2\2?\t\3\2\2\2@A\b\6\1\2AB\7\b\2\2BC\5\n\6")
        buf.write(u"\2CD\7\t\2\2DI\3\2\2\2EF\t\2\2\2FI\5\n\6\6GI\5\f\7\2")
        buf.write(u"H@\3\2\2\2HE\3\2\2\2HG\3\2\2\2IU\3\2\2\2JK\f\7\2\2KL")
        buf.write(u"\7\n\2\2LT\5\n\6\bMN\f\5\2\2NO\t\3\2\2OT\5\n\6\6PQ\f")
        buf.write(u"\4\2\2QR\t\4\2\2RT\5\n\6\5SJ\3\2\2\2SM\3\2\2\2SP\3\2")
        buf.write(u"\2\2TW\3\2\2\2US\3\2\2\2UV\3\2\2\2V\13\3\2\2\2WU\3\2")
        buf.write(u"\2\2X[\5\16\b\2Y[\5\20\t\2ZX\3\2\2\2ZY\3\2\2\2[\r\3\2")
        buf.write(u"\2\2\\^\7\21\2\2]_\7\24\2\2^]\3\2\2\2^_\3\2\2\2_\17\3")
        buf.write(u"\2\2\2`a\7\24\2\2a\21\3\2\2\2\16\30\32$&/\61>HSUZ^")
        return buf.getvalue()


class SimpleExpressionGrammerParser ( Parser ):

    grammarFileName = "SimpleExpressionGrammer.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'neuron'", u"':'", u"'state'", u"'computation'", 
                     u"'='", u"'('", u"')'", u"'**'", u"'+'", u"'-'", u"'~'", 
                     u"'*'", u"'/'", u"'%'", u"<INVALID>", u"'\n'", u"'end'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"TNumber", 
                      u"EOL", u"END", u"TString" ]

    RULE_neuron = 0
    RULE_state = 1
    RULE_computation = 2
    RULE_statementR = 3
    RULE_exprR = 4
    RULE_termR = 5
    RULE_numericLiteralR = 6
    RULE_nameR = 7

    ruleNames =  [ u"neuron", u"state", u"computation", u"statementR", u"exprR", 
                   u"termR", u"numericLiteralR", u"nameR" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    TNumber=15
    EOL=16
    END=17
    TString=18

    def __init__(self, input, output=sys.stdout):
        super(SimpleExpressionGrammerParser, self).__init__(input, output=output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class NeuronContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SimpleExpressionGrammerParser.NeuronContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token

        def END(self):
            return self.getToken(SimpleExpressionGrammerParser.END, 0)

        def EOF(self):
            return self.getToken(SimpleExpressionGrammerParser.EOF, 0)

        def TString(self):
            return self.getToken(SimpleExpressionGrammerParser.TString, 0)

        def state(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleExpressionGrammerParser.StateContext)
            else:
                return self.getTypedRuleContext(SimpleExpressionGrammerParser.StateContext,i)


        def computation(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleExpressionGrammerParser.ComputationContext)
            else:
                return self.getTypedRuleContext(SimpleExpressionGrammerParser.ComputationContext,i)


        def EOL(self, i=None):
            if i is None:
                return self.getTokens(SimpleExpressionGrammerParser.EOL)
            else:
                return self.getToken(SimpleExpressionGrammerParser.EOL, i)

        def getRuleIndex(self):
            return SimpleExpressionGrammerParser.RULE_neuron

        def enterRule(self, listener):
            if hasattr(listener, "enterNeuron"):
                listener.enterNeuron(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNeuron"):
                listener.exitNeuron(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitNeuron"):
                return visitor.visitNeuron(self)
            else:
                return visitor.visitChildren(self)




    def neuron(self):

        localctx = SimpleExpressionGrammerParser.NeuronContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_neuron)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.match(SimpleExpressionGrammerParser.T__0)
            self.state = 17
            localctx.name = self.match(SimpleExpressionGrammerParser.TString)
            self.state = 18
            self.match(SimpleExpressionGrammerParser.T__1)
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimpleExpressionGrammerParser.T__2) | (1 << SimpleExpressionGrammerParser.T__3) | (1 << SimpleExpressionGrammerParser.EOL))) != 0):
                self.state = 22
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SimpleExpressionGrammerParser.T__2]:
                    self.state = 19
                    self.state()
                    pass
                elif token in [SimpleExpressionGrammerParser.T__3]:
                    self.state = 20
                    self.computation()
                    pass
                elif token in [SimpleExpressionGrammerParser.EOL]:
                    self.state = 21
                    self.match(SimpleExpressionGrammerParser.EOL)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 27
            self.match(SimpleExpressionGrammerParser.END)
            self.state = 28
            self.match(SimpleExpressionGrammerParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StateContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SimpleExpressionGrammerParser.StateContext, self).__init__(parent, invokingState)
            self.parser = parser

        def END(self):
            return self.getToken(SimpleExpressionGrammerParser.END, 0)

        def EOL(self, i=None):
            if i is None:
                return self.getTokens(SimpleExpressionGrammerParser.EOL)
            else:
                return self.getToken(SimpleExpressionGrammerParser.EOL, i)

        def statementR(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleExpressionGrammerParser.StatementRContext)
            else:
                return self.getTypedRuleContext(SimpleExpressionGrammerParser.StatementRContext,i)


        def getRuleIndex(self):
            return SimpleExpressionGrammerParser.RULE_state

        def enterRule(self, listener):
            if hasattr(listener, "enterState"):
                listener.enterState(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitState"):
                listener.exitState(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitState"):
                return visitor.visitState(self)
            else:
                return visitor.visitChildren(self)




    def state(self):

        localctx = SimpleExpressionGrammerParser.StateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_state)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(SimpleExpressionGrammerParser.T__2)
            self.state = 31
            self.match(SimpleExpressionGrammerParser.T__1)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimpleExpressionGrammerParser.T__5) | (1 << SimpleExpressionGrammerParser.T__8) | (1 << SimpleExpressionGrammerParser.T__9) | (1 << SimpleExpressionGrammerParser.T__10) | (1 << SimpleExpressionGrammerParser.TNumber) | (1 << SimpleExpressionGrammerParser.EOL) | (1 << SimpleExpressionGrammerParser.TString))) != 0):
                self.state = 34
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SimpleExpressionGrammerParser.EOL]:
                    self.state = 32
                    self.match(SimpleExpressionGrammerParser.EOL)
                    pass
                elif token in [SimpleExpressionGrammerParser.T__5, SimpleExpressionGrammerParser.T__8, SimpleExpressionGrammerParser.T__9, SimpleExpressionGrammerParser.T__10, SimpleExpressionGrammerParser.TNumber, SimpleExpressionGrammerParser.TString]:
                    self.state = 33
                    self.statementR()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 39
            self.match(SimpleExpressionGrammerParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ComputationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SimpleExpressionGrammerParser.ComputationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def END(self):
            return self.getToken(SimpleExpressionGrammerParser.END, 0)

        def EOL(self, i=None):
            if i is None:
                return self.getTokens(SimpleExpressionGrammerParser.EOL)
            else:
                return self.getToken(SimpleExpressionGrammerParser.EOL, i)

        def statementR(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleExpressionGrammerParser.StatementRContext)
            else:
                return self.getTypedRuleContext(SimpleExpressionGrammerParser.StatementRContext,i)


        def getRuleIndex(self):
            return SimpleExpressionGrammerParser.RULE_computation

        def enterRule(self, listener):
            if hasattr(listener, "enterComputation"):
                listener.enterComputation(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitComputation"):
                listener.exitComputation(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitComputation"):
                return visitor.visitComputation(self)
            else:
                return visitor.visitChildren(self)




    def computation(self):

        localctx = SimpleExpressionGrammerParser.ComputationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_computation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(SimpleExpressionGrammerParser.T__3)
            self.state = 42
            self.match(SimpleExpressionGrammerParser.T__1)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimpleExpressionGrammerParser.T__5) | (1 << SimpleExpressionGrammerParser.T__8) | (1 << SimpleExpressionGrammerParser.T__9) | (1 << SimpleExpressionGrammerParser.T__10) | (1 << SimpleExpressionGrammerParser.TNumber) | (1 << SimpleExpressionGrammerParser.EOL) | (1 << SimpleExpressionGrammerParser.TString))) != 0):
                self.state = 45
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SimpleExpressionGrammerParser.EOL]:
                    self.state = 43
                    self.match(SimpleExpressionGrammerParser.EOL)
                    pass
                elif token in [SimpleExpressionGrammerParser.T__5, SimpleExpressionGrammerParser.T__8, SimpleExpressionGrammerParser.T__9, SimpleExpressionGrammerParser.T__10, SimpleExpressionGrammerParser.TNumber, SimpleExpressionGrammerParser.TString]:
                    self.state = 44
                    self.statementR()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
            self.match(SimpleExpressionGrammerParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementRContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SimpleExpressionGrammerParser.StatementRContext, self).__init__(parent, invokingState)
            self.parser = parser

        def exprR(self):
            return self.getTypedRuleContext(SimpleExpressionGrammerParser.ExprRContext,0)


        def EOL(self):
            return self.getToken(SimpleExpressionGrammerParser.EOL, 0)

        def nameR(self):
            return self.getTypedRuleContext(SimpleExpressionGrammerParser.NameRContext,0)


        def getRuleIndex(self):
            return SimpleExpressionGrammerParser.RULE_statementR

        def enterRule(self, listener):
            if hasattr(listener, "enterStatementR"):
                listener.enterStatementR(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitStatementR"):
                listener.exitStatementR(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitStatementR"):
                return visitor.visitStatementR(self)
            else:
                return visitor.visitChildren(self)




    def statementR(self):

        localctx = SimpleExpressionGrammerParser.StatementRContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statementR)
        try:
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.exprR(0)
                self.state = 53
                self.match(SimpleExpressionGrammerParser.EOL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.nameR()
                self.state = 56
                self.match(SimpleExpressionGrammerParser.T__4)
                self.state = 57
                self.exprR(0)
                self.state = 58
                self.match(SimpleExpressionGrammerParser.EOL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprRContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SimpleExpressionGrammerParser.ExprRContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.base = None # ExprRContext
            self.term = None # ExprRContext
            self.lpow = None # Token
            self.exponent = None # ExprRContext

        def exprR(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleExpressionGrammerParser.ExprRContext)
            else:
                return self.getTypedRuleContext(SimpleExpressionGrammerParser.ExprRContext,i)


        def termR(self):
            return self.getTypedRuleContext(SimpleExpressionGrammerParser.TermRContext,0)


        def getRuleIndex(self):
            return SimpleExpressionGrammerParser.RULE_exprR

        def enterRule(self, listener):
            if hasattr(listener, "enterExprR"):
                listener.enterExprR(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitExprR"):
                listener.exitExprR(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitExprR"):
                return visitor.visitExprR(self)
            else:
                return visitor.visitChildren(self)



    def exprR(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleExpressionGrammerParser.ExprRContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_exprR, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SimpleExpressionGrammerParser.T__5]:
                self.state = 63
                self.match(SimpleExpressionGrammerParser.T__5)
                self.state = 64
                self.exprR(0)
                self.state = 65
                self.match(SimpleExpressionGrammerParser.T__6)
                pass
            elif token in [SimpleExpressionGrammerParser.T__8, SimpleExpressionGrammerParser.T__9, SimpleExpressionGrammerParser.T__10]:
                self.state = 67
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimpleExpressionGrammerParser.T__8) | (1 << SimpleExpressionGrammerParser.T__9) | (1 << SimpleExpressionGrammerParser.T__10))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 68
                localctx.term = self.exprR(4)
                pass
            elif token in [SimpleExpressionGrammerParser.TNumber, SimpleExpressionGrammerParser.TString]:
                self.state = 69
                self.termR()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 83
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 81
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = SimpleExpressionGrammerParser.ExprRContext(self, _parentctx, _parentState)
                        localctx.base = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exprR)
                        self.state = 72
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 73
                        localctx.lpow = self.match(SimpleExpressionGrammerParser.T__7)
                        self.state = 74
                        localctx.exponent = self.exprR(6)
                        pass

                    elif la_ == 2:
                        localctx = SimpleExpressionGrammerParser.ExprRContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exprR)
                        self.state = 75
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 76
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimpleExpressionGrammerParser.T__11) | (1 << SimpleExpressionGrammerParser.T__12) | (1 << SimpleExpressionGrammerParser.T__13))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 77
                        self.exprR(4)
                        pass

                    elif la_ == 3:
                        localctx = SimpleExpressionGrammerParser.ExprRContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exprR)
                        self.state = 78
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 79
                        _la = self._input.LA(1)
                        if not(_la==SimpleExpressionGrammerParser.T__8 or _la==SimpleExpressionGrammerParser.T__9):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 80
                        self.exprR(3)
                        pass

             
                self.state = 85
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class TermRContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SimpleExpressionGrammerParser.TermRContext, self).__init__(parent, invokingState)
            self.parser = parser

        def numericLiteralR(self):
            return self.getTypedRuleContext(SimpleExpressionGrammerParser.NumericLiteralRContext,0)


        def nameR(self):
            return self.getTypedRuleContext(SimpleExpressionGrammerParser.NameRContext,0)


        def getRuleIndex(self):
            return SimpleExpressionGrammerParser.RULE_termR

        def enterRule(self, listener):
            if hasattr(listener, "enterTermR"):
                listener.enterTermR(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTermR"):
                listener.exitTermR(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitTermR"):
                return visitor.visitTermR(self)
            else:
                return visitor.visitChildren(self)




    def termR(self):

        localctx = SimpleExpressionGrammerParser.TermRContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_termR)
        try:
            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SimpleExpressionGrammerParser.TNumber]:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.numericLiteralR()
                pass
            elif token in [SimpleExpressionGrammerParser.TString]:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.nameR()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumericLiteralRContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SimpleExpressionGrammerParser.NumericLiteralRContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TNumber(self):
            return self.getToken(SimpleExpressionGrammerParser.TNumber, 0)

        def TString(self):
            return self.getToken(SimpleExpressionGrammerParser.TString, 0)

        def getRuleIndex(self):
            return SimpleExpressionGrammerParser.RULE_numericLiteralR

        def enterRule(self, listener):
            if hasattr(listener, "enterNumericLiteralR"):
                listener.enterNumericLiteralR(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNumericLiteralR"):
                listener.exitNumericLiteralR(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitNumericLiteralR"):
                return visitor.visitNumericLiteralR(self)
            else:
                return visitor.visitChildren(self)




    def numericLiteralR(self):

        localctx = SimpleExpressionGrammerParser.NumericLiteralRContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_numericLiteralR)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(SimpleExpressionGrammerParser.TNumber)
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 91
                self.match(SimpleExpressionGrammerParser.TString)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NameRContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SimpleExpressionGrammerParser.NameRContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TString(self):
            return self.getToken(SimpleExpressionGrammerParser.TString, 0)

        def getRuleIndex(self):
            return SimpleExpressionGrammerParser.RULE_nameR

        def enterRule(self, listener):
            if hasattr(listener, "enterNameR"):
                listener.enterNameR(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNameR"):
                listener.exitNameR(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitNameR"):
                return visitor.visitNameR(self)
            else:
                return visitor.visitChildren(self)




    def nameR(self):

        localctx = SimpleExpressionGrammerParser.NameRContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_nameR)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(SimpleExpressionGrammerParser.TString)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.exprR_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exprR_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         





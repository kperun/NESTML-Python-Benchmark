
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'astCalculatorleftPLUSMINUSleftTIMESDIVIDENUMBER END CALCULATOR STRING PLUS MINUS TIMES DIVIDE MODULO POW LPAREN RPAREN COLON NEWLINE DECLARATION COMPUTATION EQastCalculator : CALCULATOR STRING COLON astBody END\n    astBody : DECLARATION COLON astDeclaration END\n            | COMPUTATION COLON astComputation END\n            | astBody astBody\n    \n    astDeclaration : STRING \n                   | STRING EQ astExpression\n                   | astDeclaration astDeclaration\n    \n    astComputation : STRING EQ astExpression\n                   | astComputation astComputation     \n    \n        astExpression : NUMBER\n                      | STRING\n                      | LPAREN astExpression RPAREN\n                      | astExpression POW astExpression\n                      | PLUS astExpression\n                      | MINUS astExpression\n                      | astExpression TIMES astExpression\n                      | astExpression DIVIDE astExpression\n                      | astExpression PLUS astExpression\n                      | astExpression MINUS astExpression\n                      | astExpression MODULO astExpression\n                      | \n    '
    
_lr_action_items = {'PLUS':([16,19,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,],[25,25,-11,33,-10,25,25,25,33,25,25,25,25,25,25,-14,33,-15,33,-17,33,-16,-18,-19,-12,]),'DIVIDE':([16,19,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,],[-21,-21,-11,30,-10,-21,-21,-21,30,-21,-21,-21,-21,-21,-21,30,30,30,30,-17,30,-16,30,30,-12,]),'END':([7,11,13,14,15,16,17,18,19,20,21,22,23,24,25,27,28,29,30,31,32,33,34,35,37,38,39,40,41,42,43,44,],[10,-4,17,-5,20,-21,-3,-9,-21,-2,-7,-11,-8,-10,-21,-21,-6,-21,-21,-21,-21,-21,-21,-14,-15,-20,-17,-13,-16,-18,-19,-12,]),'STRING':([2,8,9,13,14,15,16,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,38,39,40,41,42,43,44,],[3,12,14,12,-5,14,22,12,22,14,-11,-8,-10,22,22,22,-6,22,22,22,22,22,22,-14,-15,-20,-17,-13,-16,-18,-19,-12,]),'POW':([16,19,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,],[-21,-21,-11,31,-10,-21,-21,-21,31,-21,-21,-21,-21,-21,-21,-14,31,-15,31,-17,31,-16,-18,-19,-12,]),'CALCULATOR':([0,],[2,]),'NUMBER':([16,19,25,26,27,29,30,31,32,33,34,],[24,24,24,24,24,24,24,24,24,24,24,]),'RPAREN':([22,24,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,],[-11,-10,-21,-21,-21,-21,-21,-21,-21,-21,-21,-14,44,-15,-20,-17,-13,-16,-18,-19,-12,]),'TIMES':([16,19,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,],[-21,-21,-11,32,-10,-21,-21,-21,32,-21,-21,-21,-21,-21,-21,32,32,32,32,-17,32,-16,32,32,-12,]),'COLON':([3,5,6,],[4,8,9,]),'COMPUTATION':([4,7,11,17,20,],[5,5,5,-3,-2,]),'DECLARATION':([4,7,11,17,20,],[6,6,6,-3,-2,]),'LPAREN':([16,19,25,26,27,29,30,31,32,33,34,],[26,26,26,26,26,26,26,26,26,26,26,]),'MODULO':([16,19,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,],[-21,-21,-11,29,-10,-21,-21,-21,29,-21,-21,-21,-21,-21,-21,-14,29,-15,29,-17,29,-16,-18,-19,-12,]),'EQ':([12,14,],[16,19,]),'MINUS':([16,19,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,],[27,27,-11,34,-10,27,27,27,34,27,27,27,27,27,27,-14,34,-15,34,-17,34,-16,-18,-19,-12,]),'$end':([1,10,],[0,-1,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'astCalculator':([0,],[1,]),'astComputation':([8,13,18,],[13,18,18,]),'astExpression':([16,19,25,26,27,29,30,31,32,33,34,],[23,28,35,36,37,38,39,40,41,42,43,]),'astDeclaration':([9,15,21,],[15,21,21,]),'astBody':([4,7,11,],[7,11,11,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> astCalculator","S'",1,None,None,None),
  ('astCalculator -> CALCULATOR STRING COLON astBody END','astCalculator',5,'p_astCalculator','SimpleExpressionGrammar.py',69),
  ('astBody -> DECLARATION COLON astDeclaration END','astBody',4,'p_body','SimpleExpressionGrammar.py',76),
  ('astBody -> COMPUTATION COLON astComputation END','astBody',4,'p_body','SimpleExpressionGrammar.py',77),
  ('astBody -> astBody astBody','astBody',2,'p_body','SimpleExpressionGrammar.py',78),
  ('astDeclaration -> STRING','astDeclaration',1,'p_declaration','SimpleExpressionGrammar.py',90),
  ('astDeclaration -> STRING EQ astExpression','astDeclaration',3,'p_declaration','SimpleExpressionGrammar.py',91),
  ('astDeclaration -> astDeclaration astDeclaration','astDeclaration',2,'p_declaration','SimpleExpressionGrammar.py',92),
  ('astComputation -> STRING EQ astExpression','astComputation',3,'p_computation','SimpleExpressionGrammar.py',105),
  ('astComputation -> astComputation astComputation','astComputation',2,'p_computation','SimpleExpressionGrammar.py',106),
  ('astExpression -> NUMBER','astExpression',1,'p_expression','SimpleExpressionGrammar.py',115),
  ('astExpression -> STRING','astExpression',1,'p_expression','SimpleExpressionGrammar.py',116),
  ('astExpression -> LPAREN astExpression RPAREN','astExpression',3,'p_expression','SimpleExpressionGrammar.py',117),
  ('astExpression -> astExpression POW astExpression','astExpression',3,'p_expression','SimpleExpressionGrammar.py',118),
  ('astExpression -> PLUS astExpression','astExpression',2,'p_expression','SimpleExpressionGrammar.py',119),
  ('astExpression -> MINUS astExpression','astExpression',2,'p_expression','SimpleExpressionGrammar.py',120),
  ('astExpression -> astExpression TIMES astExpression','astExpression',3,'p_expression','SimpleExpressionGrammar.py',121),
  ('astExpression -> astExpression DIVIDE astExpression','astExpression',3,'p_expression','SimpleExpressionGrammar.py',122),
  ('astExpression -> astExpression PLUS astExpression','astExpression',3,'p_expression','SimpleExpressionGrammar.py',123),
  ('astExpression -> astExpression MINUS astExpression','astExpression',3,'p_expression','SimpleExpressionGrammar.py',124),
  ('astExpression -> astExpression MODULO astExpression','astExpression',3,'p_expression','SimpleExpressionGrammar.py',125),
  ('astExpression -> <empty>','astExpression',0,'p_expression','SimpleExpressionGrammar.py',126),
]

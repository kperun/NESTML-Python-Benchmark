class Statement:
    variable = None
    type = None
    expression = None

    def __init__(self,statement):
        self.variable = statement.getName().getName()
        if statement.hasExpr():
            self.type = 'computation'
            self.expression = statement.getExpr()
        else:
            self.type = 'declaration'

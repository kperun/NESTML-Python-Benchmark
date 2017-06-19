class ASTNumericLiteral:
    value = None
    unit = None

    def __init__(self,value,unit):
        self.value = value
        self.unit = unit

    @classmethod
    def makeLiteral(cls,value):
        return cls(value,None)

    @classmethod
    def makeLiteralWithUnit(cls,value,unit):
        return cls(value,unit)


    def ASTNumericLiteral(self,value):
        self.value = value

    def getValue(self):
        return self.value

    def getUnit(self):
        return self.unit

    def hasUnit(self):
        if self.unit is not None:
            return True
        else:
            return False

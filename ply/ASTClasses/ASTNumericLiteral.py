class ASTNumericLiteral:
    value = None

    def __init__(self,value):
        self.value = value

    @classmethod
    def makeLiteral(cls,value):
        return cls(value)

    def getValue(self):
        return self.value

    def prettyPrint(self):
        return self.value
    def getVariables(self):
        return []
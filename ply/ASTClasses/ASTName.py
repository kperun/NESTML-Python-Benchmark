
class ASTName:
    name = None
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def prettyPrint(self):
        return self.name
    def getVariables(self):
        return [self.name]
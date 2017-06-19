
class ASTNeuron():
    __name = None
    __body = {}

    def __init__(self, name, body):
        self.name = name
        self.body = body

    def getName(self):
        return self.name

    def getBody(self):
        return self.body
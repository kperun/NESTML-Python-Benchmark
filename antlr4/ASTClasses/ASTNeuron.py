
class ASTNeuron():
    name = None
    body = {}

    def ASTNeuron(self, name, body):
        self.name = name
        self.body = body

    def getName(self):
        return self.name

    def getBody(self):
        return self.body
class Computation:
    statements = None

    def __init__(self):
        self.statements = []

    def appendStatement(self, statement):
        self.statements.append(statement)
class Neuron:
    name = None
    blocks = []


    def __init__(self, name):
        self.name = name

    def appendBlock(self,block):
        self.blocks.append(block)


class SimpleSymbolTable:
    symbolLookUpTable = None

    def __init__(self):
        self.symbolLookUpTable = {}

    def insert(self, key, value):
        if key in self.symbolLookUpTable.keys():
            print "Redeclaration of " + str(key)
            raise RedeclarationException
        else:
            self.symbolLookUpTable[key] = value


    def printTable(self):
        if self.symbolLookUpTable is not None:
            for i in self.symbolLookUpTable:
                print "Key:" + str(i) + " Value: " + str(self.symbolLookUpTable[i].prettyPrint())

class RedeclarationException(Exception):
    pass

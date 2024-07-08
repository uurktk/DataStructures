class Deque:
    def __init__(self):
        self.elements = []

    def addLeft(self,x):
        self.elements.insert(0,x)

    def addRight(self,x):
        self.elements.append(x)

    def popLeft(self):
        return self.elements.pop(0)

    def popRight(self):
        return self.elements.pop()

    def isEmpty(self):
        return self.elements == []

    def size(self):
        return len(self.elements)
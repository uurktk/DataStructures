class Stack:
    def __init__(self):
        self.elements = []

    def push(self, x):
        self.elements.append(x)

    def pop(self):
        return self.elements.pop()

    def isEmpty(self):
        return self.elements == []

    def size(self):
        return len(self.elements)

    def showLast(self):
        return self.elements[-1]
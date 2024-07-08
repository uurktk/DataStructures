class Queue:
    def __init__(self):
        self.elements = []

    def enqueue(self,x):
        self.elements.insert(0,x)

    def dequeue(self):
        return self.elements.pop()

    def size(self):
        return len(self.elements)

    def isEmpty(self):
        return self.elements == []
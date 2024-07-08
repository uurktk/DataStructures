# Solution of "Implement Stack using Queues"
from collections import deque


class MyStack(object):

    def __init__(self):
        self.elements = deque()

    def push(self, x):
        self.elements.append(x)

    def pop(self):
        size = len(self.elements)
        for i in range(size - 1):
            self.elements.append(self.elements.popleft())
        return self.elements.popleft()

    def top(self):
        return self.elements[-1]

    def empty(self):
        return len(self.elements) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

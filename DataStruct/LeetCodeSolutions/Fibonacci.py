class Solution(object):
    def fib(self, n):
        if n==0:
            return 0
        if n==1:
            return 1
        return self.fib(n-2)+self.fib(n-1)

class OtherSolution(object):
    def fib(self, n):
        x, y = 0, 1
        for i in range(n):
            x, y = y, x + y

        return x
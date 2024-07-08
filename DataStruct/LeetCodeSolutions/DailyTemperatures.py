class Solution(object):
    def dailyTemperatures(self, temperatures):

        days = [0] * len(temperatures)
        myStack = []

        for i, temp in enumerate(temperatures):
            while myStack and temp > myStack[-1][0]:
                stackTemp, stackIndex = myStack.pop()
                days[stackIndex] = i - stackIndex
            myStack.append([temp,i])

        return days
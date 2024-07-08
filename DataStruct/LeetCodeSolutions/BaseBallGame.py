"""
 '+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Input: ops = ["5","2","C","D","+"]
Output: 30
Solution of "BaseBall Game"
"""
class Solution(object):
    def calPoints(self, operations):

        scores = []

        for i in operations:
            if i == "+":
                scores.append(scores[-1] + scores[-2])
            elif i =="D":
                scores.append(2 * scores[-1])
            elif i == "C":
                scores.pop()
            else:
                scores.append(int(i))

        return sum(scores)
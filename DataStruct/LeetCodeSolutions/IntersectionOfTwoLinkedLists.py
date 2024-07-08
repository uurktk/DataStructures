# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        x = headA
        y = headB

        while x != y:
            # If we are at the end, continue with other one
            x = x.next if x != None else headB
            y = y.next if y != None else headA

        return x

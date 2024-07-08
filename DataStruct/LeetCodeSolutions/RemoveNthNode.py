# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        x_pointer = head
        y_pointer = head

        # Iterate the list with n distance between (x,y) pairs.
        while n > 0 and y_pointer:
            y_pointer = y_pointer.next
            n -= 1

        # y will be the last element.
        while y_pointer and y_pointer.next:
            y_pointer = y_pointer.next
            x_pointer = x_pointer.next

        # Remove the next node of x which is the nth node from end
        if x_pointer == head and not y_pointer:
            return head.next
        x_pointer.next = x_pointer.next.next

        return head
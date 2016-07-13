# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        ret = ListNode(-1)
        start = ret
        step = 0
        while l1 !=None or l2 != None:
            v1 = 0
            if l1 != None:
                v1 = l1.val
            v2 = 0
            if l2 != None:
                v2 = l2.val
            tot = v1 + v2 + step
            ret.next = ListNode(tot%10)
            ret = ret.next
            step = tot/10
            if l1 != None:
                l1 = l1.next
            if l2!=None:
                l2 = l2.next
        if step > 0:
            ret.next = ListNode(step)
        return start.next
        
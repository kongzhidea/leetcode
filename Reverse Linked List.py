# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        cur = head
        pre = None
        while cur != None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre
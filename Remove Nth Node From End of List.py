# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        cur = head
        for i in range(n -1):
            cur = cur.next

        pre = None
        nt = head
        while cur.next != None:
            cur = cur.next
            pre = nt
            nt = nt.next
        if pre == None:
            head = head.next
        else:
            pre.next = nt.next
        return head
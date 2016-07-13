# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        ret = ListNode(-1)
        start = ret
        lnode = []
        while head !=None:
            lnode.append(head)
            head = head.next
        for i in xrange(0,len(lnode),2):
            if i + 1 < len(lnode):
                ret.next = ListNode(lnode[i+1].val)
                ret = ret.next
            ret.next = ListNode(lnode[i].val)
            ret =ret.next
        return start.next
        
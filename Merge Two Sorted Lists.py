# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        head = ListNode(-1)
        ret = head
        h1 = l1
        h2 = l2
        while h1 and h2:
            if h1.val < h2.val:
                node = ListNode(h1.val)
                head.next = node
                h1 = h1.next
            else:
                node = ListNode(h2.val)
                head.next = node
                h2 = h2.next
            head = head.next
        if h1:
            head.next = h1
        if h2:
            head.next = h2
        return ret.next
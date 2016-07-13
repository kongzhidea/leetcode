# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None:
            return None
        link = ListNode(-1)
        pre = head
        tail = head.next
        link_tail =  ListNode(pre.val)
        link.next = link_tail
        while tail :
            if tail.val == pre.val:
                tail = tail.next
                continue
            link_tail.next = ListNode(tail.val)
            link_tail = link_tail.next
            pre = tail
            tail = tail.next
        return link.next
        
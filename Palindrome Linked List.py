# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return True
        if head.next == None:
            return True
        after = self.partition(head)
        rev_after = self.reverse(after)

        h = head
        p = rev_after
        while h != None:
            if h.val != p.val:
                return False
            h = h.next
            p = p.next
        return True

    def reverse(self,head):
        if head == None or head.next == None:
            return head
        t = None
        h = head
        while h != None:
            a = h.next
            h.next = t
            t = h
            h = a
        return t

    def partition(self,head):
        h = head
        p = head
        pre = h
        while p.next != None and p.next.next != None:
            p = p.next.next
            pre = h
            h = h.next
        if p.next == None:
            t = pre.next
            pre.next = None
            return t
        if p.next != None:
            t = h.next
            h.next = None
            return t
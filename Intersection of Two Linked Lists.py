class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA == None or headB == None:
            return None
        lena = self.getListLength(headA)
        lenb = self.getListLength(headB)

        ha = headA
        hb = headB
        if lena > lenb:
            for i in range(lena - lenb):
                ha = ha.next
        elif lena < lenb:
            for i in range(lenb - lena):
                hb = hb.next

        while ha!=None :
            if ha.val == hb.val:
                return ha
            ha = ha.next
            hb = hb.next
        return None

    def getListLength(self,head):
        length = 0
        while head !=None:
            length +=1
            head = head.next
        return length

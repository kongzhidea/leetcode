class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        count = 0
        for i,v in enumerate(A):
            if v != elem:
                A[count] = v
                count +=1
        return count
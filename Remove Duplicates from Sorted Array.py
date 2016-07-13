class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0:
            return 0
        count = 0
        pre = -1
        for i in A:
            if count == 0 or i != pre:
                count +=1
                pre = i
                A[count-1] = i
        return count
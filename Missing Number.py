class Solution(object):
    def missingNumber(self, nums):
        n1 = n2 = 0
        for i in xrange(1,len(nums)+1):
            n1 ^= i

        for i in nums:
            n2 ^= i

        return n1 ^ n2;
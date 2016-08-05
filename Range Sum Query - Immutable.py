class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.sum = [0] * (len(nums) + 1)
        for i in xrange(len(nums)):
            n = nums[i]
            if i == 0:
                self.sum[i+1] = n
            else:
                self.sum[i+1] = self.sum[i] + n


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum[j+1] - self.sum[i]
        


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
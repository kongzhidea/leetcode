class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1] * len(nums)
        right = [1] * len(nums)
        for i in xrange(len(nums)):
            if i == 0:
                left[0] = 1
            elif i == 1:
                left[1] = nums[0]
            elif i == 2:
                left[2] = nums[0] * nums[1]
            else:
                left[i] = (left[i-2] * nums[i-2] * nums[i-1])
        for i in xrange(len(nums)):
            r = len(nums) - i - 1
            if i == 0:
                right[r] = 1
            elif i == 1:
                right[r] = nums[r+1]
            elif i == 2:
                right[r] = nums[r+1] * nums[r+2]
            else:
                right[r] = right[r+2] * nums[r+1] * nums[r+2]
        ret = []
        for i in xrange(len(nums)):
            ret.append(left[i] * right[i])
        return ret
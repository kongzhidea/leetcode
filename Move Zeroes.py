class Solution(object):
    def moveZeroes(self, nums):
        count = 0
        for n in nums:
            if n != 0:
                nums[count] = n
                count += 1
        for i in range(count,len(nums)):
            nums[i] = 0
        print nums
class Solution(object):
    def containsDuplicate(self, nums):
        dict = {}
        for i in nums:
            if dict.get(i) == 1:
                return True
            dict[i] = 1
        return False
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict = {}
        start = end = 0
        for i in xrange(len(nums)):
            if dict.get(nums[i]) != None:
                return True
            else:
                end +=1
                dict[nums[i]] = 1
            if end - start > k:
                dict.pop(nums[start])
                start +=1
        return False
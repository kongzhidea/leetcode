class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict = {}
        for i in nums1:
            dict[i] = dict.get(i,0) + 1
        ret = []
        for i in nums2:
            if dict.get(i,0) > 0:
                ret.append(i)
                dict[i]-=1
        return ret
    

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict = {}
        mat = {}
        for i in nums1:
            dict[i] = 1
        ret = []
        for i in nums2:
            if dict.get(i,0) > 0 and mat.get(i,0) ==0:
                ret.append(i)
                mat[i] = 1
        return ret
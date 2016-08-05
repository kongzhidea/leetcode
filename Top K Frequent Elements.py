class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict = {}
        for i in nums:
            dict[i] = dict.get(i,0) + 1
        ndt = sorted(dict.items(), key=lambda d: d[1],reverse=True)
        ret = []
        for i in xrange(0,k):
            ret.append(ndt[i][0])
        return  ret
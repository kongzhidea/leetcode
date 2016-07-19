class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ret = []
        for i in xrange(0,num+1):
            s = bin(i)
            ret.append(s.count('1'))
        return ret
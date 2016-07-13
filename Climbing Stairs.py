class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        ret = []
        ret.extend([0,1,2])
        for i in xrange(3,n+1):
            ret.append(ret[i-1] + ret[i-2])
        return ret[n]
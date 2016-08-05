class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 10
        ret = 10
        for i in xrange(2,n+1):
            deta = 9 * self.a(9,i-1)
            ret += deta
        return ret

    def a(self,n,k):
        if k >= n :
            return 0
        ret = 1
        for i in xrange(n-k+1,n+1):
            ret *= i
        return ret
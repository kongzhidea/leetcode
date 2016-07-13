class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        n = len(num)
        if n == 0:
            return 0
        if(n == 1):
            return num[0]
        f = [0] * n
        f[0] = num[0]
        f[1] = max(num[0],num[1])
        for i in xrange(2,n):
            f[i] = max(f[i-1],f[i-2] + num[i])
        return f[n-1]
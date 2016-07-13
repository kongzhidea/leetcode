class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        ln = len(triangle)
        f = [0] * ln
        f[0] =triangle[0][0]
        for i in xrange(1,ln):
            t = [0] * ln
            for j in xrange(0,i+1):
                if j == 0:
                    t[j] = f[0] + triangle[i][j]
                elif j == i:
                    t[j] = f[j-1] + triangle[i][j]
                else:
                    t[j] = min(f[j-1],f[j]) + triangle[i][j]
            f[:] = t[:]
        return min(f)
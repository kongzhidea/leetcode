class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        n = len(s)
        f = [0] * n  #f[i]表示 是否可以由dict组成
        for i in xrange(n):
            if s[0:i+1] in dict:
                f[i] = 1
            if f[i] == 1:
                continue
            for j in xrange(i):
                if f[j] == 1:
                    if s[j+1:i+1] in dict:
                        f[i] = 1
        return f[n-1] == 1
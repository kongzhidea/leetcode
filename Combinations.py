class Solution:
    def __init__(self):
        self.ret = []
    # @return a list of lists of integers
    def combine(self, n, k):
        use = [0] * (n + 1)
        self.dfs(use,n,k,1,0)
        return self.ret

    def dfs(self,use,n,k,idx,count):
        if count == k:
            tmp = []
            for i in xrange(1,n+1):
                if use[i] == 1:
                    tmp.append(i)
            self.ret.append(tmp)
            return
        if idx > n:
            return
        use[idx] = 1
        self.dfs(use,n,k,idx+1,count+1)
        use[idx] = 0
        self.dfs(use,n,k,idx+1,count)
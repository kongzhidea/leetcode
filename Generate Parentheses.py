class Solution:
    def __init__(self):
        self.ret = []
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        self.dfs("",0,0,n)
        return self.ret
    def dfs(self,tmp,lc,rc,n):
        if lc + rc == n * 2:
            self.ret.append(tmp)
            return
        if lc< n:
            self.dfs(tmp + "(",lc + 1,rc,n)
        if rc < n and lc > rc:
            self.dfs(tmp + ")" ,lc,rc + 1,n)
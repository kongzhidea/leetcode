class Solution:
    # @return a string
    def countAndSay(self, n):
        if n <=0 :
            return None
        ret = "1"
        for i in xrange(1,n):
            ret = self.solve(ret)
        return ret
    def solve(self,ret):
        count = 1
        last = ret[0]
        ans = ""
        for i in range(1,len(ret) + 1):
            if i < len(ret) and last == ret[i]:
                count +=1
            else:
                ans += str(count) + last
                count = 1
                if i< len(ret):
                    last = ret[i]
        return ans
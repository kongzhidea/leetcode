class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def calcNext(self,needle):
        ln = len(needle)
        next = [0] * ln
        pre = 0;cur = 1
        next[0] = -1
        while cur < ln:
            pidx = next[cur - 1]
            if needle[cur] == needle[pidx + 1]:
                next[cur] = next[cur - 1] + 1
            else:
                next[cur]  = -1
            cur += 1
        return next
    def strStr(self, haystack, needle):
        if len(needle) == 0 :
            return 0
        # next
        next = self.calcNext(needle)
#        print next
        p1 = 0;p2 = -1
        ln1 = len(haystack);ln2 = len(needle)
        while p1 < ln1:
#            print p1,p2
            if haystack[p1] == needle[p2 + 1]:
                p1 +=1
                p2 +=1
            else:
                if p2 != -1:
                    p2 = next[p2]
                else:
                    p1 +=1
            if p2 == ln2 -1:
                return p1 - ln2
        return -1
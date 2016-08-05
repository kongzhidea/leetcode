class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.tranf(s) == self.tranf(t)

    def tranf(self,s):
        if s == None:
            return ""
        dict = {}
        count = 0
        ret = []
        for c in s:
            if dict.get(c) != None:
                ret.append(dict.get(c))
            else:
                count +=1
                dict[c] = count
                ret.append(dict.get(c))
        return "".join(map(str,ret))
class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        prefix = self.findCommonPrefix(strs[0],strs[1])
        for i in range(2,len(strs)):
            prefix = self.findCommonPrefix(prefix,strs[i])
        return "".join(prefix)
    def findCommonPrefix(self,s1,s2):
        prefix = []
        for i in range(min(len(s1),len(s2))):
            if s1[i] !=  s2[i]:
                return prefix
            prefix.append(s1[i])
        return prefix
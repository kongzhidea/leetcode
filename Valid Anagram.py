class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        dict1 = [0] * 26
        dict2 = [0] * 26
        for i in xrange(0,len(s)):
            dict1[ord(s[i]) - 97] += 1
            dict2[ord(t[i]) - 97] += 1
        for i in xrange(0,26):
            if dict1[i] != dict2[i]:
                return False
        return True
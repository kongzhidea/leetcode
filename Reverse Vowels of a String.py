class Solution(object):
    def isVowel(self,c):
        l = ['a','e','i','o','u','A','E','I','O','U']
        return c in l
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        flag = []
        vowels = []
        for c in s:
            if self.isVowel(c):
                flag.append(1)
                vowels.append(c)
            else:
                flag.append(0)
        rev = vowels[::-1]
        idx = 0
        ret = []
        for c in s:
            if self.isVowel(c):
                ret.append(rev[idx])
                idx +=1
            else:
                ret.append(c)
        return "".join(ret)
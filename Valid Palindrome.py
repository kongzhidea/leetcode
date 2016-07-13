class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if s  == "" or s == None:
            return True
        s2 = []
        for ch in s:
            if ch.isalnum():
                s2.append(ch.lower())
        if len(s2) == 0:
            return True
        for i in range(len(s2)/2):
            if s2[i] !=s2[len(s2) - i -1]:
                return False
        return True
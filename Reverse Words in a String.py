class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        ts = s.split()
        return " ".join(ts[::-1])
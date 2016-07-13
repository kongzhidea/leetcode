conv = {}
for i in range(26):
    conv[chr(i+65)] = i + 1
class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        ret = 0
        for ch in s:
            val = int(conv[ch])
            ret = ret * 26 + val
        return ret
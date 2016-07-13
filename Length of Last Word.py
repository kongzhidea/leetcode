class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        s=s.strip()
#        print s.split(" "),s.split(" ")[-1]
        return len(s.split(" ")[-1])
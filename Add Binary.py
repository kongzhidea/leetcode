class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        x = int(a,2)
        y = int(b,2)
        return str(bin(x+y))[2:]
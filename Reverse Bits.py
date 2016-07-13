class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def reverseBits(self, n):
        x = bin(n)[2:]
        l =  ['0'] * (32 - len(x))
        l.extend(x)
        y = "".join(l[::-1])
        return int(y,2)
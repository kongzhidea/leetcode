class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        bit = [0] * 32
        for i in range(32):
            for n in A:
                bit[i] += (n>>i) &1
            bit[i] %= 3
        ret = 0
        sign = 1
        if bit[31] == 1:
            sign  = -1
            for i in range(32):
                bit[i] = bit[i] ^ 1
            deta = 1
            for i in range(32):
                bit[i] += deta
                deta = bit[i] / 2
                bit[i] %= 2
        return sign * int("".join(map(str,bit[::-1])),2)
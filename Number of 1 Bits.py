class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        x = str(bin(n))
        count = 0
        for i in x[0:]:
            if i == '1':
                count +=1
        return count

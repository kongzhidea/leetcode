class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        count = 0
        while n !=0:
            count += n/5
            n /= 5
        return count
        
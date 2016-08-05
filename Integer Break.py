class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        c = n / 3
        left = n % 3
        if left == 0:
            return 3 ** c
        if left == 1:
            return (3** (c-1)) * 4
        if left == 2:
            return (3**c) * 2
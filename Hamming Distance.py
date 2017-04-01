class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bx = bin(x)
        by = bin(y)
        bx = bx[2:]
        by = by[2:]

        bx = "0" * (64-len(bx)) + bx
        by = "0" * (64-len(by)) + by

        c = 0
        for i in xrange(64):
            if bx[i] != by[i]:
                c += 1
        return c

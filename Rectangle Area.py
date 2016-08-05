class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        res = (D - B) * (C - A) + (H - F) * (G - E)
        A1 = max(A, E)
        B1 = max(B, F)
        C1 = min(C, G)
        D1 = min(D, H)
        if (D1 <= B1 or C1 <= A1):
            return res
        return res - (D1 - B1) * (C1 - A1)
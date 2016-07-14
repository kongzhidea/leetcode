class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ln = len(prices)
        m = []
        for i in xrange(0,ln):
            x = prices[ln - 1 - i]
            if i == 0:
                m.append(x)
            else:
                m.insert(0,max(x,m[0]))
        deta = 0
        for i in xrange(ln-1):
            deta = max(deta,m[i+1] - prices[i])
        return deta
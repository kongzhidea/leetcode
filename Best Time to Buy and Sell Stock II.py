class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        ln = len(prices)
        if ln < 2:
            return 0
        sum = 0
        for i in xrange(1,ln):
            if prices[i] > prices[i-1]:
                sum += prices[i] - prices[i-1]
        return sum
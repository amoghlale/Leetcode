class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        diff_global = 0
        diff_current = 0
        if len(prices) == 2 and prices[1]-prices[0] > diff_global:
            diff_global = prices[1]-prices[0]
        else:
            for i in range(len(prices)-1, 0, -1):
                if prices[i] - min(prices[i-1::-1]) > diff_current:
                    diff_current = prices[i] - min(prices[i-1::-1])
                if diff_current > diff_global:
                    diff_global = diff_current
        return diff_global

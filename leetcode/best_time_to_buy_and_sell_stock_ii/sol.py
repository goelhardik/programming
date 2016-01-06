class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if (len(prices) == 0):
            return 0
        profit = 0
        tmp = prices[0]
        # just add all the positive changes in the stock price
        for i in range(1, len(prices)):
            new_tmp = prices[i]
            prices[i] -= tmp
            tmp = new_tmp
            if (prices[i] >= 0):
                profit += prices[i]
                
        return profit

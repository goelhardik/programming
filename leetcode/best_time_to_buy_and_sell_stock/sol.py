class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if (len(prices) == 0):
            return 0
        # convert array of prices to array of price changes
        tmp = prices[0]
        prices[0] = 0
        for i in range(1, len(prices)):
            new_tmp = prices[i]
            prices[i] -= tmp
            tmp = new_tmp
            
        # solve maximum subarray problem on new prices array
        maxhere = -float("inf")
        maxsub = -float("inf")
        for i in range(len(prices)):
            maxhere = max(maxhere + prices[i], prices[i])
            maxsub = max(maxsub, maxhere)
            
        return maxsub

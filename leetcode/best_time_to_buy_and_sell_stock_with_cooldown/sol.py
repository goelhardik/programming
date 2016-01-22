class Solution(object):                                                                                                                                                                    
    def maxProfit(self, prices):                                                
        """                                                                     
        :type prices: List[int]                                                 
        :rtype: int                                                             
        """                                                                     
        profit1 = 0 # profit on day i if i sell
        profit2 = 0 # profit on day i if i do nothing
        for i in range(1, len(prices)):
            # if sell on day i, either sold on day i - 1 or did nothing on i - 1
            tmp = max(profit1 + prices[i] - prices[i - 1], profit2)
            # if nothing on i, either sold on i - 1 or nothing on i - 1
            profit2 = max(profit1, profit2)
            profit1 = tmp
            
        return max(profit1, profit2)

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if (amount == 0):
            return 0
            
        dp = [-1 for i in range(amount + 1)]
        for coin in coins:
            if (coin <= amount):
                dp[coin] = 1    # all coin values have minimum change 1
        
        for i in range(1, amount + 1):
            if (dp[i] > 0):     # for each possible amount, update all future possible amounts
                for coin in coins:
                    if (i + coin <= amount and (dp[i + coin] == -1 or dp[i + coin] > dp[i] + 1)):
                        dp[i + coin] = dp[i] + 1
                        
        return dp[amount]

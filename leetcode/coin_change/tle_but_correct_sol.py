class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        MAX = float("inf")
        change = [MAX for i in range(amount + 1)]
        change[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if (i - coin >= 0 and change[i - coin] != MAX):
                    change[i] = min(change[i], change[i - coin] + 1)
                        
        return [change[amount], -1][change[amount] == MAX]

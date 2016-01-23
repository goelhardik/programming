"""
The key is that we can buy a stock whenever a profit is possible and
then sell it later at the maximum possible price.
"""
def max_profit(prices):
    profit = 0
    max_price = prices[-1]  # maintain the maximum possible sell price
    for i in range(len(prices) - 2, -1, -1):
        if (prices[i] <= max_price):    # if a smaller price is seen, we must have bought a stock here
            profit += max_price - prices[i] # so sell it at maximum possible price
        elif (prices[i] > max_price):
            max_price = prices[i]   # if a larger price is seen, all remaining stocks will be sold at this price to earn the maximum profit
        
    return profit

# driver code
tests = int(input())
for i in range(tests):
    n = int(input())
    prices = list(map(int, input().split()))
    print(max_profit(prices))

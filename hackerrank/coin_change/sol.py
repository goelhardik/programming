def ways_of_coin_change(n, coins, m):
    if (n == 0):
        return 0
    dp = [0 for i in range(n + 1)]
    dp[0] = 1
    for coin in coins:  # for each coin, update ways of all possible amounts
        for i in range(n + 1):
            if (dp[i] > 0 and i + coin <= n):
                dp[i + coin] += dp[i]
    
    return dp[n]

# driver code
n, m = map(int, input().split())
coins = list(map(int, input().split()))
coins.sort()
print(ways_of_coin_change(n, coins, m))

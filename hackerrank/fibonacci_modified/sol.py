import fileinput

def fib(a, b, n):
    dp = [0 for i in range(n)]
    if (n == 0):
        return 0
    dp[0] = int(a)
    if (n == 1):
        return dp[0]
    dp[1] = int(b)
    for i in range(2, n):
        dp[i] = dp[i - 1] ** 2 + dp[i - 2]
        
    return dp[n - 1]
    
for line in fileinput.input():
    [a, b, n] = line.split()

print(str(fib(a, b, int(n))))

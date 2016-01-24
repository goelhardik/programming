def find_brick_ways(n):
    dp = [0 for i in range(n + 1)]
    dp[0] = 1
    for i in range(n + 1):  # like coin change problem; for each size, update future possible ways
        if (i + 1 <= n):
            dp[i + 1] += dp[i]
        if (i + 4 <= n):
            dp[i + 4] += dp[i]
            
    return dp[n]
     
def mark_mults(dp, n):
    for i in range(n * 2, len(dp) + 1, n):
        dp[i - 1] = 0
        
def find_num_primes(m): # sieve of eratosthenes method to count primes
    dp = [1 for i in range(m)]  # 0 based indexing for prime numbers
    dp[0] = 0   # 1 is not prime
    for i in range(1 + m // 2):
        if (dp[i] == 1):    # prime number encountered
            mark_mults(dp, i + 1)   # mark all multiples as non-primes
                
    return sum(dp)
    

# driver code
tests = int(input())
for i in range(tests):
    n = int(input())
    m = find_brick_ways(n)
    p = find_num_primes(m)
    print(p)

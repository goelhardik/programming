def find_max_len_child(a, b):
    n = len(a)
    if (n == 0):
        return 0
    # dp array i, j denotes, length of longest child of strings a[0..i] and b[0..j]
    dp = [[0 for j in range(n)] for i in range(n)]
    if (a[0] == b[0]):
        dp[0][0] = 1
    for j in range(1, n):   # first row
        if (a[0] == b[j]):
            dp[0][j] = 1
        else:
            dp[0][j] = dp[0][j - 1]
    for i in range(1, n):   # first column
        if (a[i] == b[0]):
            dp[i][0] = 1
        else:
            dp[i][0] = dp[i - 1][0]
    for i in range(1, n):
        for j in range(1, n):
            if (a[i] == b[j]):
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n - 1][n - 1]

# driver code
a = str(input())
b = str(input())
print(find_max_len_child(a, b))

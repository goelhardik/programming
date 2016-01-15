class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        n = len(s)
        dp = [[0 for j in range(n)] for i in range(n)]
        for l in range(1, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                if (s[i : j + 1] in wordDict):
                    dp[i][j] = 1
                else:
                    for k in range(i, j + 1):
                        if (dp[i][k] and dp[k + 1][j]):
                            dp[i][j] = 1
                            break
                        
        return (dp[0][n - 1] != 0)

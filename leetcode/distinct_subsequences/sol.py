class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # dp[i][j] means distinct subseqs for t and s upto lengths i and j respectively
        dp = [[0 for j in range(len(s))] for i in range(len(t))]
        if (len(s) == 0 or len(t) == 0):
            return 0
        
        # update the first row of dp
        if (s[0] == t[0]):
            dp[0][0] = 1
        for j in range(1, len(s)):
            if (s[j] == t[0]):
                dp[0][j] = dp[0][j - 1] + 1
            else:
                dp[0][j] = dp[0][j - 1]
        
        # update rest of the dp       
        for i in range(1, len(t)):
            for j in range(i, len(s)):
                if (t[i] == s[j]):  # if current chars are same, then we need to add two values
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
                else:   # answer will remain the same as previous length of s
                    dp[i][j] = dp[i][j - 1]
                    
        return dp[len(t) - 1][len(s) - 1]

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        n = len(s)
        dp = [0 for j in range(n + 1)]
        dp[0] = 1
        # starting from every achievable index, mark all achievable indices
        # by using dictionary words at the position
        for start in range(n):
            if (dp[start] == 0):
                continue
            for word in wordDict:
                l = len(word)
                end = start + l
                if (end > n):
                    continue
                if (s[start : end] == word):
                    dp[end] = 1
                    
        return (dp[n] == 1)

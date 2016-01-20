class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if (n == 0):
            return 0
        map = {}
        # use DP to maintain the longest subtring without repeating chars at that index
        dp = [1 for i in range(n)]
        # use map to keep track of last seen index of each character
        map[s[0]] = 0
        max_len = 1
        for i in range(1, n):
            if (s[i] in map):
                last = map[s[i]]
                max_until_here = i - last
            else:
                max_until_here = i + 1
            map[s[i]] = i
            dp[i] = min(dp[i - 1] + 1, max_until_here)
            if (dp[i] > max_len):
                max_len = dp[i]
               
                    
        return max_len

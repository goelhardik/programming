class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if (n == 0):
            return 0
        if (s[0] == '0'):
            return 0
        dp = [0 for i in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            # if next is zero then keep the count same
            if (i < n and s[i] == '0'):
                dp[i] = dp[i - 1]
            # current is zero
            elif (s[i - 1] == '0'):
                # previous was also zero or previous was greater than 2 (eg. 100 or 30)
                if (s[i - 2] == '0' or s[i - 2] > '2'):
                    return 0
                # else keep the count same (eg. 10 or 20)
                dp[i] = dp[i - 1]
            else:
                # if previous and current make valid 2 digits (eg. 17 or 26)
                if ((s[i - 2] == '2' and s[i - 1] < '7') or s[i - 2] == '1'):
                    dp[i] = dp[i - 1] + dp[i - 2]
                # else only current digit can be decoded, so no change in count
                else:
                    dp[i] = dp[i - 1]
                    
        return dp[n]

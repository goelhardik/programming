class Solution(object):
                        
    def minDistance(self, w1, w2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = len(w1)
        l2 = len(w2)
        if (l2 == 0):
            return l1
        if (l1 == 0):
            return l2
        dp = [[0 for j in range(l2)] for i in range(l1)]
        
        # udpate first row
        if (w1[0] == w2[0]):
            dp[0][0] = 0
        else:
            dp[0][0] = 1
        for j in range(1, l2):
            if (w1[0] == w2[j]):
                dp[0][j] = j
            else:
                insert = dp[0][j - 1]
                replace = j
                delete = j + 1
                dp[0][j] = 1 + min(insert, replace, delete)
                
        # update first column
        for i in range(1, l1):
            if (w1[i] == w2[0]):
                dp[i][0] = i
            else:
                insert = dp[i - 1][0]
                replace = i
                delete = i + 1
                dp[i][0] = 1 + min(insert, replace, delete)
                
        # update rest of the table
        for i in range(1, l1):
            for j in range(1, l2):
                if (w1[i] == w2[j]):
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1],    # insert
                                        dp[i - 1][j - 1],   # replace
                                        dp[i - 1][j]    # delete
                                        )
                                        
        return dp[l1 - 1][l2 - 1]

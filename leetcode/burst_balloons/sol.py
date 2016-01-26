class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) + 2
        nums = [1] + nums + [1] # add dummy balloons
        dp = [[0 for j in range(n)] for i in range(n)]
        
        for l in range(2, n):
            for i in range(n - l):
                j = i + l
                # i and j cannot be burst in this range, they are just contributors to bursting of kth balloon
                for k in range(i + 1, j):   # if k is the last balloon to be burst for balloons i to j
                    dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])
                    
        return dp[0][n - 1]

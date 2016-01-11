class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if (n == 0):
            return 0
        elif (n == 1):
            return nums[0]
        dp = [0 for i in range(n)]
        # pick 1st house
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        if (n == 2):
            return dp[1]
        # skip last house
        for i in range(2, n - 1):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        house1 = dp[n - 2]
        
        # don't pick 1st house
        dp[1] = nums[1]
        dp[2] = max(nums[1], nums[2])
        for i in range(3, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        house2 = dp[n - 1]
        
        return max(house1, house2)

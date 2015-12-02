"""
Use DP to solve this.
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if (l == 0):
            return 0
        elif (l == 1):
            return nums[0]
        
        dp = [0 for i in range(l)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, l):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
            
        return dp[l - 1]

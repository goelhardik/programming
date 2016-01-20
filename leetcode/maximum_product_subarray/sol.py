class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if (n == 0):
            return 0
        maxprod = nums[0]   # useful when current number is positive as ans = maxprod * nums[i]
        minprod = nums[0]   # useful when current number is negative as ans = minprod * nums[i]
        ans = nums[0]
        for i in range(1, n):
            new_maxprod = max(maxprod * nums[i], minprod * nums[i], nums[i])
            new_minprod = min(maxprod * nums[i], minprod * nums[i], nums[i])
            ans = max(ans, new_maxprod)
            maxprod = new_maxprod
            minprod = new_minprod
            
        return ans

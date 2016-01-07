class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum = n * (n + 1) // 2
        for i in range(n):
            sum -= nums[i]
            
        return sum

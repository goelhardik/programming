class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = 0
        min_l = float("inf")
        sum = 0
        while (end < len(nums) or sum >= s):
            if (sum < s):
                sum += nums[end]
                end += 1
            else:
                length = end - start
                if (length < min_l):
                    min_l = length
                sum -= nums[start]
                start += 1
                
        if (min_l > len(nums)):
            min_l = 0
        return min_l

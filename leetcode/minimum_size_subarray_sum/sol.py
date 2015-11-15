class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = 0
        sum = 0
        min = float("inf")
        """
        Strategy:
            Keep two pointers start and end to track the subarray.
            Keep moving forward and update the min after each pointer update.
        """
        while (end < len(nums)):
            # increment end while sum is less that target.
            while (sum < s and end < len(nums)):
                sum += nums[end]
                end += 1
            # increment start while sum is greater than equal to the target.
            while (sum >= s and start < end):
                sum -= nums[start]
                start += 1
            # pointers point to min subarray until this end; update min answer length.
            if (end - start + 1 < min):
                min = end - start + 1
            # take care of boundary condition when sum == target
            if (sum == s):
                sum -= nums[start]
                start += 1
        
        # if no such subarray found, return 0
        if (min > len(nums)):
            min = 0

        return min

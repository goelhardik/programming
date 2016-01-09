class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n - 1):
            if (nums[i] <= nums[i + 1]):
                continue
            else:
                if (i == 0 or nums[i] > nums[i - 1]):
                    return i
                    
        return (n - 1)

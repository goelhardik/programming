class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # initializing to negative infinity to consider negative subarrays in the 
        # input
        maxhere = -float("inf")
        maxsub = -float("inf")
        for i in range(len(nums)):
            maxhere = max(maxhere + nums[i], nums[i])
            maxsub = max(maxsub, maxhere)
            
        return maxsub

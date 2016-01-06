class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = list(nums)
        l = len(output)
        # check if list is empty
        if (l == 0):
            return output
            
        # calculate left product of numbers
        for i in range(1, l):
            output[i] *= output[i - 1]
        
        # store right product in rprod and update output    
        rprod = 1
        for i in range(l - 1, 0, -1):
            output[i] = output[i - 1] * rprod
            rprod *= nums[i]
            
        output[0] = rprod
        
        return output

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero = 0    # index to track element
        nonzero = 0 # index to track non zero element
        while (zero < len(nums) and nonzero < len(nums)):
            if (nums[zero] != 0):
                zero += 1
                continue
            if (nums[nonzero] == 0):
                nonzero += 1
                continue
            if (nonzero > zero):    # if the nonzero element lies to the left of zero, then don't need to swap
                nums[zero] = nums[nonzero]
                nums[nonzero] = 0
                zero += 1
            nonzero += 1

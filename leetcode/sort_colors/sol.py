class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = -1
        r = len(nums)
        i = 0
        # keep two pointers; one for zero and one for two
        while (i < r):
            if (nums[i] == 0):
                l += 1
                if (nums[l] == 0):
                    i += 1
                else:
                    nums[i] = nums[l]
                    nums[l] = 0
            elif (nums[i] == 2):
                r-= 1
                nums[i] = nums[r]
                nums[r] = 2
            else:
                i += 1

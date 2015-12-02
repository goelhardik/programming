class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums) == 0):
            return 0
        pivot = 0
        p = 1
        while (p < len(nums)):
            if (nums[p] == nums[pivot]):
                p += 1
            else:
                pivot += 1
                nums[pivot] = nums[p]
                p += 1
        
        return (1 + pivot)

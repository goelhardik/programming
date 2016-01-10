class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if (n < 3):
            return n
        p = 1
        for c in range(2, n):
            if (nums[c] == nums[p] and nums[c] == nums[p - 1]):
                pass
            else:
                p += 1
                nums[p] = nums[c]
                
        return p + 1
            

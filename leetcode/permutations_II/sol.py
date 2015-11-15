class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        out = []
        self.permute(0, nums, out)
        return out
        
    def permute(self, start, nums, out):
        if (start == len(nums)):
            out.append(list(nums))
            return
        
        """
        Swap each value with the starting one, and call permute recursively.
        Prune search for duplicates. If any duplicate element comes later in the 
        list, no need to swap it because it will generate the same results again
        """
        for i in range(start, len(nums)):
            if (nums[i] not in nums[start : i]):
                self.swap(nums, i, start)
                self.permute(start + 1, nums, out)
                self.swap(nums, i, start)
            
    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

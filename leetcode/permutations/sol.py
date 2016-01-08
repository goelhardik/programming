class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self._permute(nums, 0, len(nums) - 1, result)
        return result
        
    def _permute(self, nums, start, end, result):
        if (start == end):
            result.append(list(nums))
            return
        
        for i in range(start, end + 1):
            self.swap(nums, start, i)
            self._permute(nums, start + 1, end, result)
            self.swap(nums, start, i)
            
    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

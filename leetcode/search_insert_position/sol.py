class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = self._searchInsert(nums, 0, len(nums) - 1, target)
        return result
        
    def _searchInsert(self, nums, low, high, target):
        if (low >= high):
            if (target == nums[low]):
                return low
            elif (target < nums[low]):
                return low
            else:
                return (low + 1)
                
        mid = low + (high - low) // 2
        if (target == nums[mid]):
            return mid
        elif (target < nums[mid]):
            return self._searchInsert(nums, low, mid - 1, target)
        else:
            return self._searchInsert(nums, mid + 1, high, target)

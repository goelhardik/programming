class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = self._findMin(nums, 0, len(nums) - 1)
        return nums[index]
        
    # use a binary search like approach
    def _findMin(self, nums, low, high):
        if (low >= high):
            return low
        mid = (low + high) // 2
        if (mid > 0 and nums[mid] < nums[mid - 1]):
            return mid
        # if middle element is greater than the rightmost element, then the minimum lies in the right half
        elif (nums[mid] > nums[high]):
            return self._findMin(nums, mid + 1, high)
        # otherwise it lies in the left half
        else:
            return self._findMin(nums, low, mid - 1)

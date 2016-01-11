class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        low = 0
        high = n - 1
        
        # find start position
        start = -1
        while (low <= high):
            mid = (low + high) // 2
            if (nums[mid] == target):
                if (mid == 0 or nums[mid - 1] < target):
                    start = mid
                    break
                else:
                    high = mid - 1
            elif (nums[mid] > target):
                high = mid - 1
            else:
                low = mid + 1
        
        if (start == -1):
            return [-1, -1]
            
        # find end position
        end = start
        low = 0
        high = n - 1
        while (low <= high):
            mid = (low + high) // 2
            if (nums[mid] == target):
                if (mid == n - 1 or nums[mid + 1] > target):
                    end = mid
                    break
                else:
                    low = mid + 1
            elif (nums[mid] > target):
                high = mid - 1
            else:
                low = mid + 1
                
        return [start, end]

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        low = 0
        high = len(nums) - 1
        while (low <= high):
            mid = (low + high) // 2
            if (nums[mid] == target):
                return True
                
            # if pivot lies to the left of mid
            if (nums[low] > nums[mid]):
                if (nums[mid] < target and target <= nums[high]):
                    low = mid + 1
                else:
                    high = mid - 1
            elif (nums[low] < nums[mid]):
                # if target lies between left and mid
                if (nums[low] <= target and target < nums[mid]):
                    high = mid - 1
                else:
                    low = mid + 1
            # left is duplicate of mid
            else:
                low += 1
                
        return False

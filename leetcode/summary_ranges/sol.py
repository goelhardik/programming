class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if (len(nums) == 0):
            return []
            
        # keep two pointers to track intervals
        left = 0
        right = 1
        result = []
        while (right < len(nums)):
            if (nums[right] - nums[right - 1] == 1):
                right += 1
            else:
                if (right - left > 1):
                    result.append(str(nums[left]) + "->" + str(nums[right - 1]))
                else:
                    result.append(str(nums[left]))
                left = right
                right += 1
                
        # append last interval
        if (right - left > 1):
            result.append(str(nums[left]) + "->" + str(nums[right - 1]))
        else:
            result.append(str(nums[left]))
            
        return result

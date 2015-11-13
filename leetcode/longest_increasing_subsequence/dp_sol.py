class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums) == 0):
            return 0
        l = [1 for i in range(len(nums))]
        max = 1
        """ Recurrence relation """
        """ l[i] = 1 + max{l[j] such that j < i and nums[j] < nums[i]} """
        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                if (nums[j] < nums[i] and l[i] < l[j] + 1):
                    l[i] = l[j] + 1
                    if (l[i] > max):
                        max = l[i]
                        
        return max

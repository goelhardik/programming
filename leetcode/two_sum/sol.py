class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        map = {}
        for i in range(n):
            diff = target - nums[i]
            if (diff in map):
                index1 = map[diff]
                return [index1 + 1, i + 1]
            else:
                map[nums[i]] = i

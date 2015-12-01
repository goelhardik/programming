"""
Sort and compare adjacent values.
Can be done with a hashmap as well; will need O(n) space complexity for that.
"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(len(nums) - 1):
            if (nums[i] == nums[i + 1]):
                return True
        return False

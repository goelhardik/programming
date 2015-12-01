"""
Iterate through the list, maintain vote for majority element. If vote becomes 
negative, update the majority element.
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maj = nums[0]
        vote = 1
        for i in range(1, len(nums)):
            if (nums[i] == maj):
                vote += 1
            else:
                vote -= 1
            if (vote < 0):
                maj = nums[i]
                vote = 1
                
        return maj

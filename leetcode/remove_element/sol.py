class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        s = 0
        e = len(nums) - 1
        while (s <= e):
            if (nums[s] != val):
                s += 1
            elif (nums[e] == val):
                e -= 1
            else:
                nums[s] = nums[e]
                e -= 1
                s += 1
                
        return e + 1

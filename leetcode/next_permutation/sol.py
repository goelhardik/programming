class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        change = -1
        i = len(nums) - 1
        """
        Find the index that should be replaced, that is,
        start from back, find the first index where decreasing number is encountered.
        """
        while (i > 0):
            if (nums[i] > nums[i - 1]):
                change = i - 1
                break
            i -= 1
        
        if (change == -1):  # if no such index, array is sorted in non-increasing order
            self.reverse(nums, 0, len(nums) - 1)    # reverse and return
            return
        else:
            """
            From the right side of "change", find the least number bigger than nums[change].
            Use it to swap with "change" and sort/reverse the array to the right of "change".
            """
            i = len(nums) - 1
            while (i > change):
                if (nums[i] > nums[change]):
                    break
                i -= 1
            self.swap(nums, change, i)
            self.reverse(nums, change + 1, len(nums) - 1)
            return
        
    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
        
    def reverse(self, nums, start, end):
        while (start < end):
            self.swap(nums, start, end)
            start += 1
            end -= 1

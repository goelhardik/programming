class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        for i in range(len(nums)):
            nums[i] = str(nums[i])
            
        def compare(x, y):
            sx = x + y
            sy = y + x
            # return opposite values to sort in descending order
            if (sx > sy):
                return -1
            elif (sx == sy):
                return 0
            else:
                return 1
                
        # use custom compare function
        nums = sorted(nums, compare)
        if (nums[0] == '0'):
            return '0'
        return "".join(nums)

class Solution(object):
    def longestConsecutive(self, array):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(array)
        max_count = 0
        for num in array:
            # find max sequence starting at num, if num is still there in our set
            left = num - 1
            right = num + 1
            count = 1
            while (left in nums):
                nums.remove(left)
                count += 1
                left -= 1
                
            while (right in nums):
                nums.remove(right)
                count += 1
                right += 1
                
            max_count = max(max_count, count)
            
        return max_count

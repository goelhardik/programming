class Solution(object):

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        item = []
        max = self._LIS(1, 0, item, nums)
        return max
        
    def _LIS(self, max, start, item, nums):
        """ If more than two items and in increasing order, update max """
        """ else prune search """
        l = len(item)
        if (l > 1):
            if (item[l - 1] > item[l - 2]):
                if (l > max):
                    max = l
            else:
                return max
                
        for i in range(start, len(nums)):
            item.append(nums[i])
            max = self._LIS(max, i + 1, item, nums)
            item.pop()
        return max

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        for l in range(len(nums) + 1):
            result = []
            self.get_subsets(nums, l, 0, result, [])
            for x in result:
                ans.append(list(x))
                
        return ans
        
    def get_subsets(self, nums, l, start, result, item):
        if (len(item) > l):
            return
        if (len(item) == l and item not in result):
            result.append(list(item))
            return
        for i in range(start, len(nums)):
            item.append(nums[i])
            self.get_subsets(nums, l, i + 1, result, item)
            item.pop()

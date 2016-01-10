class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        l = 0
        n = len(nums)
        nums.sort()
        # get all subsets of each length
        for l in range(n + 1):
            result = []
            self.get_sets(l, [], result, nums, 0,  n)
            for x in result:
                ans.append(list(x))
            
        return ans
        
    # get subsets of a particular length from nums
    def get_sets(self, l, item, result, nums, start, n):
        if (l == len(item)):
            result.append(list(item))
            return
        if (l < len(item)):
            return
        for i in range(start, n):
            item.append(nums[i])
            self.get_sets(l, item, result, nums, i + 1, n)
            item.pop()

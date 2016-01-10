class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []
        self.find_comb(candidates, target, 0, [], result, 0)
        return result
        
    def find_comb(self, candidates, target, start, item, result, sum):
        if (sum > target):
            return
        if (sum == target):
            result.append(list(item))
            return
        for i in range(start, len(candidates)):
            sum += candidates[i]
            item.append(candidates[i])
            self.find_comb(candidates, target, i, item, result, sum)
            item.pop()
            sum -= candidates[i]

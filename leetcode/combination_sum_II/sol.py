class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        out = []
        candidates.sort()
        self._combination(candidates, target, [], out, 0)
        return out
        
    def _combination(self, candidates, target, item, out, start):
        if (target == 0):
            out.append(list(item)) # if the sum is achieved, append the set
            return
        for i in range(start, len(candidates)):
            target -= candidates[i]
            """
            since the array is sorted, if we exceed the sum at any point, the 
            current number cannot generate more solutions; prune the search
            """
            if (target < 0):
                return
            item.append(candidates[i])
            # skip duplicate solutions
            if (candidates[i] not in candidates[start : i]):
                self._combination(candidates, target, item, out, i + 1)
            item.pop()
            target += candidates[i]

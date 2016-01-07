class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = [-1 for i in range(n + 1)]
        return self._numTrees(1, n, m)
        
    # use a top-down memoized, recursive approach
    def _numTrees(self, low, high, m):
        if (m[high - low + 1] >= 0):
            return m[high - low + 1]
            
        if (low >= high):
            return 1
            
        total = 0
        for i in range(low, high + 1):
            left_num = self._numTrees(low, i - 1, m)
            right_num = self._numTrees(i + 1, high, m)
            total += left_num * right_num
        
        # store the number of trees for a particular value of n
        m[high - low + 1] = total
        return total

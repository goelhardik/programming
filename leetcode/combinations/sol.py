class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        self.generate_comb(k, n, [], result, 1)
        return result
        
    # dfs based function
    def generate_comb(self, k, n, item, result, start):
        if (len(item) == k):
            result.append(list(item))
            return
        if (len(item) > k):
            return
        for i in range(start, n + 1):
            item.append(i)
            self.generate_comb(k, n, item, result, i + 1)
            item.pop()

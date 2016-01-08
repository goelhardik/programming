class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        item = []
        out = []
        self.find_comb(k, n, 0, item, out, 1)
        return out
        
    def find_comb(self, k, n, sum, item, out, start):
        if (len(item) == k):
            if (sum == n):
                out.append(list(item))
                return
            else:
                return
            
        for i in range(start, 10):
            sum += i
            if (sum > n):
                return
            item.append(i)
            self.find_comb(k, n, sum, item, out, i + 1)
            item.pop()
            sum -= i

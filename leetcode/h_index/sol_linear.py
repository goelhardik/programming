class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        # keep the counts of papers with each number of citations
        counts = [0 for i in range(n + 1)]
        for i in range(n):
            if (citations[i] > n):
                citations[i] = n
            counts[citations[i]] += 1
        
        for i in range(n, 0, -1):
            # there are i papers with at least i citations each
            if (counts[i] >= i):
                return i
            counts[i - 1] += counts[i]
        
        return 0

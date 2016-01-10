class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        n = len(citations)
        hindex = 0
        for i in range(n - 1, -1, -1):
            if (hindex >= citations[i]):
                return hindex
            hindex += 1
        return hindex

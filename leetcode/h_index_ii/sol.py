class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        low = 0
        n = len(citations)
        if (n == 0):
            return 0
        high = n - 1
        while (low <= high):
            mid = (low + high) // 2
            if (n - mid == citations[mid]):
                return (n - mid)
            elif (n - mid > citations[mid]):
                low = mid + 1
            else:
                high = mid - 1
                
        return n - low

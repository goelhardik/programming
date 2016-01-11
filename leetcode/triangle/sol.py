class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        if (n == 0):
            return 0
        # start from the last row and proceed upwards, taking the minimum
        extra = list(triangle[n - 1])
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                extra[j] = min(extra[j], extra[j + 1]) + triangle[i][j]
                
        return extra[0]

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        grid = [[0 for i in range(n)] for j in range(n)]
        num = 1
        for c in range(n // 2 + 1):
            i = c
            for j in range(c, n - c):
                grid[i][j] = num
                num += 1
            j = n - c - 1
            for i in range(c + 1, n - c):
                grid[i][j] = num
                num += 1
            i = n - c - 1
            for j in range(n - c - 2, c - 1, -1):
                grid[i][j] = num
                num += 1
            j = c
            for i in range(n - c - 2, c, -1):
                grid[i][j] = num
                num += 1
                
        return grid

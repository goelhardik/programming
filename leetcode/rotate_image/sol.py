class Solution(object):
    def rotate(self, grid):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # in-place rotation layer-wise
        n = len(grid)
        for c in range(n // 2 + 1):
            i = c
            for j in range(c, n - c - 1):
                tmp = grid[i][j]
                grid[i][j] = grid[n - j - 1][i]
                grid[n - j - 1][i] = grid[n - i - 1][n - j - 1]
                grid[n - i - 1][n - j - 1] = grid[j][n - i - 1]
                grid[j][n - i - 1] = tmp

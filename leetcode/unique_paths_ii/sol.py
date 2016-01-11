class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if (m == 0):
            return 0
        n = len(grid[0])
        if (grid[0][0] == 1):
            return 0
        
        arr = [[0 for j in range(n)] for i in range(m)]
        arr[0][0] = 1
        # first column
        for i in range(1, m):
            if (grid[i][0] != 1):
                arr[i][0] = arr[i - 1][0]
                
        # first row
        for j in range(1, n):
            if (grid[0][j] != 1):
                arr[0][j] = arr[0][j - 1]
                
        for i in range(1, m):
            for j in range(1, n):
                if (grid[i][j] != 1):
                    arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
                    
        return arr[m - 1][n - 1]

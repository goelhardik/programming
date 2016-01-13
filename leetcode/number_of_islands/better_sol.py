class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if (m == 0):
            return 0
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                # if unseen island, then count it
                if (grid[i][j] == "1"):
                    count += 1
                    # mark this island as seen
                    self.mark_island(grid, i, j, m, n)
                    
        return count
        
    def mark_island(self, grid, i, j, m, n):
        if (i < 0 or i >= m or j < 0 or j >= n):
            return
        if (grid[i][j] == "0"):
            return
        # mark this cell as seen
        grid[i][j] = "0"
        # mark neighbors as seen
        self.mark_island(grid, i - 1, j, m, n)
        self.mark_island(grid, i + 1, j, m, n)
        self.mark_island(grid, i, j - 1, m, n)
        self.mark_island(grid, i, j + 1, m, n)

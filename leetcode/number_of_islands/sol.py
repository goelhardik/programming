class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        """
        Strategy:
            Start from the first index (0, 0) and color all adjacent ones with a 
            letter.
            Repeat for the remaining ones.
            Return the count of letters used.
        """
        letter = 'A'
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == '1'):
                    self.mark_all_adjacent(i, j, grid, letter)
                    letter = chr(ord(letter) + 1)
                    
        return (ord(letter) - ord('A'))
        
    """
    Recursive function to color a one with a letter and then call itself to 
    color the adjacent ones.
    """
    def mark_all_adjacent(self, i, j, grid, letter):
        if (grid[i][j] == '0'):
            return
        elif (grid[i][j] == '1'):
            grid[i][j] = letter
            if (i > 0):
                self.mark_all_adjacent(i - 1, j, grid, letter)
            if (i < len(grid) - 1):
                self.mark_all_adjacent(i + 1, j, grid, letter)
            if (j > 0):
                self.mark_all_adjacent(i, j - 1, grid, letter)
            if (j < len(grid[0]) - 1):
                self.mark_all_adjacent(i, j + 1, grid, letter)

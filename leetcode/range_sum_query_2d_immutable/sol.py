class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        m = len(matrix)
        if (m == 0):
            self.grid = []
            return
        n = len(matrix[0])
        # store the sum of submatrix upto (i, j) in the grid matrix element (i + 1, j + 1)
        self.grid = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(1, m + 1):
            rowsum = 0
            for j in range(1, n + 1):
                self.grid[i][j] += self.grid[i - 1][j] + matrix[i - 1][j - 1] + rowsum
                rowsum += matrix[i - 1][j - 1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if (len(self.grid) == 0):
            return 0
        # result will be calculated as below
        ans = self.grid[row2 + 1][col2 + 1] + self.grid[row1][col1] - self.grid[row1][col2 + 1] - self.grid[row2 + 1][col1]
        return ans


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)

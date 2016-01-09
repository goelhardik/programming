class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if (m == 0):
            return
        n = len(matrix[0])
        first_row = 0
        first_col = 0
        # first store if the first row/column have a zero
        for i in range(m):
            if (matrix[i][0] == 0):
                first_col = 1
                break
        for j in range(n):
            if (matrix[0][j] == 0):
                first_row = 1
                break
        # for each zero seen in non-first row/column, set the first element in the corresponding row and column to zero
        for i in range(1, m):
            for j in range(1, n):
                if (matrix[i][j] == 0):
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # iterate through the non-first rows/columns and set zeros based on the first row/column
        for i in range(1, m):
            for j in range(1, n):
                if (matrix[i][0] == 0 or matrix[0][j] == 0):
                    matrix[i][j] = 0
        # set the first row and column to zero based on the flags stored earlier
        if (first_col == 1):
            for i in range(m):
                matrix[i][0] = 0
        if (first_row == 1):
            for j in range(n):
                matrix[0][j] = 0

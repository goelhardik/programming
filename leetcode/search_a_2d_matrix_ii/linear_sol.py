class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if (m == 0):
            return False
        n = len(matrix[0])
        # start from top-right corner
        i = 0
        j = n - 1
        while (i < m and j > -1):
            if (matrix[i][j] == target):
                return True
            # eliminate current column
            elif (matrix[i][j] > target):
                j -= 1
            # eliminate current row
            else:
                i += 1
                
        return False

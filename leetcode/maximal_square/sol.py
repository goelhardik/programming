class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if (m == 0):
            return 0
        n = len(matrix[0])
        max_side = 0
        for i in range(m):
            for j in range(n):
                if (int(matrix[i][j]) == 0):
                    matrix[i][j] = 0
                else:
                    if (i > 0 and j > 0):
                        # DP update
                        matrix[i][j] = min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i][j - 1]) + 1
                    else:
                        matrix[i][j] = int(matrix[i][j])
                        
                # keep track of the maximum square seen so far
                if (matrix[i][j] > max_side):
                    max_side = matrix[i][j]
                    
        return max_side ** 2

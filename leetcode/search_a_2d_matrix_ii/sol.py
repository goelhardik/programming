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
        return self.search_matrix(0, m - 1, 0, n - 1, target, matrix)
        
    # binary search based divide and conquer approach; eliminate 1 of the 4 quadrants at each step
    def search_matrix(self, rl, rh, cl, ch, target, matrix):
        if (rl > rh or cl > ch):
            return False
            
        rm = (rl + rh) // 2
        cm = (cl + ch) // 2
        if (matrix[rm][cm] == target):
            return True
        elif (matrix[rm][cm] > target):
            return (self.search_matrix(rl, rm - 1, cl, ch, target, matrix) or self.search_matrix(rm, rh, cl, cm - 1, target, matrix))
        else:
            return (self.search_matrix(rm + 1, rh, cl, cm, target, matrix) or self.search_matrix(rl, rh, cm + 1, ch, target, matrix))

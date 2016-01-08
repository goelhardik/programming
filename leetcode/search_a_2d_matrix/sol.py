class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # search for the correct row
        low = 0
        high = len(matrix) - 1
        # empty matrix
        if (high < 0):
            return False
        while (low < high):
            mid = (low + high) // 2
            if (matrix[mid][0] == target):
                return True
            elif (matrix[mid][0] > target):
                high = mid - 1
            else:
                if (mid == high):
                    low = mid
                else:
                    if (matrix[mid + 1][0] > target):
                        high = mid
                    else:
                        low = mid + 1
                        
        row = low
        # search for the target
        low = 0
        high = len(matrix[0]) - 1
        while (low <= high):
            mid = (low + high) // 2
            if (matrix[row][mid] == target):
                return True
            elif (matrix[row][mid] > target):
                high = mid - 1
            else:
                low = mid + 1
                
        return False

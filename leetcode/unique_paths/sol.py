class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        paths = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            paths[i][0] = 1
        for j in range(n):
            paths[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                paths[i][j] = paths[i - 1][j] + paths[i][j - 1]
                
        return paths[m - 1][n - 1]

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if (m == 0):
            return
        n = len(board[0])
        # update the board so that bit 0 represents current state and bit 1 represents the next state
        for i in range(m):
            for j in range(n):
                live_neigh = self.get_live_neighbors(i, j, board, m , n)
                if (board[i][j] & 1 == 0):
                    if (live_neigh == 3):
                        board[i][j] = 2
                else:
                    if (live_neigh >= 2 and live_neigh <= 3):
                        board[i][j] = 3
                        
        for i in range(m):
            for j in range(n):
                board[i][j] = board[i][j] >> 1
                
    # function to calculate count of live neighbors
    def get_live_neighbors(self, i, j, board, m, n):
        count = 0
        for x in range(max(i - 1, 0), min(m - 1, i + 1) + 1):
            for y in range(max(j - 1, 0), min(n - 1, j + 1) + 1):
                count += board[x][y] & 1
                
        count -= board[i][j] & 1
        return count

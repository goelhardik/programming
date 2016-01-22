class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if (m == 0):
            return
        n = len(board[0])
        
        # mark all non-border Os as A (potential Xs)
        for i in range(m):
            for j in range(n):
                if (board[i][j] == 'O' and i > 0 and i < m - 1 and j > 0 and j < n - 1):
                    board[i][j] = 'A'
        
        # for every O, mark all A neighbors back to Os
        for i in range(m):
            for j in range(n):
                if (board[i][j] == 'O'):    # mark all adjacent As as O
                    board[i][j] = 'A'
                    self.mark_adjacent_As(board, m, n, i, j)
                        
        # mark the remaining As as X
        for i in range(m):
            for j in range(n):
                if (board[i][j] == 'A'):
                    board[i][j] = 'X'
                    
        return
    
    # use DFS to mark this A and all neighbor As as O
    def mark_adjacent_As(self, board, m, n, i, j):
        if (i < 0 or i >= m or j < 0 or j >= n):
            return
        if (board[i][j] == 'A'):
            board[i][j] = 'O'
        else:
            return
        
        self.mark_adjacent_As(board, m, n, i - 1, j)
        self.mark_adjacent_As(board, m, n, i + 1, j)
        self.mark_adjacent_As(board, m, n, i, j - 1)
        self.mark_adjacent_As(board, m, n, i, j + 1)

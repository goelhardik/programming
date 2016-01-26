class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        answer = [] 
        for start in range(n):
            board = self.create_new_board(n, start, 0)
            self.dfs(list(board), n, start, 0, n, answer)
                
        return list(answer)
        
    def create_new_board(self, n, i, j):
        board = [['-' for c in range(n)] for r in range(n)]
        return board
        
    def copy_board(self, board, n):
        x = []
        for i in range(n):
            x.append(list(board[i]))

        return x

    def dfs(self, board, n, si, sj, q_rem, answer):
        if (q_rem == 0):
            new_board = []
            for i in range(n):
                row = ''.join(board[i])
                new_board.append(row)
            if (new_board not in answer):
                answer.append(list(new_board))
            return True
        if (sj == n):   # reached end of columns
            return False
        if (board[si][sj] != '-'):  # not an available slot
            return False
            
        self.mark_unavailable_boxes(board, n, si, sj)  # mark all unavailable boxes due to this queen
        board[si][sj] = 'Q' # mark current queen
        nj = sj + 1 # next column
        for ni in range(n):
            x = self.copy_board(board, n)
            self.dfs(x, n, ni, nj, q_rem - 1, answer)    # pass a copy of board, so that current state is preserved while backtracking
            if (nj == n):
                break
            
    def mark_unavailable_boxes(self, board, n, si, sj):
        # mark row
        r = si
        for c in range(n):
            board[r][c] = '.'
        
        # mark column
        c = sj
        for r in range(n):
            board[r][c] = '.'
            
        # mark diagonal
        i = si - min(si, sj)    # left-most start coordinate
        j = sj - min(si, sj)
        for r, c in zip(range(i, n), range(j, n)):
            board[r][c] = '.'
            
        # mark reverse diagonal
        i = si + min(n - 1 - si, sj)    # left-most start coordinate
        j = sj - min(n - 1 - si, sj)
        for r, c in zip(range(i, -1, -1), range(j, n)):
            board[r][c] = '.'

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        if (m == 0):
            return False
        n = len(board[0])
        visited = [[0 for y in range(n)] for x in range(m)]
        for i in range(m):
            for j in range(n):
                if (board[i][j] == word[0]):
                    if (self.dfs(word, board, i, j, m, n, visited)):
                        return True
                        
        return False
        
    def dfs(self, word, board, i, j, m, n, visited):
        if (len(word) == 0):
            return True
        if (i < 0 or i >= m or j < 0 or j >= n):
            return False
        if (visited[i][j] == 1):
            return False
        if (board[i][j] != word[0]):
            return False
        visited[i][j] = 1
        word = word[1:]
        if (self.dfs(word, board, i, j + 1, m, n, visited) or
                self.dfs(word, board, i + 1, j, m, n, visited) or
                self.dfs(word, board, i, j - 1, m, n, visited) or
                self.dfs(word, board, i - 1, j, m, n, visited)):
                    return True
        else:
            visited[i][j] = 0
            return False

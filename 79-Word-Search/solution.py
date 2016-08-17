class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        L= len(word)
        M = len(board)
        N = len(board[0])
        def dfs(i, j, k):
            if word[k] != board[i][j]:
                return False
            if k + 1 == L:
                return True
            temp, board[i][j] = board[i][j], '#'

            res = (i - 1 >= 0 and dfs(i - 1, j, k + 1)) or (i + 1 < M and dfs(i + 1, j, k + 1)) or (j - 1 >= 0 and dfs(i, j - 1, k + 1)) or (j + 1 < N and dfs(i, j + 1, k + 1))
            board[i][j] = temp
            return res
        def DFS(i, j, l):
            if board[i][j] != word[l]: return False
            if l+1 == L: return True
            board[i][j] += '@'
            hasFound = (i-1>=0 and DFS(i-1, j, l+1)) or (i+1 < M and DFS(i+1, j, l+1)) or\
                (j-1 >= 0 and DFS(i, j-1, l+1)) or (j+1 < N and DFS(i, j+1, l+1))
            board[i][j] = board[i][j][0] #backtrace
            return hasFound

        if not board:
            return False

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False

    
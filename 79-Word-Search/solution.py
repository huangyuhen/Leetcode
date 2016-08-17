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
        # def dfs(l, i, j):
            # if word[k] != board[i][j]:
            #     return False
            # if k + 1 == len(word):
            #     return True
            # board[i][j] += '@'

            # res = (i - 1 >= 0 and dfs(k + 1, i - 1, j)) or (i + 1 <= len(board[0]) and dfs(k + 1, i + 1, j)) or (j - 1 >= 0 and dfs(k + 1, i, j - 1)) or (j + 1 <= len(board) and dfs(k + 1, i, j + 1))
            # board[i][j] = board[i][j][0]
            # return res
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
                if DFS(i, j, 0):
                    return True
        return False

    
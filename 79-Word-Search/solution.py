class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        L= len(word)
        # if not L: return True
        M = len(board)
        # if not M: return False
        N = len(board[0])
        def DFS(i, j, l):
            if board[i][j] != word[l]: return False
            if l+1 == L: return True
            board[i][j] += '@'
            hasFound = (i-1>=0 and DFS(i-1, j, l+1)) or (i+1 < M and DFS(i+1, j, l+1)) or\
                (j-1 >= 0 and DFS(i, j-1, l+1)) or (j+1 < N and DFS(i, j+1, l+1))
            board[i][j] = board[i][j][0] #backtrace
            return hasFound
        
        for i in range(M):
            for j in range(N):
                if DFS(i,j, 0):
                    return True
        return False

    
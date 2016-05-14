class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.col = [0 for i in xrange(n)]
        self.row = [0 for i in xrange(n)]
        self.diag = [0, 0]
        self.diagCord = []
        self.win = n
        temp = n-1
        for i in xrange(n):
            self.diagCord.append([temp, i])
            temp -= 1

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        change = 0
        if player == 1:
            change = 1
        elif player == 2:
            change = -1
        self.col[col] += change
        if self.col[col] == self.win or self.col[col] == -self.win:
            return [1,2][self.col[col] == -self.win]
        self.row[row] += change
        if self.row[row] == self.win or self.row[row] == -self.win:
            return [1,2][self.row[row] == -self.win]
        if row == col:
            self.diag[0] += change
        if self.diag[0] == self.win or self.diag[0] == -self.win:
            return [1,2][self.diag[0] == -self.win]
        if [row, col] in self.diagCord:
            self.diag[1] += change
        if self.diag[1] == self.win or self.diag[1] == -self.win:
            return[1,2][self.diag[1] == -self.win]
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
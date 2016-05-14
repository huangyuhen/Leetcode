class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.col = [[0,0] for i in xrange(n)]
        self.row = [[0,0] for i in xrange(n)]
        self.diag = [[0, 0] for i in xrange(2)]
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
        change = 1
        user = player - 1
        self.col[col][user] += change
        self.row[row][user] += change
        if row == col:
            self.diag[0][user] += change
        if [row, col] in self.diagCord:
            self.diag[1][user] += change
        if any([self.col[col][user] == self.win or self.row[row][user] == self.win 
                or self.diag[0][user] == self.win or self.diag[1][user] == self.win]):
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
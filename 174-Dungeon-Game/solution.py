class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if len(dungeon) == 0:
            return 0 
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[0 for _ in xrange(n) ] for _ in xrange(m)]

        dp[m - 1][n - 1] = max(1, 1 - dungeon[m - 1][n - 1])
        for i in xrange(m - 2, -1, -1):
            dp[i][n - 1] = max(dp[i + 1][n - 1] - dungeon[i][n - 1], 1)
        for i in xrange(n - 2, -1, -1):
            dp[m - 1][i] = max(dp[m - 1][i + 1] - dungeon[m - 1][i], 1)

        for i in xrange(m - 2, -1, -1):
            for j in xrange(n - 2, -1, -1):
                dp[i][j] = max(1, min(dp[i + 1][j],dp[i][j + 1]) - dungeon[i][j])
        return dp[0][0]
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        row, col = len(grid), len(grid[0])
        visited = [[False for _ in xrange(col)] for _ in xrange(row)]
        counter = 0
        for i in xrange(row):
            for j in xrange(col):
                if grid[i][j] == '1' and not visited[i][j]:
                    self.dfs(grid, visited, i, j, row, col)
                    counter += 1
        return counter

    def dfs(self, grid, visited, i, j, row, col):
        if grid[i][j] == '0' or visited[i][j]:
            return
        visited[i][j] = True
        if i != 0:
            self.dfs(grid, visited, i - 1, j, row, col)
        if i != row - 1:
            self.dfs(grid, visited, i + 1, j, row, col)
        if j != 0:
            self.dfs(grid, visited, i, j - 1, row, col)
        if j != col - 1:
            self.dfs(grid, visited, i, j + 1, row, col)
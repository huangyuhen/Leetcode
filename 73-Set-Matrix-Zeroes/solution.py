class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        col0, row, col = False, len(matrix), len(matrix[0])
        for i in xrange(row):
            if matrix[i][0] == 0:
                col0 = True
            for j in xrange(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in xrange(row - 1, -1, -1):
            for j in xrange(col - 1, 0,  -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0 == True:
                matrix[i][0] = 0
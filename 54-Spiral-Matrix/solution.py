class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        result = []

        if matrix == []:
            return result

        left, right, top, bottom = 0, len(matrix[0])-1, 0, len(matrix) - 1

        while left <= right and top <= bottom:
            for i in xrange(left, right + 1):
                result.append(matrix[top][i])
            for j in xrange(top+1, bottom):
                result.append(matrix[j][right])
            for i in reversed(xrange(left, right + 1)):
                if top < bottom:
                    result.append(matrix[bottom][i])
            for j in reversed(xrange(top+1, bottom)):
                if left < right:
                    result.append(matrix[j][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1

        return result
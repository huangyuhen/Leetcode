class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        num = pow(2, n)
        res = []
        for i in xrange(num):
            res.append(i ^ (i >> 1))
        return res
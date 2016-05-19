class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return 1/self.pow(x, -n)
        else:
            return self.pow(x, n)
    def pow(self, x, n):
        if n == 0:
            return 1
        
        res = self.pow(x, n/2)
        
        if n % 2 == 0:
            return res * res
        else:
            return res * res * x
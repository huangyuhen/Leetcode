class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if x + y < z:
            return False
        if  x == z or y == z or x + y == z:
            return True
        return z % self.GCD(x,y) == 0
    def GCD(self, x, y):
        while (y != 0):
            x, y = y, x % y
        return x
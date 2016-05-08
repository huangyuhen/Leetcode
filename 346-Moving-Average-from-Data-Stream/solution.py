class MovingAverage(object):
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.result = [0] * size
        self.size = size
        self.count = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.result[self.count % self.size] = val
        self.count += 1
        if self.count > 3:
            return float(sum(self.result)) / self.size
        return float(sum(self.result)) / self.count


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
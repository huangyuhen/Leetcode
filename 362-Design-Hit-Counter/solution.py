class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = collections.deque()
        self.k = 300
        self.counter = 0

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.getHits(timestamp)
        if self.data and self.data[-1][0] == timestamp:
            self.data[-1][1] += 1
        else:
            self.data.append([timestamp, 1])
        self.counter += 1


    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        while self.data and self.data[0][0] <= timestamp - self.k:
            self.counter -= self.data.popleft()[1]
        return self.counter


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
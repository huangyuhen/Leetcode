class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}


    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message in self.dict:
            if timestamp - self.dict.get(message) >= 10:
                self.dict[message] = timestamp
                return True
            else:
                return False
        else:
            self.dict[message] = timestamp
            return True



# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
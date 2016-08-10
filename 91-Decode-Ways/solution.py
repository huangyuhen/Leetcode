class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s == "":
            return 0
        result = [0 for _ in xrange(len(s) + 1)]
        result[len(s)] = 1
        result[len(s) - 1] = [1,0][s[len(s)-1] == "0"]
        for i in xrange(len(s) - 2, -1, -1):
            if s[i] == "0": continue
            else:
                result[i] = [result[i+1], result[i+1] + result[i+2]][int(str(s[i]) + str(s[i+1])) <= 26]
        return result[0]
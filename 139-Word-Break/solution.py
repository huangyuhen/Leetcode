class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        n = len(s)
        if not s or n == 0:
            return False
        DP = [False] * (n + 1)
        DP[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if DP[j] and s[j:i] in wordDict:
                    DP[i] = True
                    break
        return DP[-1]
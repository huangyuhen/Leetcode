class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        maxl = [1, 0, 1]
        while i + maxl[0]/2 < len(s):
            start, end = i, i
            while end + 1 < len(s) and s[start] == s[end+1]:
                end += 1
            i = end+1
            while start - 1 >= 0 and end + 1 < len(s) and s[start - 1] == s[end + 1]:
                start -= 1
                end += 1
            if (end - start) + 1 > maxl[0]:
                maxl = [end - start+1, start, end+1]
                continue
        return s[maxl[1]: maxl[2]]
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = {}
        count, leftp = 0, 0
        for i in xrange(len(s)):
            if s[i] in hashmap:
                count = max(count, i - leftp)
                leftp = max(leftp, hashmap[s[i]] + 1)
            hashmap[s[i]] = i
        return max(count, len(s) - leftp)
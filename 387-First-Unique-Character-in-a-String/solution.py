class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        def pair():
            return (0, -1)
        dict = collections.defaultdict(pair)
        for i in xrange(len(s)):
            count, index = dict[s[i]]
            dict[s[i]] = (count+1, i)
        print dict
        ans = 2 ** 32
        for key in dict.keys():
            if dict[key][0] == 1:
                ans = min(dict[key][1], ans)
        return -1 if ans == 2 ** 32 else ans
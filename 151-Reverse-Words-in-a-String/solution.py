class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        L = s.split()
        L.reverse()
        s1 = ' '.join(L)
        return s1  
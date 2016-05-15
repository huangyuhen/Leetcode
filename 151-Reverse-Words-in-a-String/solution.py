class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        i = len(s) - 1
        while i >= 0:
            if not s[i].isspace():
                temp = i
                while not s[i].isspace() and i >= 0:
                    i -= 1
                result.append(s[i+1:temp+1])
            else:
                i -= 1
        return " ".join(result)
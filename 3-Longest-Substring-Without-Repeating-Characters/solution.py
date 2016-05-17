class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest, visited = [], []
        for char in s:
            if char not in visited:
                visited.append(char)
            else:
                if len(longest) <= len(visited):
                    longest = visited
                    visited = longest[longest.index(char) + 1:]
                else:
                    visited = visited[visited.index(char)+1:]
                visited.append(char)
        if len(longest) < len(visited):
            longest = visited
        #return "".join(longest)
        return len(longest)
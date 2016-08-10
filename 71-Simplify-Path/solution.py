class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        newPath = path.split("/")
        stack = collections.deque()
        skip = ['..','.','']
        for item in newPath:
            if item == ".." and stack:
                stack.pop()
            elif item not in skip:
                stack.append(item)
        result = ""
        while stack:
            result = "/" + stack.pop() + result
        return [result, "/"][len(result) == 0]
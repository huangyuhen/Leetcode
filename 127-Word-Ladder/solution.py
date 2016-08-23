class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        visited = set()
        queue = [(beginWord, 1)]
        while queue:

            word, length = queue.pop(0)
            for i in xrange(len(word)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    tmp = word[:i] + j + word[i+1:]
                    if tmp == endWord:
                        return length + 1

                    if tmp not in visited and tmp in wordList:
                        queue.append((tmp, length+1))
                        visited.add(tmp)
        return 0
class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i, index1, index2, dist = 0, None, None, sys.maxint
        while i < len(words):
            if words[i] == word1:
                if index1 is not None:
                    dist = min(dist, abs(index1 - i))
                index1 = i
            elif words[i] == word2:
                index2 = i
            if index1 is not None and index2 is not None:
                dist = min(dist, abs(index1 - index2))
            i += 1
        return dist
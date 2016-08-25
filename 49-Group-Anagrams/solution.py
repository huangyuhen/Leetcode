class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        for s in strs:
            key = tuple(sorted(s))
            dict[key] = dict.get(key,[]) + [s]
        return dict.values()
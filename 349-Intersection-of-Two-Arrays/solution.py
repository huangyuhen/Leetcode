class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hash = {}
        res = []
        for s in nums1: hash[s] = 1
        for s in nums2:
            if s in hash:
                res.append(s)
                hash.pop(s)
        return res
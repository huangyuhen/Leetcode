class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hash = {}
        res = []
        for s in nums1:
            if s in hash:
                hash[s] += 1
            else:
                hash[s] = 1
        for s in nums2:
            if s in hash:
                res.append(s)
                hash[s] -= 1
                if hash[s] == 0:
                    hash.pop(s)
        return res
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict = collections.defaultdict(int)
        res = []
        for num in nums:
            dict[num] += 1
        freqList = [[] for i in range(len(nums) + 1)]
        for p in dict:
            freqList[dict[p]].append(p)
        for i in xrange(len(nums), 0, -1):
            res += freqList[i]
        return res[:k]
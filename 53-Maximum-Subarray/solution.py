class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        global_max, local_max = nums[0], nums[0]
        for x in xrange(1, len(nums)):
            local_max = max(nums[x], local_max + nums[x])
            global_max = max(global_max, local_max)
        return global_max
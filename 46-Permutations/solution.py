class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result, element = [], []
        self.dfs(nums, result, 0)
        return result

    def dfs(self, nums, result, n):
        if n == len(nums):
            result.append(copy.copy(nums))
            return
        for i in xrange(n, len(nums)):
            nums[n], nums[i] = nums[i], nums[n]
            self.dfs(nums, result, n + 1)
            nums[n], nums[i] = nums[i], nums[n]

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in xrange(1, len(nums)):
            if (i % 2 == 1 and nums[i-1] > nums[i]) or (i % 2 == 0 and nums[i-1] < nums[i]):
                nums[i-1], nums[i] = nums[i], nums[i-1]
        
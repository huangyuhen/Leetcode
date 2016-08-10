class Solution(object):
    def helper(self,nums, low, high):
        if low == high:
            return low
        mid1 = (low + high) / 2
        mid2 = mid1 + 1
        if nums[mid1] > nums[mid2]:
            return self.helper(nums,low,mid1)
        else:
            return self.helper(nums,mid2, high)
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return self.helper(nums, 0, len(nums) -1)
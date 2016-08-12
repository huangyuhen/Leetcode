class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums) - 1
        left, right = 0, size
        while left < right:
            if nums[left] < nums[right]:
                return nums[left]
            mid = (left + right)/2
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i, j = 0, len(nums) - 1

        while i <= j:
            mid = (i + j)/2
            if nums[mid] == target:
                return mid
            if nums[i] <= nums[mid]:
                if target < nums[mid] and target >= nums[i]:
                    j = mid - 1
                else:
                    i = mid + 1
            else:
                if target > nums[mid] and target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1
        return -1
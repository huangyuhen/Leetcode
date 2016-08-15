class Solution(object):
    def findKthLargest(self, nums, k):
        # convert the kth largest to smallest
        temp = len(nums) - 1 - k
        return self.findKthSmallest(nums, 0, len(nums) - 1, len(nums) - k)

    def findKthSmallest(self, nums, start, end, k):
        while start < end:
            pos = self.partition(nums, start, end)
            if pos < k:
                start = pos + 1
            elif pos > k:
                end = pos - 1
            else:
                break
        return nums[k]

    def partition(self, nums, start, end):
        p, i, j = start, start, end
        while i < j:
            while nums[i] <= nums[p] and i < end:
                i += 1
            while nums[j] >= nums[p] and j > start:
                j -= 1
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]
        nums[start], nums[j] = nums[j], nums[start]
        return j
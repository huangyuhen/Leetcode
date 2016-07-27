class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor, i = 0, 0
        while i < len(nums):
            xor = xor ^ i ^ nums[i]
            i += 1
        return xor ^ i
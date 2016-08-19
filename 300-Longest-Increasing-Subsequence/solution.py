class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def binarySearch(dp, digit, target):
            left, right = 0, digit
            while left + 1 < right:
                mid = left + (right - left)/2
                if dp[mid] == target:
                    return mid
                else:
                    if dp[mid] < target:
                        left = mid
                    else:
                        right = mid
            if dp[right] < target:
                return digit + 1
            elif dp[left] >= target:
                return left
            else:
                return right
        if len(nums) == 0:
            return 0
        dp = [nums[0]]
        digit = 0
        for i in range(1,len(nums)):
            pos = binarySearch(dp, digit, nums[i])
            if pos > digit:
                digit = pos
                dp.append(nums[i])
            else:
                dp[pos] = nums[i]

        return digit + 1
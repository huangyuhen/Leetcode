class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        if n < 3:
            return sum(nums)
        ans = nums[0] + nums[1] + nums[2]
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if target == temp:
                    return temp
                if abs(target - ans) > abs(target - temp):
                    ans = temp
                if temp > target:
                    k -= 1
                else:
                    j += 1
        return ans

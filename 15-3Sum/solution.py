class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sortNums = sorted(nums)
        result = []
        for i in xrange(len(nums)-2):
                j,  k= i + 1, len(nums) - 1
                while j < k:
                    temp = sortNums[i] + sortNums[j] + sortNums[k]
                    if temp > 0:
                        k -= 1
                    elif temp < 0:
                        j += 1
                    else:
                        if [sortNums[i], sortNums[j], sortNums[k]] not in result:
                            result.append([sortNums[i], sortNums[j], sortNums[k]])
                        j, k = j + 1, k - 1
                        while j < k and sortNums[j] == sortNums[j - 1]:
                            j += 1
                        while j < k and sortNums[k] == sortNums[k + 1]:
                            k -= 1
        return result
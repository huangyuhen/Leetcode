class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        diff = 0
        for i in nums:
            diff ^= i
        diff &= -diff
        result = [0,0]
        for i in nums:
            if i &diff != 0:
                result[0] ^= i
            else:
                result[1] ^= i
        return result
        
#diff' + 1 = -diff
#diff & ~(diff-1) = diff & -diff

# 00010 (diff)
# 11110 (~(diff - 1)
#=00010
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        left_product = [1 for _ in xrange(len(nums))]
        
        for i in xrange(1, len(nums)):
            left_product[i] = left_product[i-1] * nums[i-1]
            
        right_product = 1
        for i in xrange(len(nums)-2, -1, -1):
            right_product *= nums[i+1]
            left_product[i] = left_product[i] * right_product
        return left_product
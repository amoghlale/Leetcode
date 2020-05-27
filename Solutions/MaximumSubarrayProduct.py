class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            forward_product,backward_product,max_product = 0, 0, nums[0]
            for i in range(len(nums)):
                forward_product = forward_product * nums[i] or nums[i]
                backward_product = backward_product * nums[len(nums)-i-1] or nums[len(nums)-i-1]
                max_product = max(max_product,forward_product,backward_product)
            return max_product

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        else:
            l, r = (0, 1)
            counter = 1
            longest = 1
            while r < len(nums):
                if nums[r] > nums[l]:
                    l += 1
                    r += 1
                    counter += 1
                else:
                    l = r
                    r += 1
                    counter = 1
                if longest < counter:
                    longest = counter
            return longest

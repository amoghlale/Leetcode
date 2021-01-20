class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) == 1:
            if nums[0] == 1:
                return 1
            else:
                return 0
        else:
            count = 0
            max_count = 0
            for i in nums:
                if i == 1:
                    count += 1
                else:
                    if count >= max_count:
                        max_count = count
                    count = 0
            if count >= max_count:
                max_count = count
        return max_count

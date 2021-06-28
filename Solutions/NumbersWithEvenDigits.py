class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        nums = [str(i) for i in nums]
        count = 0
        for num in nums:
            if len(num) % 2 == 0:
                count += 1
        return count

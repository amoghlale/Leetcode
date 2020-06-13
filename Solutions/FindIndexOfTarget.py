class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = (0, len(nums) - 1)
        while low <= high:
            if target > nums[-1]:
                return high + 1
            elif target < nums[0]:
                return low
            else:
                mid = low + (high - low) // 2
                mid_value, prev_val = (nums[mid], nums[mid-1])
                if mid_value == target or (target not in nums and mid_value > target and prev_val < target):
                    return mid
                elif mid_value < target:
                    low = mid + 1
                else:
                    high = mid - 1
        return None

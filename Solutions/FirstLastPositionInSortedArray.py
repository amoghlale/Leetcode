class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        output_list = []
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low // 2)
            if nums[mid] == target:
                output_list.append(mid)
            if nums[mid] < target:
                low = mid + 1
            if nums[mid] >= target:
                high = mid - 1
        if len(output_list) == 0:
            return [-1, -1]
        elif len(output_list) == 1:
            return [output_list[0], output_list[0]]
        else:
            return [output_list[-1], output_list[0]]

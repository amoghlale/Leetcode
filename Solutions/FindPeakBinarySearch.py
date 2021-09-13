class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1
        else:
            low = 0
            high = len(nums) - 1
            while low <= high:
                mid = low + ((high - low) // 2)
                
                # if mid = 0 
                if mid == 0:
                    if nums[mid] > nums[mid + 1]:
                        return mid
                    else:
                        low = mid + 1
                        continue

                # mid is last element
                if mid == len(nums) - 1:
                    if nums[mid-1] < nums[mid]:
                        return mid
                    else:
                        high = mid - 1
                        continue

                # if peak
                if nums[mid-1] < nums[mid] > nums[mid+1]:
                    return mid

                # if increasing or decreasing slope
                if nums[mid-1] < nums[mid] < nums[mid+1]:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1

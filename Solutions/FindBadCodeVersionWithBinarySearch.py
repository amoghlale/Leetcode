# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = (0, n - 1)
        while low <= high:
            mid = low + (high - low) // 2
            mid_version = mid + 1
            prev_version = mid
            if isBadVersion(mid_version) == isBadVersion(prev_version):
                if isBadVersion(mid_version):
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                return mid_version
        return None

import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        elements_on_heap = []
        for i in nums:
            heapq.heappush(heap, i)

        # heapify
        heapq.heapify(heap)

        return heapq.nlargest(k, heap)[-1]

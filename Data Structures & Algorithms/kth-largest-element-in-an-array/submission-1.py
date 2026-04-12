import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Build a min-heap of length k
        # Pop root to get k largest.

        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
            

        
        return heapq.heappop(heap)
        
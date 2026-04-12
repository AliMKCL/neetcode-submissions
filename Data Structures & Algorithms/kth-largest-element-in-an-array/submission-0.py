import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Build a max-heap.
        # Pop the result k times.
        # Or build min-heap, pop len - k times.

        heap = []

        for num in nums:
            heapq.heappush(heap, num)
        

        for i in range(len(nums)-k):
            heapq.heappop(heap)
        
        return heapq.heappop(heap)
        
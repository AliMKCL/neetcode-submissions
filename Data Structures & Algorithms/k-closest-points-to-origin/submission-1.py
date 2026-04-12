import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []

        for (x, y) in points:
            heapq.heappush(heap, (-math.sqrt(math.pow((x - 0), 2) + math.pow((y - 0), 2)), [x, y]))
            if len(heap) > k:
                heapq.heappop(heap)
            
    
        result = []

        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result


        
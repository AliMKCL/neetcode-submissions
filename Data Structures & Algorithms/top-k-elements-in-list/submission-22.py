import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        """
        Top k frequent: Store items in heap:
        - As a key-value pair where key is frequency and value is the item.
        - Add / filter in heap using frequency.
        """

        if not nums:
            return []

        freq_map = {}

        for i in nums:
            if i not in freq_map:
                freq_map[i] = 1
            else:
                freq_map[i] += 1
        
        heap = []

        for num in freq_map.keys():
            heapq.heappush(heap, (freq_map[num], num)) # (frequency, number)
            if len(heap) > k:
                heapq.heappop(heap) # heappop removes the smallest.
        
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result








        
            

            
            




        





        
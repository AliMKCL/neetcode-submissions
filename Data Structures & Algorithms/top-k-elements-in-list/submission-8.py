from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = defaultdict(list)

        for number in nums:
            if number not in hashmap:
                hashmap[number] = 1
            else:
                hashmap[number] += 1
        
        #array = [[]]*(len(nums)+1)
        array = [[] for _ in range(len(nums) + 1)]


        for number in hashmap:
            index = hashmap[number]
            array[index].append(number)
        
        index = len(array)-1
        caught = 0
        target_item = []
        while index >= 0 and caught != k:
            if array[index]:
                for item in array[index]:   
                    target_item.append(item)
                    caught += 1
            index -= 1
        return target_item




        
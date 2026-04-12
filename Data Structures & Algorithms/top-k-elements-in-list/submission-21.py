class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {}

        # Add all numbers to the hashmap in format number:frequency
        for number in nums:
            if number not in hashmap:
                hashmap[number] = 1
            else:
                hashmap[number] += 1
        
        # Each index of the array responds to elements with frequency equal to that index.
        array = [[] for _ in range(len(nums)+1)]

        for number in hashmap:
            array[hashmap[number]].append(number)

        count = 0;
        index = len(array)-1
        output = []
        while index >= 0 and count != k:
            while not array[index]:
                index -= 1
            for item in array[index]:

                output.append(item)
                count += 1
            index -=1
        
        return output




        
            

            
            




        





        
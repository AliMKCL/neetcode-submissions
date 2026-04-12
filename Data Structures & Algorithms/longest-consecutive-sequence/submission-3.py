class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        hashset = set(nums)

        counter = 1
        top_counter = 1

        for number in hashset:
            if number-1 not in hashset: # It is a starting number of a sequence

                # Despite being a nested loop, since walking froward from start elements,
                # Each number is visited once.
                while number+1 in hashset:
                    counter +=1
                    number +=1

                top_counter = max(counter, top_counter)
                counter = 1

        return top_counter



  
            




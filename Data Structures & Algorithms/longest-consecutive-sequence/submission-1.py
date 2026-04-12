class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()

        i = 0
        top_counter = 1
        counter = 1

        while i < len(nums)-1:
        
            if nums[i+1] == nums[i] + 1:
                counter +=1
            elif nums[i+1] == nums[i]:
                pass
            else:
                counter = 1
            i+=1

            if counter >= top_counter:
                top_counter = counter
        
        return top_counter



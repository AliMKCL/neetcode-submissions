class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1

        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        while end - start != 1:
            middle = (start + end) // 2

            if nums[middle] == target:
                return middle
            
            if target < nums[middle]:
                end = middle
            else:
                start = middle
        
        if nums[end] == target:
            return end
        elif nums[start] == target:
            return start
        else:
            return -1

                
        
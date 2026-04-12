class Solution:
    def findMin(self, nums: List[int]) -> int:

        # Idea: Binary search where target is the 1st index that is smaller than its left.
        
        start = 0
        end = len(nums)-1
        first = nums[0]
        last = nums[len(nums)-1]


        while start < end:
            middle = (end + start) // 2

            if end - start == 1:
                if nums[start] > nums[end]:
                    return nums[end]
                else:
                    return nums[start]
            
            if nums[middle] < nums[middle-1]:
                return nums[middle]
            else:
                if nums[middle] < first:
                    end = middle
                else:
                    if first < last:
                        return first
                    else:
                        start = middle
                    
        
        return first
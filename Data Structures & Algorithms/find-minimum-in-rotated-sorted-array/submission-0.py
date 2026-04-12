class Solution:
    def findMin(self, nums: List[int]) -> int:

       # Idea: Binary search where target is the 1st index that is smaller than its left.
       first = nums[0]
       start = 0
       end = len(nums) - 1

       while start < end:
            middle = int((end+start)/2)

            if len(nums) == 2:
                if nums[0] < nums[1]:
                    return nums[0]
                else:
                    return nums[1]

            if nums[middle - 1] > nums[middle]:
                return nums[middle]
            else:
                if nums[middle] > first:
                    # Go right
                    start = middle
                else:
                    # Go left
                    end = middle
            
            if end - start <= 1:
                if nums[start] > nums[end]:
                    return nums[end]
                else:
                    return nums[0]

       return nums[0] 
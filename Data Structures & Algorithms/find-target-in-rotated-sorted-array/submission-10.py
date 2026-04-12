class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start = 0
        end = len(nums)-1
        first = nums[0]
        last = nums[len(nums)-1]

        if not nums:
            return -1
        elif len(nums) == 1:
            if nums[0] == target: 
                return 0 
            else:
                return -1

        while start < end:
            middle = (start + end) // 2

            if end - start == 1:
                if nums[end] == target:
                    return end
                elif nums[start] == target:
                    return start
                else:
                    return -1

            if nums[middle] == target:
                return middle
            
            if nums[middle] > first: 
                if first < last:    # List is sorted, turning point on left
                    if target < nums[middle]:
                        end = middle
                    else:
                        start = middle
                else: # Turning point is on the right
                    if target > last:
                        if target > nums[middle]:
                            start = middle
                        else:
                            end = middle
                    else:
                        start = middle
            else: # Turning point is on the left
                if target < nums[middle]:
                    end = middle
                else:
                    if target > last:
                        end = middle
                    else:
                        start = middle
            

        return -1
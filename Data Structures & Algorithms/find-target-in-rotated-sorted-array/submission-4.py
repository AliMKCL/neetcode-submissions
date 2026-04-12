class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Base conditions
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        # Algorithm start

        start = 0
        end = len(nums)-1
        first = nums[0]

        while start < end:
            middle = int((start + end)/2)
            if nums[start] == target:
                return start
            if nums[end] == target:
                return end

            if end - start == 1:
                if nums[start] == target:
                    return start
                elif nums[end] == target:
                    return end
                else:
                    return -1

            if nums[middle] == target:
                return middle
            else:
                if target < nums[middle]:
                    if nums[middle] > first and target < first:
                        start = middle
                    elif nums[middle] > first and target > first:
                        end = middle
                    elif nums[middle] < first:
                        end = middle
                elif target > nums[middle]:
                    if nums[middle] > first:
                        start = middle
                    elif nums[middle] < first and target > first:
                        end = middle
                    elif nums[middle] < first and target < first:
                        start = middle
        return -1
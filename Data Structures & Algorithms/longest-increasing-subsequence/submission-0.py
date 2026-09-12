class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        arr = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]: # At least j --> i is an increasing seq
                    arr[i] = max(arr[i], arr[j]+1)
        
        return max(arr)
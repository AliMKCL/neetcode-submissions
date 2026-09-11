from collections import defaultdict

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        arr = []
        hash = defaultdict(list)

        if len(nums) < 3:
            return [[]]

        i = 0
        while i < len(nums):
            l = i+1
            r = len(nums)-1

            while r > l:
                if nums[l] + nums[r] == -nums[i]:
                    arr.append([nums[i], nums[l], nums[r]])
                    while r > l and nums[r] == nums[r-1]:
                        r -= 1
                    r-=1
                    while r > l and nums[l] == nums[l+1]:
                        l += 1
                    l+=1
                else:
                    if nums[l] + nums[r] > -nums[i]:
                        r -= 1
                    else:
                        l += 1
            if i < len(nums) - 1 and nums[i] == nums[i+1]:
                while i < len(nums) - 1 and nums[i] == nums[i+1]:
                    i += 1
                i += 1
            else:
                i += 1

        return arr
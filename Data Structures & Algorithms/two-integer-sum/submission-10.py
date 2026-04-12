class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
    
        for i, number in enumerate(nums):
            difference = target - number
            if difference in hash:
                return [hash[difference], i]
            hash[number] = i
        return []
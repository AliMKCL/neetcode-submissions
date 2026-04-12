class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, number in enumerate(nums):
            hash[number] = i
        
        for i, num in enumerate(nums):
            if target - num in hash and hash[target-num] != i:
                return [i, hash[target-num]]
        return []
        
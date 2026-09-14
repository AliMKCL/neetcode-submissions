class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # O(n) time version, removed the .pop()'s causing o(n) due to shifting.
        l = 0
        r = len(numbers)-1

        while l < r:
            sum = numbers[l] + numbers[r]
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                return [l+1, r+1]
        
        return []
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hash = {}
        for number in nums:
            if f"{number}" in hash:
                return True
            else:
                hash.update({f"{number}": 1}) 
        
        return False




        
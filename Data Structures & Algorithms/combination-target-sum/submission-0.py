class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        # How: call combinationSum on the remaining part with target - num
        combinations = set()

        def combSum(arr, target, index):
            if target < 0:
                pass
            elif target == 0:
                combinations.add(tuple(arr))
                pass
            else:
                if index > len(candidates)-1:
                    return

                arr.append(candidates[index])
                combSum(arr, target-candidates[index], index)

                # We get this when it fails / sum(arr) > target, remove last repeat and go to next number
                last = arr.pop()
                combSum(arr, target, index+1)
        
        combSum([],target, 0)

        result = []

        for i in combinations:
            result.append(list(i))
        return result
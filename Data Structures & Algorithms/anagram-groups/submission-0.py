from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash = {}
        output = []

        for i, string in enumerate(strs):
            s = Counter(string)
            if f"{sorted(s.items())}" in hash:
                hash[f"{sorted(s.items())}"] += [string]
            else:
                hash[f"{sorted(s.items())}"] = [string]
                                 
        for strs in hash.values():
            output.append(strs)
        return output

        
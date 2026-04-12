from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for string in strs: # O(n)
            count = [0]*26
            
            for character in string: # O(m)
                count[ord(character) - ord("a")] +=1

            # Built the frequency list in O(n * m)

            hashmap[tuple(count)].append(string)
            # Mutable: Value can be change after being created.
            # Lists can't be dict keys (mutable) but tuples can (non-mutable).
            # Since hashmap is a dict of lists, we can append the string to each count tuple key.
        
        return list(hashmap.values())




        
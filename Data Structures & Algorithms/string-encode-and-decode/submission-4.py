class Solution:


    def encode(self, strs: List[str]) -> str:
        output = [] #O(n) space
        for i in strs: # O(n) time but negligable (m is worse) 
            output.append(str(len(i)))
            output.append("#")
            output.append(i)
        return "".join(output)

    def decode(self, s: str) -> List[str]:
        output = [] # O(m)
        # Format: length#string...

        i = 0 # For tracking position to start
        while i < len(s):
            j = i
            while s[j] != "#":  # Until which part is for length
                j+=1
            length = int(s[i:j])
            
            # Until here j is the #
            i = j + 1 # start of string (1 after #)
            j = i + length # end of string (start + length)
            output.append(s[i:j])   # i is start, j is end of string
            i = j
        return output

        

        
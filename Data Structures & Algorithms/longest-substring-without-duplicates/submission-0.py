class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        l = 0
        r = 0

        max_window = 0
        curr_window = 0
        hashset = set()

        while r < len(s):
            while r<len(s) and s[r] not in hashset:
                hashset.add(s[r])
                curr_window += 1
                r += 1
            max_window = max(max_window, curr_window)

            if r<len(s) and s[r] in hashset:
                hashset.remove(s[l])
                l += 1
                curr_window -=1
            max_window = max(max_window, curr_window)
            
            
            
        
        return max_window

            

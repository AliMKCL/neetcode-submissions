class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Look for the largest substring with k outliers.

        # Acc criteria: r - l - most_comm_count > k means there are more required to change than the number of changes allowed.


        count = {}  # Keeps track of characters in the window.
        max_len = 0
        l = 0
        max_freq = 0

        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1
            
            max_freq = max(max_freq, count[s[r]]) # Most frequent's count
            
            
            if r - l - max_freq < k:  # Allowed number of fails
                max_len = max(max_len, r - l + 1)
            else:               # Not allowed, shift 1 right
                count[s[l]] -= 1
                l += 1
                # r += 1
        
        return max_len
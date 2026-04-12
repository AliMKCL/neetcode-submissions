class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hash = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in hash:
                hash[s[i]] = 1
            else:
                hash[s[i]] +=1

        for i in range(len(t)):
            if t[i] in hash and hash[t[i]]>0:
                hash[t[i]] -= 1
            else:
                return False


        return True

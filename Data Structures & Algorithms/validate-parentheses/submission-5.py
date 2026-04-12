class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False

        chars = {"(": ")",
                "[": "]",
                "{": "}"}
        
        stack = []

        for character in s:
            if character in "([{":
                stack.append(character)
            else:
                if stack:
                    if chars[stack[-1]] == character:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        
        if len(stack) > 0:
            return False
        return True

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        paranthesis = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for p in s:
            if p in paranthesis and (not stack or stack[-1] != paranthesis[p]):
                return False
            elif p in paranthesis:
                if len(stack) == 0:
                    return False
                stack = stack[:-1]
            else:
                stack.append(p)

        return len(stack) == 0


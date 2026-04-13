class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2 - val1)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(float(val2) / float(val1)))
            else:
                stack.append(int(t))
        return stack.pop()


                
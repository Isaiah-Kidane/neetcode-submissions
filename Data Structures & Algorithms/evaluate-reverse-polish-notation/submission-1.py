class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        new=0
        stack = []

        for i in range(len(tokens)):
            
            if tokens[i] == "+":
                new = int(stack[-1]) + int(stack[-2])
                stack.pop()
                stack.pop()
                stack.append(new)
            elif tokens[i] == "-":
                new = int(stack[-2]) - int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(new)
            elif tokens[i] == "*":
                new = int(stack[-1]) * int(stack[-2])
                stack.pop()
                stack.pop()
                stack.append(new)
            elif tokens[i] == "/":
                new = int(int(stack[-2]) / int(stack[-1]))
                stack.pop()
                stack.pop()
                stack.append(new)
            else:
                stack.append(int(tokens[i]))
            
        return stack[-1]

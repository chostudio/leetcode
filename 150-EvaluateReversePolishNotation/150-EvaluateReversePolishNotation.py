# Last updated: 9/11/2025, 12:32:27 PM
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in "+-*/":
                r = stack.pop()
                l = stack.pop()
                if i == "+":
                    stack.append(l + r)
                elif i == "-":
                    stack.append(l - r)
                elif i == "*":
                    stack.append(l * r)
                elif i == "/":
                    stack.append(int(l / r)) # int conversion always truncates towards 0 in python.
            else: # it's a number
                stack.append(int(i))
        return stack.pop()
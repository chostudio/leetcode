# Last updated: 9/18/2025, 1:06:54 PM
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket == "(" or bracket == "{" or bracket == "[":
                stack.append(bracket)
            elif bracket == ")" and len(stack) > 0 and stack[-1] == "(":
                stack.pop()
            elif bracket == "}" and len(stack) > 0 and stack[-1] == "{":
                stack.pop()
            elif bracket == "]" and len(stack) > 0 and stack[-1] == "[":
                stack.pop()
            else:
                return False
        return len(stack) == 0
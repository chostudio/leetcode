# Last updated: 9/18/2025, 1:08:21 PM
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = ['(', '[', '{']
        for bracket in s:
            if bracket in open:
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                lastElement = stack.pop()
                if bracket == ")" and lastElement == "(":
                    continue
                elif bracket == "}" and lastElement == "{":
                    continue
                elif bracket == "]" and lastElement == "[":
                    continue
                return False
        return len(stack) == 0 # need to make sure nothing is left in the stack
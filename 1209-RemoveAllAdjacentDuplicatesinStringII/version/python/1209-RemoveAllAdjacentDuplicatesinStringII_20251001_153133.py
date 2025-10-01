# Last updated: 10/1/2025, 3:31:33 PM
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if len(stack) != 0 and char == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else: # nothing in stack or not matching char, start new one
                stack.append([char, 1])
        # essentially rebuilding the string
        return "".join(char * count for char, count in stack)

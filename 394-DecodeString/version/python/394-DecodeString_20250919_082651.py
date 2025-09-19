# Last updated: 9/19/2025, 8:26:51 AM
class Solution:
    def decodeString(self, s: str) -> str:
        from collections import deque 
        stack = [] # remember that stack is just an arr not dequeue
        for char in s:
            if char == "]":
                # get letters then number
                letters = deque()
                while len(stack) != 0 and stack[-1] != "[":
                    letters.appendleft(stack.pop()) # appendleft
                stack.pop() # remove "["
                num = deque()
                while len(stack) != 0 and stack[-1].isdigit():
                    num.appendleft(stack.pop())
                num = int("".join(num))
                combo = "".join(letters) * num # remember to join letters
                stack.append(combo)
            else:
                stack.append(char)
        return "".join(stack) # reember to return the entire stack, not just first val
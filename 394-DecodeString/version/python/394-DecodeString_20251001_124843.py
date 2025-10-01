# Last updated: 10/1/2025, 12:48:43 PM
from collections import deque
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == ']':
                word = deque()
                while stack[-1] != '[':
                    word.appendleft(stack.pop())
                stack.pop() # get rid fo left bracket
                number = deque()
                while len(stack) != 0 and stack[-1].isdigit():
                    number.appendleft(stack.pop())
                
                number = int("".join(number))
                word = "".join(word)
                stack.append(number * word)
            else:
                stack.append(s[i])
        return "".join(stack)
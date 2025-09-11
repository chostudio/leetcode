# Last updated: 9/11/2025, 12:30:21 PM
class Solution:
    def clearDigits(self, s: str) -> str:
        stackLetters = []
        for i in s:
            if i.isdigit():
                stackLetters.pop()
            else:
                stackLetters.append(i)
        return "".join(stackLetters)
# Last updated: 9/11/2025, 12:30:29 PM
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        arr = []
        for i in range(len(words)):
            for j in words[i]:
                if j == x: # if j is the char we want
                    arr.append(i)
                    break
        return arr
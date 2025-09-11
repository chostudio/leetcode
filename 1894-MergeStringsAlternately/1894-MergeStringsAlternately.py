# Last updated: 9/11/2025, 12:30:54 PM
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        one, two = 0, 0
        while one < len(word1) and two < len(word2):
            merged += word1[one]
            merged += word2[two]
            one += 1
            two += 1
        if len(word1) > len(word2):
            while one < len(word1):
                merged += word1[one]
                one += 1
        elif len(word1) < len(word2):
            while two < len(word2):
                merged += word2[two]
                two += 1
        return merged
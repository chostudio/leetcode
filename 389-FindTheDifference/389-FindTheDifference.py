# Last updated: 9/11/2025, 12:31:56 PM
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import defaultdict
        hashmap = defaultdict(int)
        for letter in s:
            hashmap[letter]+=1
        for letter in t:
            hashmap[letter] -=1
        for key in hashmap.keys():
            if hashmap[key] != 0:
                return key
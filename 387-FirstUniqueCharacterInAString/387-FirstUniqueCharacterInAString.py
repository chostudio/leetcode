# Last updated: 9/11/2025, 12:31:57 PM
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # it's whatever character has only 1 of it. but it also has to be the first character index wise if there's multiple char of only 1
        hashmap = defaultdict(int)
        for element in s:
            hashmap[element] += 1
        
        for index in range(len(s)):
            if hashmap[s[index]] == 1:
                return index
        return -1

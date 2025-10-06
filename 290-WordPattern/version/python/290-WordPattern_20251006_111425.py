# Last updated: 10/6/2025, 11:14:25 AM
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # split sentence string loop through both at same time, hash, if there is a mismatch then false, else go thru entire thing then retunr true all good
        
        arr = s.split()
        if len(pattern) != len(arr): # LEN OF ARRAY NOT the og string
            return False
        # print(arr)
        hashmap = defaultdict(str)
        
        for i in range(len(pattern)):
            if pattern[i] in hashmap and hashmap[pattern[i]] != arr[i]:
                return False
            # else not in hashmap yet or already in and matches. either add it in or overwrite it with the exact same thing
            else:
                hashmap[pattern[i]] = arr[i]
        
        seen = set()
        for i in hashmap.values(): # all words should be mapped to only one letter. if multiple words then multiple letters to multiple words. FALSE
            if i in seen:
                return False
            seen.add(i)
        return True
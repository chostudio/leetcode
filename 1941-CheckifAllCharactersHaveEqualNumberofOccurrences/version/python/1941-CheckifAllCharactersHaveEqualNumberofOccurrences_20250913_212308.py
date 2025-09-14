# Last updated: 9/13/2025, 9:23:08 PM
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        hashmap = collections.defaultdict(int)
        amount = 0
        for letter in s:
            hashmap[letter] += 1

        for freq in hashmap.values():
            if amount == 0:
                amount = freq
            if amount != freq:
                return False
        return True
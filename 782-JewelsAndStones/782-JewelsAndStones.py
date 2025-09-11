# Last updated: 9/11/2025, 12:31:33 PM
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelsSet = set(jewels)
        count = 0
        for i in stones:
            if i in jewelsSet:
                count += 1
        return count
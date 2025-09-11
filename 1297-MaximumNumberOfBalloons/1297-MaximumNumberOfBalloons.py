# Last updated: 9/11/2025, 12:31:12 PM
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashmap = defaultdict(int)
        for i in text:
            if i == "b" or i == "a" or i == "l" or i == "o" or i == "n":
                hashmap[i] += 1
        count = 10000
        if len(hashmap.keys()) != 5 : return 0
        for key, val in hashmap.items():
            if key == "l" or key == "o":
                count = min(count, val//2)
            else:
                count = min(count, val)
        return count

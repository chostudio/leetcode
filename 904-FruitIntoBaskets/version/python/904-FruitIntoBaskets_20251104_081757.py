# Last updated: 11/4/2025, 8:17:57 AM
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # sliding sindow at most two different values what is longest length of sligind window. hard part is what to determine which two values we want to keep. maybe hashset? but amount of things matter bc we need ot know how far we need to go until L pointer is all good again. so mb hashmap until 0 val?
        longest = 1
        hashmap = defaultdict(int) # of how many there is of something
        
        l, r = 0, 0 #obv dont starrt r at negative one lol
        while r < len(fruits):
            hashmap[fruits[r]] += 1
            while len(hashmap.keys()) > 2:
                hashmap[fruits[l]] -= 1
                if hashmap[fruits[l]] == 0:
                    del hashmap[fruits[l]]
                l += 1

            longest = max(longest, r - l + 1) # width
            r += 1
        return longest
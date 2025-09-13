# Last updated: 9/12/2025, 3:18:15 PM
class Solution:
    def maxFreqSum(self, s: str) -> int:
        # simple hashmap counter
        vowels = ['a', 'e', 'i', 'o', 'u']
        v = collections.defaultdict(int)
        c = collections.defaultdict(int)
        for char in s:
            if char in vowels:
                v[char] += 1
            else:
                c[char] += 1
        vmax, cmax = 0, 0
        for char in v:
            vmax = max(v[char], vmax)
        for char in c:
            cmax = max(c[char], cmax)
        return vmax + cmax
# Last updated: 9/28/2025, 9:15:32 PM
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        # pretty sure this one is just two pointer go biggest first then go down list
        count = 0
        i= 0
        j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                count += 1
                j += 1
            i += 1
        return count
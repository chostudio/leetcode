# Last updated: 9/25/2025, 6:40:53 PM
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = defaultdict(int)
        for i in arr:
            count[i] += 1
        
        seen = set()
        for i in count.values():
            if i in seen:
                return False
            seen.add(i)
        return True
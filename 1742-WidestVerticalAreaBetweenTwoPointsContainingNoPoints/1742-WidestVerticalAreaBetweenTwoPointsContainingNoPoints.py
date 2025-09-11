# Last updated: 9/11/2025, 12:30:58 PM
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:

        # only worry about x values
        aset = set()
        for i in range(len(points)):
            aset.add(points[i][0])
        
        sortedSet = sorted(aset)
        maximum = 0
        for x in range(1, len(sortedSet)):
            maximum = max(maximum, sortedSet[x]-sortedSet[x-1])
        return maximum
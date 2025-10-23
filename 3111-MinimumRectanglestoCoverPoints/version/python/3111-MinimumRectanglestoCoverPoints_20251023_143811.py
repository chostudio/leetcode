# Last updated: 10/23/2025, 2:38:11 PM
class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        # it is greedy, sort it asc first then kind of like sliding window based on thing
        # really only looking at x index
        if not points: # if there's nothing
            return 0

        if len(points) == 1:
            return 1
        aset = set()
        for x, y in points:
            aset.add(x)
        
        if w == 0:
            return len(aset)

        arr = list(aset)
        arr.sort()
        rect = 0
        # for loop index will always go by + 1. must use while loop if you want to jump the index
        r = 0
        # takes too long to go from 0-> 1 billion must loop through set values
        while r < arr[-1]+1: # last value is biggest value
            # start the rectanle at the next point
            if r in aset:
                r += w # then the for loop + 1 so it's like w + 1
                rect += 1
            r += 1
        
        return rect
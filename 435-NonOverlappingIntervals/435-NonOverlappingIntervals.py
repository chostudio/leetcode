# Last updated: 9/11/2025, 12:31:49 PM
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res, recentEnd = 0, float('-inf')
        intervals.sort(key=lambda x: x[1])
        for i in intervals:
            currStart, currEnd = i
            if currStart < recentEnd: # make sure you don't mix up which end you need to check
                res += 1 # we have to get rid of one of them and it aint going to be the earlier one
            else:
                recentEnd = currEnd # they don't overlap and we need to update the recentend we want to make sure they don't overlap with
        return res


# Last updated: 9/15/2025, 10:49:35 AM
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0]) # sort does not return anything
        ans = []
        for interval in intervals:
            # for first one just put something in it
            if len(ans) == 0 or ans[-1][1] < interval[0]: # or doesnt overlap
                ans.append(interval)
            # else there is something in there
            # if last ending overlaps with current start
            # if ans[-1][1] >= interval[0]:
            else: # they do overlap
                # then take to furthest out end date
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans
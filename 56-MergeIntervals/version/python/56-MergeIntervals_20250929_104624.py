# Last updated: 9/29/2025, 10:46:24 AM
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0]) # first value in the inner array
        stack = []
        for interval in intervals:
            # handles the case if nothingin stack yet (first internval) and so we can then check if there is an interval in there and if its end doenst conflict with the current start of the current interval then we're good and can just append normally
            if len(stack) == 0 or stack[-1][1] < interval[0]:
                stack.append(interval)
            else: # else they do conflict so we need to merge by updating with furthest out end time (bc the start time is obv the prev start interval already in stack)
                stack[-1][1] = max(stack[-1][1], interval[1])
            
        return stack
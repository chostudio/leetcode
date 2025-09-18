# Last updated: 9/17/2025, 2:02:18 PM
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals based on start times
        intervals.sort(key=lambda x: x[0])
        # two scenarios, either put into stack bc nothing in there or no overlap with the last element in stack ending with curr interval start

        stack = []
        for interval in intervals:
            if len(stack) == 0 or stack[-1][1] < interval[0]:
                stack.append(interval)
        # of there is overlap with the last element in the stack, so you merge them with the further out ending time. furthest out time either the stack last element curr ending time or the curr interval we're at's ending time
            else:
                stack[-1][1] = max(stack[-1][1], interval[1])
        return stack